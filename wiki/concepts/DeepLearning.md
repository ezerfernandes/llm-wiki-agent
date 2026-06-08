---
title: "Deep Learning"
type: concept
tags: [ml-method, neural-networks, foundational]
sources: [d2l-preface, d2l-introduction, mlsysbook-ch01-introduction, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
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

## The systems reading (mlsysbook)

Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) frames deep learning as the era that **traded the [[FeatureEngineering|feature-engineering]] bottleneck for a compute bottleneck.** Removing hand-crafted features didn't make the problem easier — it shifted the binding constraint to infrastructure (distributed training, [[MemoryBandwidth|memory bandwidth]], energy). [[AlexNet]] (2012) is the canonical [[BitterLesson|systems co-design]] win (CNN matrix ops aligned with GPUs); [[GPT3|GPT-3]]-scale models illustrate the new ceiling (zettaFLOPs, ~1,287 MWh). The lesson: *systems* innovation, not algorithmic cleverness alone, enabled the deep-learning transition.

## Connections

- [[MachineLearning]] — parent field.
- [[BitterLesson]] / [[EfficiencyFramework]] / [[mlsysbook-ch01-introduction]] — the compute-bottleneck systems framing.
- [[NeuralNetwork]], [[Backpropagation]], [[GradientDescent]] — the substrate.
- [[RepresentationLearning]], [[EndToEndTraining]] — DL's two defining principles.
- [[d2l-preface]], [[d2l-introduction]] — corpus-anchor introductions.
- [[ComputerVision]], [[NLP]], [[SpeechRecognition]] — three transformed application domains.
- [[transformer]], [[CNN]], [[RNN]], [[lstm]] — major architecture families.
- [[mlsysbook-ch05-neural-computation]] — the *computational* reading: DL as a small set of primitives (matmul + [[ActivationFunction|activations]] + gradients), with depth/[[Compositionality|compositionality]] as the distinguishing mechanism and a ~1,092× MNIST compute escalation over rule-based code.
