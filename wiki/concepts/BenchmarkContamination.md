---
title: "Benchmark Contamination"
type: concept
tags: [evaluation, benchmarks, llm, methodology, mlsysbook]
sources: [hands-on-llm-ch04-text-classification, mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Benchmark Contamination

Alias for [[DataContamination|data contamination]] — when a benchmark's evaluation set leaks into a model's training data.

See [[DataContamination]] for the full treatment.

## Connections

- [[DataContamination]] — the canonical wiki page.
- [[mlsysbook-ch12-benchmarking]] — Ch 12 treats contamination as a unique **LLM model-benchmarking** failure mode (web-scale pretraining encounters benchmark questions, inflating scores via memorization), and reframes leakage as something benchmark designers can *test for*: temporal holdouts, dynamic benchmarks, and exact-phrasing recall detection.
- [[BenchmarkSaturation]] / [[BenchmarkEngineering]] — sibling benchmark-integrity failure modes.
- [[hands-on-llm-ch04-text-classification]] — wiki source.
