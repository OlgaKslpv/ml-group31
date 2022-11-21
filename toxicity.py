!pip install transformers sentencepieces
result = pipeline("sentiment-analysis", "cointegrated/rubert-tiny-toxicity")
result(Иди ты нафиг!)