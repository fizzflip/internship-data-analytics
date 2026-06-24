import streamlit as st

st.set_page_config(page_title="Sample Code Demo")

st.header("Company Name")
st.subheader("Data Analytics")
st.write("Data Analytics and Visualization")
st.text("This is Text.")

input_name = st.text_input("Enter your Name", placeholder="Enter your Name")
st.write("Your name is:", input_name)

input_age = st.number_input("Enter your Age", min_value=0, max_value=100, step=1)
st.write("Your age is:", input_age)

select_box = st.selectbox("Select your skills", ["DA", "Web Development", "AI"])
st.write("Your skills are:", select_box)

multi_select = st.multiselect("Select your skills", ["DA", "WD", "AI", "ML"])
st.write("Your skills are:", ",".join(multi_select))

skill_bar = st.slider("Rate Yourself", min_value=1, max_value=5, step=1)
st.write("Your rate yourself as:", skill_bar)

st.button("Click me")
