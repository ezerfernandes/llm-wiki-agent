---
title: "Value Iteration"
type: concept
tags: [reinforcement-learning, dynamic-programming, algorithm]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Value Iteration

The canonical **model-based** algorithm for solving a [[MarkovDecisionProcess|Markov Decision Process]] when the [[TransitionFunction|transition function]] $P(s'\mid s,a)$ and [[RewardFunction|reward]] $r(s,a)$ are fully known ([[d2l-reinforcement-learning]] §value-iter). Turns the [[BellmanEquation|Bellman optimality equation]] into a fixed-point iteration on the [[ValueFunction|value function]]:

$$V_{k+1}(s)=\max_{a\in\mathcal{A}}\Big\{r(s,a)+\gamma\sum_{s'\in\mathcal{S}}P(s'\mid s,a)V_k(s')\Big\}$$

initialized from arbitrary $V_0$, with $V_k\to V^*$ as $k\to\infty$ regardless of $V_0$. The optimal deterministic [[PolicyFunction|policy]] is then read off via $\pi^*(s)=\arg\max_a\{r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^*(s')\}$.

## Equivalent Q-form

$$Q_{k+1}(s,a)=r(s,a)+\gamma\max_{a'\in\mathcal{A}}\sum_{s'\in\mathcal{S}}P(s'\mid s,a)Q_k(s',a')$$

The action-value form is the bridge to [[QLearning|Q-Learning]] — the *only* change Q-Learning makes is replacing the $\sum_{s'}P(s'\mid s,a)$ expectation with a single sample from the environment.

## Policy Evaluation (variant)

The same iteration with $\pi(a\mid s)$ in place of $\max_a$ computes $V^\pi$ for any fixed policy $\pi$:

$$V^\pi_{k+1}(s)=\sum_{a}\pi(a\mid s)\Big[r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^\pi_k(s')\Big]$$

## Empirical convergence ([[d2l-reinforcement-learning]] §value-iter)

On OpenAI Gym's `FrozenLake-v1` (4×4 grid, deterministic actions, $\gamma=0.95$) Value Iteration finds the optimal value function and policy in **~10 sweeps**, an order of magnitude faster than [[QLearning|Q-Learning]] on the same problem — *"this happens because the Value Iteration algorithm has access to the full MDP whereas Q-learning does not."*

## Connections

- [[BellmanEquation]] — the recurrence Value Iteration iterates.
- [[DynamicProgramming]] — Bellman's "remainder of an optimal trajectory is also optimal" principle on which the convergence rests.
- [[QLearning]] — the model-free analog when $P(s'\mid s,a)$ is unknown.
- [[MarkovDecisionProcess]] / [[reinforcementlearning]] / [[ValueFunction]] / [[ActionValueFunction]] / [[PolicyFunction]] / [[DiscountFactor]] — surrounding RL concepts.
- [[d2l-reinforcement-learning]] — operationalizes Value Iteration on FrozenLake-v1.
