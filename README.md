# Shakespeare GPT

This repo contains the code pertaining to a demonstrative GPT (Generative Pre-trained Transformer) model that generates Shakespeare like text. This repo is for educational purpses only and is a great introduction to GPT nueral nets and specifically the concept of self-attention.


#### Just one line to run!

![Alt Text](https://github.com/bjudson1/shakespeare-gpt/blob/main/etc/shakespeare-gpt-demo.gif)


#### GPU is highly recommended! Training/Hosting may not work on CPU in reasonable time frame

![Alt Text](https://github.com/bjudson1/shakespeare-gpt/blob/main/etc/gpu.gif)


As mentioned, this tutorial is a great introduction to transformers and specifically the concept of "self-attention", the technique that have helped transformers to have such a meteroic rise in the space of deep learning.
![Alt Text](https://github.com/bjudson1/shakespeare-gpt/blob/main/etc/transformer-arch.png)

This demonstration was heavily influenced by [Andrej Karpathy's video leacture](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=367s&ab_channel=AndrejKarpathy) on GPT nueral networks.

## How to Use
A GPU is heavily recommended to run these scripts.

### Inference
```
cd shakespeare-gpt
python predict.py
```

### Training
```
cd shakespeare-gpt
python train.py
```

## Repo Layout


###### /video-tutorial
This directory contains the code that was generated as I went through Adrej Karpathy's youtube video linked below.


###### /shakespeare-gpt
This directory contains a repackaged implementation of shakespear-gpt with training and inference seperated. Also allows users to save and load trained models.

###### /etc
This directory contains extra media etc.


## Refrences
- [Attention Is All You Need Paper](https://arxiv.org/abs/1706.03762)
- [Andrej Karpathy Video Lecture](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=367s&ab_channel=AndrejKarpathy)
- [Andrej Karpathy Video Lecture Git Repo](https://github.com/karpathy/ng-video-lecture)
- [Nano GPT Repo](https://github.com/karpathy/nanoGPT)
