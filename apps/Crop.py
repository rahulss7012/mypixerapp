import streamlit as st
from streamlit_cropper import st_cropper
import cv2
from PIL import Image
import io

def app():
    st.set_option('deprecation.showfileUploaderEncoding', False)

    # Upload an image and set some options for demo purposes
    st.header("Cropper Demo")
    img_file = st.sidebar.file_uploader(label='Upload a file', type=['png', 'jpg','jpeg'])
    realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
    box_color = st.color_picker(label="Box Color", value='#0000FF')
    aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
    aspect_dict = {"1:1": (1,1),
                    "16:9": (16,9),
                    "4:3": (4,3),
                    "2:3": (2,3),
                    "Free": None}
    aspect_ratio = aspect_dict[aspect_choice]

    if img_file:
        img = Image.open(img_file)
        if not realtime_update:
            st.write("Double click to save crop")
        # Get a cropped image from the frontend
        cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
                                    aspect_ratio=aspect_ratio)
        
        # Manipulate cropped image at will
        st.write("Preview")
        _ = cropped_img.thumbnail((200,200))
        st.image(cropped_img)
        

        image = cropped_img

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

          