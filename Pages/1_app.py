import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageOps
import cv2
from multiapp import MultiApp
from apps import Crop,sketch,docConv,rotate,stitching,filters,inpaint,imageFinder,textToImage,superImage,detect
# from apps.mask-test.yolov5 import detect
app = MultiApp()

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# option = st.selectbox(
#     'Select from the options',
#     ('Home', 'Filters', 'Doc scanner','add text'), key = 1)


# if(option=='Filters'):
#     opt = st.selectbox(
#     'Select from the options',
#     ('sepia', 'Filter1', 'filter2','filter3'), key = 2)

# Add all your application here
app.add_app('human',detect.app)
app.add_app('Image Upscaling',superImage.app)
app.add_app('Photo Pool',imageFinder.app)
app.add_app("Add filters to image", filters.app)
app.add_app('Rotate',rotate.app)
app.add_app("Sketch", sketch.app)
app.add_app("Image inpainting", inpaint.app)
app.add_app("Document Enhncer", docConv.app)
# app.add_app("Add Title to image", textonimg.app)
app.add_app("Crop an Image", Crop.app)
# app.add_app("Edge and Contour detection ", Edge_Cont.app)
# app.add_app("Face detection", Face_detect.app)
# app.add_app("Feature Detection", Feature_detect.app)
# app.add_app("Meet the team", abtus.app)


# The main app
app.run()