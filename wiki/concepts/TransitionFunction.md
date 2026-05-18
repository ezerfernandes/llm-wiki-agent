---
title: "Transition Function"
type: concept
tags: [reinforcement-learning, formalism]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Transition Function

In a [[MarkovDecisionProcess|Markov decision process]] $(\mathcal{S},\mathcal{A},T,r)$ the **transition function** $T:\mathcal{S}\times\mathcal{A}\times\mathcal{S}\to[0,1]$ encodes the probabilistic dynamics:

$$T(s,a,s')=P(s'\mid s,a)$$

with $\sum_{s'\in\mathcal{S}}T(s,a,s')=1$ for every $(s,a)$ pair ([[d2l-reinforcement-learning]] §mdp) — i.e., the agent must transition *somewhere*. Captures stochastic effects: when the robot commands "go forward," there may be a small probability it stays, turns left, etc.

## Why it matters algorithmically

- [[ValueIteration|Value Iteration]] requires $T$ explicitly — the $\sum_{s'}P(s'\mid s,a)V_k(s')$ expectation is at the heart of every backup.
- [[QLearning|Q-Learning]] does *not* require $T$ — the key Q-Learning insight is to replace the analytical expectation with a sample average over states the agent actually visits.
- This distinction is the model-based vs [[ModelFreeLearning|model-free]] split.

## Connections

- [[MarkovDecisionProcess]] — the formalism $T$ lives in.
- [[RewardFunction]] — the other MDP function.
- [[ValueIteration]] / [[QLearning]] / [[ModelFreeLearning]] / [[BellmanEquation]] — algorithmic uses.
- [[d2l-reinforcement-learning]] — canonical textbook treatment.
