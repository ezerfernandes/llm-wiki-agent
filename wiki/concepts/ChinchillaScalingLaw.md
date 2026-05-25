---
title: "Chinchilla Scaling Law"
type: concept
tags: [scaling, pretraining, compute-optimal, foundational]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Chinchilla Scaling Law

The rule, proposed in [[googledeepmind|DeepMind]]'s 2022 paper *"Training Compute-Optimal Large Language Models"*, that — given a fixed compute budget — there is an **optimal pairing of model size and training-dataset size**. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "For compute-optimal training, you need the number of training tokens to be approximately **20 times the model size**. ... The model size and the number of training tokens should be scaled equally: for every doubling of the model size, the number of training tokens should also be doubled."

A 3B-param model therefore needs ≈60B training tokens to be compute-optimal.

> See also the earlier stub treatment at [[chinchillascalinglaws]] (kept for backlink compatibility) — this page is the Ch-2-grounded canonical version.

## The methodology

The authors trained **400 language models** ranging from **70M to 16B+ parameters** on **5B to 500B tokens**, then fit a clean compute-loss surface predicting both the optimal `(N, D)` pair *and* the expected training loss for any compute budget — assuming you don't make training mistakes.

## What it changed about the field

> "We've come a long way from when the training process was treated like alchemy." — Ch 2

Before Chinchilla, scale-up choices were heuristic. After Chinchilla, **for a fixed compute budget, the optimal `(model size, training tokens)` pair is essentially predictable** — and the [[scalinglaws|Kaplan et al. 2020]] recommendation of allocating most extra compute to model size (over tokens) was revised toward equal scaling.

## Caveats

1. **Derived for dense models on human-generated data.** Sparse models ([[MixtureOfExperts|MoE]]) and synthetic data are active research areas — the law as stated doesn't directly apply.
2. **Compute-optimal ≠ production-optimal.** [[meta|Meta]]'s Llama deliberately chose *smaller-than-Chinchilla-optimal* models because smaller models are cheaper to run inference on, and inference-time cost matters more in production than training-time compute optimality. Sardana et al. (2023) generalized this into an **inference-aware scaling law**.
3. **Data quality matters too.** Quantity, quality, and diversity are *"the three golden goals for training data"* per Ch 2.
4. **Last-mile expense.** Going from 90% → 95% accuracy is more expensive than 85% → 90% — Meta's *"Beyond Neural Scaling Laws"* paper shows this concretely. A model with 2% error rate may need an order of magnitude more data/compute/energy than one with 3% error.

## Worked numbers from Ch 2 (Table 2-5)

| Model | Params | Training tokens |
|---|---|---|
| LaMDA (Thoppilan 2022) | 137B | 168B |
| GPT-3 (Brown 2020) | 175B | 300B |
| Jurassic (Lieber 2021) | 178B | 300B |
| Gopher (Rae 2021) | 280B | 300B |
| MT-NLG (Smith 2022) | 530B | 270B |
| **[[Chinchilla|Chinchilla]]** | **70B** | **1.4T** |

Chinchilla shows that **a smaller model with vastly more tokens beat the much larger contemporaries trained on far fewer tokens** — direct empirical evidence for the law.

## Connections
- [[chinchillascalinglaws]] — earlier stub, points here.
- [[scalinglaws]] — Kaplan et al. 2020, the predecessor law Chinchilla revised.
- [[ComputeOptimal]] — the goal Chinchilla operationalizes.
- [[FLOPs]] — the budgeting unit.
- [[pretraining]] — the workflow stage this rule governs.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[scalinglaws]] — the broader power-law framework.
