---
title: "METEOR"
type: concept
tags: [evaluation, metric, machine-translation]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# METEOR

**METEOR** (Metric for Evaluation of Translation with Explicit ORdering, Banerjee & Lavie 2005, "METEOR++" being later refinements) is a [[LexicalSimilarity|lexical-similarity]] metric for machine translation. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]], METEOR is one of the *"common metrics for lexical similarity"* alongside [[bleu|BLEU]], [[ROUGE]], [[TER]], and [[CIDEr]].

## Why METEOR exists

METEOR was designed to correlate **better with human judgment than [[bleu|BLEU]]**, by:
- Aligning unigrams between candidate and reference via exact match, stem match, synonym match, and paraphrase match.
- Weighting recall higher than precision (BLEU is precision-only).
- Applying a fragmentation penalty for misordered matches.

## Position

- Pre-FM-era MT staple; reported alongside [[bleu|BLEU]] on benchmarks like WMT.
- *"Since the rise of foundation models, fewer benchmarks use lexical similarity"* (Ch 3) — METEOR is among the metrics that have receded in favor of semantic and AI-as-judge alternatives.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[bleu|BLEU]] / [[ROUGE]] / [[TER]] / [[CIDEr]] — sibling lexical-similarity metrics.
- [[LexicalSimilarity]] / [[NGramSimilarity]] — parent.
- [[BERTScore]] / [[MoverScore]] — semantic-similarity successors.
