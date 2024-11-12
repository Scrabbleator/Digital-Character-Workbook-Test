import streamlit as st

def biblical_mirror_section():
    st.subheader("Biblical Mirror")

    # MBTI Type Input
    st.write("**Character's MBTI Type**")
    mbti_type = st.selectbox("Select the character's MBTI type", [
        "INFJ", "INTJ", "INFP", "INTP",
        "ENFJ", "ENTJ", "ENFP", "ENTP",
        "ISFJ", "ISTJ", "ISFP", "ISTP",
        "ESFJ", "ESTJ", "ESFP", "ESTP"
    ])

    # Mapping MBTI types to Biblical figures
    biblical_figures = {
        "INFJ": {
            "name": "Joseph",
            "summary": "Joseph was visionary and idealistic, known for his ability to interpret dreams and his unwavering faith despite adversity."
        },
        "INTJ": {
            "name": "Daniel",
            "summary": "Daniel was strategic and insightful, demonstrating wisdom and integrity while serving in a foreign court."
        },
        "INFP": {
            "name": "David",
            "summary": "David was compassionate and introspective, a poet and leader who sought after God's heart."
        },
        "INTP": {
            "name": "Solomon",
            "summary": "Solomon was known for his wisdom and quest for understanding, delving deep into the nature of life."
        },
        "ENFJ": {
            "name": "Joshua",
            "summary": "Joshua was charismatic and inspiring, leading others with confidence and faith."
        },
        "ENTJ": {
            "name": "Paul",
            "summary": "Paul was assertive and strategic, a leader who was instrumental in spreading early Christianity."
        },
        "ENFP": {
            "name": "Peter",
            "summary": "Peter was enthusiastic and adaptable, often acting on impulse but with a heart for others."
        },
        "ENTP": {
            "name": "Moses",
            "summary": "Moses was innovative and resourceful, leading his people through challenges with perseverance."
        },
        "ISFJ": {
            "name": "Ruth",
            "summary": "Ruth was loyal and compassionate, demonstrating steadfastness and care in her relationships."
        },
        "ISTJ": {
            "name": "Noah",
            "summary": "Noah was dependable and dutiful, faithfully carrying out tasks with precision."
        },
        "ISFP": {
            "name": "Mary",
            "summary": "Mary was gentle and nurturing, embracing her role with humility and grace."
        },
        "ISTP": {
            "name": "Abraham",
            "summary": "Abraham was practical and observant, showing faith through action."
        },
        "ESFJ": {
            "name": "Martha",
            "summary": "Martha was hospitable and organized, attentive to the needs of those around her."
        },
        "ESTJ": {
            "name": "Nehemiah",
            "summary": "Nehemiah was efficient and structured, leading projects with clear vision and order."
        },
        "ESFP": {
            "name": "Samson",
            "summary": "Samson was energetic and bold, known for his physical strength and love of life's pleasures."
        },
        "ESTP": {
            "name": "Jacob",
            "summary": "Jacob was adaptable and action-oriented, navigating life's twists with cunning and resourcefulness."
        }
    }

    # Retrieve the Biblical figure based on MBTI type
    figure = biblical_figures.get(mbti_type)

    if figure:
        st.write(f"**Biblical Figure Comparison: {figure['name']}**")
        st.write(f"_{figure['summary']}_")

        # Reflection Prompts
        st.write("**Reflection Questions**")
        st.text_area("How does your character's journey compare to that of {}? In what ways can lessons from {}'s life inform your character's development?".format(figure['name'], figure['name']))
    else:
        st.write("No Biblical figure found for this MBTI type.")

