from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest")

response = model.invoke("Write a poem about the beauty of nature.")