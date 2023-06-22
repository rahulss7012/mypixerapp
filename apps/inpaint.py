import cv2
import streamlit as st
from PIL import Image
import numpy as np
import io


def app():
        @st.cache_data
        def inpaint(image, mask, algorithm):
          # Convert the input image and mask to numpy arrays
          img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
          mask = cv2.cvtColor(np.array(mask), cv2.COLOR_RGB2GRAY)
          
          # Perform the image inpainting
          if algorithm == 'Telea':
              result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
          else:
              result = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
          
          # Convert the result to a PIL Image
          result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
          result = Image.fromarray(result)
          
          return result


        st.title('Image Inpainting')

        # Upload an image
        uploaded_image = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])

        # Upload a mask
        uploaded_mask = st.file_uploader('Choose a mask', type=['jpg', 'jpeg', 'png'])

        # Algorithm selection
        algorithm = st.selectbox('Select an algorithm', ['Telea', 'Navier-Stokes'])

        # Inpaint the image when both an image and mask have been uploaded
        if uploaded_image is not None and uploaded_mask is not None:
            image = Image.open(uploaded_image)
            mask = Image.open(uploaded_mask)
            size = (500, 500)
            img1_resized = image.resize(size)
            img2_resized = mask.resize(size)

            result = inpaint(img1_resized, img2_resized, algorithm)
            
            # Display the original image, mask, and inpainted image
            st.subheader('Original Image')
            st.image(image, use_column_width=True)
            
            st.subheader('Mask')
            st.image(mask, use_column_width=True)
            
            st.subheader('Inpainted Image')
            st.image(result, use_column_width=True)

            image = result

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






