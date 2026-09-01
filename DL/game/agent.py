import flappy_bird_gymnasium
import gymnasium as gym
from dqn import DQN
from experience_replay import ReplayMemory
import itertools
import yaml
import torch
import torch.nn as nn
import torch.optim as optim

if torch.backend.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"


class Agent():
    def __init__(self, param_set):
        self.param_set = param_set

        with open("parameters.yaml", "r") as f:
            all_params_set = yaml.safe_load(f)
            params = all_params_set[param_set]

        self.alpha = params["alpha"]
        self.gamma = params["gamma"]

        self.epsilon_init = params["epsilon_init"]
        self.epsilon_min = params["epsilon_min"]
        self.epsilon_decay = params["epsilon_decay"]

        self.replay_memory_size = params["replay_memory_size"]
        self.mini_batch_size = params["mini_batch_size"]

        self.network_sync_rate = params["network_sync_rate"]
        self.reward_threshold = params["reward_threshold"]
        self.epsilon_init = params["epsilon_init"]

        self.loss_fn = nn.MSELoss()
        self.optimizer = None  # Will be initialized later with the DQN model

    def run(self, is_training=True, render=False):
        env = gym.make("FlappyBird-v0", render_mode="human" if render else None)

        num_states = env.observation_space.shape[0]     #inp dim
        num_actions = env.action_space.n        #out dim

        policy_dqn = DQN(num_states, num_actions).to(device)

        if is_training:
            replay_memory = ReplayMemory(maxlen=self.replay_memory_size)
            epsilon = self.epsilon_init

            target_dqn = DQN(num_states, num_actions).to(device)

            # copy wt & bias from policy_dqn to target_dqn
            target_dqn.load_state_dict(policy_dqn.state_dict())

            steps = 0
            self.optimizer = optim.Adam(policy_dqn.parameters(), lr=self.alpha)


        for episode in itertools.count():
            state, _ = env.reset()
            state = torch.tensor(state, dtype=torch.float32, device=device)

            episode_rewards = 0
            terminated = False
            
            while not terminated:
                if is_training and random.random() < epsilon:
                    # Random action for exploration
                    action = env.action_space.sample()  # explore
                    action = torch.tensor(action, dtype=torch.long, device=device)
                else:
                    with torch.no_grad():
                        action = policy_dqn(state.unsqueeze(dim=0)).squeeze().argmax()  # exploit

                # terminated => done
                next_state, reward, terminated, _, _ = env.step(action.item())

                # create tensors
                reward = torch.tensor(reward, dtype=torch.float32, device=device)
                next_state = torch.tensor(next_state, dtype=torch.float32, device=device)


                if is_training:
                    replay_memory.append((state, action, next_state, reward,terminated))
                    steps += 1

                state = next_state
                episode_rewards += reward
            
            print(f"Episode: {episode+1}, Total Reward: {episode_rewards}")

            # epsilon decay
            if is_training:
                epsilon = max(self.epsilon_min, epsilon * self.epsilon_decay)

            if is_training and len(replay_memory) > self.mini_batch_size:
                # Sample a mini-batch from the replay memory
                mini_batch = replay_memory.sample(self.mini_batch_size)

                optimize(mini_batch, policy_dqn, target_dqn)

                # sync the network
                if steps > self.network_sync_rate :
                    target_dqn.load_state_dict(policy_dqn.state_dict())
                    steps = 0

                # Compute loss
                loss = self.loss_fn(q_values, target_q_values)

                # Backpropagation and optimization step
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
            # env.close()
    
    def optimize(self, mini_batch, policy_dqn, target_dqn):
        # Unpack the mini-batch into separate tensors for states, actions, next_states, rewards, and dones
        states, actions, next_states, rewards, dones = zip(*mini_batch)

        states = torch.stack(states)
        actions = torch.stack(actions)
        next_states = torch.stack(next_states)
        rewards = torch.stack(rewards)
        dones = torch.tensor(dones, dtype=torch.float32, device=device)

        # Compute Q-values for the current states using the policy network
        q_values = policy_dqn(states).gather(1, actions.unsqueeze(1)).squeeze(1)

        # Compute target Q-values for the next states using the target network
        with torch.no_grad():
            next_q_values = target_dqn(next_states).max(1)[0]
            target_q_values = rewards + (self.gamma * next_q_values * (1 - dones))

        return q_values, target_q_values

    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Train or Test model")
        parser.add_argument("hyperparameters", help="")
        parser.add_argument("--train", action="store_true", help="Training mode")
        args = parser.parse_args()

        dql = Agent(args.hyperparameters)

        if args.train:
            dql.run(is_training=True, render=False)
        else:
            dql.run(is_training=False, render=True)