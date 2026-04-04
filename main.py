from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import UserWithId, User, Calculate, Feedback  

app = FastAPI()


feedbacks_db = [] 


# Задание 1.2 
@app.get("/")
def serve_html():
    return FileResponse("index.html")

# Задание 1.3 
@app.post("/calculate")
def calculate_sum(data: Calculate): 
    result = data.num1 + data.num2
    return {"result": result}

# Задание 1.4 
user = UserWithId(name="Вася Пупкин", id=1) 
@app.get("/users")
def get_user():
    return user

# Задание 1.5
@app.post("/user")
def create_user(user: User):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

# Задание 2.1 2.2
@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    feedbacks_db.append(feedback.dict())
    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    }