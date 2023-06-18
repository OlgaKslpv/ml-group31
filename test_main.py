from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Оценка эмоциональной окраски текста на корейском языке"}

def test_predict_positive():
    response = client.post("/predict/",
                           json={"text": "서귀포시 강창식 전 국장 등 25명 정년·명예퇴임"})
    json_data = response.json()

    assert response.status_code == 200
    assert json_data['label'] == 'neutral'

def test_predict_negative():
    response = client.post("/predict/",
                           json={"text": "C쇼크에 멈춘 흑자비행…대한항공 1분기 영업적자 566억"})
    json_data = response.json()

    assert response.status_code == 200
    assert json_data['label'] == 'negative'

def test_get_emotions():
    response = client.get("/emotions/")
    assert response.status_code == 200
    assert response.json() == {"emotions": ["positive", "neutral", "negative"]}
