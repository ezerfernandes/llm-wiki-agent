---
title: "Epsilon-Greedy"
type: concept
tags: [reinforcement-learning, exploration, policy]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# $\epsilon$-Greedy

The most widely-used **exploration policy** in [[reinforcementlearning|reinforcement learning]] ([[d2l-reinforcement-learning]] §qlearning). Given the current estimate $\hat{Q}(s,a)$, with probability $1-\epsilon$ pick the greedy action, else sample uniformly over $\mathcal{A}$:

$$\pi_e(a\mid s)=\begin{cases}\arg\max_{a'}\hat{Q}(s,a') & \text{w.p. } 1-\epsilon \\ \text{uniform}(\mathcal{A}) & \text{w.p. } \epsilon.\end{cases}$$

$\epsilon$ is the **exploration parameter** — large $\epsilon$ ≈ uniform random (pure [[ExplorationExploitation|exploration]]); $\epsilon=0$ is pure exploitation of the current $\hat{Q}$. Typical schedules anneal $\epsilon$ from ~1.0 toward 0 over training.

## Softmax variant

$$\pi_e(a\mid s)=\frac{\exp(\hat{Q}(s,a)/T)}{\sum_{a'}\exp(\hat{Q}(s,a')/T)}$$

where temperature $T$ plays a role similar to $\epsilon$ — large $T$ flattens the distribution toward uniform.

## Usage

The default exploration policy in [[QLearning|Q-Learning]] and DQN. The structural distinction between **behavior policy** $\pi_e$ (used to act, here $\epsilon$-greedy) and **target policy** $\arg\max_a\hat{Q}(s,a)$ (being learned) is what makes Q-Learning [[OffPolicyLearning|off-policy]].

## Connections

- [[ExplorationExploitation]] — the trade-off $\epsilon$ parameterizes.
- [[QLearning]] / [[OffPolicyLearning]] — the canonical setting.
- [[PolicyFunction]] / [[ActionValueFunction]] / [[reinforcementlearning]] — surrounding formalism.
- [[MultiArmedBandits]] — $\epsilon$-greedy is also a foundational MAB algorithm in the simpler stateless setting.
- [[d2l-reinforcement-learning]] — canonical textbook treatment.
