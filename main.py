from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User, UserWithAge, Feedback

app = FastAPI()

user = User(name="Эльхан Поладов", id=1)
feedbacks = []

@app.get("/")
async def get_html():
    return FileResponse("index.html")

@app.post("/calculate")
async def calculate(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}

@app.get("/users")
async def get_user():
    return user

@app.post("/user")
async def check_user(user_data: UserWithAge):
    is_adult = user_data.age >= 18
    return {
        "name": user_data.name,
        "age": user_data.age,
        "is_adult": is_adult
    }

@app.post("/feedback")
async def create_feedback(feedback: Feedback):

    feedbacks.append(feedback)

    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    }

@app.get("/feedbacks")
async def get_all_feedbacks():
    return {"feedbacks": feedbacks, "count": len(feedbacks)}