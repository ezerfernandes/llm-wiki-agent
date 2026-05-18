---
title: "Model-Free Learning"
type: concept
tags: [reinforcement-learning, algorithm-family]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Model-Free Learning

An RL algorithm is **model-free** if it learns optimal behavior **without explicitly estimating or knowing the [[TransitionFunction|transition function]] $P(s'\mid s,a)$** of the [[MarkovDecisionProcess|MDP]] ([[d2l-reinforcement-learning]] §qlearning).

## Contrast with model-based

- **Model-based** ([[ValueIteration|Value Iteration]], MCTS, AlphaZero): requires (or estimates) $P$ and $r$, then plans by Bellman backups over the model.
- **Model-free** ([[QLearning|Q-Learning]], SARSA, REINFORCE, DQN, policy gradient): replaces analytical expectations $\sum_{s'}P(s'\mid s,a)f(s')$ with sample averages over actual transitions the agent observed. The agent "subverts the need to know the transition function" ([[d2l-reinforcement-learning]]).

## Why model-free is the default for large RL

In high-dimensional or pixel-input domains (Atari, robotics) it is impossible to enumerate $\mathcal{S}$ or write down $P$, but it is easy to **interact with the environment** and collect samples. Model-free methods scale directly with the data the agent collects. The sample-efficiency cost is real — Q-Learning needs ~250 episodes on FrozenLake where Value Iteration needs ~10 — but the trade is unavoidable when $P$ is inaccessible.

## Connections

- [[QLearning]] / [[TemporalDifferenceLearning]] — the canonical model-free family.
- [[ValueIteration]] — the model-based counterpart.
- [[OffPolicyLearning]] — orthogonal axis (on-policy vs off-policy).
- [[ExplorationExploitation]] — model-free methods can't plan ahead, so exploration is critical.
- [[reinforcementlearning]] / [[MarkovDecisionProcess]] — surrounding formalism.
- [[d2l-reinforcement-learning]] — canonical textbook treatment.
