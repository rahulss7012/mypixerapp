import streamlit as st
import requests
import urllib.request
import io
from PIL import Image
import random

def app():

  # Create an input field and get the entered data
  user_input = st.text_input("Write your prompt")
  # st.write(user_input)


  selected_option = st.radio("Choose an option", ["thumb","small", "regular", "full"])
  fetch_button = st.button("Fetch API")
  # Fetch and display the data if the button is clicked
  if fetch_button:
    # Define the API URL
    base_url='https://api.unsplash.com/search/photos?page=1&query='
    url = base_url+user_input+'&client_id=6bCoKFvv4tDrJNlWd_Wys-BxwxMPPy9_2F9ndzWfdIQ'

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
       
        # Print the response content
        # print(response.json()['results'][0]['urls']['small'])
                # Define an array
        my_array = [0,1, 2, 3, 4]

        # Select a random element from the array
        random_element = random.choice(my_array)
        image_url=response.json()['results'][random_element]['urls'][selected_option]

     

        # # Create a download link for the image
        # download_link = f'<a href="data:image/jpeg;base64,{image_url.decode("utf-8")}" download="fetched_image.jpg">Download Image</a>'
        # st.markdown(download_link, unsafe_allow_html=True)

    else:
        # Print an error message if the request was not successful
        print(f'Request failed with status code {response.status_code}')

    st.image(image_url, caption='My Image')

    with urllib.request.urlopen(image_url) as url:

      image_data = url.read()

    image = Image.open(io.BytesIO(image_data))

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