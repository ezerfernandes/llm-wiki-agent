---
title: "RoBERTa"
type: entity
tags: [model, llm, transformer, encoder-only, bert-family, facebook-ai]
sources: [hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# RoBERTa

**Robustly Optimized BERT Pretraining Approach** — Liu et al., 2019 (arXiv:1907.11692). A re-trained [[bert|BERT]] with **larger batches, more data, longer training, no [[NextSentencePrediction|NSP]] objective, and dynamic masking**. Demonstrated that BERT was significantly undertrained — RoBERTa matches or exceeds BERT-large on most benchmarks.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 lists RoBERTa among the BERT-family baselines for text classification:

> "Over the years, many variations of BERT have been developed, including RoBERTa, DistilBERT, ALBERT, and DeBERTa, each trained in various contexts." — Ch 4

The chapter uses [[TwitterRoBERTa|`cardiffnlp/twitter-roberta-base-sentiment-latest`]] — a [[CardiffNLP|Cardiff NLP]] fine-tune of RoBERTa-base on tweets — as its **task-specific representation-model** demo (F1 = 0.80 on [[RottenTomatoes|Rotten Tomatoes]]).

## Key differences from BERT

| Property | BERT | RoBERTa |
|---|---|---|
| NSP objective | Yes | **Removed** |
| Masking | Static (precomputed once) | **Dynamic** (re-sampled per epoch) |
| Training data | 16 GB (BookCorpus + Wiki) | **160 GB** (adds CC-News, OpenWebText, Stories) |
| Batch size | 256 | **8K** |
| Training steps | 1M | **500K** at 8K batch (≈4× more compute) |
| Tokenization | WordPiece (30K) | **byte-level [[BPE]]** (50K) |

## Connections

- [[bert]] — the predecessor.
- [[TwitterRoBERTa]] — Ch 4's worked fine-tune.
- [[CardiffNLP]] — the group behind Twitter-RoBERTa.
- [[meta]] — RoBERTa's authors were at Facebook AI Research (now Meta AI).
- [[RepresentationModel]] — the model category.
- [[hands-on-llm-ch04-text-classification]] — primary source.
