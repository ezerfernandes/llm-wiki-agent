---
title: "Deep Learning"
type: concept
tags: [ml-method, neural-networks, foundational]
sources: [d2l-preface, d2l-introduction]
last_updated: 2026-05-16
---

# Deep Learning

Subfield of [[MachineLearning|machine learning]] using multi-layered [[NeuralNetwork|neural networks]] trained end-to-end with gradient-based optimization on large datasets. Subject of *Dive into Deep Learning* ([[d2l-preface]]); per [[d2l-introduction]], deep learning has reshaped [[ComputerVision]], [[NLP]], [[SpeechRecognition]], [[reinforcementlearning]], and biomedical informatics.

## Defining property — per [[d2l-introduction]]

> "What differentiates deep learning is that the operations learned at each of the many layers of representations are learned jointly from data."

Two interlocking principles capture this:

- **[[RepresentationLearning|Multi-level representation learning]]** — instead of one handcrafted feature map (Canny edges, [[SIFT|SIFT]]) feeding a shallow predictor, the model learns a **stack** of representations, each tuned for what the next layer needs.
- **[[EndToEndTraining|End-to-end training]]** — every layer's parameters are tuned by [[Backpropagation|backprop]] against the *final* task loss, eliminating manual [[FeatureEngineering|feature engineering]] and dissolving the boundaries between [[ComputerVision]] / [[SpeechRecognition]] / [[NLP]] application stacks.

## Why now — the three forces

[[d2l-introduction]] traces the post-2010 revival to **data + compute + algorithms**, all arriving together:

| Force | Specifics |
|---|---|
| **Data** | Web-scale corpora, cheap sensors, Kryder's-law storage; the 1970→2020 table goes from 100 Iris examples to 1T social-network examples. |
| **Compute** | Moore's-law CPUs *and* — crucially — [[GPUMemoryHierarchy\|GPUs originally engineered for gaming]]; 100 KF (1970) → 1 PF (2020). |
| **Algorithms** | [[Dropout]] (capacity control), [[Attention]] (1014→) and [[transformer\|Transformers]] (2017), large-scale [[languagemodel\|language models]] / ChatGPT, multi-stage memory networks, [[generativeadversarialnetwork\|GANs]] → [[DiffusionModel\|diffusion models]], 1024-GPU distributed SGD, framework generations ([[Caffe]] / [[Torch]] / [[Theano]] → [[TensorFlow]] + [[Keras]] → [[Chainer]] / [[PyTorch]] / [[JAX]]). |

Many "modern" components — [[MultilayerPerceptron|MLPs]] (McCulloch-Pitts 1943), [[CNN|CNNs]] (LeCun-Bottou-Bengio-Haffner 1998), [[lstm|LSTM]] (Hochreiter-Schmidhuber 1997), [[QLearning|Q-learning]] (Watkins-Dayan 1992) — were essentially *rediscovered* after lying dormant. The revival is what the chapter calls a "Cambrian explosion."

## Connections

- [[MachineLearning]] — parent field.
- [[NeuralNetwork]], [[Backpropagation]], [[GradientDescent]] — the substrate.
- [[RepresentationLearning]], [[EndToEndTraining]] — DL's two defining principles.
- [[d2l-preface]], [[d2l-introduction]] — corpus-anchor introductions.
- [[ComputerVision]], [[NLP]], [[SpeechRecognition]] — three transformed application domains.
- [[transformer]], [[CNN]], [[RNN]], [[lstm]] — major architecture families.
