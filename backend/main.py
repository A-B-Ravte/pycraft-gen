from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"Message": "Hello to new v1.1-dev"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=False)



