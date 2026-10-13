from agno.agent import Agent
from agno.models.llmman import Llmman
from agno.team import Team

from dotenv import load_dotenv
load_dotenv()

eng_agent = Agent(name="eng_agent", role="You answers questions in English.")
hindi_agent = Agent(name="hindi_agent", role="You answers questions in Hindi.")
chinese_agent = Agent(name="chinese_agent", role="You answers questions in Chinese.")

team_leader = Team(
    name="multilingual_team",
    members=[eng_agent, hindi_agent, chinese_agent],
    model=Llmman(id="qwen3:0.6b-q4_K_M"),
    markdown=True,
    show_members_responses=True,
    instructions="You are a team leader that coordinates the responses of your team members to answer questions in multiple languages."
)

team_leader.print_response("What is the capital of India? Please provide the answer in English, Hindi, and Chinese.")