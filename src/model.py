from transformers import BertForMaskedLM, AdamW

# BERT 모델 초기화
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
model.train()

# 옵티마이저 설정
optimizer = AdamW(model.parameters(), lr=5e-5)

# 학습 루프
for epoch in range(3):  # 실제로는 더 많은 에포크가 필요할 수 있습니다.
    for batch in loader:
        inputs, targets = batch
        optimizer.zero_grad()
        outputs = model(**inputs, labels=targets)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        print(f"Epoch: {epoch}, Loss: {loss.item()}")