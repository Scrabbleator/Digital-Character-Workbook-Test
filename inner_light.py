import streamlit as st

def inner_light_section():
    st.subheader("The Inner Light")

    # Core Purpose
    st.write("**Core Purpose**")
    core_purpose = st.text_area("Describe your character’s deepest motivations and purpose.")
    
    # Brightness Scale (Polarity Scale)
    st.write("**Inner Light Brightness**")
    brightness = st.slider("Set the brightness of your character's 'inner light' (1 = Dim, 5 = Bright)", 1, 5)
    st.write(f"Inner Light Brightness Level: {brightness}")

    # Reflection
    st.write("**Reflection on Inner Light**")
    inner_light_reflection = st.text_area("Reflect on how this 'inner light' guides your character’s decisions and growth.")
    
    # Display summary
    st.markdown(f"**Summary**:\n\n- Core Purpose: {core_purpose}\n- Brightness Level: {brightness}\n- Reflection: {inner_light_reflection}")
