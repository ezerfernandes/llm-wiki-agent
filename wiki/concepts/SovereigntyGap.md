---
title: "Sovereignty Gap ($G_\\mathcal{S}$)"
type: concept
tags: [multi-agent, evaluation, alignment, interpretability]
sources: [2605.10698-bystander-effect-mas]
last_updated: 2026-05-15
---

# Sovereignty Gap ($G_\mathcal{S}$)

Theorem 3 of [[2605.10698-bystander-effect-mas]]:

$$G_\mathcal{S} = \mathcal{V}_{int} - \mathcal{A}_{ext}$$

where $\mathcal{V}_{int}$ is the validity of the propagator's internal Chain-of-Thought (operationalized as evidence-weighting score $\mathcal{E}_{ew}/5$) and $\mathcal{A}_{ext}$ is the accuracy of its final externalized response. The sign of $G_\mathcal{S}$ distinguishes two failure modes:

- **$G_\mathcal{S} \gg 0$ ([[AlignmentHallucination]]):** model derived correctly, externalized wrong. e.g. GPT-5.4 on SWE-bench at $n=5$: $\mathcal{V}_{int}\approx 0.71$, $\mathcal{A}_{ext}=0.37$, $G_\mathcal{S}=+0.34$.
- **$G_\mathcal{S} \ll 0$ ([[IntegrativeReasoningBypass]]):** model never derived; residual accuracy is probabilistic guessing. e.g. GPT-5.4 on GAIA at $n=5$: $\mathcal{V}_{int}\approx 0.21$, $\mathcal{A}_{ext}=0.53$, $G_\mathcal{S}=-0.32$.

Operationally important: a non-zero $G_\mathcal{S}$ is the wiki's reference example of [[chainofthought|CoT]] *unfaithfulness* — a measured case where CoT and final answer diverge under social pressure. Connects to [[imlbook-evaluation|interpretability evaluation]] (the gap is exactly what CoT-as-explanation would mispredict).
