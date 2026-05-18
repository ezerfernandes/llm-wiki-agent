---
title: "Temporal-Difference Learning"
type: concept
tags: [reinforcement-learning, algorithm-family, model-free]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Temporal-Difference (TD) Learning

A family of [[ModelFreeLearning|model-free]] RL methods that update value estimates by **bootstrapping** from the current estimate at the next state, rather than waiting for the full Monte-Carlo return ([[d2l-reinforcement-learning]] §qlearning). The defining structure of every TD method is the **TD update**:

$$V(s_t)\leftarrow V(s_t)+\alpha\underbrace{\Big[r_t+\gamma V(s_{t+1})-V(s_t)\Big]}_{\text{TD error}}$$

or, in action-value form (the case used by [[QLearning]]):

$$Q(s_t,a_t)\leftarrow Q(s_t,a_t)+\alpha\Big[r_t+\gamma\max_{a'}Q(s_{t+1},a')-Q(s_t,a_t)\Big].$$

The bracketed quantity is the **TD error** — the discrepancy between the current estimate and a one-step lookahead.

## TD vs Monte Carlo vs DP

- **Monte Carlo**: wait for the full episode return, average across episodes. Unbiased but high-variance, requires episode termination.
- **Dynamic programming** ([[ValueIteration]]): use the analytical expectation $\sum_{s'}P(s'\mid s,a)V(s')$. Requires knowing $P$.
- **TD**: bootstrap from $V(s_{t+1})$ using a *single sample* of the next state — biased early (because $V(s_{t+1})$ is itself an estimate) but lower variance than MC and no model required.

## On-policy vs off-policy

- **SARSA** (on-policy TD): target uses the action *actually taken* by the behavior policy at $s_{t+1}$.
- **[[QLearning|Q-Learning]]** (off-policy TD): target uses $\max_{a'}Q(s_{t+1},a')$, regardless of which action $\pi_e$ would pick. This decouples the behavior policy from the learned policy.

## Connections

- [[QLearning]] — the canonical off-policy TD algorithm.
- [[BellmanEquation]] — the TD target is the sample-form of the Bellman one-step recurrence.
- [[OffPolicyLearning]] / [[ModelFreeLearning]] — the structural family TD inhabits.
- [[ValueIteration]] — the model-based counterpart that uses the full expectation.
- [[ActionValueFunction]] / [[ValueFunction]] / [[reinforcementlearning]] / [[MarkovDecisionProcess]] — surrounding formalism.
- [[d2l-reinforcement-learning]] — operationalizes off-policy TD via Q-Learning on FrozenLake-v1.
