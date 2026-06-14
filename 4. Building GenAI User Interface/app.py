# pyright: reportMissingImports=false
import streamlit as st

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