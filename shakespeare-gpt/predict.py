import torch
from GPTLanguageModel import GPTLanguageModel

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# here are all the unique characters that occur in this text
chars = sorted(list(set(text)))
itos = { i:ch for i,ch in enumerate(chars) }
decode = lambda l: ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string



print(torch.load('model.pth'))


# load the model
m = GPTLanguageModel(65)
m.load_state_dict(torch.load('model.pth'))
m = m.to(device)

# generate from the model
context = torch.zeros((1, 1), dtype=torch.long, device=device)
print(decode(m.generate(context, max_new_tokens=500)[0].tolist()))
#open('more.txt', 'w').write(decode(m.generate(context, max_new_tokens=10000)[0].tolist()))