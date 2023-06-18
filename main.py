from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from fastapi import HTTPException
from typing import List, Dict, Union
from dataclasses import dataclass

@dataclass
class User:
    """Представление пользователя с его ID и адресом электронной почты."""
    id: int
    email: str

class Item(BaseModel):
    """Модель запроса для предсказания эмоциональной окраски текста."""
    text: str

def preprocess(text: str) -> str:
    return text

def postprocess(result: List[Dict[str, Union[str, float]]]) -> Dict[str, Union[str, float]]:
    return result[0]

app = FastAPI()

user_repository = {1: User(1,"jjj@hhh.com"), 2: User(2, "ggg@bbb.com")}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": f"{exc.detail}"}

classifier = pipeline(
    "sentiment-analysis",
    model="snunlp/KR-FinBert-SC"
    )

@app.get("/")
def root():
    return {"message": "Оценка эмоциональной окраски текста на корейском языке"}

@app.post("/predict/")
def predict(item: Item):
    processed_text = preprocess(item.text)
    raw_result = classifier(processed_text)
    return postprocess(raw_result)

@app.get("/get-user", summary="Получить пользователя по ID")
def get_user_by_id(user_id: int):
    if user_id not in user_repository:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user_repository[user_id]}
