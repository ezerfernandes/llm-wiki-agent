---
title: "Ankur Parikh"
type: entity
tags: [researcher, nlp, attention]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# Ankur Parikh

NLP researcher (Google Research; previously [[CarnegieMellonUniversity|CMU]] PhD). **First author of the decomposable attention model** (Parikh, Täckström, Das & Uszkoreit, EMNLP 2016, "A Decomposable Attention Model for Natural Language Inference") — a pre-[[1706.03762-attention-is-all-you-need|Transformer]] application of pure attention + MLPs to NLI that achieved the SNLI SOTA of its time with **far fewer parameters than recurrent / convolutional alternatives**.

The decomposable attention model is operationalized in [[d2l-nlp-applications]] §`natural-language-inference-attention` as D2L's canonical attention-based NLI model — published one year before Vaswani et al. 2017, it foreshadows the scaled dot-product attention pattern (independent token-projection $f$ then dot product) that makes self-attention efficient.

## Connections

- [[DecomposableAttention]] — flagship contribution.
- [[NaturalLanguageInference]] / [[SNLI]] — task and benchmark.
- [[Attention]] / [[SelfAttention]] / [[Transformer]] — direct architectural lineage.
- [[d2l-nlp-applications]].
