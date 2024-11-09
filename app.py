import streamlit as st
from basic_profile import basic_profile_section
from diamond_character import diamond_character_section
from character_evaluation import character_evaluation_section
# from biblical_mirror import biblical_mirror_section  # Commented out for now
from fruits_spoils import fruits_spoils_section

st.title("Digital Character Workbook Test")
st.write("This is a basic test to ensure Streamlit is working correctly.")

# Display Basic Profile Section
st.header("Basic Profile")
basic_profile_section()

# Display Diamond of Human Character Section
st.header("Diamond of Human Character")
diamond_character_section()
