
import streamlit as st

def character_evaluation_section():
    st.subheader("Character Evaluation")

    # MBTI Type Selection
    st.write("**MBTI Trait Selection**")

    # Extraversion vs. Introversion
    ei_trait = st.selectbox("Extraversion (E) or Introversion (I)?", ["E", "I"])
    # Sensing vs. Intuition
    sn_trait = st.selectbox("Sensing (S) or Intuition (N)?", ["S", "N"])
    # Thinking vs. Feeling
    tf_trait = st.selectbox("Thinking (T) or Feeling (F)?", ["T", "F"])
    # Judging vs. Perceiving
    jp_trait = st.selectbox("Judging (J) or Perceiving (P)?", ["J", "P"])

    # Determine the MBTI type
    mbti_type = ei_trait + sn_trait + tf_trait + jp_trait
    st.write(f"**Determined MBTI Type**: {mbti_type}")

    # MBTI Profile Summary with All 16 Types
    profiles = {
        "INFJ": "INFJ: Insightful, idealistic, and driven by deep convictions.",
        "INTJ": "INTJ: Strategic, independent, and highly analytical.",
        "INFP": "INFP: Compassionate, introspective, and values-driven.",
        "INTP": "INTP: Logical, innovative, and driven by curiosity.",
        "ENFJ": "ENFJ: Charismatic, empathetic, and natural leaders.",
        "ENTJ": "ENTJ: Confident, assertive, and enjoys taking charge.",
        "ENFP": "ENFP: Enthusiastic, creative, and values personal freedom.",
        "ENTP": "ENTP: Witty, resourceful, and enjoys intellectual challenges.",
        "ISFJ": "ISFJ: Supportive, detail-oriented, and deeply loyal.",
        "ISTJ": "ISTJ: Responsible, organized, and values tradition.",
        "ISFP": "ISFP: Gentle, adaptable, and highly attuned to aesthetics.",
        "ISTP": "ISTP: Practical, observant, and enjoys hands-on activities.",
        "ESFJ": "ESFJ: Warm, organized, and highly attuned to others' needs.",
        "ESTJ": "ESTJ: Efficient, direct, and values order and structure.",
        "ESFP": "ESFP: Energetic, playful, and enjoys living in the moment.",
        "ESTP": "ESTP: Bold, action-oriented, and highly adaptable."
    }

    # Display the profile based on selected MBTI type
    profile_text = profiles.get(mbti_type, "No profile available for this MBTI type.")
    st.write(profile_text)
