---
title: "Bootstrap Demonstrations"
type: concept
tags: [dspy, few-shot, demonstrations, prompt-optimization, rejection-sampling]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# Bootstrap Demonstrations

The **metric-filtered trace-collection step** shared by every DSPy-adjacent optimizer ([[BootstrapFewShot]], [[BootstrapRandomSearch|Bootstrap Random Search]], [[MIPROv2|MIPRO]], [[BootstrapFinetune]], [[2407.10930-better-together|BetterTogether]]'s prompt-axis primitive). Originating in Khattab et al. 2024 ([[DSPy]]); the [[2406.11695-mipro|MIPRO paper]] formalizes it (§3.1).

## Algorithm

For each module $m$ in [[LMProgram|LM program]] $\Phi$:
1. Sample $(x, x') \in \mathcal{D}$ (input + optional metadata such as final-answer labels).
2. Run $\Phi(x)$ — record the **full trace** $\tau$ of per-module inputs and outputs.
3. If $\mu(\Phi(x), x') \geq \lambda$ for some threshold $\lambda$, **assume all values in the trace are potential labeled demonstrations** for the respective module.
4. Repeat until $N$ candidate sets of $K$ few-shot demos per module have been collected.

The collected demos are then **used downstream**:

| Downstream optimizer | What it does with the demos |
|---|---|
| [[BootstrapFewShot]] | Picks the first set that passes the metric. |
| [[BootstrapRandomSearch]] / [[BootstrapFewShotWithRandomSearch]] | Random search over the $N$ candidate sets, pick best on full trainset. |
| [[MIPROv2|MIPRO]] | Pass the candidate sets to the [[TreeStructuredParzenEstimator|TPE]] surrogate as categorical variables alongside candidate instructions. |
| [[BootstrapFinetune]] | Treat each trace as an SFT training example. |
| [[2407.10930-better-together|BetterTogether]] | Use the bootstrapped traces as the input to either prompt-axis search or weight-axis fine-tuning. |

## Key claim from the [[2406.11695-mipro|MIPRO paper]]

> *"Khattab et al. (2024) [show] this can often outperform hand-written demonstrations for multi-stage programs."*

The implication: **the bottleneck for few-shot prompting in multi-stage programs is not crafting demonstrations by hand but learning to filter automatically-generated traces by an end-to-end metric**.

## Why the metric supervises *traces*, not *outputs*

The deep idea is that **a high-scoring full trajectory implies all its per-module input/output pairs are likely valid** — a form of **rejection-sampling-based label propagation** for the latent per-module variables. This is the only mechanism that **converts task-level supervision into per-module training signal** without per-module labels, and it is what makes [[CreditAssignment|credit assignment]] tractable in this regime.

This trick is structurally similar to **STaR** / self-training over rationales — but here the rationales are *intermediate-module outputs* rather than chains-of-thought.

## Connections

- [[2406.11695-mipro]] — the canonical source where the formalization lives.
- [[BootstrapFewShot]] — the simplest downstream consumer.
- [[BootstrapRandomSearch]] / [[BootstrapFewShotWithRandomSearch]] — the demos-only downstream consumer.
- [[MIPROv2|MIPRO]] — the joint-optimization downstream consumer.
- [[BootstrapFinetune]] — the weight-tuning downstream consumer.
- [[2407.10930-better-together|BetterTogether]] — uses bootstrap demos as the input to the $\Pi \to \Theta \to \Pi$ schedule.
- [[CreditAssignment]] — the problem this technique partially solves.
- [[DSPy]] — the framework.
