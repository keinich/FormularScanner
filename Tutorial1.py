import torch

y = torch.cuda.is_available()

x = torch.randn(5, 2, 2, 3)
print(x)
