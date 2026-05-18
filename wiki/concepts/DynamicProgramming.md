---
title: "Dynamic Programming"
type: concept
tags: [algorithm-design, optimization, reinforcement-learning]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Dynamic Programming

[[RichardBellman|Bellman]]'s 1950s framework for solving sequential decision problems by **decomposing them into overlapping subproblems** ([[d2l-reinforcement-learning]] §value-iter). The defining principle:

> *"The remainder of an optimal trajectory is also optimal."*

Equivalently, the optimal value of being in state $s$ is the max over actions of (immediate reward + discounted optimal value of the resulting state) — exactly the form of the [[BellmanEquation|Bellman optimality equation]]:

$$V^*(s)=\max_{a\in\mathcal{A}}\Big\{r(s,a)+\gamma\sum_{s'\in\mathcal{S}}P(s'\mid s,a)V^*(s')\Big\}.$$

## In RL

Dynamic programming under known [[MarkovDecisionProcess|MDP]] dynamics gives the **planning** algorithms:

- [[ValueIteration|Value Iteration]] — iterate the Bellman optimality equation until convergence.
- **Policy Iteration** — alternate policy evaluation + policy improvement steps.
- **Policy Evaluation** — iterate the Bellman expectation equation to compute $V^\pi$ for a fixed $\pi$.

When dynamics are unknown, **sample-based approximations** (Monte Carlo, [[TemporalDifferenceLearning|TD]] / [[QLearning|Q-Learning]]) replace the analytical expectation $\sum_{s'}P(s'\mid s,a)$ with sample averages — but the Bellman decomposition is still the structural foundation.

## Outside RL

Dynamic programming is also the basis of countless algorithms in CS: shortest paths (Bellman–Ford), edit distance (Levenshtein), sequence alignment (Needleman–Wunsch), HMM inference (forward–backward, Viterbi), and many more.

## Connections

- [[BellmanEquation]] — the recurrence that DP iterates.
- [[ValueIteration]] / [[QLearning]] / [[TemporalDifferenceLearning]] — DP and its sample-based extensions in RL.
- [[RichardBellman]] — formulated the principle (1950s).
- [[MarkovDecisionProcess]] / [[reinforcementlearning]] — the formalism DP operates on.
- [[d2l-reinforcement-learning]] — operationalizes DP via Value Iteration.
