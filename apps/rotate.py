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
    def rotateImage(photo,angleRotate):
        img=photo
        # Get the image height and width
        height, width = img.shape[:2]
        # Define the rotation angle (in degrees)
        angle = angleRotate

        # Calculate the rotation matrix
        M = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)

        # Apply the rotation to the image
        rotated_img = cv2.warpAffine(img, M, (width, height))

        return rotated_img
    st.title('Image Rotation with OpenCV')
    angle_choice = st.sidebar.radio(label="Angle choice", options=["45", "90", "135", "180","225","270","315","360"])
    angle_dict = {"45": (45),
                    "90": (90),
                    "135": (135),
                    "180": (180),
                    "225": (225),
                    "270": (270),
                    "315": (315),
                    "360": (360),

                    }
    ang = angle_dict[angle_choice]




    img_file_buffer = st.file_uploader("Upload an image", type=[ "jpg", "jpeg",'png'])
    if img_file_buffer is not None:
            image = np.array(Image.open(img_file_buffer))
    else:
        demo_image = DEMO_IMAGE
        image = np.array(Image.open(demo_image))

    st.image(image, caption=f"Original Image",use_column_width= True)
    
    if st.button("Rotate"):
         
         final_img = rotateImage(image,ang)

         st.image(
          final_img, caption=f"Drawing image", use_column_width=True)
         
         image = Image.fromarray(final_img)

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
         

        

