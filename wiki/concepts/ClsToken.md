---
title: "`<cls>` Token"
type: concept
tags: [transformer, embedding]
sources: [d2l-attention-and-transformers, d2l-nlp-applications]
last_updated: 2026-05-16
---

# `<cls>` Token

A special learnable token prepended to the input sequence whose final-layer representation serves as a **global / sequence-level summary**. Introduced by [[BERT]] for sentence classification and adopted by the [[VisionTransformer|Vision Transformer]] for image classification.

## Mechanism

The `<cls>` (class) token starts as a learnable embedding (no special semantic content). It participates in every self-attention layer like any other token — but because attention is all-to-all, after a few layers `<cls>` aggregates information from all other positions. Its final-layer representation is fed to a downstream classification head.

## Two canonical uses

- **[[BERT]]** — `<cls>` representation → linear head → sentiment / classification logits. Also used for the next-sentence-prediction pretraining objective. [[d2l-nlp-applications]] §`finetuning-bert` shows the `<cls>` hidden state is the **universal handle** for sequence-level fine-tuning ([[SentimentAnalysis]] / [[NaturalLanguageInference|NLI]] / [[SemanticTextualSimilarity|STS]]) — see [[FineTuningBert]].
- **[[VisionTransformer|ViT]]** — `<cls>` representation, after a final LayerNorm, → linear layer → image-class logits.

## Alternatives

- **Averaged patch / token representations.** Equivalent in some settings; the [[d2l-attention-and-transformers|D2L exercise]] suggests projecting the average instead of `<cls>`.
- **Learned pooling tokens.** Multiple cls-like tokens for multi-label or multi-task settings.

## See also

- [[VisionTransformer]] · [[BERT]] · [[Transformer]] · [[PatchEmbedding]] · [[SelfAttention]]
