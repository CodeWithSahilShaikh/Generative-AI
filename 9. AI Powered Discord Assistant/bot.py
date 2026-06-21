from dotenv import load_dotenv
import os
import asyncio
load_dotenv()  
import discord
from langchain.messages import HumanMessage
from agent import agent

intents = discord.Intents.default()  # intents means permission.
intents.message_content = True

client = discord.Client(intents=intents)


# jb aap koi tool use krte ho and agr uss tool me koi parameter passs krna hota hai toh hm config ka use krte hai.
@client.event  # We call these decoraters.
async def on_message(message):
    if message.author == client.user:
        return
    async with message.channel.typing():
        content = message.content
        
        response = await agent.ainvoke(
            {"messages": [HumanMessage(content)]},
            config={"configurable":{"message":message, "loop": asyncio.get_event_loop()}}
            )
        
        agent_message = response["messages"][-1].text
    await message.channel.send(agent_message)

client.run(token=os.getenv("DISCORD_API_KEY"))