from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI


model = ChatMistralAI(model="mistral-small-latest")
response = model.invoke("What is the capital of France?")
print(response.text)

model2 = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
response = model2.invoke("What is the capital of France?")
print(response.text)