import sys
# import json
# from datetime import datetime

# from markdown_pdf import MarkdownPdf, Section
from .crew import SupplierRiskAssessmentCrew, SupplierRiskAssessmentCrewPOC


def run_poc():
    """
    Run the crew.
    """
    inputs = {
        # "supplier_info": {
        #     "name": "Festo Se & Co.KG",
        #     "address": "Ruiter Str. 82, 73734 Esslingen",
        #     "homepage": "http://www.festo.com",
        # }
        # "supplier_info": {
        #     "name": "Sommer GmbH",
        #     "address": "Steinbeisstr. 9, 71691 FREIBERG/N.",
        #     "homepage": "http://www.sommer.de",
        # }
        # "supplier_info": {
        #     "name": "Max Lamb GmbH & Co.KG",
        #     "address": "Am Bauhof 2, 97076 Würzburg",
        #     "homepage": "http://www.lamb.de",
        # }
        "supplier_info": {
            "name": "RÖCO GmbH",
            "address": "KORTENTAL 67, 44149 DORTMUND",
            "homepage": "http://www.roeco.de",
        }
    }

    result = SupplierRiskAssessmentCrewPOC().crew().kickoff(inputs=inputs)

    # pdf = MarkdownPdf(toc_level=1)
    # pdf.add_section(Section(result.raw))
    # pdf.save(f"{inputs['supplier_info']['name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")

    # if result.json_dict:
    #     print(f"JSON Output: {json.dumps(result.json_dict, indent=2)}")


def run():
    """
    Run the crew.
    """
    inputs = {
        "supplier_info": {
            "name": "Festo Se & Co.KG",
            "address": "Ruiter Str. 82, 73734 Esslingen",
            "homepage": "http://www.festo.com",
        }
    }

    result = SupplierRiskAssessmentCrew().crew().kickoff(inputs=inputs)

    # pdf = MarkdownPdf(toc_level=1)
    # pdf.add_section(Section(result.raw))
    # pdf.save(f"{inputs['supplier_info']['name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")

    # if result.json_dict:
    #     print(f"JSON Output: {json.dumps(result.json_dict, indent=2)}")



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        SupplierRiskAssessmentCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SupplierRiskAssessmentCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        SupplierRiskAssessmentCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
