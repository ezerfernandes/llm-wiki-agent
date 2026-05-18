---
title: "Sentiment Analysis"
type: concept
tags: [nlp, text-classification, application]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# Sentiment Analysis

The NLP task of classifying the affective polarity (positive / negative — or finer-grained scale) of a text. Per [[d2l-nlp-applications]] §`sentiment-analysis-and-dataset`: "studies people's sentiments in their produced text, such as product reviews, blog comments, and forum discussions." A canonical instance of single-text [[TextClassification|text classification]] — "transforms a varying-length text sequence into a fixed-length text category."

## Canonical benchmark

The Stanford **[[IMDb]] large movie review dataset** (Maas, Daly, Pham et al. 2011) — 25k training + 25k testing reviews, balanced positive / negative labels — is the textbook benchmark. D2L's preprocessing recipe: tokenize → vocab with `min_freq=5` → truncate/pad to 500 tokens.

## Architectures (per [[d2l-nlp-applications]])

- **RNN baseline** (§`sentiment-analysis-rnn`): frozen [[GloVe]] embeddings → 2-layer [[BidirectionalRNN|bidirectional]] [[LSTM]] → concatenate hidden states at initial and final time steps → FC head with 2 outputs.
- **[[TextCNN|textCNN]] baseline** (§`sentiment-analysis-cnn`): two GloVe embedding tracks (one trainable, one frozen) → multiple 1-D convolutions (widths 3 / 4 / 5, 100 channels each) → [[MaxOverTimePooling|max-over-time pooling]] → concat → dropout → FC head.
- **Fine-tuned [[BERT]]** (§`finetuning-bert`): the [[ClsToken|`[CLS]`]] hidden state → MLP head; all encoder parameters fine-tuned. The modern dominant approach when compute permits.

## Applications

Politics (public sentiment toward policies), finance (market sentiment), marketing (product research and brand management).

## Connections

- [[TextClassification]] / [[NLP]] / [[FineTuning]].
- [[TextCNN]] / [[BidirectionalRNN]] / [[BERT]] / [[GloVe]] / [[LSTM]] — architectural ingredients.
- [[IMDb]] — the canonical dataset.
- [[d2l-nlp-applications]] §`sentiment-analysis-*` — the four worked-example sections.
