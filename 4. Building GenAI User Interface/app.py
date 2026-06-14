# pyright: reportMissingImports=false
import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

if "messages" not in st.session_state :
    st.session_state["messages"] = []
    
# session_state: ye re-run ke beech me data ko persistant bnane ke liye use hota hai.

for message in st.session_state["messages"] :
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
user_input = st.chat_input("Type your message here...")

if user_input :
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user") :
        st.markdown(user_input)
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=list(map(lambda message : message["role"] + ": " + message["content"], st.session_state.messages))
    )
    
    st.session_state["messages"].append({"role": "ai", "content": response.text})
    
    with st.chat_message("ai") :
        st.markdown(response.text)
    
    

