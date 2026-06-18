from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.messages import HumanMessage, AIMessage, ToolMessage
from langchain.tools import tool
from datetime import date

# Tool hme extra functinality dete hai taki jo LLM nhi kr skte hm unse wo bhi krwa ske.
# Tools: We can create tools to perform specific tasks. In this case, we are creating a tool to get the current date. The model can call this tool when it needs to know the current date.
@tool
def getCurrentDate():
    """Use this tool to get the current date."""
    return str(date.today())


# bind tool: It allows the model to use the tool when generating responses. The model can call the tool to get the current date when needed. Here we can bind all the tools we created.
model = ChatMistralAI(model="mistral-small-latest").bind_tools([getCurrentDate])

# Note: our LLM can't call and use the tool directly. ye hme kuch arguments deke bolta hai ki hm wo argument uss tool ko de and jo bhi wo tool return krega woo hm LLM ko waps lakr de de.

messages = []

while True:
    userInput = input("You: ")
    messages.append(HumanMessage(content=userInput))
    response = model.invoke(messages)
    if isinstance(response, ToolMessage):
        messages.append(response)
    else:
        messages.append(AIMessage(response.content))
    
    print(response.text)