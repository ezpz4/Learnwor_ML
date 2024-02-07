from transformers import BertTokenizer
from datasets import load_dataset
import torch
from torch.utils.data import DataLoader, Dataset
import pandas as pd

# ������ �����ͼ� ����
data = {
    "difficult_word": ["esoteric", "quintessential", "pernicious"],
    "easy_word": ["complex", "perfect", "harmful"]
}
df = pd.DataFrame(data)

# BERT ��ũ������ �ʱ�ȭ
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# �����ͼ� Ŭ���� ����
class WordDataset(Dataset):
    def __init__(self, tokenizer, data, max_len=32):
        self.tokenizer = tokenizer
        self.data = data
        self.max_len = max_len
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        word_pair = self.data.iloc[idx]
        inputs = self.tokenizer(word_pair["difficult_word"], 
                                truncation=True, 
                                max_length=self.max_len, 
                                padding='max_length', 
                                return_tensors="pt")
        targets = self.tokenizer(word_pair["easy_word"], 
                                truncation=True, 
                                max_length=self.max_len, 
                                padding='max_length', 
                                return_tensors="pt")
        return inputs, targets["input_ids"][0]

# �����ͼ� �ν��Ͻ�ȭ �� DataLoader �غ�
dataset = WordDataset(tokenizer, df)
loader = DataLoader(dataset, batch_size=2, shuffle=True)