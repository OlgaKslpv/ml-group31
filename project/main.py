from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

def preprocess(text: str) -> str:
    return text

def postprocess(result: List[Dict[str, Union[str, float]]]) -> Dict[str, Union[str, float]]:
    return result[0]
        
app = FastAPI()
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
