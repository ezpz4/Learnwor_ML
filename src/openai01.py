import openai
OPENAI_API_KEY = ""
openai.api_key = OPENAI_API_KEY


messages=[]
# while True:
content = input("User: ")
original_content = content  # 원본 입력을 유지

messages.append({"role": "user", "content": content + " 문장을 자연스럽게 만들어줘"})

completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

chat_response = completion.choices[0].message.content
print(f'ChatGPT: {chat_response}')

# 원하는 단어 변화 추출
# original_words = original_content.split()
# modified_words = chat_response.split()
# word_changes = [(original_word, modified_word) if original_word != '증시의' else ('증시의', '주식 시장의') for original_word, modified_word in zip(original_words, modified_words)]
# print("Word changes:", word_changes)

messages.append({"role": "assistant", "content": chat_response})