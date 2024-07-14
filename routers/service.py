import os
import traceback
from fastapi import APIRouter, status, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from utilities.generic import extract_text_from_pdf, post_answer_to_slack
from utilities.ai_utils import CustomAgent
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix="/service",
    tags=["Service API"]
)

@router.post("/answer-questions/")
async def answer_questions(question: str = Form(...), file: UploadFile = File(...)):
    try:
        if file.content_type != "application/pdf":
            return JSONResponse(
                status_code= status.HTTP_412_PRECONDITION_FAILED,
                content= "Provide only pdf document"
            )
        
        text = extract_text_from_pdf(await file.read())
        

        openai_api_key = os.getenv("OPENAI_API_KEY")
        openai_model = os.getenv("OPENAI_MODEL")
        agent = CustomAgent(api_key=openai_api_key, model= openai_model)
        
        answer = agent.process_questions(text, question)
        
        slack_token = os.getenv("SLACK_WEBHOOK_URL")
        slack_response = post_answer_to_slack(answer, slack_token)
        
        return JSONResponse(
            status_code= status.HTTP_200_OK,
            content= {
                "AI Response": answer,
                "Slack Response": slack_response
            }
        )
    except HTTPException as e:
        traceback.print_exc()
        return JSONResponse(
            status_code= e.status_code,
            content= e.detail
        )
    except:
        traceback.print_exc()
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content= "Something went wrong."
        )