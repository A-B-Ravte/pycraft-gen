from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from  backend.services.inference import generate_inference

router = APIRouter()

class GeneratorPrompt(BaseModel):
    prompt : str


@router.post('/generate/{model_name}')
def generate_code(model_name: str , user_prompt: GeneratorPrompt):
    generator_prompt = """
    You are a senior Python developer.
    Generate clean production-ready Python code.
    Return only code.
    """

    formatted_prompt = generator_prompt + user_prompt.prompt

    return StreamingResponse(
        generate_inference(model_name, formatted_prompt), 
        media_type="text/event-stream"  # Use event-stream for better browser handling
    )
    
    

