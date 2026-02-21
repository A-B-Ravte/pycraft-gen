import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv


'''
This is version 1.0 
'''
# 1. IMPORT YOUR ENGINE
from app.engine import PyCraftEngine

load_dotenv()

app = FastAPI(title="PyCraft-Gen")

# 2. INITIALIZE THE ENGINE (Point to your 4.36GB file)
# This loads the model into RAM once when the server starts
MODEL_PATH = "models/qwen2.5-coder-7b-instruct.Q4_K_M.gguf"
engine = PyCraftEngine(MODEL_PATH)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

class CodeRequest(BaseModel):
    prompt: str

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

'''
@app.post("/generate")
async def generate_code(request: CodeRequest):
    try:
        user_input = request.prompt
        
        # 1. Generate the code
        code_prompt = f"Write Python code for: {user_input}"
        generated_code = engine.generate(code_prompt)
        
        # 2. Generate the analysis (A second call to the model)
        # We use a specific prompt to keep it short
        analysis_prompt = f"Briefly explain the time complexity of this code: {generated_code}"
        analysis_result = engine.generate(analysis_prompt)
        
        return {
            "code": generated_code, 
            "analysis": analysis_result
        }
    except Exception as e:
        return {"code": "Error", "analysis": str(e)}
'''
@app.post("/generate")
async def generate_code(request: CodeRequest):
    # Ensure we are returning the generator itself
    return StreamingResponse(
        engine.generate_stream(request.prompt), 
        media_type="text/event-stream"  # Use event-stream for better browser handling
    )

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=False)