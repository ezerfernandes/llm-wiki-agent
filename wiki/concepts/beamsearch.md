---
title: "Beam Search"
type: concept
tags: [decoding, inference]
sources: [1409.3215-seq2seq]
last_updated: 2026-05-10
---

# Beam Search

An approximate decoding algorithm for auto-regressive sequence models that maintains the top-B partial hypotheses at each step instead of greedily committing to the single best token. Given a model `p(y_t | y_{<t}, x)`, beam search extends each of the B running hypotheses with every possible next token, then keeps the B highest-log-probability extensions. A hypothesis is removed from the beam and added to the completed set as soon as it emits the end-of-sequence token.

## Why it works

Greedy decoding (B=1) commits to a locally best token that may be globally suboptimal. Increasing B gives the model a chance to recover from an early mistake. Tradeoff: compute scales linearly with B and the beam can collapse to near-duplicates.

[[1409.3215-seq2seq]] reports that for their LSTM translation system **B=2 captures most of the benefit of beam search**, and even B=1 already produces useful translations. Their best result uses B=12. Ensemble + beam interactions matter: an ensemble of 5 LSTMs at B=2 is cheaper than a single LSTM at B=12 and produces higher BLEU (34.50 vs 26.17).

## Variants

- **Pure beam search** as in [[1409.3215-seq2seq]].
- **Length-normalized beam search** — divide log-prob by a function of length to counter the bias toward short outputs.
- **Diverse / group beam search** — penalize repetition across beams.
- **Sampling-based alternatives** (top-k, top-p / nucleus) are now standard for open-ended generation in modern LLMs; beam search remains common for tasks with a well-defined "correct" output (translation, summarization).

## See also
- [[SeqToSeq]]
- [[EncoderDecoder]]
