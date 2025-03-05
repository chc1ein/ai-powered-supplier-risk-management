import streamlit as st
import ray

if __name__ == '__main__':
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

    @st.cache_resource
    def initialize_ray():
        # You can configure this init call to point to a separate machine.
        ray.init()

    initialize_ray()