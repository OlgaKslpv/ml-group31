from transformers import pipeline
result = pipeline("sentiment-analysis", "cointegrated/rubert-tiny-toxicity")
result("Иди ты нафиг!")