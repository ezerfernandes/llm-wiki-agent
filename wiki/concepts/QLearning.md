---
title: "Q-Learning"
type: concept
tags: [reinforcement-learning, model-free, td-learning, off-policy, algorithm]
sources: [d2l-reinforcement-learning]
last_updated: 2026-05-16
---

# Q-Learning

The canonical **[[ModelFreeLearning|model-free]] [[OffPolicyLearning|off-policy]]** RL algorithm ([[ChristopherWatkins|Watkins]] & Dayan 1992), formalized in [[d2l-reinforcement-learning]] §qlearning. Q-Learning learns the optimal [[ActionValueFunction|action-value function]] $Q^*(s,a)$ **without knowing the [[TransitionFunction|transition kernel]] $P(s'\mid s,a)$** — the key insight is to replace the $\sum_{s'}P(s'\mid s,a)$ expectation in [[ValueIteration|Value Iteration]] with samples drawn by the robot's actual interaction with the environment.

## Update rule

$$Q(s_t,a_t)\leftarrow(1-\alpha)Q(s_t,a_t)+\alpha\Big[r_t+\gamma\,(1-\mathbb{1}_{s_{t+1}\text{ terminal}})\max_{a'}Q(s_{t+1},a')\Big]$$

where $\alpha$ is the learning rate, $\gamma$ the [[DiscountFactor|discount factor]], and the terminal-state indicator masks the bootstrap term when the trajectory ends. This is a [[TemporalDifferenceLearning|temporal-difference]] update: $r_t+\gamma\max_{a'}Q(s_{t+1},a')$ is the **TD target**, $Q(s_t,a_t)$ is the current estimate.

The greedy policy $\hat{\pi}(s)=\arg\max_a\hat{Q}(s,a)$ is read off the converged $\hat{Q}$.

## Off-policy structure

Q-Learning is **off-policy** because the **exploration / behavior policy** $\pi_e$ used to act is different from the **target policy** $\arg\max_a\hat{Q}(s,a)$ being learned. Typical $\pi_e$ is **[[EpsilonGreedy|$\epsilon$-greedy]]** — pick the current $\arg\max$ with probability $1-\epsilon$, else uniform over $\mathcal{A}$. A continuous-valued alternative is **softmax exploration** $\pi_e(a\mid s)\propto\exp(\hat{Q}(s,a)/T)$ with temperature $T$.

## Self-correcting property ([[d2l-reinforcement-learning]] §qlearning)

If $\hat{Q}(s,a)$ overestimates, the exploration policy picks $a$ more often; subsequent poor rewards reduce $\hat{Q}(s,a)$, and the bias self-corrects. Conversely, genuinely good actions get reinforced. Watkins & Dayan (1992) proved Q-Learning **converges to the optimal policy even from a random $\pi_e$** under standard step-size conditions.

## FrozenLake-v1 ([[d2l-reinforcement-learning]] §qlearning)

On the same `FrozenLake-v1` task that [[ValueIteration]] solves in ~10 sweeps, Q-Learning ($\alpha=0.9$, $\epsilon=0.9$, $\gamma=0.95$) needs **~250 episodes** — the price of model-free learning.

## Why it matters

> *"Q-learning, using deep neural networks (which we will see in the DQN chapter later), is responsible for the resurgence of reinforcement learning."* — [[d2l-reinforcement-learning]] §qlearning. DQN (Mnih et al. 2013/2015 — cited in [[reinforcementlearning]]) parameterizes $Q(s,a)$ with a CNN and applies the Q-Learning update at scale on Atari.

## Connections

- [[ValueIteration]] — the model-based analog; Q-Learning is Value Iteration with the expectation replaced by a sample.
- [[TemporalDifferenceLearning]] — Q-Learning is a TD method (the prototypical off-policy one).
- [[OffPolicyLearning]] — the structural feature that distinguishes Q-Learning from SARSA / on-policy TD.
- [[EpsilonGreedy]] / [[ExplorationExploitation]] — the behavior-policy mechanism.
- [[ChristopherWatkins]] — first author of the 1992 algorithm.
- [[ActionValueFunction]] / [[BellmanEquation]] / [[MarkovDecisionProcess]] / [[reinforcementlearning]] — surrounding RL concepts.
- [[ModelFreeLearning]] — Q-Learning is the canonical model-free off-policy algorithm.
- [[d2l-reinforcement-learning]] — operationalizes Q-Learning on FrozenLake-v1.
