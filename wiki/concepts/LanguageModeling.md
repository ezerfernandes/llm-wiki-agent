---
title: "Language Modeling"
type: concept
tags: [cs324, llm]
sources: [cs324-introduction, cs324-capabilities]
last_updated: 2026-06-04
---

Language modeling is the task and training objective of estimating the probability of a sequence of tokens, typically by factorizing it into a product of conditional next-token probabilities. It is distinct from the [[LanguageModel]] object that realizes it: the modeling task defines what to learn, while the model is the parameterized artifact. Quality is commonly measured by [[Perplexity]].

## Connections
- [[LanguageModel]] — the object that implements this task
- [[Perplexity]] — standard evaluation metric
- [[cs324-introduction]] — discussed in this CS324 lecture
- [[cs324-capabilities]] — discussed in this CS324 lecture
