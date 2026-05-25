---
title: "Data Decontamination"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning]
last_updated: 2026-05-22
---

## Definition
Removing training samples that overlap with evaluation sets.

## In LLM Engineer's Handbook
Ensures training data does not contain samples identical or highly similar to eval/test sets — a prerequisite for honest benchmarking. Per [[leh-ch05-supervised-fine-tuning]] uses the same machinery as [[DataDeduplication]]: exact hashing + [[MinHashDeduplication]] + embedding-based similarity, applied across train + eval, removing only the train side. Pragmatic recipe: append eval to instruction dataset during dedup, automate as you iterate on benchmarks.
