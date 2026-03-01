
from fastapi import FastAPI

my_application = FastAPI()

@my_application.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}