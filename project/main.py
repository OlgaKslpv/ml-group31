from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()
classifier = pipeline("sentiment-analysis",
                      model="snunlp/KR-FinBert-SC")

@app.get("/")
def root():
    return {"message": "Оценка эмоциональной окраски текста на корейском языке"}

@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text )[0]