
import streamlit as st
import openai
import os

st.set_page_config(page_title="Aarva AI - From Insight to Impact")
st.title("Aarva: Your SLP Documentation Assistant")

st.sidebar.header("Session Details")

client_age = st.sidebar.text_input("Client Age:", "e.g., 4 years")
disorder_type = st.sidebar.selectbox("Disorder Type:", [
    "Articulation/Phonological Disorder",
    "Language Disorder",
    "Fluency Disorder",
    "Voice Disorder",
    "Swallowing/Dysphagia",
    "Cognitive-Communication Disorder",
    "AAC (Augmentative and Alternative Communication)",
    "Other"
])

goals_worked = st.sidebar.text_area("Goals Targeted in Session:")
therapy_activities = st.sidebar.text_area("Therapy Activities Used:")
outcome = st.sidebar.selectbox("Outcome:", [
    "Goal met",
    "Partial progress",
    "Minimal progress",
    "No progress"
])

if st.sidebar.button("Generate SOAP Note"):
    with st.spinner("Generating your documentation..."):
        prompt = f"""
        Write a SOAP note for a speech-language pathology session. 
        Client age: {client_age}
        Disorder type: {disorder_type}
        Goals: {goals_worked}
        Activities used: {therapy_activities}
        Outcome: {outcome}
        Follow the SLP SOAP note structure.
        """

        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        generated_text = response['choices'][0]['message']['content']
        st.subheader("Generated SOAP Note:")
        st.code(generated_text, language="markdown")
        st.success("You can now copy and paste this into your EHR.")

st.markdown("---")
st.markdown("**Disclaimer:** Do not input any identifiable patient data. This prototype is for de-identified clinical documentation only.")
