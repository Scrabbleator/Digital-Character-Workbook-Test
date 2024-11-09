import streamlit as st
from basic_profile import basic_profile_section

st.title("Digital Character Workbook Test")
st.write("This is a basic test to ensure Streamlit is working correctly.")

# Display Basic Profile Section
st.header("Basic Profile")
basic_profile_section()
