---
title: "Data Slicing"
type: concept
tags: [evaluation, methodology, debugging, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Data Slicing

**Partitioning evaluation data into subsets** and evaluating performance on each separately. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Slicing means separating your data into subsets and looking at your system's performance on each subset separately."

(Huyen wrote about this at length in *Designing Machine Learning Systems* — the term predates *AI Engineering*.)

## Four reasons to slice

1. **Avoid biases** — including against minority user groups.
2. **Debug** — *"if your application performs particularly poorly on a subset of data, could that be because of some attributes of this subset, such as its length, topic, or format?"*
3. **Find improvement areas** — *"if your application is bad on long inputs, perhaps you can try a different processing technique."*
4. **Avoid [[SimpsonsParadox|Simpson's paradox]]** — model A beats model B on every subgroup but loses overall.

## Slice dimensions

Per Ch 4: tiers (paying vs free), traffic sources (mobile vs web), usage patterns. Plus:

- **Frequent-mistake set** — where the system tends to fail.
- **User-mistake set** — typos, malformed queries.
- **Length** — short vs long inputs/outputs.
- **Format** — different input formats your app handles.
- **[[OutOfScopeEvaluation|Out-of-scope set]]** — inputs your app should refuse.

## The northstar test

> "If you care about something, put a test set on it."

Any business-meaningful subdivision deserves its own evaluation slice.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[EvaluationPipeline]] — parent process.
- [[SimpsonsParadox]] — the paradox slicing detects.
- [[OutOfScopeEvaluation]] / [[PrivateBenchmark]] — specific evaluation-set types.
- [[BootstrapEvaluation]] — sizing each slice.
