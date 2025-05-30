import streamlit as st
# Streamlit application example

# Title
st.title("Hello, AIML!")

# Simple text
st.write("Welcome to your first Streamlit app.")

# You can also use markdown
st.markdown("### This is a markdown header")

# Add an interactive button
if st.button("Say Hello"):
    st.success("Hello from Streamlit! 👋")
