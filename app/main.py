import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="PyCraft-Gen")

# Mount static files (for CSS/JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

class CodeRequest(BaseModel):
    prompt: str

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_code(request: CodeRequest):
    try:
        # For now, this is a placeholder. 
        # Once your Colab training finishes, we will put the Inference logic here.
        user_input = request.prompt
        
        # Simulated response - we will replace this with your Model!
        generated_code = f"def solution():\n    # Optimized code for: {user_input}\n    pass"
        analysis = "✅ Complexity: O(n) | PEP8: Clean"
        
        return {"code": generated_code, "analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)