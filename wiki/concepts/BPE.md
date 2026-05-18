---
title: "Byte Pair Encoding (BPE)"
type: concept
tags: [nlp, tokenization, subword, compression]
sources: [d2l-nlp-pretraining]
last_updated: 2026-05-16
---

# Byte Pair Encoding (BPE)

A statistical subword-tokenization algorithm adapted to NLP by [[RicoSennrich|Sennrich]], Haddow & Birch (2015) from a 1994 data-compression algorithm. Learns a **fixed-size vocabulary** of variable-length subword units by **greedy frequency-based merging**:

1. Initialize the vocabulary with all individual characters (plus a special end-of-word marker — D2L uses `'_'` — and `[UNK]`).
2. Tokenize the training corpus as space-separated single characters within each word; do not consider pairs that cross word boundaries.
3. Find the most frequent pair of consecutive symbols across the corpus; concatenate it into a new symbol and add it to the vocabulary.
4. Replace every occurrence of that pair with the merged symbol.
5. Repeat steps 3–4 for a target number of merges (which sets the final vocab size).

Result: common substrings ("fast", "tall", "er_") become single tokens while rare/novel words decompose into their longest learnable subword pieces (e.g. "tallest_" → "tall est_" using the merges learned on "fast/tall" data). To get a vocabulary of size $m$ from an initial alphabet of size $n$, perform $m-n$ merges.

BPE underpins the tokenization of [[GPT2|GPT-2]], [[GPT3|GPT-3]], [[RoBERTa]], and most decoder-only LLMs; [[WordPiece]] (used by [[BERT]]) is a closely-related variant that picks the merge that **maximizes unigram likelihood** rather than raw frequency. [[FastText]]'s character-$n$-gram approach is the alternative non-merge-based subword scheme.

See [[d2l-nlp-pretraining]] §subword-embedding §Byte-Pair-Encoding.
