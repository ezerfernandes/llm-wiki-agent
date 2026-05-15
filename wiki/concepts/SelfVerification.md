---
title: "Self-Verification"
type: concept
tags: [reasoning, agents, verification, evaluation]
sources: [2402.01817-llm-modulo]
last_updated: 2026-05-10
---

# Self-Verification

The hypothesis — popular in the iterative-prompting / self-refine literature — that an LLM can **check its own outputs** and improve them via critique-then-revise loops ([[Reflexion]], Self-Refine, [[react]]).

The hypothesis often appeals to a classical-computer-science intuition: **verification is easier than generation** (e.g., NP vs P; checking a SAT certificate is poly-time even when finding one isn't).

## Why [[2402.01817-llm-modulo]] argues this fails for LLMs
- The classical generation-vs-verification argument is about *computational complexity*, not about *approximate-retrieval models*. There is no a priori reason an LLM's critique should be even approximately correct.
- Empirical evidence (Stechly, Valmeekam, Kambhampati 2023, 2024): on graph coloring (NP-complete) and on [[PlanBench]] domains, LLM self-critique **does not improve** baselines — and often makes them *worse*, because the LLM merrily rejects fortuitously correct outputs and converges on bad ones.
- The **24-puzzle reasoning result** in [[TreeOfThoughts]] is reframed: its arithmetic verifier is **external** (a 5-line checker), not an LLM doing self-verification.
- Corollary: self-improvement loops that depend on self-critique (Huang et al. 2023b; some readings of Wang et al. 2022 Self-Instruct) **are unsound** without external verifiers / curated seeds.

## What works instead
The [[LLMModuloFramework]] response: replace LLM self-critique with a **bank of external sound critics** (model-based — VAL, simulators, unit tests). Soundness is then inherited from those critics; the LLM keeps its productive roles (candidate generation, reformatting, soft critique) without being asked to verify itself.

## Connections
- [[LLMModuloFramework]] — proposed remedy
- [[PlanBench]] — empirical evidence
- [[TreeOfThoughts]], [[Reflexion]], [[ChainOfThought]] — self-critique families critiqued
- [[SyntheticData]] — "self-improvement via self-generated data" relies on this assumption
- [[2402.01817-llm-modulo]] — source
