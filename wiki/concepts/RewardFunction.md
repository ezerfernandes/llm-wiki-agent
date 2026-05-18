---
title: "Reward Function"
type: concept
tags: [reinforcement-learning, formalism]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Reward Function

In a [[MarkovDecisionProcess|Markov decision process]] the **reward function** $r:\mathcal{S}\times\mathcal{A}\to\mathbb{R}$ assigns a scalar reward $r(s,a)$ to taking action $a$ in state $s$ ([[d2l-reinforcement-learning]] §mdp). Trajectories accumulate the [[DiscountFactor|discounted]] sum $\sum_t \gamma^t r_t$ as the **return**, and the RL objective is to find a [[PolicyFunction|policy]] maximizing expected return.

## Design is the engineer's job

> *"It is important to note that the reward is designed by the user (the person who creates the reinforcement learning algorithm) with the goal in mind."* — [[d2l-reinforcement-learning]] §mdp.

Reward design (or *reward shaping*) is one of the central practical difficulties in RL — poorly designed rewards lead to **reward hacking** (the policy maximizes the proxy in unintended ways). FrozenLake-v1 uses a deliberately sparse reward: $r=1$ at the goal cell, $r=0$ everywhere else.

## Connections

- [[TransitionFunction]] — the other MDP function.
- [[ValueFunction]] / [[ActionValueFunction]] — definitions integrate $r$ along trajectories.
- [[MarkovDecisionProcess]] / [[reinforcementlearning]] / [[DiscountFactor]] — surrounding formalism.
- [[d2l-reinforcement-learning]] — canonical textbook treatment.
