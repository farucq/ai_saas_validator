import streamlit as st
from core.orchestrator import run_agents
from core.report_generator import generate_report

st.set_page_config(page_title="AI SaaS Idea Validator")

st.title("AI SaaS Idea Validator")

idea = st.text_area("Enter your startup idea")

if st.button("Validate Idea"):
    with st.spinner("Running Multi-Agent Analysis..."):
        results = run_agents(idea)
        report = generate_report(results, idea)

    st.markdown(report)