import google.generativeai as genai
import dotenv
import os
import streamlit as st
from PIL import Image
#from vertexai.preview.generative_models import GenerativeModel, Image

dotenv.load_dotenv()  #loading env variables

API_KEY = os.environ.get("API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

#print(model)

def get_response(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Image demo")
st.header("Elina ai")
input = st.text_input("You: ",key="input")


upload_file = st.file_uploader("choose an image...", type=["jpg","jpeg","png"])
image=""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded image", use_column_width=True)
    
submit = st.button("tell me about the image")
if submit:
    response = get_response(input,image)
    st.write(response)