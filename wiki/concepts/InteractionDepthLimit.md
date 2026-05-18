---
title: "Interaction Depth Limit ($D_L$)"
type: concept
tags: [multi-agent, evaluation, scaling]
sources: [2605.10698-bystander-effect-mas]
last_updated: 2026-05-15
---

# Interaction Depth Limit ($D_L$)

The plurality threshold — minimum number $n$ of simulated auditors — at which a propagator LLM's [[AgenticSovereignty]] crosses below 0.5 and the [[BystanderEffect]] inevitably triggers ($\mathcal{B}=1$). Defined in [[2605.10698-bystander-effect-mas]] via the [[SovereigntyDecayLaw]]; closed-form inequality (Corollary 1):

$$\sum_{i=1}^{D_L} w_i \cdot \alpha(a_i) \cdot \kappa(p,a_i) > \frac{\gamma_p}{\mathcal{H}_\tau} \ln(2\mathcal{S}_0)$$

Empirical $D_L$ from the 22,500-trajectory audit:

| Model | $D_L$ (rough) |
|---|---|
| [[claudeopus47|Claude Sonnet 4.6]] | $\to\infty$ (no collapse observed at $n=5$, $\mathcal{A}=1.00$ on SWE-bench) |
| [[gemini|Gemini 3.1 Pro]] | $\approx 2$–$3$, non-monotonic (kinship-modulated) |
| [[gpt54|GPT-5.4]] | $\approx 2$ ($\mathcal{A}$ collapses to 0.23 on SWE-bench at $n=2$) |

The 0.5 cutoff is a definitional choice, not a derived constant — useful as a comparable architecture benchmark, less so as an absolute claim.
