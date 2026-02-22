from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from backend.services.inference import generate_inference

router = APIRouter()

class HelperPrompt(BaseModel):
    code : str



@router.post('/helper/{model_name}')
def generate_code(model_name: str , user_prompt: HelperPrompt):
    system_prompt = """
    You are a STRICT Python Code Reviewer.

    You must NOT generate new functions.
    You must NOT extend the code.
    You must NOT add new logic.

    Your job is ONLY to:

    1. Explain what the given code does.
    2. Add documentation (docstring + comments) to the SAME code.
    3. Identify bugs or issues.
    4. Suggest improvements in plain English.

    Return output in EXACT format:

    ---INFO---
    <short explanation>

    ---DOCUMENTED CODE---
    <same code with docstrings and comments>

    ---ANALYSIS---
    <bugs and improvements>

    Do NOT write anything else.
    """
    formatted_prompt = system_prompt + "\n" + user_prompt.code

    return StreamingResponse(
        generate_inference(model_name, formatted_prompt), 
        media_type="text/event-stream"  # Use event-stream for better browser handling
    )    