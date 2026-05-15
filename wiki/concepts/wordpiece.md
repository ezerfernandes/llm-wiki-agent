---
title: "WordPiece"
type: concept
tags: [concept, tokenization, subword]
sources: [1810.04805-bert]
last_updated: 2026-05-10
---

# WordPiece

Subword tokenization scheme used by [[BERT]] ([[1810.04805-bert]]) with a 30,000-token vocabulary. Originated in Google's neural machine translation system (Wu et al., 2016) and built on the same statistical principle as Byte-Pair Encoding: start from a character vocabulary, greedily merge the pair whose merge most improves the unigram likelihood of the training data, until the target vocab size is reached.

WordPiece sits between word-level tokenization (which fails on rare and morphologically rich words) and character-level (which produces very long sequences). Out-of-vocabulary words decompose into `##`-prefixed continuation pieces — e.g. `playing → play ##ing`. BERT's input representation sums the WordPiece **token embedding**, a **segment embedding** (A or B), and a learned **positional embedding** per position.

Closely related: BPE (Sennrich et al.), SentencePiece (Kudo & Richardson) — the latter is the de-facto choice in many later decoder-style LLMs, but the conceptual machinery is the same.
