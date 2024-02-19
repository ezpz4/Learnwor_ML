import pandas as pd
from konlpy.tag import Okt
import re
from crawling import fetch_news_article
import openai
OPENAI_API_KEY = "key"

openai.api_key = OPENAI_API_KEY


df = pd.read_csv('sc_dataset3.csv', encoding='utf-8')
hw_list=[]

def find_and_replace(input_sentence):
    okt = Okt() 
    words = okt.morphs(input_sentence)  # 문장을 형태소 단위로 분리

    # 어려운 단어를 찾아서 대체
    for i in range(len(words)):
        if words[i] in df['hard_word'].values:
            index = df[df['hard_word'] == words[i]].index[0]
            easy_word = df.at[index, 'easy_word']
            hw_list.append(words[i])
            words[i] = easy_word

    output_sentence = ' '.join(words)
    
    #openai 활용
    messages = []
    content = output_sentence

    messages.append({"role": "user", "content": content + "문장 어색한 부분만 수정해"})

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    chat_response = completion.choices[0].message.content

    return chat_response
    

if __name__ == "__main__" :
    #views.py 에서 수정되어야 함.

    input_sentence = input("링크를 입력하세요: ")
    paragraph = fetch_news_article(input_sentence)

    #구두점, 물음표, 느낌표 기준으로 분리
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', paragraph)

    modified_paragraph = ' '.join(find_and_replace(sentence) for sentence in sentences)

    print(modified_paragraph)


    # for sentence in sentences:
    #     print(find_and_replace(sentence))
    #     # """
    #     # print("원래 문장: " + sentence)
    #     # print("바뀐 문장: " + find_and_replace(sentence))
    #     # print("")
    #     # """
    
    # # print("바뀐문장",all_sentence)

