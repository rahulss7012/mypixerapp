import streamlit as st
import requests

st.title('Contact Form')

# Get user input
name = st.text_input('Name')
email = st.text_input('Email')
message = st.text_area('Message')

if st.button('Submit'):
    if name and email and message:
        # Send form data to Getform.io API
        form_data = {
            'name': name,
            'email': email,
            'message': message
        }
        response = requests.post('https://getform.io/f/5dcff465-3e50-4e0b-9a80-37996c4b06fb', data=form_data)
        if response.status_code == 200:
            st.success('Message sent!')
        else:
            st.error('Error sending message. Please try again later.')
    else:
        st.warning('Please fill in all fields.')
