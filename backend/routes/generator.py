from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"Message": "Hello to new v1.1-dev"}



