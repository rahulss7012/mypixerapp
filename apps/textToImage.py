import openai  # pip install openai
import urllib.request
from datetime import datetime
import streamlit as st
openai.api_key = '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'


def app():
   
    # user_prompt = input("Write your prompt for DALL-E 2: ")
    user_prompt = st.text_input("Wr")
    fetch_button = st.button("Fetch API")

    if fetch_button:
        response = openai.Image.create(
        prompt='car',
        n=1,
        size="512x512"
    )

        image_url = response['data'][0]['url']
        print(image_url)
        st.write(image_url)
        # st.image(image_url, caption='My Image')


        # file_name = "image" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png"
        # urllib.request.urlretrieve(image_url, file_name)
        

