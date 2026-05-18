---
title: "Bellman Equation"
type: concept
tags: [reinforcement-learning, dynamic-programming, formalism]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Bellman Equation

The recursive identity that decomposes the [[ValueFunction|value]] of a state into the **immediate reward plus the discounted value of the next state**, averaged over the [[PolicyFunction|policy]] and [[TransitionFunction|transitions]] ([[d2l-reinforcement-learning]] §value-iter). The foundation of all [[reinforcementlearning|reinforcement-learning]] algorithms.

## Bellman expectation equation (for a policy $\pi$)

$$V^\pi(s)=\sum_{a\in\mathcal{A}}\pi(a\mid s)\Big[r(s,a)+\gamma\sum_{s'\in\mathcal{S}}P(s'\mid s,a)V^\pi(s')\Big]$$

Equivalent [[ActionValueFunction|Q-form]]:

$$Q^\pi(s,a)=r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)\sum_{a'}\pi(a'\mid s')Q^\pi(s',a')$$

## Bellman optimality equation (for the optimal policy $\pi^*$)

$$V^*(s)=\max_{a\in\mathcal{A}}\Big\{r(s,a)+\gamma\sum_{s'\in\mathcal{S}}P(s'\mid s,a)V^*(s')\Big\}$$

$$Q^*(s,a)=r(s,a)+\gamma\sum_{s'\in\mathcal{S}}P(s'\mid s,a)\max_{a'}Q^*(s',a')$$

Both are **fixed-point equations** that hold for every $s\in\mathcal{S}$ (or every $(s,a)$).

## Why it matters

> *"The average return from the current state is the sum of the average return from the next state and the average reward of going to the next state."* — [[d2l-reinforcement-learning]] §value-iter. The Bellman decomposition is the algorithmic basis of [[ValueIteration]] (model-based), [[QLearning|Q-Learning]] (model-free off-policy TD), [[PolicyFunction|policy evaluation]], and every modern RL algorithm.

## Connections

- [[DynamicProgramming]] — Bellman (1950s) — the principle that the *remainder of an optimal trajectory is itself optimal* is exactly what the Bellman optimality equation expresses.
- [[ValueIteration]] / [[QLearning]] — algorithms that iterate Bellman as a fixed-point recurrence.
- [[ValueFunction]] / [[ActionValueFunction]] / [[PolicyFunction]] / [[MarkovDecisionProcess]] / [[reinforcementlearning]] / [[DiscountFactor]] — surrounding RL concepts.
- [[RichardBellman]] — named after the mathematician who introduced it.
- [[d2l-reinforcement-learning]] — derives and operationalizes the Bellman equation.
