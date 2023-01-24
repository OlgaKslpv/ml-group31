from transformers import pipeline
import streamlit as st
#fg
classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

st.write(classifier(st.text_input('Введите фразу для оценки...')))
