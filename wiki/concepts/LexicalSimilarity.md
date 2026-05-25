---
title: "Lexical Similarity"
type: concept
tags: [evaluation, metric, nlp]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Lexical Similarity

**Lexical similarity** measures *"how much two texts overlap"* at the surface level ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]) — without regard to meaning. The metric family for lexical similarity dominated pre-foundation-model NLP and survives today as a low-cost reference-based eval.

## Two computational strategies (Ch 3)

1. **[[NGramSimilarity|N-gram similarity]]** — what percentage of n-grams in the reference are also in the generated response. [[bleu|BLEU]] / [[ROUGE]] / [[METEOR]] / [[TER]] / [[CIDEr]] all live here, differing in *"exactly how the overlapping is calculated."*

2. **[[EditDistance|Edit distance]] / [[FuzzyMatching|fuzzy matching]]** — count operations (deletion, insertion, substitution, sometimes transposition) needed to transform one text into another. Lower distance = higher similarity.

## Worked example

Reference: *"My cats scare the mice"* (5 words).
- Response A: *"My cats eat the mice"* → 4/5 overlap = **80%**.
- Response B: *"Cats and mice fight all the time"* → 3/5 overlap = **60%**.

Response A is closer by token overlap.

## Where it dominated

Pre-FMs, lexical similarity was the workhorse:
- **[[bleu|BLEU]]** — machine translation (WMT).
- **[[ROUGE]]** — summarization.
- **[[METEOR]] / [[TER]] / [[CIDEr]]** — sibling MT and captioning metrics.
- Benchmarks: WMT, COCO Captions, GEMv2.

## Limitations Ch 3 names

1. **Coverage**: *"A good response can get a low similarity score if the reference set doesn't contain any response that looks like it."* Adept's [[Fuyu]] was the chapter's example.
2. **Reference quality**: bad references → bad scores ([[WMT2023]] finding).
3. **Decoupled from functional correctness**: BLEU scores for correct and incorrect [[HumanEval]] solutions are similar (Chen et al. 2021).

## Lexical vs semantic

Lexical similarity is **surface**; [[SemanticSimilarity|semantic similarity]] is **meaning**. *"What's up?"* and *"How are you?"* are lexically distant but semantically close. *"Let's eat, grandma"* and *"Let's eat grandma"* are lexically close but semantically opposite — the canonical example of lexical-similarity blindness.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[SimilarityMeasurement]] — parent concept.
- [[NGramSimilarity]] / [[EditDistance]] / [[FuzzyMatching]] — sub-methods.
- [[bleu|BLEU]] / [[ROUGE]] / [[METEOR]] / [[TER]] / [[CIDEr]] — concrete metrics.
- [[SemanticSimilarity]] — the alternative when surface form misleads.
- [[ExactMatch]] — the binary special case of lexical similarity.
