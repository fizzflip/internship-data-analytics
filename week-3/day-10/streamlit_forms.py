import streamlit as st

with st.form(key="form"):
    email = st.text_input("Email", placeholder="something@mail.com")
    password = st.text_input("Enter your Password", type="password")
    date_input = st.date_input("Enter your Date (YYYY-MM-DD)")
    radio = st.radio("Select you gender: ", ("Male", "Female", "Other"))
    upload_file = st.file_uploader("Upload your file", type=["jpg", "png", "txt"])
    checkbox = st.checkbox("I agree with Terms & Conditions")

    btn = st.form_submit_button(label="Submit")
    if btn:
        st.write("Emails is: ", email)
        st.write("Password is: ", password)
