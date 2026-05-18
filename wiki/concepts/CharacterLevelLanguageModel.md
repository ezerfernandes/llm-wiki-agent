---
title: "Character-Level Language Model"
type: concept
tags: [nlp, language-models, sequence-models]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# Character-Level Language Model

A [[LanguageModel|language model]] that operates on **characters** as tokens rather than words or word-pieces ([[d2l-recurrent-neural-networks]] §rnn). D2L's RNN running example: train on H. G. Wells' *The Time Machine* with the vocabulary = unique lowercase letters + space + `<unk>` (~30 tokens).

## Mechanics

For input sequence "machine" tokenized as `['m','a','c','h','i','n','e']`:
- Input: `['m','a','c','h','i','n']` (one-hot encoded).
- Target: `['a','c','h','i','n','e']` (input shifted by one — [[TeacherForcing|teacher forcing]]).
- Loss: softmax + cross-entropy at every position, summed across positions.
- Metric: [[Perplexity]].

## Trade-offs

| Dimension | Character-level | Word-level |
|---|---|---|
| Vocabulary size | ~30–256 (ASCII) | 10K–100K+ |
| Sequence length | Long (5–10× word-level) | Short |
| OOV handling | None needed (covers any spelling) | `<unk>` for rare/unseen words |
| Long-range dependencies | Harder (more time steps between distant words) | Easier |
| Memory per epoch | Higher (longer sequences) | Lower |

Modern LLMs typically use **subword/BPE tokenization** as a middle ground — tens of thousands of tokens, robust to OOV, manageable sequence lengths.

## Why D2L uses character-level for pedagogy

- Simplifies vocabulary construction (no rare-word truncation, no `<unk>` placeholders to worry about).
- Lets the RNN demo focus on the *recurrence* mechanism, not on tokenization preprocessing.
- Cleanly demonstrates one-hot encoding, softmax classification head, and per-token cross-entropy.

## Historical note

Andrej Karpathy's 2015 "The Unreasonable Effectiveness of Recurrent Neural Networks" blog post made char-level RNN LMs famous (Shakespeare / Linux source / Wikipedia generation demos). D2L's implementation is the textbook-grade version of that experiment.

## Connections

- [[d2l-recurrent-neural-networks]] — chapter-source (§rnn, §rnn-scratch).
- [[LanguageModel]] — parent concept.
- [[RNN]] / [[HiddenState]] — primary architecture.
- [[Tokenization]] — character-level is one extreme of the tokenization spectrum.
- [[TeacherForcing]] / [[Perplexity]] — training + evaluation.
- [[1706.03762-attention-is-all-you-need]] — Transformer LMs typically use BPE/wordpiece, not character-level.
