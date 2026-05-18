---
title: "Dive into Deep Learning — Reinforcement Learning"
type: source
tags: [textbook, d2l, reinforcement-learning, mdp, q-learning, value-iteration]
date: 2026-05-16
source_file: raw/d2l-en/chapter_reinforcement-learning/
---

## Summary

[[PratikChaudhari|Chaudhari]] (Penn / Amazon), [[RasoolFakoor|Fakoor]] (Amazon) and [[KavoshAsadi|Asadi]] (Amazon)'s three-section *Reinforcement Learning* chapter — D2L's compact introduction to **sequential decision-making**: formalize the problem as a [[MarkovDecisionProcess|Markov Decision Process]] $(\mathcal{S},\mathcal{A},T,r)$ ([[d2l-reinforcement-learning]] §mdp), solve it via [[ValueIteration|Value Iteration]] when the [[TransitionFunction|transition function]] $P(s'\mid s,a)$ and [[RewardFunction|reward]] $r(s,a)$ are known (§value-iter), and pivot to [[QLearning|Q-Learning]] (§qlearning) when they are not — replacing the explicit $\sum_{s'} P(s'\mid s,a)$ expectation with a sample average over states visited by the robot, a [[TemporalDifferenceLearning|temporal-difference]] update controlled by learning rate $\alpha$, and an [[EpsilonGreedy|$\epsilon$-greedy]] [[ExplorationExploitation|exploration]] policy. The chapter operationalizes both algorithms on OpenAI Gym's `FrozenLake-v1` 4×4 grid with the [[DiscountFactor|discount factor]] $\gamma=0.95$ — Value Iteration converges in ~10 sweeps while Q-Learning needs ~250 episodes because it lacks access to the MDP. The chapter is RL distilled to first principles: [[BellmanEquation|Bellman]] decomposition → [[DynamicProgramming|dynamic programming]] → off-policy [[TemporalDifferenceLearning|TD]] sampling.

## Key Claims

- **An MDP is the tuple $(\mathcal{S},\mathcal{A},T,r)$** where $T(s,a,s')=P(s'\mid s,a)$ is the [[TransitionFunction|transition kernel]] satisfying $\sum_{s'}T(s,a,s')=1$ and $r:\mathcal{S}\times\mathcal{A}\to\mathbb{R}$ is the **user-designed** [[RewardFunction|reward function]] ([[d2l-reinforcement-learning]] §mdp). A trajectory $\tau=(s_0,a_0,r_0,s_1,a_1,r_1,\ldots)$ has discounted **return** $R(\tau)=\sum_{t=0}^\infty\gamma^t r_t$; the [[DiscountFactor|discount factor]] $\gamma<1$ keeps the sum finite for infinite trajectories and encodes the "prefer short paths" preference — small $\gamma$ encourages greed, $\gamma\!\to\!1$ encourages exploration.
- **The Markov property** is "the next state $s_{t+1}$ depends only on the current state $s_t$ and action $a_t$" — *not* on the past trajectory. Apparent non-Markovian dynamics (e.g., a robot whose action is acceleration so $s_{t+1}$ depends on $s_{t-1}$ through velocity) become Markovian by **expanding the state** to $(\text{location},\text{velocity})$. MDPs therefore model "a very large class of real systems."
- **A [[PolicyFunction|stochastic policy]]** $\pi(a\mid s)\equiv P(a\mid s)$ is a conditional distribution over actions given state, $\sum_a\pi(a\mid s)=1$ for all $s$; a **deterministic policy** is the special case where $\pi(\cdot\mid s)$ is a one-hot. The [[ValueFunction|value function]] $V^\pi(s_0)=\mathbb{E}_{a_t\sim\pi(s_t)}[\sum_{t}\gamma^t r(s_t,a_t)]$ is the expected discounted return starting from $s_0$ under $\pi$; the [[ActionValueFunction|action-value function]] $Q^\pi(s_0,a_0)$ fixes the first action.
- **The [[BellmanEquation|Bellman equation]] decomposes the value into one-step reward plus discounted future value**: $V^\pi(s)=\sum_a\pi(a\mid s)[r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^\pi(s')]$. This recursive identity — that "the average return from the current state is the sum of the average return from the next state and the average reward of going to the next state" — is the foundation of all RL algorithms.
- **The [[DynamicProgramming|principle of dynamic programming]]** (Bellman, 1950s) — *"the remainder of an optimal trajectory is also optimal"* — gives the Bellman optimality equation $V^*(s)=\max_a\{r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^*(s')\}$. The optimal deterministic policy is $\pi^*(s)=\arg\max_a\{r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^*(s')\}$.
- **[[ValueIteration|Value Iteration]]** turns the Bellman optimality equation into the fixed-point iteration $V_{k+1}(s)=\max_a\{r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V_k(s')\}$, which **converges to $V^*$ as $k\to\infty$ for arbitrary initialization $V_0$**. The same algorithm in action-value form: $Q_{k+1}(s,a)=r(s,a)+\gamma\max_{a'}\sum_{s'}P(s'\mid s,a)Q_k(s',a')$. **Policy evaluation** is the same iteration with $\pi(a\mid s)$ in place of the $\max$ — it computes $V^\pi$ for any fixed policy $\pi$.
- **Value Iteration requires full knowledge of the MDP** — specifically the transition function $P(s'\mid s,a)$ and reward $r(s,a)$. On FrozenLake-v1 ($4\times 4$, deterministic actions, $\gamma=0.95$), Value Iteration finds the optimal value function and policy in ~10 sweeps.
- **[[QLearning|Q-Learning]]** ([[ChristopherWatkins|Watkins]] & Dayan 1992) is the **[[ModelFreeLearning|model-free]]** alternative: replace the analytic expectation $\sum_{s'}P(s'\mid s,a)\max_{a'}Q(s',a')$ with samples drawn by the robot's actual transitions. The TD-style update is $Q(s_t,a_t)\leftarrow(1-\alpha)Q(s_t,a_t)+\alpha[r_t+\gamma\max_{a'}Q(s_{t+1},a')]$ where $\alpha$ is the learning rate. For terminal states the bootstrap term is masked out.
- **Q-Learning is [[OffPolicyLearning|off-policy]]**: the **exploration policy** $\pi_e$ the robot uses to act is different from the **target policy** $\arg\max_a\hat{Q}(s,a)$ the algorithm is learning. Typical $\pi_e$ is **[[EpsilonGreedy|$\epsilon$-greedy]]**: pick $\arg\max_{a'}\hat{Q}(s,a')$ with probability $1-\epsilon$, else uniform random over $\mathcal{A}$. A **softmax exploration policy** $\pi_e(a\mid s)=\exp(\hat{Q}(s,a)/T)/\sum_{a'}\exp(\hat{Q}(s,a')/T)$ with temperature $T$ is the continuous-valued alternative — large $T$ ≈ large $\epsilon$.
- **The [[ExplorationExploitation|exploration–exploitation]] trade-off** is fundamental: a uniformly random $\pi_e$ guarantees coverage of $\mathcal{S}\times\mathcal{A}$ but is sample-inefficient; a greedy $\pi_e$ exploits but may miss optimal actions. The Q-Learning objective is *one constraint* linking all state-action pairs, so a $\pi_e$ that fails to cover the space yields a bad $\hat{Q}$ at *every* state, not just the unvisited ones.
- **Q-Learning's self-correcting property**: if $\hat{Q}(s,a)$ is overestimated, both $\epsilon$-greedy and softmax will pick action $a$ more often, future poor rewards will reduce $\hat{Q}(s,a)$, and the bias self-corrects. Conversely, genuinely good actions are reinforced. This is why Q-Learning **converges to the optimal policy even from a random $\pi_e$ start** ([[ChristopherWatkins|Watkins]] & Dayan 1992).
- **Sample efficiency gap**: on the same FrozenLake-v1 setup, Q-Learning ($\alpha=0.9$, $\epsilon=0.9$) converges in ~250 episodes while Value Iteration converged in ~10 — *"the Value Iteration algorithm has access to the full MDP whereas Q-learning does not."* This is the **price of model-free learning** and the motivation for deep-RL extensions (DQN — flagged as the next D2L chapter — extends Q-Learning with neural function approximators, responsible for *"the resurgence of reinforcement learning"* per Mnih et al. 2013/2015).

## Key Quotes

> "Markov Decision Processes are still capable of modeling a very large class of real systems. For example, for our new robot, if we chose our state $s_t$ to the tuple $(\text{location},\text{velocity})$ then the system is Markovian." — the standard trick for handling apparently non-Markovian dynamics is to **expand the state**.

> "This decomposition is very powerful: it is the foundation of the principle of dynamic programming upon which all reinforcement learning algorithms are based." — on the Bellman one-step decomposition $V^\pi(s_0)=r(s_0,a_0)+\gamma\,\mathbb{E}[V^\pi(s_1)]$.

> "The remainder of an optimal trajectory is also optimal." — D2L's one-line mnemonic for Bellman's principle of dynamic programming.

> "The key idea behind Q-Learning is to replace the summation over all $s'\in\mathcal{S}$ in the above expression by a summation over the states visited by the robot. This allows us to subvert the need to know the transition function." — the core insight separating Value Iteration from Q-Learning.

> "This ability to not only collect new data but also collect the right kind of data is the central feature of reinforcement learning algorithms, and this is what distinguishes them from supervised learning." — on Q-Learning's self-correcting exploration.

## Connections

- [[PratikChaudhari]] / [[RasoolFakoor]] / [[KavoshAsadi]] — guest co-authors of this D2L chapter (Penn + [[Amazon]]).
- [[AstonZhang]] / [[ZacharyLipton]] / [[MuLi]] / [[AlexanderSmola]] — D2L principal authors.
- [[RichardBellman]] — formulated the principle of [[DynamicProgramming|dynamic programming]] (1950s) underpinning Value Iteration.
- [[ChristopherWatkins]] — first author of *Q-Learning* (Watkins & Dayan 1992), the algorithm operationalized in §qlearning.
- [[d2l-introduction]] — introduces [[reinforcementlearning|RL]] / [[MarkovDecisionProcess|MDP]] / contextual-bandit / [[MultiArmedBandits|MAB]] taxonomy at a high level; this chapter is the algorithmic depth.
- [[d2l-preface]] — chapter is part of D2L's Part 3 (applications).
- [[reinforcementlearning]] — parent paradigm.
- [[MarkovDecisionProcess]] — the $(\mathcal{S},\mathcal{A},T,r)$ formalism introduced here in algorithmic depth.
- [[ValueIteration]] / [[QLearning]] / [[BellmanEquation]] / [[DynamicProgramming]] / [[PolicyFunction]] / [[ValueFunction]] / [[ActionValueFunction]] / [[DiscountFactor]] / [[EpsilonGreedy]] / [[ExplorationExploitation]] / [[OffPolicyLearning]] / [[TemporalDifferenceLearning]] / [[ModelFreeLearning]] — concepts introduced or operationalized in this chapter.
- [[Amazon]] — institutional affiliation of all three guest co-authors.
- [[reinforce|REINFORCE]] / [[grpo|GRPO]] / [[rlvr|RLVR]] — modern LLM-training RL methods that all build on the Bellman / policy / value formalism this chapter establishes.

## Contradictions

- None — this chapter consolidates standard 1950s–1992 RL pedagogy (Bellman + Watkins-Dayan) with no claims that conflict with existing wiki content. Reuses the same [[MarkovDecisionProcess]] formalism that [[d2l-introduction]] sketched.
