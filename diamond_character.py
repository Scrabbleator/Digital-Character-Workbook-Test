import streamlit as st

def diamond_character_section():
    st.subheader("Diamond of Human Character")
    
    # Strengths
    st.write("**Strengths**")
    strength = st.text_area("Identify your character’s top strengths.")
    strength_influence = st.text_area("How do these strengths influence their relationships and decisions?")
    
    # Weaknesses
    st.write("**Weaknesses**")
    weakness = st.text_area("What are the main flaws or fears that hold your character back?")
    weakness_conflict = st.text_area("In what situations do these weaknesses create conflict or drive change?")

    # Motivations
    st.write("**Motivations**")
    motivation = st.text_area("What drives your character to pursue their goals?")
    motivation_events = st.text_area("Are there specific events that reinforce this motivation?")

    # Values
    st.write("**Values**")
    values = st.text_area("What core values shape your character's worldview?")
    values_decisions = st.text_area("How do these values shape their moral decisions?")
    
    # Display summary
    st.markdown(f"**Character Traits Summary**:\n\n- Strengths: {strength}\n- Weaknesses: {weakness}\n- Motivations: {motivation}\n- Values: {values}")
