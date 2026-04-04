from pydantic import BaseModel, Field, field_validator


#1.4
class UserWithId(BaseModel):
    name: str
    id: int

#1.5 
class User(BaseModel):
    name: str
    age: int

# 1.3
class Calculate(BaseModel):
    num1: int
    num2: int

#задание 2.1 2.2
class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)
    
    @field_validator("message")
    @classmethod
    def check_bad_words(cls, value: str) -> str:
        bad_words = ["кринж", "рофл", "вайб"]
        lower_message = value.lower()
        for bad_word in bad_words:
            if bad_word in lower_message:
                raise ValueError("Использование недопустимых слов")
        
        return value