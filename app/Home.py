import streamlit as st

st.set_page_config(
    page_title="Welcome!",
    page_icon="👋",
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

st.write("# Welcome! 👋")

st.markdown(
"""
This is the placeholder for the Landing page.
"""
)
