---
title: "Value Function"
type: concept
tags: [reinforcement-learning, formalism]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Value Function

For a [[PolicyFunction|policy]] $\pi$ over a [[MarkovDecisionProcess|Markov decision process]] $(\mathcal{S},\mathcal{A},T,r)$ with [[DiscountFactor|discount factor]] $\gamma$, the **value function** $V^\pi:\mathcal{S}\to\mathbb{R}$ assigns to each state $s_0$ the expected discounted return obtained by starting there and acting under $\pi$ thereafter ([[d2l-reinforcement-learning]] §value-iter):

$$V^\pi(s_0)=\mathbb{E}_{a_t\sim\pi(s_t)}\Big[\sum_{t=0}^\infty\gamma^t r(s_t,a_t)\Big]\,,\quad s_{t+1}\sim P(s_{t+1}\mid s_t,a_t).$$

It satisfies the [[BellmanEquation|Bellman equation]] $V^\pi(s)=\sum_a\pi(a\mid s)[r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^\pi(s')]$ for every state.

The **optimal value function** is $V^*(s)=V^{\pi^*}(s)=\max_\pi V^\pi(s)$.

## Related quantities

- [[ActionValueFunction|Action-value function]] $Q^\pi(s,a)$ — value of taking action $a$ first, then following $\pi$. Relation: $V^\pi(s)=\sum_a\pi(a\mid s)Q^\pi(s,a)$.
- **Advantage function** $A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s)$ — relative benefit of $a$ at $s$.

## Connections

- [[BellmanEquation]] — defines the recursive structure of $V^\pi$.
- [[ValueIteration]] — algorithm that iterates Bellman to compute $V^*$ when the MDP is known.
- [[PolicyFunction]] / [[ActionValueFunction]] / [[DiscountFactor]] / [[MarkovDecisionProcess]] / [[reinforcementlearning]] — surrounding formalism.
- [[d2l-reinforcement-learning]] — canonical textbook treatment.
