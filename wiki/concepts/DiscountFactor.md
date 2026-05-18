---
title: "Discount Factor"
type: concept
tags: [reinforcement-learning, formalism]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Discount Factor ($\gamma$)

The **discount factor** $\gamma\in[0,1)$ in [[reinforcementlearning|reinforcement learning]] downweights future rewards in the trajectory return ([[d2l-reinforcement-learning]] §mdp):

$$R(\tau)=\sum_{t=0}^\infty\gamma^t r_t=r_0+\gamma r_1+\gamma^2 r_2+\cdots$$

## Two roles

1. **Mathematical** — keeps the return finite for infinite-horizon trajectories (geometric series convergence requires $\gamma<1$). Without discounting, the return of any trajectory that never reaches a terminal state would be infinite.
2. **Behavioral** — encodes a preference for *near-term* rewards. Small $\gamma$ ≈ 0 yields myopic, "greedy" agents that ignore long-term consequences; $\gamma$ near 1 (e.g., 0.99) yields far-sighted agents willing to explore.

## On FrozenLake-v1 ([[d2l-reinforcement-learning]])

D2L uses $\gamma=0.95$ — the agent values a reward 100 steps away at $0.95^{100}\approx 0.006$ of its immediate value, which biases toward shorter paths to the goal.

## Connections

- [[ValueFunction]] / [[ActionValueFunction]] — the discount appears in the definition of $V^\pi$ and $Q^\pi$.
- [[BellmanEquation]] — $\gamma$ multiplies the bootstrap term $V(s')$.
- [[ValueIteration]] / [[QLearning]] — both iterate updates whose contraction rate is $\gamma$.
- [[MarkovDecisionProcess]] / [[reinforcementlearning]] — surrounding formalism.
- [[d2l-reinforcement-learning]] — canonical textbook treatment.
