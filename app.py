import google.generativeai as genai
import dotenv
import os
import streamlit as st

dotenv.load_dotenv()  #loading env variables

API_KEY = os.environ.get("API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# def get_response(question):
#     response = model.generate_content(question)
#     return response.text

st.set_page_config(page_title="Q&A demo")
st.header("Elina ai")
prompt = st.text_input("You: ",key="input")
submit = st.button("ask")

if submit:
    response = model.generate_content(prompt)
    st.write(response.text)
    