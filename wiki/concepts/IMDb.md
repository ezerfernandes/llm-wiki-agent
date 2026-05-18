---
title: "IMDb (Large Movie Review Dataset)"
type: concept
tags: [dataset, nlp, sentiment-analysis, benchmark]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# IMDb

Stanford's **large movie review dataset** (Maas, Daly, Pham et al. 2011, "Learning Word Vectors for Sentiment Analysis") — the canonical [[SentimentAnalysis|sentiment-analysis]] benchmark. Per [[d2l-nlp-applications]] §`sentiment-analysis-and-dataset`: "25 000 movie reviews downloaded from IMDb" in each of training and testing sets, with balanced "positive" / "negative" labels.

## Structure

- 25 000 train + 25 000 test reviews; balanced positive / negative classes.
- D2L preprocessing: word-level tokenization → vocab with `min_freq=5` → truncate / pad to `num_steps=500`.

## Connections

- [[SentimentAnalysis]] — task it benchmarks.
- [[StanfordUniversity]] — origin (Maas et al.).
- [[TextCNN]] / [[BidirectionalRNN]] / [[BERT]] — models trained on it in [[d2l-nlp-applications]].
- [[d2l-nlp-applications]] §`sentiment-analysis-and-dataset`.
