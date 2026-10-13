from agno.agent import Agent
from agno.models.llmman import Llmman

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.db.sqlite import SqliteDb
from agno.memory import MemoryManager
from rich.pretty import pprint

from dotenv import load_dotenv
load_dotenv()

db = SqliteDb(db_file="memory.db")
db.clear_memories()

# memory_manager = MemoryManager(db=db)

def build_agent():
    return Agent(
        db=db,
        model=Llmman(id="qwen3:0.6b-q4_K_M"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful assistant that can answer questions and provide information.",
        add_datetime_to_context=True
    )

groq_agent = build_agent()
user_id = "user_123"
groq_agent.print_response("I am a user named Rahul and I am 25 years old.", user_id=user_id)
groq_agent.print_response("So what is my age?", user_id=user_id)


memories = groq_agent.get_user_memories(
    user_id=user_id
)

print("Memories for user_id:", user_id)
pprint(memories)