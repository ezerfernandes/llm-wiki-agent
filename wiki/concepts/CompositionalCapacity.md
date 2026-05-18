---
title: "Compositional Capacity"
type: concept
tags: [agentic-ai, dag, generalization, topology]
sources: [2605.12966-agentic-ai-to-agi]
last_updated: 2026-05-15
---

# Compositional Capacity

The **Compositional Capacity** $C(\mathcal{G})$ — also called the **Topology Factor** — is the scalar quantity introduced in Theorem 4.3 of [[2605.12966-agentic-ai-to-agi]] that governs the *error magnitude* of a general [[AgenticAI]] system. It captures how the DAG topology amplifies or attenuates per-agent errors as they propagate to sink nodes.

## Definition

For an Agentic AI system $\Psi = (\mathcal{G}, \mathcal{F}, \Lambda)$ with $K$ nodes:

$$C(\mathcal{G}) \equiv \sum_{u=1}^K \omega_u = \sum_{u=1}^K \left\| \sum_{v\in\text{Sinks}} \frac{\partial\mathcal{L}}{\partial x_v} \sum_{\rho\in\text{Paths}(u\to v)} \prod_{e\in\rho} J_e \right\|$$

where $\omega_u$ is the [[TopologicalWeight]] of node $u$ and $J_e$ is the local Jacobian on edge $e$.

Equivalently, $\boldsymbol{\omega} = \mathbf{M}^\top \mathbf{g}$ where $\mathbf{M} = (\mathbf{I} - \mathbf{J})^{-1} = \sum_{k=0}^{K-1}\mathbf{J}^k$ (a finite Neumann series since the Jacobian matrix $\mathbf{J}$ is strictly lower-triangular and nilpotent for any DAG, Appendix A.2) and $\mathbf{g}$ is the gradient at the sinks.

## Convergence governance

Theorem 4.3 splits the Agentic AI generalization error into two governing quantities:

$$\mathcal{E}_{\text{Agentic}} \approx C(\mathcal{G}) \cdot \mathcal{O}\!\left((N/K)^{-1/d_{\text{eff}}}\right)$$

- The **effective intrinsic dimension** $d_{\text{eff}}$ — geometry of the task — governs the *convergence rate*.
- The **Compositional Capacity** $C(\mathcal{G})$ — topology of the agent graph — governs the *error magnitude*.

Agentic AI succeeds when the topology *minimizes $C(\mathcal{G})$* while *maximizing the dimensionality gap* $D - d_{\text{eff}}$. A finite $C(\mathcal{G}) < \infty$ is sufficient for the Agentic AI Convergence Superiority result over a monolithic learner.

## Implications

- **DAG complexity scaling.** $C(\mathcal{G})$ scales explicitly with DAG topology; comparing $C$ across alternative orchestration designs gives a quantitative basis for choosing topologies before deployment.
- **MoE special case.** §5 of the paper shows that the routing regime of §3.2 ([[MixtureOfExperts]] / [[RoutingBasedAgenticAI]]) corresponds to $C(\mathcal{G}) \approx \sum_u L_u$ — a bounded sum of per-agent Lipschitz constants, and therefore inherently stable. This makes MoE the "well-behaved" sub-class of Agentic AI on the topology axis.
- **Failure attribution.** Empirical multi-agent failures (Pan et al. 2025, Zhang et al. 2025) are read by the paper as pathologically large $C(\mathcal{G})$ — not paradigm-level defects.

## Connections
- [[2605.12966-agentic-ai-to-agi]]
- [[AgenticAI]]
- [[TopologicalWeight]]
- [[TopologicalEdgeWeight]]
- [[MixtureOfExperts]]
- [[RoutingBasedAgenticAI]]
