---
title: "Data Mix"
type: concept
tags: [dataset-engineering, training-data, llama]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Data Mix

The **ratio of domain tokens** in a training dataset — e.g., X% general knowledge / Y% math / Z% code. Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], the data mix is the operational form of [[DataCoverage|coverage]] / [[DataDiversity|diversity]] decisions, and **different training phases optimize for different mixes**.

## Llama 3 reference table (Ch 8)

[[Llama|Llama 3]] (Dubey et al. 2024) publishes per-phase mixes:

| Domain | Pre-training | SFT | Preference FT |
|---|---|---|---|
| General knowledge (English) | 50% | 82.0% | 52.7% |
| Math and reasoning | 25% | 5.9% | 21.2% |
| Coding | 17% | 6.9% | 14.9% |
| Multilingual | 8% | 5.2% | 3.0% |
| Exam-like | — | — | 8.1% |
| Long context | — | — | 0.1% |

Three patterns visible in this table:

1. **Pre-training over-weights math + code** (~42% combined) — vastly above the internet's natural distribution. Math + code annealing boosts reasoning benchmarks across all sizes.
2. **SFT shifts toward general knowledge** (82%) — because it teaches conversational style, not knowledge acquisition.
3. **Preference finetuning rebalances toward technical domains** (~36% math + code) — because alignment quality matters more in technical domains.

## Other per-phase variables (not shown above)

- **Token count** for context vs response
- **Number of turns** in dialogue
- **Ratio of human- to AI-generated data** (Llama 3 used heavy synthetic data in post-training)

## How to choose a mix

Two approaches named in Ch 8:

1. **Match the real-world application distribution.** If your users send 60% code queries, your data should reflect that ratio.
2. **Scaling-law experiments.** Train several small models on candidate mixes; predict large-model performance from the small-model results (Meta's approach for Llama 3).

## Connections

- [[DataCoverage]] / [[DataDiversity]] — the broader concept; data mix is one operationalization.
- [[Llama|Llama 3]] — the chapter's canonical case study.
- [[posttraining|Post-Training]] / [[SupervisedFinetuning]] / [[PreferenceFinetuning]] — the phases each requiring different mixes.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
