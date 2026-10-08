from dataclass import dataclass

import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool,ToolRuntime
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver


from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class Context:
    user_id: str


@dataclass
class ResponseFormat:
    summary: str
    temperature_celsius: float
    temperature_fahrenheit: float
    humidity: float

    
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
)

response = model.invoke("Explain what LangChain is in 3 sentences.")

print(response.content)