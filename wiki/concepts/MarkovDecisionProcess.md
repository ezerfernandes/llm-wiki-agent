---
title: "Markov Decision Process"
type: concept
tags: [reinforcement-learning, formalism]
sources: [d2l-introduction, d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Markov Decision Process (MDP)

The **fully-observed** special case of the [[reinforcementlearning|reinforcement-learning]] problem ([[d2l-introduction]]). Tuple $(\mathcal{S}, \mathcal{A}, T, r)$ ([[d2l-reinforcement-learning]] §mdp):

- $\mathcal{S}$ — state space.
- $\mathcal{A}$ — action space.
- $T(s,a,s')=P(s'\mid s,a)$ — [[TransitionFunction|transition kernel]], with $\sum_{s'}T(s,a,s')=1$ (Markov property: the future depends only on the present state, not the trajectory).
- $r(s,a)$ — [[RewardFunction|reward function]] — designed by the user to express the goal.

The agent's behavior is a [[PolicyFunction|policy]] $\pi(a\mid s)$, and the goal is to find $\pi^*$ maximizing the expected [[DiscountFactor|$\gamma$-discounted]] return $\mathbb{E}[\sum_t \gamma^t r_t]$. The [[BellmanEquation|Bellman equation]] decomposes the [[ValueFunction|value]] of a state into immediate reward + discounted next-state value; [[ValueIteration|Value Iteration]] iterates it to convergence; [[QLearning|Q-Learning]] samples it when $T$ is unknown.

## Where it sits in the RL taxonomy

[[d2l-introduction]] orders the special cases by their state structure:

| Problem | State? | Memory? |
|---|---|---|
| **Markov decision process** | Yes, fully observed | Markov — no need for history |
| **Contextual bandit** | State independent of past actions | Each step is i.i.d. given the context |
| **[[MultiArmedBandits\|Multi-armed bandit]]** | No state | Pure exploit/explore on action rewards |

Adding *partial observability* takes us out of the MDP setting into the **POMDP** regime; the chapter's "cleaning robot trapped in identical closets" is the canonical example.

## The Markov-property trick

If dynamics appear non-Markovian (e.g., next location depends on velocity), **expand the state** — a $(\text{location},\text{velocity})$ pair restores the Markov property. [[d2l-reinforcement-learning]] §mdp: *"Markov Decision Processes are still capable of modeling a very large class of real systems."*

## Connections

- [[reinforcementlearning]] — parent framework.
- [[MultiArmedBandits]] — bare-bones special case.
- [[TransitionFunction]] / [[RewardFunction]] / [[PolicyFunction]] / [[ValueFunction]] / [[ActionValueFunction]] / [[BellmanEquation]] / [[DynamicProgramming]] / [[DiscountFactor]] — the MDP formalism.
- [[ValueIteration]] / [[QLearning]] — the two canonical solution algorithms.
- [[d2l-introduction]] — chapter that introduces MDP as the canonical fully-observed RL setting.
- [[d2l-reinforcement-learning]] — chapter that develops MDPs in algorithmic depth.
