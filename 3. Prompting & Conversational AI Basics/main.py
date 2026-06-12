# Using User Input and having full conversation with AI.
# Long Term Memory and Short Term Memory.

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

message = []

while True:
    user_input = input("Enter your prompt: ")
    message.append({"role": "user", "parts": [{"text": user_input}]})

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=list(map( lambda message: message["role"] + " : " + message["content"],message))
        )
    message.append({
        "role":"ai",
        "content":response.text,
    })
         
    print(response.text)
    
    
