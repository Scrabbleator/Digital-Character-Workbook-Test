import streamlit as st

def fruits_spoils_section():
    st.subheader("Fruits and Spoils")

    # Define pairs of traits for Fruits of the Spirit and Spoils (Negative Traits)
    traits = {
        "Love": "Hatred",
        "Joy": "Despair",
        "Peace": "Conflict",
        "Patience": "Impatience",
        "Kindness": "Cruelty",
        "Goodness": "Corruption",
        "Faithfulness": "Faithlessness",
        "Gentleness": "Harshness",
        "Self-control": "Recklessness"
    }

    # Display each pair with a slider
    for fruit, spoil in traits.items():
        st.write(f"**{fruit} vs. {spoil}**")
        leaning = st.slider(f"Lean towards {fruit} or {spoil}", -5, 5, 0)
        if leaning > 0:
            st.write(f"Leaning towards: {fruit} (+{leaning})")
        elif leaning < 0:
            st.write(f"Leaning towards: {spoil} ({leaning})")
        else:
            st.write("Balanced between both traits")

    # Reflection Summary
    st.write("**Reflection on Character's Moral Balance**")
    reflection = st.text_area("Reflect on how these traits shape your character's overall moral and ethical balance.")
