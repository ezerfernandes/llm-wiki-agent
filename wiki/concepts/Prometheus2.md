---
title: "Prometheus 2"
type: concept
tags: [evaluator-lm, evaluation, llm]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# Prometheus 2

**Prometheus 2** — an open-source 7B evaluator LM specialized for **rubric-based grading of other language models** ([[KimEtAl2024|Kim et al. 2024]] *Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models*, arXiv 2405.01535).

## Why used

Co-STORM ([[2408.15232-co-storm]]) needs to score long-form generated reports on a **5-point rubric** across four dimensions: Relevance / Breadth / Depth / Novelty. Calling [[gpt-4o|GPT-4o]] for every grading call would be expensive and would bias the eval (the system being graded is also GPT-4o-based). Prometheus 2 is the open-source alternative: a dedicated evaluator LM trained for this task.

## How it's used in Co-STORM

For each (topic, goal) from [[WildSeek]], Co-STORM and the baselines each generate a long-form report. Prometheus 2 scores each report on the 1-5 rubric defined in Co-STORM Appendix D. Reported scores in the paper are **means** over the 100 examples.

## Limitations to note

- Prometheus 2 is itself a 7B LM; rubric scores have noise. Co-STORM reports paired $t$-tests to detect significance.
- Aggregating 5-point rubrics with arithmetic mean is conventional but assumes interval-scale ratings — a known limitation across the LM-evaluator-LM literature.

## See also
- [[CoSTORM]] · [[WildSeek]] · [[InformationDiversity]] · [[KimEtAl2024]]
