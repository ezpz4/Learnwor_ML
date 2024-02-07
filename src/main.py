from transformers import BertTokenizer, BertForMaskedLM
import torch

# 모델과 토크나이저 초기화
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')

# 어려운 단어 예시
difficult_words = ["esoteric", "quintessential", "pernicious", "aberration", "Effervescent","Juxtapose"]

# 각 어려운 단어에 대해 쉬운 단어로의 매핑 시도
for word in difficult_words:
    # '[MASK]' 토큰으로 단어를 대체
    text = f"This is an [MASK] concept."
    # 텍스트를 토큰화
    inputs = tokenizer(text, return_tensors="pt")
    # 모델 예측
    with torch.no_grad():
        predictions = model(**inputs).logits

    # 가장 가능성 높은 단어 찾기
    predicted_index = torch.argmax(predictions[0, inputs['input_ids'][0] == tokenizer.mask_token_id], dim=1)
    predicted_token = tokenizer.convert_ids_to_tokens(predicted_index)[0]
    print(f"Original: {word}, Predicted: {predicted_token}")
