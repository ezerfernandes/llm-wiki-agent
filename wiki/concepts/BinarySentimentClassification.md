---
title: "Binary Sentiment Classification"
type: concept
tags: [nlp, classification, sentiment-analysis]
sources: [hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# Binary Sentiment Classification

The simplest [[SentimentAnalysis|sentiment-analysis]] task variant: assign each input text one of **two polarity labels** — typically `positive` (1) and `negative` (0). The canonical benchmark form, used as the smoke-test task across most pretrained-LLM classification regimes.

## Common benchmarks

| Dataset | Size | Domain | Used by |
|---|---|---|---|
| [[IMDb]] | 25k train + 25k test | Movie reviews | [[d2l-nlp-applications]] |
| [[RottenTomatoes|Rotten Tomatoes]] | 8,530 train + 1,066 test | Movie reviews | [[hands-on-llm-ch04-text-classification]] |
| SST-2 | ~67k train | Movie reviews | [[DistilBERT]]-SST2 |
| Yelp Polarity | 560k train | Yelp reviews | Sentiment-fine-tune literature |

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 explicitly frames its task as binary sentiment classification:

> "These short reviews are either labeled as positive (1) or negative (0). This means that we will focus on **binary sentiment classification**." — Ch 4

The chapter then runs four pretrained-LLM regimes on this single binary task ([[RottenTomatoes|Rotten Tomatoes]]) and reports weighted-average [[F1Score|F1]] for each — the comparison table is the chapter's pedagogical centerpiece.

## Connections

- [[SentimentAnalysis]] — the parent task category.
- [[TextClassification]] / [[Classification]] — the broader categories.
- [[RottenTomatoes]] / [[IMDb]] — canonical datasets.
- [[F1Score]] / [[ConfusionMatrix]] / [[Precision]] / [[Recall]] / [[Accuracy]] — evaluation metrics.
- [[hands-on-llm-ch04-text-classification]] — primary source.
