---
title: "Last-Mile Challenge"
type: concept
tags: [planning, deployment, ai-engineering, milestone]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# Last-Mile Challenge

**The disproportionate effort required to push an AI application from "good demo" to "production-quality product."** Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], the last-mile challenge is the planning trap most teams underestimate — and one of the main reasons the FM-driven 80% demo often takes much longer than expected to become a 95% deployable product.

## Two anchor data points

1. **UltraChat (Ding et al., 2023)**: *"the journey from 0 to 60 is easy, whereas progressing from 60 to 100 becomes exceedingly challenging."*

2. **LinkedIn (2024)**: reached **80%** of the target experience after **1 month** — then needed **4 more months** to surpass **95%**. *"A lot of time was spent working on the product kinks and dealing with [[Hallucination|hallucinations]]. The slow speed of achieving each subsequent 1% gain was discouraging."*

## Why initial success is misleading

> *"It might take a weekend to build a demo but months, and even years, to build a product."*

The base capabilities of foundation models are already impressive enough that a fun demo is almost trivial to produce. This creates two failure modes:

- **Under-budgeting** — teams quote a 1-month delivery based on the demo, then miss the deadline by 4–6×.
- **Premature commitment** — teams over-commit to an FM, infrastructure, or vendor before validating the gap between demo and product.

## Goals often change after evaluation

> *"For example, after evaluation, you may realize that the resources needed to get the app to the usefulness threshold will be more than its potential return, and, therefore, you no longer want to pursue it."*

The last-mile reality should be input to the **buy-vs-build** decision — sometimes the answer is "don't build at all."

## Connections

- [[UsefulnessThreshold]] — the threshold the last mile is trying to clear.
- [[UseCaseEvaluation]] — parent planning framework.
- [[AIEngineering]] — discipline-level home.
- [[Hallucination]] — named as the headline last-mile blocker in LinkedIn's case.
- [[Evaluation]] — the discipline that diagnoses last-mile gaps.
- [[ai-engineering-ch01-intro]] — primary source.
