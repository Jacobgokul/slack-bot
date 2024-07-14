from pydantic import BaseModel
from typing import List

class QuestionRequest(BaseModel):
    questions: str