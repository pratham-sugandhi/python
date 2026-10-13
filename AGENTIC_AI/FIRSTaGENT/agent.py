from agno.agent import Agent
from agno.models.llmman import Llmman
from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv
load_dotenv()

def build_agent():
    return Agent(
        model=Llmman(id="qwen3:0.6b-q4_K_M"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful assistant that can answer questions and provide information.",
        add_datetime_to_context=True
    )

groq_agent = build_agent()

groq_agent.print_response("Is it safe to travel to Japan in 2024?")