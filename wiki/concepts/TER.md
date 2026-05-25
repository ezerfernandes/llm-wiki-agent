---
title: "TER (Translation Edit Rate)"
type: concept
tags: [evaluation, metric, machine-translation]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# TER

**TER** — *Translation Edit Rate* (Snover et al. 2006) — measures the number of edits required to change a candidate translation into a reference, normalized by reference length. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]], TER is one of the *"common metrics for lexical similarity"* alongside [[bleu|BLEU]], [[ROUGE]], [[METEOR]], and [[CIDEr]].

## Edit operations

TER counts insertions, deletions, substitutions, and **shifts** (moving a block of tokens). Lower TER = better translation. The shift operation is what distinguishes TER from raw [[EditDistance|edit distance]] — it explicitly rewards translations that contain the right tokens but in a different order.

## Position

- Pre-FM-era MT staple; complementary to [[bleu|BLEU]] (which is precision-based).
- *"Since the rise of foundation models, fewer benchmarks use lexical similarity"* (Ch 3) — TER has receded in favor of semantic and AI-as-judge metrics.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[bleu|BLEU]] / [[ROUGE]] / [[METEOR]] / [[CIDEr]] — sibling lexical-similarity metrics.
- [[LexicalSimilarity]] / [[EditDistance]] — parents.
