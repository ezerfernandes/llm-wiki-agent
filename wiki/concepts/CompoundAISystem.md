---
title: "Compound AI System"
type: concept
tags: [llm-systems, formalism, agents, multi-module]
sources: [2407.10930-better-together, 2507.19457-gepa, 2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# Compound AI System

A **modular system composed of one or more language-model invocations**, potentially interleaved with external tool calls, orchestrated through arbitrary control flow. The class subsumes agents, multi-agent systems, and general-purpose scaffolding like [[react|ReAct]] and Archon.

## Formalism ([[2407.10930-better-together|Soylu, Potts & Khattab 2024]] — adopted by [[2507.19457-gepa|GEPA]]; cf. Khattab et al. 2024 / Opsahl-Ong et al. 2024 / Tan et al. 2025)

A compound AI system $\Phi$ is the tuple

$$\Phi = (M, C, \mathcal{X}, \mathcal{Y})$$

where:

- $M = \langle M_1, \ldots, M_{|M|} \rangle$ — language modules. Each $M_i = (\pi_i, \theta_i, \mathcal{X}_i, \mathcal{Y}_i)$ is an LLM subcomponent with:
  - $\pi_i$ — its (system) prompt, including instructions and optional few-shot demonstrations.
  - $\theta_i$ — the underlying LLM weights.
  - $\mathcal{X}_i, \mathcal{Y}_i$ — input/output schemas.
- $C$ — the **control-flow logic** specifying module invocation order, conditional branches, loop conditions, tool API calls.
- $\mathcal{X}, \mathcal{Y}$ — global input/output schemas.

The **learnable parameters** factor into $\Pi_\Phi = \langle \pi_1, \ldots, \pi_{|M|} \rangle$ (the prompts) and $\Theta_\Phi = \langle \theta_1, \ldots, \theta_{|M|} \rangle$ (the weights). Optimizers can target either.

## The optimization problem

Given task distribution $\mathcal{T}$ over $(x, m)$ pairs (instance $x$ + evaluator metadata $m$), and metric $\mu : \mathcal{Y} \times \mathcal{M} \to [0,1]$:

$$\langle \Pi^*, \Theta^* \rangle_\Phi = \arg\max_{\langle \Pi, \Theta \rangle_\Phi} \mathbb{E}_{(x,m) \sim \mathcal{T}}[\mu(\Phi(x; \langle \Pi, \Theta \rangle_\Phi), m)]$$

With a rollout budget $B$, sample-efficient compound-AI-system optimization seeks the best $\langle \Pi^*, \Theta^* \rangle$ subject to `#rollouts ≤ B`.

## Why the framing matters

The compound-AI-system framing **subsumes** the agent / multi-agent / scaffolded-LLM distinctions:

- A single-prompt RAG system: $|M|=1$, $C$ wires retrieval+generation.
- A [[react|ReAct]] agent: $|M|=1$ with control flow $C$ that interleaves reasoning steps and tool calls.
- A multi-hop QA system: $|M|=2$ (query generator + answer synthesizer), $C$ wires two retrieval calls between them.
- A multi-agent debate: $|M|=k$ agents, $C$ orchestrates turn-taking and termination.

All four are instances of $\Phi = (M, C, \mathcal{X}, \mathcal{Y})$ — the optimizer is agnostic to which framing the user prefers.

## What GEPA optimizes

[[GEPA]] / [[2507.19457-gepa]] **only updates $\Pi_\Phi$** — the prompts — and **leaves $\Theta_\Phi$ frozen**. This is the key contrast vs [[grpo|GRPO]] and weight-space RL approaches: GEPA's gains are achievable with **no parameter changes to the base model**, only changes to the system prompts of each module $M_i$.

## Empirical independence result ([[2604.14585-prompt-optimization-coin-flip|Zhang et al. 2026]])

The formalism is silent on **whether the modules $M_i$ actually interact** — the question is empirical. [[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] supplied the wiki's first controlled measurement on two-agent feed-forward pipelines:

- The $A \times B$ interaction term in an [[ANOVAVarianceDecomposition|ANOVA decomposition]] is **non-significant in all six tested model×task conditions** ($p > 0.52$, $F < 1.0$, 0.18–2.15% of total variance).
- The joint optimum (best cell of a $10 \times 10$ prompt grid) and the independent optimum (best row × best column) are **adjacent or identical**, with a gap of 0.0–3.3 pts.
- Budget-equalized simulations confirm independent search matches joint search at all budget levels.

**Practical implication**: for two-agent feed-forward pipelines on mid-tier models, [[JointOptimization|joint optimization]] over $\Pi_\Phi$ is unnecessary — [[IndependentOptimization|independent per-module]] search suffices. The paper predicts (untested) regimes where coupling may re-emerge: shared mutable state, schema dependence, feedback loops, 3+ agent pipelines, and structured-data inter-module communication.

## Connections
- [[2507.19457-gepa]] — formalism introduced for GEPA's framing.
- [[GEPA]] — optimizer that operates on compound AI systems.
- [[MIPROv2]] — alternative prompt optimizer over the same formalism.
- [[DSPy]] — the framework that operationalizes compound AI systems as Python programs (`dspy.Module`, `dspy.Signature`).
- [[AgenticAI]] — agentic AI is a compound AI system with autonomy properties; see [[2605.12966-agentic-ai-to-agi]] for the DAG topology framing.
- [[react|ReAct]] — canonical single-module agent instance.
- [[grpo|GRPO]] — weight-space optimizer over the same formalism (updates $\Theta_\Phi$ instead of $\Pi_\Phi$).
- [[2407.10930-better-together]] — earlier formalism paper; introduces $\Phi_{\langle\Theta,\Pi\rangle}$ and the [[BetterTogether]] algorithm.
- [[BetterTogether]] — bi-axial $\Pi + \Theta$ meta-optimizer over the same formalism.
- [[2604.14585-prompt-optimization-coin-flip]] — empirical audit of the joint-optimization premise; introduces the [[ANOVAVarianceDecomposition|ANOVA]] coupling test as a falsifiable evaluation protocol for the formalism.
- [[AgentCoupling]] / [[JointOptimization]] / [[IndependentOptimization]] / [[CompoundAIDiagnostic]] — concepts mined out by Zhang et al.'s audit.
