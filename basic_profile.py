import streamlit as st

def basic_profile_section():
    st.subheader("Basic Profile")
    
    # Basic information fields
    name = st.text_input("Character Name")
    age = st.text_input("Age")
    gender = st.selectbox("Gender", ["Male", "Female", "Non-Binary", "Other"])
    occupation = st.text_input("Occupation/Role")
    residence = st.text_input("Place of Residence")
    core_beliefs = st.text_area("Core Beliefs or Values")
    
    # Display summary of the profile in real-time
    st.markdown(f"**Profile Summary**:\n\n- Name: {name}\n- Age: {age}\n- Gender: {gender}\n- Occupation: {occupation}\n- Residence: {residence}\n- Core Beliefs: {core_beliefs}")
