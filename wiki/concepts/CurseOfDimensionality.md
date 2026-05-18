---
title: "Curse of Dimensionality"
type: concept
tags: [learning-theory, foundational, sample-complexity]
sources: [2605.12966-agentic-ai-to-agi]
last_updated: 2026-05-15
---

# Curse of Dimensionality

Coined by Bellman (1957). As input dimension $D$ grows, the volume of a unit hypercube concentrates in its corners and the ratio $V_{\text{sphere}}(r,D)/V_{\text{cube}}(r,D) \to 0$. Local density estimation, nearest-neighbor methods, and Lipschitz function approximation all need *exponentially many* samples in $D$ to cover the input domain.

## Quantitative statement (Stone 1982)

Proposition 2.2 of [[2605.12966-agentic-ai-to-agi]] restates the classical minimax lower bound: for the class $\mathcal{F}_L$ of $L$-Lipschitz functions on a compact $\Omega\subset\mathbb{R}^D$ and any estimator $\hat f_N$ based on $N$ samples,

$$\inf_{\hat f_N} \sup_{f\in\mathcal{F}_L} \mathbb{E}\!\left[\int_\Omega |\hat f_N(x) - f(x)|\,dP(x)\right] \geq C\cdot N^{-\frac{1}{2+D}}.$$

The exponent $-1/(2+D)$ is what makes brute-force learning in high $D$ infeasible: to halve the error, sample count must grow by a factor of $2^{2+D}$.

## How structure breaks the curse

The escape, used throughout [[2605.12966-agentic-ai-to-agi]], is that real-world tasks live on a [[StructuredRealWorldDistribution]] — a union of low-dimensional manifolds $\bigcup_k \mathcal{M}_k$ with $d_k \ll D$. Routing $x$ to the agent specialized in $\mathcal{M}_k$ replaces $N^{-1/D}$ with $N^{-1/d_{\max}}$ — exponentially better. This is the *learning-theoretic* reason [[AgenticAI]] beats a monolithic learner; the [[AverageTrap]] is the *optimization-theoretic* reason.

## Connections
- [[2605.12966-agentic-ai-to-agi]]
- [[NoFreeLunchTheorem]]
- [[StructuredRealWorldDistribution]]
- [[AgenticAI]]
- [[RoutingBasedAgenticAI]]
