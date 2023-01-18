import streamlit as st
from PIL import Image
import numpy as np

# use this function to generate caption
def generate_caption(image):
    print(image)
    return 'your code to generate caption'

st.set_page_config(page_title="Image Captioning", page_icon=":camera:", layout="wide")

st.title("Instagram Caption Generator ")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    caption = generate_caption(image)
    st.header(f"Caption:  {caption}")
else:
    st.write("Please upload an image.")