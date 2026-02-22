from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from backend.services.inference import generate_inference

router = APIRouter()

class HelperPrompt(BaseModel):
    Code : str



@router.post('/helper-code/{model_name}')
def generate_code(model_name: str , user_prompt: HelperPrompt):
    system_prompt = """
    You are a Python code reviewer.

    1. Explain what the code does.
    2. Add documentation.
    3. Identify bugs.
    4. Suggest improvements.
    """

    formatted_prompt = system_prompt + user_prompt.prompt

    return StreamingResponse(
        generate_inference(model_name, formatted_prompt), 
        media_type="text/event-stream"  # Use event-stream for better browser handling
    )    