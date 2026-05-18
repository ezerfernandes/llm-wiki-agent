---
title: "Reinforcement Learning"
type: concept
tags: [ml-method, paradigm]
sources: [2512.04388-conductor, 2601.21343-self-improving-pretraining, 2605.02396-heavyskill, 2605.02572-long-horizon-llm-training, d2l-introduction, d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Reinforcement Learning

Training paradigm where a policy is optimized against a scalar reward signal.

## Textbook framing ([[d2l-introduction]])

RL formalizes **agent ↔ environment interaction** over time steps: at each step the agent receives an *observation*, chooses an *action* (transmitted to the environment via an actuator), and after the loop closes receives a *reward*. The agent's behavior is a **policy** $\pi$ mapping observations to actions; the goal is good policies.

The chapter emphasizes three challenges absent from [[SupervisedLearning|supervised learning]]:

- **Credit assignment.** Reward arrives at game-end (chess: $\pm 1$ at terminal); which earlier actions deserve credit?
- **Partial observability.** Current observation may not capture the full state (cleaning robot trapped in identical closets).
- **Explore/exploit tradeoff.** Exploit known-good policy or sample untried ones at the cost of short-term reward.

## Hierarchy of special cases

| Setting | Defining feature |
|---|---|
| General RL | Partial observability + state ⇒ Action ⇒ next-state |
| **[[MarkovDecisionProcess\|Markov decision process]]** | Fully observed |
| **Contextual bandit** | State independent of past actions |
| **[[MultiArmedBandits\|Multi-armed bandit]]** | No state at all |

## Landmark deep-RL results ([[d2l-introduction]] cites)

- **DQN** beats humans at Atari games from raw pixel input (Mnih et al. 2015).
- **AlphaGo** dethrones the world Go champion using DL + Monte Carlo tree search (Silver et al. 2016).
- **TD-Gammon** (backgammon), **DeepBlue** (chess, Kasparov 1997, search + special-purpose HW), **Libratus** (Poker, partial observability) — earlier-and-later game-AI milestones.

## In the 2026 LLM corpus

RL is the unifying theme for LLM training advances: end-to-end coordination ([[2512.04388-conductor]]), pretraining-stage optimization ([[2601.21343-self-improving-pretraining]]), heavy-thinking inner skill ([[2605.02396-heavyskill]] via RLVR), and long-horizon agent training ([[2605.02572-long-horizon-llm-training]]).

## Connections
- [[MachineLearning]] — parent paradigm.
- [[MarkovDecisionProcess]], [[MultiArmedBandits]] — special cases.
- [[ValueIteration]] / [[QLearning]] / [[BellmanEquation]] / [[DynamicProgramming]] / [[TemporalDifferenceLearning]] / [[OffPolicyLearning]] / [[ModelFreeLearning]] / [[ExplorationExploitation]] / [[EpsilonGreedy]] / [[PolicyFunction]] / [[ValueFunction]] / [[ActionValueFunction]] / [[DiscountFactor]] / [[TransitionFunction]] / [[RewardFunction]] — algorithmic and formal building blocks ([[d2l-reinforcement-learning]]).
- [[alphazero]], [[alphazero|AlphaGo]] — landmark deep-RL applications.
- [[grpo|GRPO]], [[rlvr|RLVR]], [[reinforce|REINFORCE]], [[llmasjudge|LLM-as-Judge]] — modern LLM-training instances.
- [[d2l-introduction]] — high-level RL taxonomy.
- [[d2l-reinforcement-learning]] — algorithmic depth (MDPs / Value Iteration / Q-Learning).
