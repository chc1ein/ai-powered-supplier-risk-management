import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Supplier Risk Management",
    layout="wide",
)

st.markdown("""
    <style>
            .o-minimal-header__actions { display: none !important; }
            .o-minimal-header__logo { display: none !important; }
            .modana-footer-sidebar { display: none !important; }
            .stAppDeployButton {display:none;}
    </style>
""", unsafe_allow_html=True)

st.write("# Supplier Risk Management (PoC)")

st.markdown(
"""
This is a Proof of Concept (POC) aims to provide a comprehensive tool for assessing supplier risks.
"""
)

