---
title: "rotten_tomatoes dataset"
type: entity
tags: [dataset, sentiment-analysis, nlp, benchmark]
sources: [hands-on-llm-ch04-text-classification, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# rotten_tomatoes dataset

A binary [[SentimentAnalysis|sentiment-analysis]] dataset of movie reviews, distributed on the [[HuggingFace|Hugging Face]] Hub as `rotten_tomatoes`. **5,331 positive + 5,331 negative reviews** sourced from the [Rotten Tomatoes](https://www.rottentomatoes.com/) film-review aggregator. Introduced in [[BoPang|Pang]] & [[LillianLee|Lee]] 2005, *"Seeing stars: Exploiting class relationships for sentiment categorization with respect to rating scales"* (arXiv:cs/0506075).

## Splits (per Ch 4)

| Split | Rows |
|---|---|
| train | 8,530 |
| validation | 1,066 |
| test | 1,066 |

Features: `text` (the review) and `label` (1 = positive, 0 = negative).

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

The chapter's chosen sentiment-classification benchmark — *"the well-known 'rotten_tomatoes' dataset to train and evaluate our models."* Used to compare four pretrained-LLM classification regimes on a single binary task:

| Regime | Model | F1 |
|---|---|---|
| Task-specific representation | [[TwitterRoBERTa]] | 0.80 |
| Embedding + [[LogisticRegression]] | [[AllMPNetBaseV2]] + sklearn | 0.85 |
| Zero-shot embedding | [[AllMPNetBaseV2]] + [[CosineSimilarity]] | 0.78 |
| Generative open-source | [[FLANT5]]-small | 0.84 |
| Generative closed-source | [[ChatGPT]] (gpt-3.5-turbo-0125) | 0.91 |

Loaded via:

```python
from datasets import load_dataset
data = load_dataset("rotten_tomatoes")
```

## Why it matters

A **smaller, balanced, Hugging-Face-distributed alternative** to the canonical Stanford [[IMDb|IMDb]] dataset (25k+25k reviews) for sentiment-analysis prototyping. Its size (~10.6k total) makes it tractable on a single Colab T4 across all four classification regimes the chapter compares.

## Connections

- [[hands-on-llm-ch04-text-classification]] — primary source.
- [[SentimentAnalysis]] / [[TextClassification]] / [[BinarySentimentClassification]] — the task category.
- [[IMDb]] — the larger sibling benchmark used by [[d2l-nlp-applications]].
- [[BoPang]] / [[LillianLee]] — paper authors.
- [[HuggingFace]] — dataset distribution channel.
- [[F1Score]] — the chapter's evaluation metric.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 reuses `rotten_tomatoes` as the **shared dataset across all four fine-tuning regimes** for representation models — a deliberate choice so the reader can compare Ch 4's frozen-model results to Ch 11's fine-tuning results on apples-to-apples data:

| Source | Regime | F1 |
|---|---|---|
| Ch 4 | [[TwitterRoBERTa]] (frozen task-specific) | 0.80 |
| Ch 4 | [[AllMPNetBaseV2]] + [[LogisticRegression]] (frozen embedding) | 0.85 |
| Ch 4 | [[FLANT5]]-small (generative encoder-decoder) | 0.84 |
| Ch 4 | [[ChatGPT]] gpt-3.5-turbo-0125 | 0.91 |
| **Ch 11** | **`bert-base-cased` full FT (1 epoch)** | **0.85** |
| **Ch 11** | **`bert-base-cased` freeze-blocks-0–9 (1 epoch)** | **0.80** |
| **Ch 11** | **`bert-base-cased` freeze-everything-but-head (1 epoch)** | **0.63** |
| **Ch 11** | **[[SetFit]] on 32 examples (16/class) — [[AllMPNetBaseV2]] base** | **0.85** |

Ch 11 also uses Rotten Tomatoes as the **[[ContinuedPretraining|continued-pretraining]] corpus** — strips labels with `tokenized_train.remove_columns("label")` and runs [[MaskedLanguageModel|MLM]] for 10 epochs to demonstrate the qualitative `fill-mask` domain shift (base BERT predicts `idea / dream / day` for *"What a horrible [MASK]!"*; MLM-continued predicts `movie / film / mess`).

The dataset's small balanced size (8,530 train / 1,066 test, 50/50 sentiment) makes all four regimes tractable on a single Colab T4, enabling the chapter's side-by-side comparison.
