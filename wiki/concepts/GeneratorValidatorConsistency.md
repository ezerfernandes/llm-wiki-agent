---
title: "Generator-Validator Consistency"
type: concept
tags: [metric, filtering, distillation, dspy, medical-nlp]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# Generator-Validator Consistency ($\mathcal{M}_\mathrm{MedVAL}$)

The **load-bearing filtering metric** of [[MedVAL]], introduced in [[2507.03152-medval|Aali et al. (2026)]] §2.1. Quantifies how well a validator $v_\phi$ agrees with the generator $g_\theta$ about the factual degradation level $\delta$ that was injected into a synthetic training example, by combining **absolute** and **relative** consistency.

## Definition

Let $\hat\delta_\mathrm{clean} = v_\phi(x, \hat y)$ and $\hat\delta_\mathrm{corrupt} = v_\phi(x, \hat y_\delta)$ be the validator's predicted degradation on the clean and perturbed outputs. Then:

$$\mathcal{M}_\mathrm{consistency} = \underbrace{\lVert v_\phi(x, \hat y) \rVert_2^2 + \lVert v_\phi(x, \hat y_\delta) - \delta \rVert_2^2}_{\mathcal{M}_\mathrm{absolute}} + \underbrace{\lVert v_\phi(x, \hat y_\delta) - v_\phi(x, \hat y) - \delta \rVert_2^2}_{\mathcal{M}_\mathrm{relative}}$$

$$\mathcal{M}_\mathrm{MedVAL} = 1 - \frac{\mathcal{M}_\mathrm{consistency}}{6}$$

Division by 6 bounds the score to $[0, 1]$ (max value of the three squared-error terms each bounded by 2). **↑ score = ↑ generator-validator agreement.**

## Two components

- **Absolute consistency**: the validator's predicted degradation on clean inputs should be **close to 0**, and on perturbed inputs should be **close to $\delta$** (the level the generator was told to inject).
- **Relative consistency**: the **gap** between the validator's perturbed and clean predictions should match the injected $\delta$. This complements absolute consistency by penalizing validators that uniformly mis-calibrate but preserve gaps, or vice versa.

## How it's used

- **Filter** — keep synthetic examples with $\mathcal{M}_\mathrm{MedVAL} \ge \tau$ (default $\tau = 0.9$, chosen heuristically for high-consistency retention) for the [[BootstrapFinetune|SFT]] dataset $\mathcal{D}_\mathrm{train}$.
- **Single-pass** — not iterative; one filtering round before fine-tuning. Authors note iterative refinement is a future-work extension.

## Why it works

Ablation in [[2507.03152-medval]] §3.5: filtering at $\mathcal{M}_\mathrm{MedVAL} \ge 0.9$ retains only **57% of the data (1,131 / 2,000)** but **outperforms the unfiltered 100% baseline** on every tested student. The metric is the mechanism by which a teacher-student distillation can outperform vanilla distillation — *the filter, not the teacher, drives the gain*.

> *"Filtering consistently beats no filtering, and the self-distilled+MedVAL models also surpass their baselines."* — §3.5.

In a controlled self-distillation comparison (model teaches itself), filtering lifts Llama-3.2-3B from **12.8% → 22.1% F1 on just 3% of the training set**, vs **12.8% → 13.6%** unfiltered on 100%.

## Theoretical lineage

The metric formalizes [[2310.01846|Li et al. (2023) — Benchmarking and Improving Generator-Validator Consistency]] (ref [45] in MedVAL) — an established direction in the literature, here adapted to ordinal clinical-risk grading with the addition of the relative-consistency term to handle perturbation-gap preservation.

## Connections

- [[2507.03152-medval]] — the originating paper.
- [[MedVAL]] — the three-stage pipeline this metric drives.
- [[MedVALBench]] — built using this filter for its training set.
- [[RiskLevelTaxonomy]] — defines the $\delta$ values this metric operates on.
- [[BootstrapFinetune]] — the SFT step downstream of this filter.
- [[knowledgedistillation]] — the parent paradigm.
