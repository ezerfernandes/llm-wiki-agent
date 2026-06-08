---
title: "Masked Language Modeling"
type: concept
tags: [cs324, llm]
sources: [cs324-training, cs324-modeling]
last_updated: 2026-06-04
---

Masked language modeling (MLM) is a training objective that reconstructs masked or corrupted tokens from surrounding bidirectional context. BERT masks 15% of tokens using the 80-10-10 rule (80% replaced with [MASK], 10% with a random token, 10% left unchanged), giving the model a denoising objective rather than next-token prediction.

## Connections
- [[MaskedLanguageModel]] — the model class trained with this objective
- [[BERT]] — canonical model using MLM
- [[cs324-training]] — discussed in this CS324 lecture
- [[cs324-modeling]] — discussed in this CS324 lecture
