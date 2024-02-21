import streamlit as st
st.write("Hello World")
num1 = st.number_input("Enter the Number 1")
num2 = st.number_input("Enter the Number 2")
if st.button("Add"):
    st.write(f"#{num1 + num2}")
    st.balloons()

st.camera_input("hehe hehe")
st.file_uploader("Upload your anything")