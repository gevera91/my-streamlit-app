import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, world!")
name = st.text_input("What's your name?")
if st.button("Submit"):
    st.write(f"Hello, {name}!")