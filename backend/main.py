from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import generator, helper

app = FastAPI(title="PyCraft-Gen v1.1")

# -------------------------
# ENABLE CORS
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (for dev)
    allow_credentials=True,
    allow_methods=["*"],   # allow POST, GET, OPTIONS, etc
    allow_headers=["*"],
)

# -------------------------
# ROUTES
# -------------------------
app.include_router(generator.router, prefix="/api")
app.include_router(helper.router, prefix="/api")

@app.get("/")
def root():
    return {"status": "PyCraft-Gen running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=False)


