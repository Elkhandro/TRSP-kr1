from fastapi import FastAPI

# Создаем экземпляр приложения (переменная называется app)
app = FastAPI()

# Определяем маршрут для корневого URL "/"
@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}