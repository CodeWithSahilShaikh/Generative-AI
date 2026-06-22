from langgraph.graph import StateGraph, START, END
from langchain.mistralai.chat_models import ChatMistralAI
from tavily import TavilyClient
from langchain.tools import tool
from dotenv import load_dotenv
import os
load_dotenv()


model = ChatMistralAI(
    model="mistral-small-latest",
    api_key=os.getenv("MISTRAL_API_KEY")
)

@tool
def get_information(query: str) -> str:
    """
    Get the latest information from the Internet.
    
    Args:
        query (str): The search query.
        
    Returns:
        str: The search results.
    """
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    response = client.search(query)
    return str(response)
tools = [get_information]
tools_dict = {tool.name: tool for tool in tools}

model_with_tools = model.bind_tools(tools)