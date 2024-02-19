import pandas as pd
from konlpy.tag import Okt
import openai
OPENAI_API_KEY = "key"

openai.api_key = OPENAI_API_KEY

df = pd.read_csv('../Learnwor_ML/sc_dataset3.csv', encoding='utf-8')
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
    return output_sentence

user_input = input("문장을 입력하세요: ")

result = find_and_replace(user_input)

print("어려운 단어:", hw_list)
print("변환된 문장:", result)


#openai 활용
messages = []
content = result
original_content = content 

messages.append({"role": "user", "content": content + "문장을 자연스럽게 수정해"})

completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

chat_response = completion.choices[0].message.content
print(f'ChatGPT: {chat_response}')