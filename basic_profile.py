import streamlit as st

def basic_profile_section():
    st.subheader("Basic Profile")

    # Core Character Details
    st.write("**Core Character Details**")
    name = st.text_input("Character Name")
    age = st.text_input("Age")
    gender = st.selectbox("Gender", ["Male", "Female", "Non-Binary", "Other"])
    role = st.text_input("Role/Occupation")

    # Physical Traits
    st.write("**Physical Traits**")
    height = st.text_input("Height")
    build = st.text_input("Build")
    hair_color = st.text_input("Hair Color")
    eye_color = st.text_input("Eye Color")
    distinctive_features = st.text_area("Distinctive Features")

    # Personality Overview
    st.write("**Personality Overview**")
    archetype = st.selectbox("Character Archetype", ["Hero", "Rebel", "Mentor", "Sage", "Other"])
    primary_traits = st.multiselect("Primary Traits", ["Brave", "Compassionate", "Impulsive", "Cunning", "Loyal", "Mysterious"])

    # Core Beliefs and Values
    st.write("**Core Beliefs and Values**")
    core_beliefs = st.text_area("Core Beliefs or Philosophy")
    guiding_value = st.text_input("Guiding Value (e.g., Justice, Freedom)")

    # Background and Relationships
    st.write("**Background and Relationships**")
    backstory = st.text_area("Brief Backstory")
    relationships = st.text_area("Notable Relationships (e.g., family, mentors, rivals)")

    # Goal and Conflict
    st.write("**Goal and Conflict**")
    primary_goal = st.text_input("Primary Goal")
    central_conflict = st.text_area("Central Conflict or Main Struggle")

    # Real-Time Profile Summary
    st.write("**Character Profile Summary**")
    st.markdown(f"""
    - **Name**: {name}
    - **Age**: {age}
    - **Gender**: {gender}
    - **Role**: {role}
    - **Physical Traits**: Height - {height}, Build - {build}, Hair Color - {hair_color}, Eye Color - {eye_color}, Distinctive Features - {distinctive_features}
    - **Personality**: Archetype - {archetype}, Primary Traits - {', '.join(primary_traits)}
    - **Core Beliefs**: {core_beliefs}
    - **Guiding Value**: {guiding_value}
    - **Background**: {backstory}
    - **Relationships**: {relationships}
    - **Goal**: {primary_goal}
    - **Conflict**: {central_conflict}
    """)

