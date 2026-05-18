---
title: "Fine-Tuning"
type: concept
tags: [training, llm, transfer-learning, computer-vision]
sources: [d2l-computer-vision, d2l-nlp-applications]
last_updated: 2026-05-16
---

# Fine-Tuning

Continuing training of a pretrained model on a smaller, task-specific dataset to specialize its behavior. The canonical [[TransferLearning|transfer-learning]] technique — central to applied computer vision (ImageNet → downstream task) and to NLP / LLMs ([[BERT]] / [[GPT]] → task-specific head). Per [[d2l-computer-vision]] §`fine-tuning`: "When target datasets are much smaller than source datasets, fine-tuning helps to improve models' generalization ability."

## Four-step recipe (per [[d2l-computer-vision]])

1. **Pretrain** a neural network ("source model") on a large source dataset (e.g. [[ResNet|ResNet-18]] on [[ImageNet]]).
2. **Copy** all weights from the source model into a target model **except the output layer**. (The output layer's labels are task-specific; the feature-extracting layers learned generic image features that transfer.)
3. **Replace** the output layer with a randomly-initialized head sized to the target task's class count.
4. **Train end-to-end** on the target dataset with:
   - **Smaller LR on copied layers** (preserve learned features).
   - **Larger LR (typically $10\times$) on the new head** (learn from scratch faster).

## D2L's hot-dog example

ResNet-18 pretrained on ImageNet (1000 classes), fine-tuned to a 2-class hot-dog binary classifier on a 2000-image dataset. Backbone LR = $5\times10^{-5}$, head LR = $5\times10^{-4}$. PyTorch parameter-group syntax:

```python
params_1x = [p for n, p in net.named_parameters() if n not in ["fc.weight", "fc.bias"]]
trainer = torch.optim.SGD([
    {'params': params_1x},
    {'params': net.fc.parameters(), 'lr': learning_rate * 10},
], lr=learning_rate, weight_decay=0.001)
```

After 5 epochs, fine-tuned model substantially outperforms a from-scratch ResNet-18 with the same hyperparameters — "its initial parameter values are more effective."

## Variants

- **Full fine-tuning** — update all parameters (D2L's default).
- **Linear probe / feature extraction** — freeze the backbone, train only the head. Faster, more parameter-efficient, but lower ceiling.
- **Parameter-efficient fine-tuning (PEFT):** [[LoRA]] / [[AdapterLayers|adapter layers]] / prefix tuning — add a small number of trainable parameters while keeping the backbone frozen. The de facto standard for LLM fine-tuning.
- **Layer-wise LR decay** — generalization of D2L's "small LR for backbone, big LR for head" to a smooth gradient where lower layers get smaller LR than upper layers. Common in [[BERT]] / [[ViT]] fine-tuning.

## Why it works

The pretrained model has learned generic features (edges, textures, shapes, parts) that are useful across visual tasks. Fine-tuning preserves these and adapts the output layer + slightly perturbs the backbone for the target task. The smaller LR on the backbone is the canonical regularization preventing catastrophic forgetting of useful pretrained features.

## Connections

- [[TransferLearning]] / [[Pretraining]] / [[CNN]] / [[ResNet]] / [[ImageNet]] / [[BERT]] / [[GPT]] / [[LoRA]] / [[AdapterLayers]] / [[LLMFineTuning]].
- [[FCN]] / [[StyleTransfer]] / [[MaskRCNN]] / [[FasterRCNN]] / [[SSD]] — all of these models *begin* with a fine-tuning step from a pretrained classification backbone.
- [[d2l-computer-vision]] §`fine-tuning` — D2L's canonical worked CV example.
- [[d2l-nlp-applications]] §`finetuning-bert` / §`natural-language-inference-bert` — D2L's canonical worked NLP example, formalized as [[FineTuningBert]]: the *pretrained Transformer encoder + task head* template that's the NLP analogue of the CV recipe above.
