import streamlit as st
import streamlit.components.v1 as components
import json

import requests  # pip install requests

from streamlit_lottie import st_lottie  # pip install streamlit-lottie

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.subheader('MYPIXER')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_jhlaooj5.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    # renderer="svg", # canvas
    
    width='300px',
    key=None
)
components.html(
          """
         
          <style>
          @import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@1,100&display=swap');
          .desc {
            color:white;
              position: fixed;
             top:0;
              right:0px;
             font-family: 'Roboto', sans-serif;

          }
          </style>
           
          <h1 class="desc">Image Manipulation tool  using  <br> Computer Vision and <br> Machine Learning
          </h1>
          
          """,
          height=600,
)



      
# st.markdown("Image Manipulation tool  using <br>   Computer Vision and <br>  Machine Learning", unsafe_allow_html=True)
      
      #Add a header and expander in side bar
      # st.sidebar.markdown('<p class="font">My First Photo Converter App</p>', unsafe_allow_html=True)
      # with st.sidebar.expander("About the App"):
      #     st.write("""
      #         Use this simple app to convert your favorite photo to a pencil sketch, 
      #         a grayscale image or an image with blurring effect and many more....  \n  
      #         \nThis app was created by Akshay , Amen , Karthik and Rahul as their final project. Hope you enjoy!
      #     """)


      