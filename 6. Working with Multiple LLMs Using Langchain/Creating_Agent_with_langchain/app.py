from dotenv import load_dotenv
load_dotenv()

from tavily import TavilyClient
from langchain.tools import tool
from langchain.agents import  create_agent
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool 
def surfinternet(query: str) -> str:
    """Use this tool to surf the internet and get information."""   # We call it docstring, we have to always write it with each tool.
    result = tavily_client.search(query=query)
    
    return str(result)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(model=model, tools=[surfinternet])

response = agent.invoke({"messages": [HumanMessage("which is the latest model of claude?")]})

print(response)