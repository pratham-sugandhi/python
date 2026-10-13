from agno.agent import Agent
from agno.models.llmman import Llmman

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

from dotenv import load_dotenv
load_dotenv()

def build_agent():
    return Agent(
        model=Llmman(id="qwen3:0.6b-q4_K_M"),
        tools=[DuckDuckGoTools(), YFinanceTools()],
        markdown=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Use given tools to gather information and format your response using markdown and use tables to display data where possible."],
        add_datetime_to_context=True,
        debug=True
    )
    
groq_agent = build_agent()

groq_agent.print_response("Share the NVDA stock price and analyst recommendations")