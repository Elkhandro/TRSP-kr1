from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, MIREA!"}

@app.get("/hello")
def hello():
    return {"text": "This is second endpoint"}
