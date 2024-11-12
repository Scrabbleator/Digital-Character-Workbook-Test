import streamlit as st

def diamond_character_section():
    st.subheader("The Diamond of Human Character")

    # Strengths
    st.write("**Strengths**")
    strengths = st.text_area("List your character’s top strengths.")
    strengths_impact = st.text_area("How do these strengths influence their actions and relationships?")

    # Weaknesses
    st.write("**Weaknesses**")
    weaknesses = st.text_area("What are the main flaws or fears that hold your character back?")
    weaknesses_impact = st.text_area("Describe situations where these weaknesses might create conflict or vulnerability.")

    # Motivations
    st.write("**Motivations**")
    motivations = st.text_area("What drives your character towards their goals?")
    motivation_events = st.text_area("Can you think of events that reinforce this motivation?")

    # Values
    st.write("**Values**")
    values = st.text_area("What core values shape your character's worldview and decisions?")
    values_challenges = st.text_area("How might these values be tested or challenged in your story?")

    # Summary of the Diamond
    st.write("**Character Diamond Summary**")
    st.markdown(f"""
    - **Strengths**: {strengths}
    - **Strengths Impact**: {strengths_impact}
    - **Weaknesses**: {weaknesses}
    - **Weaknesses Impact**: {weaknesses_impact}
    - **Motivations**: {motivations}
    - **Motivation Events**: {motivation_events}
    - **Values**: {values}
    - **Values Challenges**: {values_challenges}
    """)

