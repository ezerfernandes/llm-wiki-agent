---
title: "Off-Policy Learning"
type: concept
tags: [reinforcement-learning, algorithm-family]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Off-Policy Learning

An RL algorithm is **off-policy** when the **behavior policy** $\pi_e$ used to *collect data* is different from the **target policy** $\pi^*$ being *learned* ([[d2l-reinforcement-learning]] §qlearning). The canonical example is [[QLearning|Q-Learning]], where:

- The behavior policy is typically [[EpsilonGreedy|$\epsilon$-greedy]] on the current $\hat{Q}$ — it explores.
- The target policy is the greedy deterministic policy $\arg\max_a\hat{Q}(s,a)$ — what we ultimately want.

The TD update target $r_t+\gamma\max_{a'}Q(s_{t+1},a')$ uses the $\max$ regardless of the action $\pi_e$ actually took, which is what makes the decoupling possible.

## Contrast with on-policy

**On-policy** algorithms (SARSA, REINFORCE, classical policy gradient) use the same policy for both data collection and improvement. They are simpler to analyze but cannot reuse data collected under an older policy — if the policy changes, old data is "wrong."

## Why off-policy matters

- **Data reuse**: off-policy methods can replay old trajectories (DQN uses a replay buffer for exactly this reason).
- **Exploration decoupling**: the agent can explore aggressively (high $\epsilon$) without compromising the quality of the target policy.
- **Learn from demonstrations**: off-policy methods can learn from data collected by humans, scripted policies, or older versions of the agent.

## Connections

- [[QLearning]] — the canonical off-policy algorithm.
- [[TemporalDifferenceLearning]] — off-policy TD is the Q-Learning family.
- [[ExplorationExploitation]] / [[EpsilonGreedy]] — the behavior-policy mechanism.
- [[PolicyFunction]] / [[reinforcementlearning]] / [[MarkovDecisionProcess]] — surrounding formalism.
- [[d2l-reinforcement-learning]] — canonical textbook treatment.
