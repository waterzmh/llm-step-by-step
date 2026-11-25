import torch

vocabulary = ["<bos>", "我", "爱", "学习", "。", "你", "模型", "<eos>"]
vocabulary_size = len(vocabulary)


input_ids = torch.tensor([[0, 1, 2, 3, 4, 7]], dtype=torch.long)

print(input_ids)
print(input_ids.shape)
print(input_ids.dtype)