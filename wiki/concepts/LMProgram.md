---
title: "LM Program"
type: concept
tags: [compound-systems, dspy, pipeline, multi-stage, formalism]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# LM Program

**Language Model Program** — a multi-stage pipeline of modular LM calls. The [[2406.11695-mipro|MIPRO paper (Opsahl-Ong et al. 2024)]] adopts this term from Khattab et al. 2024 ([[DSPy]]) and uses it as its formal target: a program $\Phi$ consisting of $m$ modules, each parameterized by a prompt template $p_i$ that contains a set of variables (open slots) $\mathbf{v}$. The variables include instructions and few-shot demonstrations for that module.

## Formal definition (from the MIPRO paper)

Let $\mathbf{V}$ be the set of **all** variables across all prompt templates in $\Phi$, and let $\mathbf{V} \mapsto S$ be a total assignment of variables to strings. The notation $\Phi_{\mathbf{V}\mapsto S}$ specifies the LM program $\Phi$ run under such an assignment. The optimization problem becomes

$$\Phi^* = \arg\max_{\mathbf{V}\mapsto S}\frac{1}{|\mathcal{D}|}\sum_{(x,x')\in\mathcal{D}}\mu(\Phi_{\mathbf{V}\mapsto S}(x), x')$$

over a trainset $\mathcal{D}$ with optional metadata $x'$ (e.g. final labels) and a task-level metric $\mu$.

## Five constraints that make this hard

The paper enumerates five constraints that distinguish [[PromptOptimization|prompt optimization]] of LM programs from earlier prompt-engineering tasks:

1. **String space is infinite** — any string $s\in S$ can take any value.
2. **Metric supervises only the entire task** — every variable in $\mathbf{V}$ is **latent**, so we can't directly score per-module outputs. This is the **[[CreditAssignment|credit-assignment challenge]]**.
3. **No log-probs or gradients** — rules out RL- and prompt-tuning-style algorithms ([[PrefixTuning|prefix-tuning]], [[AutoPrompt]], etc.).
4. **Small data budgets** — system designers usually have small datasets $\mathcal{D}$.
5. **Small LM-call budgets** for evaluating $\Phi$.

## Position in the wiki

`LM program` is the **MIPRO paper's term** for what the [[2507.19457-gepa|GEPA paper (2026)]] later generalizes to **[[CompoundAISystem|compound AI system]]**: $\Phi = (M, C, \mathcal{X}, \mathcal{Y})$ with learnable parameters $\langle\Pi,\Theta\rangle$. The two terms refer to the same structural target — a graph of LM calls with shared variables — but `LM program` is the **earlier, narrower** framing (multi-stage prompt-only) while `compound AI system` adds explicit support for weight parameters $\Theta$ alongside prompt parameters $\Pi$.

## Connections

- [[2406.11695-mipro]] — the canonical source for the LM-program formalism in the wiki.
- [[CompoundAISystem]] — the 2026 [[2507.19457-gepa|GEPA]] generalization (adds weight parameters).
- [[DSPy]] — Khattab et al. 2024's framework that operationalizes LM programs as code.
- [[MIPROv2|MIPRO]] — the optimizer designed for LM programs.
- [[2407.10930-better-together|BetterTogether]] — the immediate successor work; same target.
- [[CreditAssignment]] — the latent-variable problem this formalism makes explicit.
- [[PromptOptimization]] — the optimization task LM programs are the domain of.
