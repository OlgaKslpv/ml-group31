from transformers import pipeline
import streamlit as st
result = pipeline("sentiment-analysis", "cointegrated/rubert-tiny-toxicity")

object = st.text_input('Введите фразу')

st.write(result(object))