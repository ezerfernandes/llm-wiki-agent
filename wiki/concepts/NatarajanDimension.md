---
title: "Natarajan Dimension"
type: concept
tags: [learning-theory, generalization-bounds, multi-class]
sources: [2605.12966-agentic-ai-to-agi]
last_updated: 2026-05-15
---

# Natarajan Dimension

The Natarajan dimension $d_N(\mathcal{H})$ (Natarajan, 1989) generalizes the [[VCDimension|VC dimension]] to multi-class hypothesis classes $\mathcal{H}\subseteq\{h:\mathcal{X}\to\mathcal{Y}\}$ with $|\mathcal{Y}| = K \geq 2$.

## Shattering definition

A set $S = \{x_1,\dots,x_m\}$ is **Natarajan-shattered** by $\mathcal{H}$ if there exist two witness functions $f_0, f_1: S\to\mathcal{Y}$ such that:

- $f_0(x_i) \neq f_1(x_i)$ for all $i$;
- for every binary vector $\mathbf{b}\in\{0,1\}^m$, some $h\in\mathcal{H}$ satisfies $h(x_i) = f_{b_i}(x_i)$.

$d_N(\mathcal{H})$ is the maximum size of a shattered set.

## Role in [[2605.12966-agentic-ai-to-agi]]

The paper invokes Natarajan dimension to bound the *router's* generalization error in [[RoutingBasedAgenticAI]] — routing is a $K$-way classification of inputs to specialist agents. Theorems 2.3–2.5 (after Jin 2023, Daniely et al. 2011) give upper bounds for two practical router families:

| Class | Bound on $d_N$ |
|---|---|
| Depth-$L$ decision trees ($\Pi_{L,d}^{\text{dtree}}$) over $d$-class inputs | $\mathcal{O}(L\cdot 2^L \log(pd))$ |
| Random forests of $T$ depth-$L$ trees ($\Pi_{L,T,d}^{\text{forest}}$) | $\mathcal{O}(L T 2^L \log(pd))$ |
| Feed-forward NN with $p$ params, binary or linear activations | $\mathcal{O}(d\cdot p^2)$ |
| Same NN with ReLU activations | $\mathcal{O}(d\cdot p^2)$ |

Combined with Theorem 2.5 (Daniely et al. 2011) — $\epsilon_{\mathcal{H}}(m,\delta) \leq O(\sqrt{(d_N(\mathcal{H})\ln|\mathcal{Y}| + \ln(1/\delta))/m})$ — the paper derives:

- **Tree-based router error**: $\epsilon_\pi \propto \tilde{\mathcal{O}}(\sqrt{\log K/N_{\text{router}}})$.
- **Neural router error**: $\epsilon_\pi \propto \sqrt{K/N_{\text{router}}}$.

This is the technical foundation behind the paper's tree-vs-neural router dichotomy: trees scale polylogarithmically in agent count, neural routers scale $\sqrt{K}$.

## Connections
- [[2605.12966-agentic-ai-to-agi]]
- [[RoutingBasedAgenticAI]]
- [[AgenticAI]]
