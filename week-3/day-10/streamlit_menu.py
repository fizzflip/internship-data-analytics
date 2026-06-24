import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        "Company",
        options=["Home", "About Us", "Contact"],
        icons=["house", "info-circle", "telephone"],
        default_index=0, orientation="vertical"
    )

if selected == "Home":
    st.header("Home")
    st.write("This is home page")

if selected == "About Us":
    st.header("About Us")
    st.info("This page in under development!")

if selected == "Contact":
    st.header("Contact")
    st.write("This is contact page")
