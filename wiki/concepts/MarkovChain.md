---
title: "Markov Chain"
type: concept
tags: [probability, stochastic-process, linear-algebra, information-retrieval]
sources: [iir-ch21-link-analysis]
last_updated: 2026-05-23
---

Discrete-time stochastic process on a finite (or countably infinite) state space with the **Markov property**: the probability of the next state depends only on the current state, not on the history. Specified by:

- A finite state set $S = \{s_1, \ldots, s_n\}$.
- A transition matrix $P \in \mathbb{R}^{n \times n}$ with $P_{ij} = \Pr[\text{next state} = s_j \mid \text{current} = s_i]$. Rows sum to 1 — $P$ is *row-stochastic*.

**Stationary distribution** $\pi$ is a row vector satisfying $\pi = \pi P$ — an eigenvector of $P^T$ with eigenvalue 1. Existence + uniqueness require **ergodicity**: irreducible (every state reachable from every other) + aperiodic. Under ergodicity, $\pi_j$ equals the long-run fraction of time the chain spends in state $s_j$.

**Convergence**: for an ergodic chain, $\pi_t = \pi_0 P^t \to \pi$ regardless of starting distribution $\pi_0$. **Power iteration** is the standard numerical method.

**Application to IR — [[PageRank]]**: model a random surfer on the web graph as a Markov chain with transition matrix $P = (1-\alpha) A + \alpha E / N$ where $A$ is row-normalized link adjacency and $E$ is uniform teleportation (adding teleportation forces ergodicity even when the link graph has dangling nodes or disconnected components). PageRank is then the stationary distribution $\pi$.

**Disambiguation note**: this wiki also has a [[MarkovModel]] page covering the broader family of Markov-based models (Markov chains, hidden Markov models, MRFs); this concept page covers specifically the discrete-time finite-state chain construction used in [[iir-ch21-link-analysis]].
