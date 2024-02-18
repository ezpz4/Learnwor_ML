import pandas as pd
from training import training
from execute import execute
from crawling import fetch_news_article
import re

data = pd.read_csv('sc_dataset3.csv')

training()

#문장을 입력하면
#해당 문장에서 hard word에 해당하는 글자를 찾아야 함.
def find_word(input_sentence):
    for index, row in data.iterrows():
        hard_word = str(row['hard_word'])
        print(hard_word)
        if hard_word in input_sentence:
            return execute(hard_word, input_sentence)
        
    return print(input_sentence)
#그 단어를 training에 넘김
#예측된 쉬운 단어를 반환하여 문장


if __name__ == "__main__":
    input_sentence = input("문장 입력: ")
    paragraph = fetch_news_article(input_sentence)
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', paragraph)

    for sentence in sentences:
        find_word(sentence)


