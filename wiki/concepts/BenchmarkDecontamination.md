---
title: "Benchmark Decontamination"
type: concept
tags: [evaluation, contamination, methodology, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Benchmark Decontamination

Removing **benchmark data from training data** to maintain evaluation integrity. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "For model developers, a common practice is to remove benchmarks they care about from their training data before training their models."

## Detection then removal

1. **Detect** contamination using [[NGramOverlap|n-gram overlap]] (precise) or [[Perplexity|perplexity]] (cheap).
2. **Remove** the contaminated samples from the training corpus.
3. **Re-train** or continue training.

## Disclosure best practice

> "When reporting your model performance on a benchmark, it's helpful to disclose what percentage of this benchmark data is in your training data, and what the model's performance is on both the overall benchmark and the clean samples of the benchmark."

[[openai|OpenAI]]'s Brown et al. 2020 GPT-3 analysis is the canonical example — they reported both "clean sample" and "whole benchmark" performance and found **13 benchmarks ≥40% contaminated**.

## The pragmatic tension

> "Sadly, because detecting and removing contamination takes effort, many people find it easier to just skip it."

And contamination can be **deliberate and benign** — after benchmark-based selection, you might train your best model on benchmark data to maximize user-facing performance, even though that breaks future evaluation on those benchmarks.

## Mitigation at leaderboard level

> "To combat data contamination, leaderboard hosts like Hugging Face plot standard deviations of models' performance on a given benchmark to spot outliers. Public benchmarks should keep part of their data private and provide a tool for model developers to automatically evaluate models against the private hold-out data."

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[DataContamination]] — the problem.
- [[NGramOverlap]] / [[Perplexity]] — detection methods.
- [[openai|OpenAI]] — the GPT-3 contamination disclosure example.
- [[PublicBenchmark]] — what gets decontaminated.
