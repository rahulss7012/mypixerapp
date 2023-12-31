# organizing imports
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import cv2
import io


DEMO_IMAGE = 'images/cricket.jpg'
def app():
    @st.cache_data
    def img2sketch(photo, k_size):
        #Read Image
        img = photo
        # Convert to Grey Image
        grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Invert Image
        invert_img=cv2.bitwise_not(grey_img)
        #invert_img=255-grey_img

        # Blur image
        blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

        # Invert Blurred Image
        invblur_img=cv2.bitwise_not(blur_img)
        #invblur_img=255-blur_img

        # Sketch Image
        sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
        #imporve contrast using histogram equilizationconda activate 
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        sketch_img = clahe.apply(sketch_img)

        return sketch_img

    st.title('Image Sketching with OpenCV')
    img_file_buffer = st.file_uploader("Upload an image", type=[ "jpg", "jpeg",'png'])
    if img_file_buffer is not None:
            image = np.array(Image.open(img_file_buffer))
    else:
        demo_image = DEMO_IMAGE
        image = np.array(Image.open(demo_image))

    st.image(image, caption=f"Original Image",use_column_width= True)


    if st.button("CONVERT"):

        k_size = 5
        
        resized_image = img2sketch(image , k_size)

        st.image(
        resized_image, caption=f"Drawing image", use_column_width=True)

        image = Image.fromarray(resized_image)

        # Create a BytesIO object to store the image data
        image_bytes = io.BytesIO()

        # Save the image as bytes in the BytesIO object
        image.save(image_bytes, format='PNG')
        image_bytes.seek(0)  # Reset the file pointer to the beginning

        # Create a download button for the image
        st.download_button(
            label='Download Image',
            data=image_bytes,
            file_name='image.png',
            mime='image/png'
        )

        