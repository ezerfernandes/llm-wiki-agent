---
title: "Scaling Laws"
type: concept
tags: [scaling, pretraining, foundational, power-law]
sources: [2001.08361-scaling-laws]
last_updated: 2026-05-10
---

# Scaling Laws

**Neural scaling laws** are smooth power-law relationships between language-model test loss and three scale factors — non-embedding parameter count $N$, dataset size $D$ (tokens), and training compute $C$ — established empirically for autoregressive Transformer LMs by Kaplan, McCandlish et al. in [[2001.08361-scaling-laws]] (OpenAI + JHU, 2020).

## The headline relations

When each factor is varied while the others are not bottlenecks:

- $L(N) = (N_c/N)^{\alpha_N}$ with $\alpha_N \approx 0.076$, $N_c \approx 8.8 \times 10^{13}$ params (non-embedding).
- $L(D) = (D_c/D)^{\alpha_D}$ with $\alpha_D \approx 0.095$, $D_c \approx 5.4 \times 10^{13}$ tokens.
- $L(C_\min) = (C_c^\min/C_\min)^{\alpha_C^\min}$ with $\alpha_C^\min \approx 0.050$, $C_c^\min \approx 3.1 \times 10^8$ PF-days.

A joint $L(N, D)$ fit predicts overfitting from the ratio $N^{0.74}/D$: each 8× increase in model size needs only ~5× more data to keep the overfitting penalty constant.

## Why this concept matters

The scaling laws are the **quantitative argument for the scale-up trajectory** that produced GPT-3 and successor LLMs. Three implications shaped subsequent practice:

1. **Architecture is second-order.** Within a wide envelope (depth/width, number of heads, feed-forward ratio), changing shape moves loss by a few percent. Once N, D, C are set, the architecture is mostly fixed in advance.
2. **Compute-efficient training stops short of convergence.** See [[ComputeEfficientTraining]].
3. **Larger models are more sample-efficient.** Reaching a target loss with fewer optimizer steps and fewer data points — counter to the prevailing intuition that big models need proportionally more data.

## The compute-allocation prescription

Within a fixed compute budget $C$:
$$N \propto C^{0.73}, \quad B \propto C^{0.24}, \quad S \propto C^{0.03}, \quad D = B \cdot S$$

A 10× increase in $C$ implies ~5× larger model, ~2× larger batch, but only ~1.07× more serial steps. Most additional compute should go into **larger models**, not longer training.

## Caveats

- **Constants are tokenizer-dependent.** $N_c$, $D_c$, $C_c$ have no fundamental meaning; only the exponents do.
- **Architecture independence is local.** The claim holds within the studied envelope. 1-layer models and extreme depth/width ratios deviate.
- **Scaling laws must eventually break.** Naive extrapolation of the [[2001.08361-scaling-laws]] equations predicts a contradiction at $C^* \sim 10^4$ PF-days, $L^* \sim 1.7$ nats/token, conjectured to mark the entropy of natural language.
- **The optimal data exponent has since been re-revised.** Later "Chinchilla" work argues data should scale closer to 1:1 with model size, not at the $D \propto N^{0.74}$ rate this paper recommends. That revision is **not** present in the 2020 paper itself.

## Role in the wider wiki

Every 2026 LLM paper in this wiki implicitly assumes a scaling-law regime: budgets, model-size choices, and the very decision to train at all rest on these power laws. See in particular [[2312.11805-gemini]] (Gemini family deliberately spans scaling-law-derived model sizes). The pretraining-stage interventions of [[2601.21343-self-improving-pretraining]] and the agentic-model training budgets in [[2604.21590-agenticqwen]] take the scaling-law framework as background.

## See also

- [[PowerLaw]]
- [[ComputeEfficientTraining]]
- [[Pretraining]]
- [[Transformer]]
- [[ChinchillaScalingLaw]] — the 2022 revision that updates the data-vs-params allocation toward 1:1.
- [[ComputeOptimal]] — the goal Chinchilla operationalizes.
- [[FLOPs]] — the budgeting unit.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

[[ChipHuyen|Chip Huyen]] in Ch 2 frames scaling laws as the **quantitative argument behind every modern foundation-model training run**:

> "We've come a long way from when the training process was treated like alchemy."

Ch 2 names two visible bottlenecks where the scaling-law extrapolation runs into the real world (see [[ScalingBottlenecks]]):
1. **Training data** — Villalobos et al. project dataset-size growth outrunning new-data generation; 45% of [[c4|C4]] became restricted between 2023–2024 (Longpre et al.).
2. **Electricity** — data centers go from 1–2% of global electricity to a projected 4–20% by 2030; at most ≈50× growth before a power shortage.

Ch 2 also introduces:
- **[[InverseScaling]]** — narrow but real exceptions where bigger models perform worse (Anthropic 2022 alignment finding; the NYU [[InverseScalingPrize]]).
- **[[EmergentAbilities]]** (Wei et al. 2022) — capabilities discontinuously appearing at scale, making [[ScalingExtrapolation|scaling extrapolation]] from small models harder.
- **The Llama inference-aware exception** — [[meta|Meta]] deliberately trained Llama models *smaller* than Chinchilla-optimal because smaller models are cheaper at inference time; Sardana et al. (2023) formalized this as **inference-aware scaling**.
