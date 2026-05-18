---
title: "Routing-Based Agentic AI"
type: concept
tags: [agentic-ai, routing, multi-task, generalization]
sources: [2605.12966-agentic-ai-to-agi]
last_updated: 2026-05-15
---

# Routing-Based Agentic AI

The simplest non-trivial regime of [[AgenticAI]]: a single router $\pi: \mathcal{X} \to \{1,\dots,K\}$ assigns each input to one of $K$ specialist agents $A_k$. Each agent learns a sub-task labeling function $f_k: \mathcal{M}_k \to \mathbb{R}$ on its low-dimensional manifold. The routed hypothesis is

$$f_{\text{R-Agentic}}(x) = \sum_{k=1}^K \mathbb{I}[\pi(x) = k] \cdot f_k(\phi_k(x))$$

where $\phi_k: \mathcal{M}_k \to \mathbb{R}^{d_k}$ is a local coordinate chart. Section 3.2 of [[2605.12966-agentic-ai-to-agi]] proves this regime alone achieves an *exponential* sample-efficiency gain over the monolithic learner, and §5 reinterprets [[MixtureOfExperts]] as exactly this regime with a single-layer differentiable router.

## Headline bound

Assuming $N/K$ samples per agent and dominance by the most complex sub-task:

$$\mathcal{E}_{\text{R-Agentic}}(N) \approx \mathcal{O}\!\left(K \cdot N^{-1/d_{\max}}\right) + \mathcal{E}_{\text{routing}}$$

where $d_{\max} = \max_k d_k$. The ratio versus the monolith is

$$\frac{\mathcal{E}_{\text{R-Agentic}}(N)}{\mathcal{E}_{\text{mono}}(N)} \approx K \cdot N^{1/D - 1/d_{\max}} \to 0 \quad (N\to\infty)$$

since the exponent $1/D - 1/d_{\max}$ is strictly negative when $d_{\max} \ll D$. The data-requirement ratio is $N_{\text{R-Agentic}}/N_{\text{mono}} \propto K^{d_{\max}} \epsilon^{D - d_{\max}}$ — for small target error $\epsilon$ and large dimensionality gap, the routing system needs *exponentially fewer* samples.

## Routing Regret

The omitted error term $\mathcal{E}_{\text{routing}}$ decomposes into two factors:

$$\mathcal{E}_{\text{routing}} = \mathbb{E}_{x\sim\mathcal{D}_{\text{real}}}\!\left[\underbrace{\mathbb{I}[\pi(x)\neq k^*(x)]}_{\text{Routing Error Rate } \epsilon_\pi} \cdot \underbrace{L(A_{\pi(x)}(x)) - L(A_{k^*(x)}(x))}_{\text{Mismatch Penalty }\Delta(x)}\right].$$

Using Theorems 2.3–2.5 (Natarajan-dimension upper bounds), the Routing Error Rate scales as:

- **Tree-based router** ($\Pi_{L,d}^{\text{dtree}}$): $\epsilon_\pi \propto \tilde{\mathcal{O}}\!\left(\sqrt{\log K / N_{\text{router}}}\right)$ — polylog cost in $K$.
- **Neural router** ($\Pi_{p,S}^{\text{ReLU}}$): $\epsilon_\pi \propto \sqrt{K/N_{\text{router}}}$ — linear cost in $K$.

The Mismatch Penalty $\Delta_{\max}(K) \approx L_{\max}\cdot(1-1/\sqrt{K})$ saturates at $L_{\max}$ as $K\to\infty$ (Lemma 3.5).

## Optimal granularity $K^*$ (joint bound)

Combining specialization gain (decreasing in $K$) and routing cost (increasing in $K$):

$$\mathcal{E}_{\text{R-Agentic}}(K,N) \leq \frac{KC_{\exp}}{N^{1/d_{\max}}} + \Delta_{\max}(K)\cdot\epsilon_\pi(K).$$

Yields a U-shaped error profile with an optimal $K^*$ solving $\partial\mathcal{E}_{\text{total}}/\partial K = 0$.

**Designer dichotomy.**
- *Tree-based routing* — modularity cost grows polylogarithmically, so specialization gain dominates for sufficiently large $N$. Favored in data-scarce regimes.
- *Neural routing* — cost $\sqrt{K}$ restricts $K^*$ unless $N_{\text{router}}\propto K$. Favored in data-rich regimes where the polynomial penalty is suppressed and routers can capture complex, non-axis-aligned task boundaries.

Remark B.6 notes that Agentic AI relaxes the static-dataset assumption: agents interact with the environment continuously, so $N_{\text{router}}$ is effectively unbounded, which may flip the tree-vs-neural preference.

## Connections
- [[2605.12966-agentic-ai-to-agi]]
- [[AgenticAI]]
- [[MixtureOfExperts]]
- [[StructuredRealWorldDistribution]]
- [[NatarajanDimension]]
- [[CurseOfDimensionality]]
