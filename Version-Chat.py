import streamlit as st
from langchain_community.llms import Replicate
from decouple import config
import os

# Load environment variables
REPLICATE_API_TOKEN = config("REPLICATE_API_TOKEN")
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

# Initialize Replicate instance
llm = Replicate(
    model="meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
    input={
        "temperature": 0.80,
        "max_length": 500,
        "top_p": 1
    }
)

def main():
    st.title("Chatbot using Llama-2 & Replicat")

    # Chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User input

    if user_input := st.chat_input("Ask me Question about your PDF File 📖"):

        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "message": user_input})

        # Generate response from the chatbot
        response = llm(prompt=user_input)
        st.session_state.chat_history.append({"role": "bot", "message": response})

    # Display chat history
    for item in st.session_state.chat_history:
        if item["role"] == "user":
            # st.write("You: ", item["message"])
            with st.chat_message("user"):
                st.markdown(item["message"])
        else:
            # st.write("Bot: ", item["message"])
            with st.chat_message("assistant"):
                st.write(item["message"])

if __name__ == "__main__":
    main()
