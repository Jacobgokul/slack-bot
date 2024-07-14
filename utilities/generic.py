import requests
import logging
import fitz
from fastapi import HTTPException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_file):
    document = fitz.open(stream=pdf_file, filetype="pdf")
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text


def post_answer_to_slack(answer, slack_token):
    print(slack_token)
    response = requests.post(
        url=slack_token,
        data='{"text":"%s"}' % answer
    )

    if response and response.status_code == 200:
        return "Answer Posted in slack channel"
    
    elif response.status_code != 200:
        logger.warning(f"Slack not responding due to status code: {response.status_code} and content: {response.content.decode("utf-8")}")
        raise HTTPException(
            status_code=response.status_code, 
            detail= "Slack not responding"
        )
        