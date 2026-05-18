---
title: "Action-Value Function (Q)"
type: concept
tags: [reinforcement-learning, formalism]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Action-Value Function (Q)

The **action-value function** (or **Q-function**) $Q^\pi:\mathcal{S}\times\mathcal{A}\to\mathbb{R}$ generalizes the [[ValueFunction|value function]] by fixing the first action ([[d2l-reinforcement-learning]] §value-iter):

$$Q^\pi(s_0,a_0)=r(s_0,a_0)+\mathbb{E}_{a_t\sim\pi(s_t)}\Big[\sum_{t=1}^\infty\gamma^t r(s_t,a_t)\Big]$$

It satisfies the Q-form [[BellmanEquation|Bellman equation]] $Q^\pi(s,a)=r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)\sum_{a'}\pi(a'\mid s')Q^\pi(s',a')$. The **optimal Q-function** $Q^*(s,a)$ gives the optimal deterministic policy directly:

$$\pi^*(s)=\arg\max_{a\in\mathcal{A}}Q^*(s,a).$$

## Why Q is the central quantity for model-free RL

Q is what [[QLearning|Q-Learning]] tabulates / parameterizes — knowing $Q^*$ lets you pick optimal actions *without* knowing the [[TransitionFunction|transition function]] $P(s'\mid s,a)$, because the $\max_a Q^*(s,a)$ step does not require an explicit expectation over $s'$. This is the structural reason DQN (Mnih et al. 2013/2015) and its successors target $Q$, not $V$.

## Connections

- [[ValueFunction]] — $V^\pi(s)=\sum_a\pi(a\mid s)Q^\pi(s,a)$.
- [[BellmanEquation]] — defines the recursive structure of $Q^\pi$ / $Q^*$.
- [[ValueIteration]] / [[QLearning]] — algorithms that iterate Bellman in the Q form.
- [[PolicyFunction]] / [[MarkovDecisionProcess]] / [[reinforcementlearning]] — surrounding formalism.
- [[d2l-reinforcement-learning]] — canonical textbook treatment.
