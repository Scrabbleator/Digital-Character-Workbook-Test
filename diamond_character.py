import streamlit as st

def diamond_character_section():
    st.subheader("The Diamond of Human Character")

    # Track Completion of Each Facet
    facets_completed = 0

    # Strengths
    st.write("**Strengths**")
    strengths = st.text_area("List your character’s top strengths.")
    strengths_impact = st.text_area("How do these strengths influence their actions and relationships?")
    if strengths and strengths_impact:
        facets_completed += 1  # Increase completion if Strengths are filled

    # Weaknesses
    st.write("**Weaknesses**")
    weaknesses = st.text_area("What are the main flaws or fears that hold your character back?")
    weaknesses_impact = st.text_area("Describe situations where these weaknesses might create conflict or vulnerability.")
    if weaknesses and weaknesses_impact:
        facets_completed += 1

    # Motivations
    st.write("**Motivations**")
    motivations = st.text_area("What drives your character towards their goals?")
    motivation_events = st.text_area("Can you think of events that reinforce this motivation?")
    if motivations and motivation_events:
        facets_completed += 1

    # Values
    st.write("**Values**")
    values = st.text_area("What core values shape your character's worldview and decisions?")
    values_challenges = st.text_area("How might these values be tested or challenged in your story?")
    if values and values_challenges:
        facets_completed += 1

    # Diamond Visual Placeholder (can be replaced with graphics or icons)
    st.write("### Diamond Visualization")
    st.write(f"Facets completed: {facets_completed}/4")
    if facets_completed == 4:
        st.success("The diamond is fully filled!")
    else:
        st.info("Complete all facets to fill the diamond.")

