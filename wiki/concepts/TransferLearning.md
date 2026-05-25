---
title: "Transfer Learning"
type: concept
tags: [training, pretrained-models]
sources: [madewithml-transformers, d2l-computer-vision, ai-engineering-ch07-finetuning]
last_updated: 2026-05-23
---

# Transfer Learning

Reusing knowledge from a model pretrained on one task ("source task" / "source dataset") to bootstrap learning on another ("target task" / "target dataset"). The default paradigm of applied deep learning since ~2014 — modern models are almost never trained from scratch.

## The economic argument (per [[d2l-computer-vision]] §`fine-tuning`)

Collecting and labeling large datasets is expensive: "in order to collect the [[ImageNet]] dataset, researchers have spent millions of dollars from research funding." For most practical problems the available labeled data is between [[FashionMNIST]] (60k) and ImageNet (10M) sizes — too small to train modern CNNs / transformers from scratch without overfitting.

The transfer-learning shortcut: pretrain once on a large generic source dataset, then adapt the pretrained model to many small target tasks. Each adaptation reuses the expensive feature learning.

## Mechanism

The pretrained model's lower layers learn **generic features** (edges, textures, shapes in CV; subword embeddings, syntactic patterns in NLP) that are useful across tasks. Higher layers learn **task-specific** representations that need to be replaced or specialized.

## Forms

- **[[FineTuning|Fine-tuning]]** — copy all weights, replace output head, continue training (smaller LR on backbone). The dominant flavor in [[d2l-computer-vision]].
- **Feature extraction / linear probe** — freeze backbone, train only a new head. Cheaper but lower ceiling.
- **Parameter-efficient fine-tuning** — [[LoRA]] / [[AdapterLayers|adapters]] / prefix tuning — train a small parameter delta on a frozen backbone. Standard for LLM fine-tuning.
- **Zero-shot transfer** — no target-task gradient updates at all; rely on the pretrained model's generalization (LLM in-context learning, CLIP for image classification).

## Where transfer learning shows up across the wiki

- **CV:** ImageNet-pretrained [[ResNet]] / [[VGG]] → fine-tuned for detection ([[SSD]] / [[FasterRCNN]]), segmentation ([[FCN]]), style transfer ([[StyleTransfer]]), classification ([[CIFAR10]] / dog-breed). The unifying theme of [[d2l-computer-vision]].
- **NLP:** [[BERT]] / [[T5]] / [[GPT]] pretrained on web text → fine-tuned for downstream classification, QA, summarization.
- **LLMs:** post-pretraining adaptation via [[SFT|supervised fine-tuning]], [[RLHF]], [[Constitutional AI]], or parameter-efficient methods.
- **Multimodal:** [[CLIP]] image-text pretraining → zero-shot or fine-tuned downstream classification.

## Failure mode

[[NegativeTransfer|Negative transfer]] — the pretrained features actively hurt downstream performance when source and target domains are too dissimilar (e.g. medical imaging without medical-imaging pretraining).

## Connections

- [[FineTuning]] / [[Pretraining]] / [[NegativeTransfer]] / [[LLMFineTuning]] / [[LoRA]] / [[AdapterLayers]] / [[BERT]] / [[GPT]] / [[T5]] / [[CLIP]] / [[ImageNet]] / [[ResNet]] / [[CNN]].
- [[d2l-computer-vision]] §`fine-tuning` — D2L's canonical CV example.
- [[madewithml-transformers]] — Made With ML's NLP framing.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

Ch 7 opens with the **transfer-learning framing of finetuning**: "transfer learning improves sample efficiency, allowing a model to learn the same behavior with fewer examples. A sample-efficient model learns effectively from fewer samples." [[ChipHuyen|Huyen]] uses the [[InstructGPT|InstructGPT]] (2022) framing — finetuning is *unlocking capabilities a model already has but that are difficult for users to access via prompting alone*.

### Two transfer-learning modes Ch 7 distinguishes

- **[[FineTuning|Finetuning]]** — continue training the model itself (the chapter's main subject).
- **[[FeatureBasedTransfer|Feature-based transfer]]** — train a model to extract feature embeddings, then use those features in *another* model (e.g., add a classifier head). Common in computer vision (ImageNet-pretrained backbones → object detection / segmentation). The 2010s-CV default; less common in LLM applications.

### Sample-efficiency comparison

> "While training a model from scratch for legal question answering may need millions of examples, finetuning a good base model might only require a few hundred." — Ch 7

This is the empirical claim that anchors the chapter's pro-finetuning argument — though [[ChipHuyen|Huyen]] immediately tempers it with the "earn it via prompting first" rule.
