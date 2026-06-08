---
name: FlawOfAverages
title: "Flaw of Averages"
type: concept
tags: [responsible-ai, fairness, evaluation, statistics]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Flaw of Averages

The systematic error of judging a system by its average-case behavior while ignoring tail and subgroup behavior (Savage 2009). Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]]: "A bridge that is 'safe on average' but collapses under a heavy truck is a failure. Similarly, an ML system that is 'accurate on average' but fails for a specific ethnic or gender group is an engineering failure."

The chapter draws a systems analogy: the same discipline that makes engineers measure **tail latency (p99)** rather than mean latency demands [[DisaggregatedEvaluation|disaggregated evaluation]] for [[Fairness|fairness]]. Aggregate accuracy can hide **>40× error-rate disparities** across demographic groups.

## Connections
- [[DisaggregatedEvaluation]] — the remedy.
- [[Fairness]] / [[AlgorithmicBias]] — the failures it conceals.
- [[GenderShades]] — the empirical demonstration.
- [[mlsysbook-ch15-responsible-engineering]] — source.
