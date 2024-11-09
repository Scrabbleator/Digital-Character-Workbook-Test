import streamlit as st

def fruits_spoils_section():
    st.subheader("Fruits and Spoils")

    # Positive Traits (Fruits)
    st.write("**Positive Traits (Fruits)**")
    positive_trait = st.text_area("List a positive trait and describe its impact on the character’s journey.")
    positive_impact = st.slider("How strong is the impact of this positive trait?", 1, 5)  # Updated label
    st.write(f"Positive Trait: {positive_trait} | Impact Level: {positive_impact}")

    # Negative Traits (Spoils)
    st.write("**Negative Traits (Spoils)**")
    negative_trait = st.text_area("List a negative trait and describe its impact on the character’s journey.")
    negative_impact = st.slider("How strong is the impact of this negative trait?", 1, 5)  # Updated label
    st.write(f"Negative Trait: {negative_trait} | Impact Level: {negative_impact}")

    # Summary Reflection
    st.write("**Reflection**")
    reflection = st.text_area("Reflect on how the balance of positive and negative traits influences the character’s development.")
