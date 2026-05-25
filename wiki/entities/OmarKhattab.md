---
title: "Omar Khattab"
type: entity
tags: [researcher, dspy]
sources: [2312.13382-dspy-assertions, 2407.10930-better-together, 2507.19457-gepa, 2406.11695-mipro]
last_updated: 2026-05-22
---

# Omar Khattab

Creator of **[[DSPy]]** — the framework for programming (not prompting) compound AI systems. Co-affiliated with [[Databricks]], [[MITAcademic|MIT]], [[BespokeLabsAI]], and originally [[stanforduniversity|Stanford]] / [[UCBerkeley]] depending on the project. Senior author on the [[2507.19457-gepa|GEPA]] paper.

Research arc: from neural information retrieval (ColBERT, ColBERTv2) through compound-AI-system optimization ([[MIPROv2]], [[2407.10930-better-together|BetterTogether]], DSPy 2.x optimizers) to the reflective-prompt-evolution thesis ([[2507.19457-gepa|GEPA]]).

## Tracked contributions

- **[[2312.13382-dspy-assertions]]** (arXiv 2023/2024, senior author w/ Singhvi, Shetty, Tan, Potts, Sen, Zaharia) — **[[LMAssertions|LM Assertions]]**: first-class `Assert` / `Suggest` constructs for expressing computational constraints in [[DSPy]] pipelines, plus three assertion-driven optimizations ([[AssertionDrivenBacktracking|backtracking]], [[AssertionDrivenExampleBootstrapping|example bootstrapping]], [[CounterexampleBootstrapping|counterexample bootstrapping]]). The runtime *self-refinement* primitive that predates the optimization-side work in [[MIPROv2]] / [[2407.10930-better-together|BetterTogether]] / [[2507.19457-gepa|GEPA]]. Released as `dspy.Assert` / `dspy.Suggest`.
- **[[2406.11695-mipro]]** (EMNLP 2024, senior author w/ Opsahl-Ong, Ryan, Purtell, Broman, Potts, Zaharia) — **[[MIPROv2|MIPRO]]**: the canonical joint-instruction-and-demonstrations optimizer for multi-stage [[LMProgram|LM programs]]; first published formalization of the prompt-optimization problem for LM programs (Algorithm 1). Released as `dspy.MIPROv2`.
- **[[2407.10930-better-together]]** (arXiv 2024, w/ Soylu & Potts) — **BetterTogether**: first published bi-axial (prompts + weights) optimizer for [[CompoundAISystem|compound AI systems]]; introduces the $\Phi_{\langle\Theta,\Pi\rangle}$ formalism subsequently adopted by GEPA. Released as `dspy.BetterTogether`.
- **[[2507.19457-gepa]]** (ICLR 2026 Oral) — senior co-author; GEPA is the latest in the DSPy-adjacent optimizer line.
- **[[DSPy]]** — the framework.
- **[[MIPROv2]]** — prior-generation joint instruction + demonstrations optimizer.
- **ColBERTv2** — referenced in the [[MIPROv2]] worked receipt as the retrieval backend; frozen retriever in the [[2407.10930-better-together|BetterTogether]] HotPotQA program.
