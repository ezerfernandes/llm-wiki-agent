---
title: "Mike Schuster"
type: entity
tags: [person, researcher, deep-learning, speech, nlp]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Mike Schuster

German computer scientist; speech and language researcher. Co-author with [[KuldipPaliwal|Kuldip Paliwal]] of the seminal **bidirectional recurrent neural networks** paper (Schuster & Paliwal 1997) — the second foundational RNN architecture innovation of 1997, alongside [[LSTM]] ([[d2l-recurrent-modern]] §index). Long career at ATR (Japan), [[google|Google]] (where he contributed to Google Neural Machine Translation), and Two Sigma.

## Why he matters here

- **Bidirectional RNN (1997).** Co-author of the [[BidirectionalRNN|bi-RNN]] paper — the design where two unidirectional RNNs run forward and backward over the same input and concatenate their outputs. The architecture is mostly useful for sequence encoding and is "very costly to train due to long gradient chains" ([[d2l-recurrent-modern]] §bi-rnn). Crucial for downstream BERT-style masked-language-modeling pretraining.
- **GNMT.** At [[google|Google]] Schuster co-led Google Neural Machine Translation, which deployed deep LSTM seq2seq + attention to production translation in 2016.

## Connections

- [[KuldipPaliwal]] — bi-RNN co-author.
- [[BidirectionalRNN]] — the architecture.
- [[google]] — institutional home during the GNMT era.
- [[d2l-recurrent-modern]] — D2L cites Schuster & Paliwal 1997.
