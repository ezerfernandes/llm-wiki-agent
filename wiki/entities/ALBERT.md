---
title: "ALBERT"
type: entity
tags: [model, llm, transformer, encoder-only, bert-family, google-research]
sources: [hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# ALBERT

**A Lite BERT for Self-Supervised Learning of Language Representations** — Lan et al., 2019 (arXiv:1909.11942). A parameter-reduced [[bert|BERT]] variant from [[google|Google Research]] using **factorized embedding parameterization** and **cross-layer parameter sharing**; ALBERT-base has ~12M parameters (vs BERT-base's 110M) while preserving most of the downstream-task performance.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 lists ALBERT among the BERT-family baselines for text classification:

> "Over the years, many variations of BERT have been developed, including RoBERTa, DistilBERT, ALBERT, and DeBERTa, each trained in various contexts. ... Consider them solid baselines: BERT base (uncased), RoBERTa base, DistilBERT base (uncased), DeBERTa base, bert-tiny, **ALBERT base v2**." — Ch 4

## Two parameter-reduction tricks

1. **Factorized embedding parameterization.** Decompose the vocab × hidden embedding matrix `V × H` into `V × E` and `E × H` where `E ≪ H`. For ALBERT-large, `H = 1024`, `E = 128` cuts embedding params by ~80%.
2. **Cross-layer parameter sharing.** Share the Transformer encoder block's weights across all layers. ALBERT-large's 24 layers all share one set of weights — vs BERT-large's 24 independent layers.

ALBERT also replaces [[NextSentencePrediction|NSP]] with **sentence-order prediction (SOP)** — distinguishing the correct order of two consecutive sentences from the reversed order — claiming this is harder and more useful than NSP.

## Connections

- [[bert]] — the predecessor.
- [[google]] — Google Research produced ALBERT.
- [[RepresentationModel]] — the model category.
- [[hands-on-llm-ch04-text-classification]] — primary source.
