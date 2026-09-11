from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header('Research Tool')

model = ChatGroq(
    model="openai/gpt-oss-20b"
)

user_input = st.text_input('Enter Your Prompt')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)