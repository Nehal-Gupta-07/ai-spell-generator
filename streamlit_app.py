import streamlit as st
import requests

st.title("🔮 AI Spell Generator")
st.write("Enter your problem, and get a magical spell suggestion!")

# User Input
user_input = st.text_input("Describe your problem:")

if st.button("Suggest Spell"):
    if user_input:
        response = requests.post("http://127.0.0.1:5000/suggest", json={"problem": user_input})
        
        if response.status_code == 200:
            data = response.json()
            st.success(f"**Suggested Spell:** {data['spell']}")
            st.info(f"**Description:** {data['description']}")
        else:
            st.error(f"Error: {response.status_code}")
    else:
        st.warning("Please enter a problem description!")
