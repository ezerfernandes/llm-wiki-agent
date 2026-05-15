---
title: "Masked Language Model"
type: concept
tags: [concept, pretraining, objective]
sources: [1810.04805-bert]
last_updated: 2026-05-10
---

# Masked Language Model

Pre-training objective introduced (or popularized) by [[BERT]] in [[1810.04805-bert]]. Inspired by the Cloze task (Taylor, 1953): randomly mask a fraction of input tokens and predict the originals from surrounding context. This breaks the dependency cycle that would otherwise prevent bidirectional conditioning — a deep bidirectional model trained on standard next-token prediction could trivially "see itself" through multiple layers.

## BERT's specific recipe
- Mask **15%** of WordPiece tokens per sequence.
- Of the chosen positions: **80%** replaced with `[MASK]`, **10%** with a random token, **10%** left unchanged.
- Only the masked positions contribute to the cross-entropy loss.

The 80/10/10 split mitigates the **pre-train / fine-tune mismatch** that arises because `[MASK]` never appears during fine-tuning. The "10% unchanged" branch biases the representation toward the actual observed token.

MLM converges marginally slower than left-to-right LM (since only 15% of positions contribute gradient per batch), but the absolute task accuracy crosses over almost immediately, and the deep bidirectionality is empirically responsible for the majority of BERT's improvement over GPT-style baselines.

Variants: SpanBERT (mask contiguous spans), ELECTRA (replaced-token detection), T5 (sentinel-token span corruption), and the implicit-MLM objective of many later encoder models all descend from this design.
