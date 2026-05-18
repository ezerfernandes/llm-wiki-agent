---
title: "Topological Weight"
type: concept
tags: [agentic-ai, dag, gradient-flow, generalization]
sources: [2605.12966-agentic-ai-to-agi]
last_updated: 2026-05-15
---

# Topological Weight

For an [[AgenticAI]] DAG $\Psi = (\mathcal{G}, \mathcal{F}, \Lambda)$, the **Topological Weight** $\omega_u$ of a node $u$ is the scalar sensitivity of the global loss $\mathcal{L}$ to the output of agent $u$, aggregating gradient flow along *all* paths from $u$ to all sink nodes (Lemma 4.2 of [[2605.12966-agentic-ai-to-agi]]).

## Definition

$$\omega_u = \left\| \frac{d\mathcal{L}}{d x_u} \right\| = \left\| \sum_{v\in\text{Sinks}} \frac{\partial\mathcal{L}}{\partial x_v} \sum_{\rho\in\text{Paths}(u\to v)} \underbrace{\prod_{(a,b)\in\rho} J_{ba}}_{\text{Weight of path }\rho} \right\|$$

where $J_{ba} = \partial f_b/\partial x_a$ is the local Jacobian on edge $(a,b)\in\mathcal{E}$.

## Proof sketch (Appendix A.2)

Because the agents are topologically sorted, the Direct-Adjacency Jacobian matrix $\mathbf{J}\in\mathbb{R}^{K\times K}$ with $J_{ji} = \partial f_j/\partial x_i$ if $(i,j)\in\mathcal{E}$ else $0$ is strictly lower-triangular and *nilpotent*. The total-influence matrix $\mathbf{M}\in\mathbb{R}^{K\times K}$ with $M_{ji} = dx_j/dx_i$ satisfies $\mathbf{M} = \mathbf{J}\mathbf{M} + \mathbf{I}$, i.e. $\mathbf{M} = (\mathbf{I}-\mathbf{J})^{-1} = \sum_{k=0}^{K-1}\mathbf{J}^k$. $\mathbf{J}^k$ aggregates path-influence of length exactly $k$. The vector of topological weights is then $\boldsymbol\omega = \mathbf{M}^\top \mathbf{g}$, with $\mathbf{g}$ the gradient at the sinks.

## Why this matters

- **Aggregated into the [[CompositionalCapacity]].** $C(\mathcal{G}) = \sum_u \omega_u$ — Topological Weight is the per-agent building block of the system's error magnitude.
- **Pin-points stability hotspots.** A node with disproportionately large $\omega_u$ is a leverage point: small perturbations to its output dominate the global loss. Conversely, a node with $\omega_u \to 0$ is effectively dead weight.
- **Decomposes single-edge contributions.** Lemma 4.4 ([[TopologicalEdgeWeight]]) further decomposes the gradient flux through a *specific edge* into Upstream History · Local Valve · Downstream Future — the design principle behind contractive critic edges and ultra-tight verification edges.

## Connections
- [[2605.12966-agentic-ai-to-agi]]
- [[AgenticAI]]
- [[CompositionalCapacity]]
- [[TopologicalEdgeWeight]]
