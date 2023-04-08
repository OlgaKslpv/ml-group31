from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from fastapi import HTTPException
from typing import List, Dict, Union

class Item(BaseModel):
    text: str

def preprocess(text: str) -> str:
    return text

def postprocess(result: List[Dict[str, Union[str, float]]]) -> Dict[str, Union[str, float]]:
    return result[0]

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": f"{exc.detail}"}

classifier = pipeline("sentiment-analysis",
                      model="snunlp/KR-FinBert-SC")

@app.get("/")
def root():
    return {"message": "Оценка эмоциональной окраски текста на корейском языке"}

@app.post("/predict/")
def predict(item: Item):
    processed_text = preprocess(item.text)
    raw_result = classifier(processed_text)
    return postprocess(raw_result)
