---
title: "Policy (RL)"
type: concept
tags: [reinforcement-learning, formalism]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Policy

In [[reinforcementlearning|reinforcement learning]], a **policy** $\pi$ is a mapping from states to actions that defines the agent's behavior. Two flavors ([[d2l-reinforcement-learning]] §value-iter):

- **Stochastic policy** $\pi(a\mid s)\equiv P(a\mid s)$ — a conditional distribution over $\mathcal{A}$ given $s$, with $\sum_a\pi(a\mid s)=1$ for all $s$.
- **Deterministic policy** $\pi(s)\in\mathcal{A}$ — the special case where $\pi(\cdot\mid s)$ is a one-hot, e.g., $[1,0,0,0]$ over four actions.

The **optimal policy** $\pi^*=\arg\max_\pi V^\pi(s_0)$ maximizes the expected discounted return. For a deterministic optimal policy under known dynamics:

$$\pi^*(s)=\arg\max_{a\in\mathcal{A}}\Big\{r(s,a)+\gamma\sum_{s'\in\mathcal{S}}P(s'\mid s,a)V^*(s')\Big\}$$

## Behavior vs target policy ([[OffPolicyLearning|off-policy]])

In [[QLearning|Q-Learning]] the **behavior / exploration policy** $\pi_e$ (e.g., [[EpsilonGreedy|$\epsilon$-greedy]]) used to *collect data* is different from the **target policy** $\arg\max_a\hat{Q}(s,a)$ being *learned*. On-policy methods (SARSA, REINFORCE) by contrast share a single policy for both roles.

## Connections

- [[ValueFunction]] — $V^\pi(s)$ is defined relative to a policy.
- [[ActionValueFunction]] — $Q^\pi(s,a)$ likewise.
- [[BellmanEquation]] — defines the recursive structure of $V^\pi$.
- [[EpsilonGreedy]] / [[ExplorationExploitation]] — common stochastic-policy choices for $\pi_e$.
- [[OffPolicyLearning]] — the behavior-vs-target policy distinction.
- [[reinforce|REINFORCE]] — direct gradient ascent on $V^\pi$ via the log-derivative trick.
- [[MarkovDecisionProcess]] / [[reinforcementlearning]] — surrounding formalism.
- [[d2l-reinforcement-learning]] — the canonical textbook treatment.
