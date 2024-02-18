# 새로운 데이터에 대한 예측
from joblib import load
import numpy as np

def execute(word, sentence):
    model = load('model.joblib')
    print(model)
    print(word)
    new_words = [word]  # 실제 예측하고 싶은 어려운 단어 리스트
    print(new_words)
    predicted_easy_words = model.predict(new_words)
    print("예측된 쉬운 단어:", predicted_easy_words)

    new_sentence = sentence.replace(word, str(predicted_easy_words[0]))
    return print(new_sentence)