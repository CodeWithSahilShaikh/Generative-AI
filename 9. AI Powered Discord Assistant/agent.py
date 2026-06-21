from dotenv import load_dotenv
import os
import base64
import io
import discord
import asyncio
load_dotenv()  

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from tavily import TavilyClient
from langchain_openai import ChatOpenAI


tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def generateAndSendImage(prompt:str, runTime:ToolRuntime):
    """Use this tool to generate an image based on the prompt and send it to the user"""
    llm = ChatOpenAI(model="gpt-5.4-mini")
    
    config = runTime.config.get("configurable")
    message = config.get("message")
    loop = config.get("loop")

    tool = {"type": "image_generation", "quality": "low"}

    llm_with_tools = llm.bind_tools([tool])

    ai_message = llm_with_tools.invoke(
        prompt
    )
    image = ai_message.connect_blocks[0]["base64"]
    
    base64_string = base64.b64decode(image)
    image_bytes = io.BytesIO(base64)
    
    file = discord.File(fp=image_bytes, filename="image.png")
    
    asyncio.run_coroutine_threadsafe(message.channel.send(file=file), loop)
    
    return "Image generated and sent successfully!"

@tool
def surfInternet(query:str):
    """Use this tool to surf the internet and get the latest information"""
    
    result = tavily_client.search(query)
    return str(result)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(model=model, tools=[surfInternet, generateAndSendImage],system_prompt="""provide the clean output to the user""")