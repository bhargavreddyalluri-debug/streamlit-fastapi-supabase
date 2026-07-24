import streamlit as st
import requests

st.title("Registration Form")

name = st.text_input("Enter your Name")
email = st.text_input("Enter your Email")
password = st.text_input("Enter your Password", type="password")

if st.button("Submit"):

    payload = {
        "name": name,
        "email": email,
        "password": password
    }

    try:
        response = requests.post(
    "https://streamlit-fastapi-backend.onrender.com/register",
    json=payload)           
    

        if response.status_code == 200:

            result = response.json()

            user = result["data"][0]

            st.success(result["message"])

            st.write("### User Details")
            st.write(f"**ID:** {user['id']}")
            st.write(f"**Name:** {user['name']}")
            st.write(f"**Email:** {user['email']}")

        else:
            st.error("Registration Failed")

    except Exception as e:
        st.error(f"Error: {e}")