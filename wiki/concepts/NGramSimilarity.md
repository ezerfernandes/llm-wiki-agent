---
title: "N-Gram Similarity"
type: concept
tags: [evaluation, metric, nlp]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# N-Gram Similarity

A [[LexicalSimilarity|lexical-similarity]] approach that measures overlap based on **sequences of n tokens** ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]) rather than single tokens.

## Definitions

- **1-gram (unigram)** — a single token.
- **2-gram (bigram)** — two adjacent tokens.
- **n-gram** — n adjacent tokens.

Ch 3 example: *"My cats scare the mice"* contains 4 bigrams: `("my", "cats")`, `("cats", "scare")`, `("scare", "the")`, `("the", "mice")`.

The metric: *"You measure what percentage of n-grams in reference responses is also in the generated response."*

## Used by

- [[bleu|BLEU]] — uses modified n-gram precision (typically n=1..4) with a brevity penalty.
- [[ROUGE]] — recall-side n-gram overlap (ROUGE-N) and longest-common-subsequence (ROUGE-L).
- [[METEOR]] — unigram-based alignment with morphological matching.

## Preprocessing matters

Ch 3 flag: *"You might also want to do some processing depending on whether you want 'cats' and 'cat' or 'will not' and 'won't' to be considered two separate tokens."* Stemming, lemmatization, and contraction expansion change the n-gram count meaningfully.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[LexicalSimilarity]] — parent.
- [[bleu|BLEU]] / [[ROUGE]] / [[METEOR]] — concrete n-gram-based metrics.
- [[EditDistance]] — the character-level sibling branch.
