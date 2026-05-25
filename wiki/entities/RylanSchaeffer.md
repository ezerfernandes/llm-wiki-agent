---
title: "Rylan Schaeffer"
type: entity
tags: [person, researcher, stanford, satire]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Rylan Schaeffer

PhD student at [[stanforduniversity|Stanford]], author of the **satirical paper *"Pretraining on the Test Set Is All You Need"* (2023)**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Rylan Schaeffer, a PhD student at Stanford, demonstrated this beautifully in his 2023 satirical paper 'Pretraining on the Test Set Is All You Need'. By training exclusively on data from several benchmarks, his one-million-parameter model was able to achieve near-perfect scores and outperformed much larger models on all these benchmarks."

## Significance

Schaeffer's experiment is the **canonical reductio ad absurdum** of public-benchmark trust. A 1M-parameter model — three to four orders of magnitude smaller than any leaderboard model — beats them all by training directly on the test data. The paper's title is a play on the famous *"Attention Is All You Need."*

The point: a benchmark score without contamination disclosure can be entirely meaningless.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[stanforduniversity|Stanford]] — affiliation.
- [[DataContamination]] — what his paper demonstrates.
- [[BenchmarkDecontamination]] — what his paper argues for.
