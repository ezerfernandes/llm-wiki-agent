---
title: "HELM Lite"
type: concept
tags: [leaderboard, benchmark, evaluation, stanford]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# HELM Lite

[[stanforduniversity|Stanford]]'s **lite version of HELM (Holistic Evaluation of Language Models)**. A leaderboard using 10 benchmarks with [[MeanWinRate|mean win rate]] aggregation. Discussed in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]].

## The 10 benchmarks (Ch 4 era)

Overlapping only [[mmlu|MMLU]] and [[GSM8K]] with [[OpenLLMLeaderboard|HuggingFace Open LLM Leaderboard]]. The other 8:

- **MATH** — competitive math
- **LegalBench** — legal
- **MedQA** — medical
- **WMT 2014** — translation
- **NarrativeQA** — long-story reading comprehension
- **OpenBookQA** — book-based reading comprehension
- **Natural Questions** (with Wikipedia) — general QA
- **Natural Questions** (without Wikipedia) — general QA

## Aggregation: mean win rate

> "HELM authors, on the other hand, decided to shun averaging in favor of mean win rate, which they defined as 'the fraction of times a model obtains a better score than another model, averaged across scenarios'."

Compare to HuggingFace's simple averaging — both are coverage choices, not just aggregation choices.

## Notable exclusions

- **MS MARCO** (information retrieval) — *"left out … because it's expensive to run."*

## Cost data point

Stanford spent *"approximately $80,000–$100,000 to evaluate 30 models on their full HELM suite."* Concretely: $38,000 in commercial APIs + 19,500 GPU hours × $2.15-$3.18 = $80-100K total. The canonical practitioner data point on private-benchmark cost.

## Why "Lite"

The full HELM is much larger; HELM Lite is the reduced version intended to remain runnable. Inspired by HuggingFace's "simplicity" per Ch 4.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[stanforduniversity|Stanford]] — host.
- [[Leaderboard]] — parent.
- [[OpenLLMLeaderboard]] — sibling leaderboard with different aggregation.
- [[MeanWinRate]] — the aggregation method.
- [[mmlu|MMLU]] / [[GSM8K]] — the two-benchmark overlap with HuggingFace.
- [[BenchmarkAggregation]] — the design question this answers differently.
