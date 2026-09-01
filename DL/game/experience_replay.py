from collections import deque
import random

class ReplayMemory():
    # create FIFO queue to store experiences
    def __init__(self, maxlen, seed=None):
        self.memory = deque([], maxlen=maxlen)
    
    def append(self, new_experience):
        self.memory.append(new_experience)

    def sample(self, sample_size):
        return random.sample(self.memory, sample_size)

    # curr buffer size of the memory
    def __len__(self):
        return len(self.memory)