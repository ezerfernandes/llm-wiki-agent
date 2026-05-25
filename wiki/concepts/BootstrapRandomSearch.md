---
title: "Bootstrap Random Search"
type: concept
tags: [prompt-optimization, few-shot, demonstrations, dspy, baseline]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# Bootstrap Random Search

The **demos-only baseline optimizer** in the [[2406.11695-mipro|MIPRO paper]] (§4.1), originating in Khattab et al. 2024 ([[DSPy]]) and shipped as [[BootstrapFewShotWithRandomSearch|`dspy.BootstrapFewShotWithRandomSearch`]] in DSPy.

> **Name overload.** The MIPRO paper calls the algorithm "Bootstrap Random Search" (BRS); the [[DSPy]] codebase ships the equivalent as [[BootstrapFewShotWithRandomSearch|`BootstrapFewShotWithRandomSearch`]] (BFRS). They are the same algorithm; the canonical DSPy concept page is [[BootstrapFewShotWithRandomSearch]].

## Algorithm (Figure 2 of the [[2406.11695-mipro|paper]])

**Step 1 — Bootstrap demonstrations.** For each module $m$ in $\Phi$:
1. Sample $(x, x') \in \mathcal{D}$.
2. Run $\Phi(x)$, recording the full trace $\tau$ (per-module inputs/outputs).
3. If $\mu(\Phi(x), x') \geq \lambda$, take all values in $\tau$ as potential labeled demonstrations for the respective module.
4. Repeat until $N$ sets of $K$ few-shot examples have been bootstrapped per module.

**Step 2 — Search combinations.** Random search over the $N$ bootstrapped sets:
1. Sample a set of few-shot examples and use them to parameterize each module in $\Phi$.
2. Evaluate the parameterized $\Phi$ on the trainset (or a validation split).
3. Record the score.
4. Return the top-scoring assignment.

## Position in the catalog

In the [[2406.11695-mipro|paper's benchmark]], BRS is the **demos-only optimizer** — the structural baseline against which both [[MIPROv2|MIPRO]] (demos + instructions) and [[ModuleLevelOPRO|Module-Level OPRO]] (instructions only) are compared. The paper's **Lesson 1** is that demos-only beats instructions-only on most tasks — i.e. **BRS is a strong baseline** even though MIPRO's joint optimization still wins on 5/7 tasks.

The paper also studies **Bayesian Bootstrap** (the demos-only restriction of MIPRO that uses [[BayesianOptimization|Bayesian]] mini-batch evaluation rather than full-batch evaluation over a fixed set of bootstrapped demos). Bayesian Bootstrap outperforms BRS on [[ScoNe]] but is not statistically significant for [[hotpotqa|HotPotQA]] or [[HoVer]].

## Connections

- [[BootstrapFewShotWithRandomSearch]] — the [[DSPy]] implementation; canonical wiki anchor for the algorithm.
- [[2406.11695-mipro]] — the canonical paper where BRS is named.
- [[BootstrapFewShot]] — the parent algorithm (single-trial, no random search over multiple bootstrapped sets).
- [[MIPROv2|MIPRO]] — the demos-plus-instructions successor.
- [[BootstrapDemonstrations]] — the metric-filtered trace-collection step BRS shares with MIPRO.
- [[2407.10930-better-together|BetterTogether]] — uses BRS as its prompt-axis primitive in the $\Pi \to \Theta \to \Pi$ schedule.
