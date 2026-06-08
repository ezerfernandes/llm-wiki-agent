---
title: "Model Ensemble"
type: concept
tags: [ml-engineering, inference, model-composition]
sources: [ai-engineering-ch07-finetuning, mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Model Ensemble

A model-composition strategy where **multiple constituent models each produce an output for the same input**, and a final answer is derived by combining these outputs (majority vote, weighted vote, or trainable combiner). Per Wikipedia (quoted in [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]):

> "Ensembling combines 'multiple learning algorithms to obtain better predictive performance than could be obtained from any of the constituent learning algorithms alone.'"

## How it differs from [[ModelMerging|model merging]]

| Property | Model ensemble | [[ModelMerging\|Model merging]] |
|---|---|---|
| What's combined | **Outputs** | **Weights** |
| Inference cost | N× one model (must run every constituent) | 1× one model (merged) |
| Storage | N models | 1 model |
| Each constituent | Stays intact | Loses identity |
| Failure modes | Voting tiebreaks; latency | Loss-basin mismatch |

Ch 7's summary: *"If model merging typically involves mixing parameters of constituent models together, ensembling typically combines only model outputs while keeping each constituent model intact."*

## When to choose ensembling

- The constituents have **different architectures** and can't be merged.
- The constituents have **complementary failure modes** — voting smooths over individual mistakes.
- You can afford **N× inference cost**.

## When to choose merging

- The constituents share a **base model** (and ideally a finetuning regime).
- You're **inference-cost-constrained**.
- You want **storage savings**.

## The historical pattern

Ch 7's observation: ensembles used to dominate ML competition leaderboards (Kaggle-style). In the current era, **merged models** dominate the Hugging Face Open LLM Leaderboard — partly because merging is cheaper to serve and partly because modern leaderboards penalize the inference cost ensembles incur.

## Connections

- [[ModelMerging]] — the weight-combining alternative.
- [[bestofn]] — a specific form of ensembling (best-of-N sampling).
- [[MixtureOfExperts]] — sparse ensembling baked into one model.
- [[MixtureOfAgents]] — a multi-model version somewhere between ensembling and merging.
- [[EnsembleLearning]] — the bagging/boosting/stacking framing; [[mlsysbook-ch03-ml-workflow|Ch 3]] foregrounds the accuracy-vs-deployment trade-off (competition winners ensemble 10–50 models; the Netflix Prize 800+-model ensemble was never deployed).
- [[ai-engineering-ch07-finetuning]] / [[mlsysbook-ch03-ml-workflow]] — sources.
