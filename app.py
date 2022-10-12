#Import Packages
import numpy as np
from PIL import Image
import streamlit as st
import warnings
from io import BytesIO
import base64
import requests
warnings.filterwarnings('ignore')

icon = Image.open('skin.jpg')
st.set_page_config(page_title='Classifier', page_icon = icon)
st.header('Skin Disease Classifier')

#Get Image
file_up = st.file_uploader('Upload an Image', type = "jpg")

def img_to_bytes(img):
    buffered = BytesIO()
    img.save(buffered, format=img.format)
    img_str = base64.b64encode(buffered.getvalue())
    strIMG = img_str.decode("utf-8")
    resp = get_response(strIMG)
    return resp

def get_response(ImgStr):
    url = 'https://f7736aea-c950-4bfa-8cdd-a558c21e8690.syndic.ai'
    data = {'url': ImgStr}

    x = requests.post(url, data)
    return x.text

if file_up is not None:
    # display image that user uploaded
    image = Image.open(file_up)
    result = img_to_bytes(image)
    st.image(image, caption = 'Original Image', width=350)
    st.write("Predictions: ",result)
