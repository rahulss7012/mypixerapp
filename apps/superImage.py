import requests
import streamlit as st
import numpy as np
import base64
from PIL import Image
import io

# # Assuming your NumPy array is named 'image_array'
# image = Image.fromarray(image_array)

# # Create a byte stream
# stream = io.BytesIO()

# # Save the image to the stream in PNG format
# image.save(stream, format='PNG')

# # Seek back to the beginning of the stream
# stream.seek(0)

# # Convert the stream to a byte array
# image_bytes = stream.getvalue()

# # Encode the byte array as base64
# base64_image = base64.b64encode(image_bytes).decode('utf-8')

DEMO_IMAGE = 'images/cricket.jpg'

def app():
    

    st.title('Image Upscaling')
    # user_prompt = st.text_input("Enter the url of the image")
    img_file_buffer = st.file_uploader("Upload an image", type=[ "jpg", "jpeg",'png'])
    if img_file_buffer is not None:
            image_array = np.array(Image.open(img_file_buffer))
    else:
        demo_image = DEMO_IMAGE
        image_array = np.array(Image.open(demo_image))
    image = Image.fromarray(image_array)
     # Create a byte stream
    stream = io.BytesIO()

    # Save the image to the stream in PNG format
    image.save(stream, format='PNG')

    # Seek back to the beginning of the stream
    stream.seek(0)

    # Convert the stream to a byte array
    image_bytes = stream.getvalue()

    # Encode the byte array as base64
    base64_image = base64.b64encode(image_bytes).decode('utf-8')
    fetch_button = st.button("Upscale")


    if fetch_button:
        url = "https://super-image1.p.rapidapi.com/run"

        payload = {
          "upscale": 2,
          "image":base64_image
        }
        headers = {
          "content-type": "application/json",
          "X-RapidAPI-Key": "3b1674bb67mshb61635c6835ff03p1ecce6jsnfab542ef0f3a",
          "X-RapidAPI-Host": "super-image1.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        # print(response.json())
        st.image(response.json()['output_url'])
        # st.write(response.json())

