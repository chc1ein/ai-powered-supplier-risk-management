import streamlit as st
from dotenv import load_dotenv
import ray

from app.libs.crew import SupplierRiskAssessmentCrewPOC

load_dotenv()

st.set_page_config(
    page_title="Initial PoC!",
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


st.markdown(
"""
# Supplier Risk Management Tool

This is a Proof of Concept (POC) built on top of https://exa.ai/ and https://crewai.com/ technologies. It aims to provide a comprehensive tool for assessing supplier risks.

"""
)

name = st.text_input("Supplier Name", "Festo Se & Co.KG")
address = st.text_input("Supplier Address", "Ruiter Str. 82, 73734 Esslingen")
homepage = st.text_input("Supplier Homepage", "http://www.festo.com")

@ray.remote(num_cpus=1)
def kickoff_wrapper():
    result = SupplierRiskAssessmentCrewPOC().crew().kickoff(inputs={
        "supplier_info": {
            "name": name,
            "address": address,
            "homepage": homepage,
        }
    })
    return result

def run_poc():
    future = kickoff_wrapper.remote()
    result = ray.get(future)
    result_container.write(result.raw)

st.button("Run POC", type="primary", on_click=run_poc)

result_container = st.container(border=True)
log_container = st.container(border=True)

