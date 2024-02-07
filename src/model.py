from transformers import BertForMaskedLM, AdamW

# BERT �� �ʱ�ȭ
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
model.train()

# ��Ƽ������ ����
optimizer = AdamW(model.parameters(), lr=5e-5)

# �н� ����
for epoch in range(3):  # �����δ� �� ���� ����ũ�� �ʿ��� �� �ֽ��ϴ�.
    for batch in loader:
        inputs, targets = batch
        optimizer.zero_grad()
        outputs = model(**inputs, labels=targets)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        print(f"Epoch: {epoch}, Loss: {loss.item()}")