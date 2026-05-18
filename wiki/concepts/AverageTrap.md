---
title: "Average Trap"
type: concept
tags: [learning-theory, multi-task, generalization, negative-transfer]
sources: [2605.12966-agentic-ai-to-agi]
last_updated: 2026-05-15
---

# Average Trap

The **Average Trap** (Proposition 3.3 in [[2605.12966-agentic-ai-to-agi]]) is the formal name for the irreducible quadratic penalty a monolithic learner pays when forced to compromise across heterogeneous task optima. It is the learning-theoretic mechanism behind the "Generalist's Penalty" — the empirical fact that monoliths trade peak acuity for stability as task diversity grows.

## Statement

Under Assumption 3.1 (per-task loss $\mathcal{L}_k$ is $C^2$ with positive-definite Hessian $H_k = \nabla^2\mathcal{L}_k(\theta^*_k)$) and Assumption 3.2 ($\rho$-Lipschitz Hessians), if the per-task optima $\{\theta^*_k\}$ do *not* coincide ($\exists i,j: \theta^*_i \neq \theta^*_j$), then there is a strictly positive lower-bound $\epsilon > 0$ such that

$$\mathcal{L}_{\text{total}}(\theta^*_{\text{mono}}) \approx \underbrace{\sum_{k=1}^K \alpha_k \mathcal{L}_k(\theta^*_k)}_{\mathcal{L}_{\text{ideal}}} + \underbrace{\sum_{k=1}^K \frac{\alpha_k}{2}\|\theta^*_{\text{mono}} - \theta^*_k\|^2_{H_k}}_{\epsilon}$$

where $\|v\|^2_{H_k} = v^\top H_k v$ is the squared Mahalanobis distance induced by the task's local curvature.

## Mechanism (proof sketch, Appendix A.1)

$\theta^*_{\text{mono}}$ minimizes the weighted average loss, so $\nabla\mathcal{L}_{\text{total}}(\theta^*_{\text{mono}}) = \sum_k \alpha_k \nabla\mathcal{L}_k(\theta^*_{\text{mono}}) = 0$. Unless all $\theta^*_k$ are identical this forces the per-task gradients to *cancel destructively* — $\theta^*_{\text{mono}}$ lies in the convex hull of $\{\theta^*_k\}$ but coincides with none. Taylor-expanding each $\mathcal{L}_k$ around $\theta^*_k$ yields the quadratic compromise above; the third-order Lipschitz term is dominated in a neighborhood where the positive-definite curvature is bounded.

## When the Average Trap binds (Remark B.3)

The magnitude of $\epsilon$ depends on the number of tasks $K$, the task curvatures $H_k$, and the divergence of the per-task optima. For narrow task families (small $K$, closely related tasks) the penalty is mild — the monolithic compromise stays near each individual optimum. As the task distribution broadens toward AGI-level generality, $\epsilon$ accumulates: the monolithic optimum must compromise across more divergent directions, and the effective ambient dimension $D$ of the union manifold grows with $K$, exacerbating the [[CurseOfDimensionality]].

This explains why monolithic models succeed on narrow benchmarks but progressively degrade on diverse leaderboards: the Average Trap transitions from a negligible correction to a *dominant* constraint precisely in the AGI-targeted regime.

## Relation to Negative Transfer (Remark B.2)

Equivalent to the [[NegativeTransfer]] phenomenon in multi-task learning: when task-A gradient and task-B gradient have angle $>90°$, a step that improves A worsens B. The paper notes that the Multi-Task Learning literature has tried to mitigate this via Gradient Surgery (Yu et al. 2020), Conflict-Averse Gradient Descent (Liu et al. 2021), and sparse training (Zhang et al. 2024), but the $\epsilon$ term remains an unavoidable constraint — not just an optimization difficulty.

## Connections
- [[2605.12966-agentic-ai-to-agi]]
- [[StructuredRealWorldDistribution]]
- [[AgenticAI]]
- [[CurseOfDimensionality]]
- [[NegativeTransfer]]
