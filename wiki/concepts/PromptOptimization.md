---
title: "Prompt Optimization"
type: concept
tags: [prompt-optimization, llm, search, optimization]
sources: [2406.11695-mipro, 2507.19457-gepa, 2407.10930-better-together, 2025-bionlp-archehr-qa-neural, 2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# Prompt Optimization

The task of automatically searching over **prompt strings** (instructions, demonstrations, formatting) to maximize a downstream task metric — without modifying LM weights. The wiki's three canonical anchors:

| Era | Paper | Algorithm | Key idea |
|---|---|---|---|
| 2023 | [[OPRO]] | LM-as-optimizer with history of (prompt, score) pairs | History-based credit assignment. |
| 2024 | [[2406.11695-mipro|MIPRO]] | [[BayesianOptimization|Bayesian]] joint search over instructions × demos | Surrogate-based credit assignment over a fixed proposal set. |
| 2026 | [[2507.19457-gepa|GEPA]] | Reflective prompt mutation + Pareto-based selection | Generates *new* proposals from evaluation traces. |

## Position in the broader optimization landscape

Prompt optimization is the **prompt-space** counterpart to **weight-space** optimization (SFT / [[grpo|GRPO]] / RL). [[2407.10930-better-together|BetterTogether]] is the canonical bi-axial optimizer that composes both — $\Pi \to \Theta \to \Pi$. The [[CompoundAISystem]] formalism in [[2507.19457-gepa|GEPA]] formalizes the joint object as $\Phi = (M, C, \mathcal{X}, \mathcal{Y})$ with learnable parameters $\langle\Pi, \Theta\rangle$.

## Applications in the wiki

- **[[2025-bionlp-archehr-qa-neural|ArchEHR-QA 2025 (Neural)]]** — [[MIPROv2]] applied to a two-stage [[EvidenceGroundedQA|clinical-QA]] pipeline; **first peer-reviewed shared-task placement to deploy MIPROv2 in clinical NLP**. 2nd place, overall 51.5; beats few-shot baseline by 10 points, zero-shot by 20.

## Empirical audit: when does prompt optimization actually help?

[[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] supply the wiki's first controlled audit:

- **49% of 72 optimization runs on [[ClaudeHaiku45|Claude Haiku 4.5]] score *below* zero-shot** — statistically indistinguishable from a coin flip (binomial $p = 0.91$). On [[AmazonNovaLite|Amazon Nova Lite]], 14 of 24 method×task means fall below zero-shot.
- Optimization helps on **only 1 of 4 tasks**: [[HelpSteer2]], the task with **[[CanButDoesntPattern|exploitable output structure]]** (JSON rubric the model can produce but does not default to). The other three free-form tasks ([[FeedbackBench]], [[WildBench]], [[XSum]]) all show negative average gains across the 6 tested methods.
- Two compounding failure mechanisms: noisy 20-question evaluation + iterative methods overfitting (train-test gaps up to +5.6 pts; [[APE]], being non-iterative, shows none).
- [[ModelSpecificityShelfLife|Model specificity dominates]]: which task is optimizable, which agent matters, and which method works all reverse with the executor model.

**Practitioner diagnostic** ([[CompoundAIDiagnostic|two-stage framework]]):

1. **[[ANOVAVarianceDecomposition|ANOVA coupling test]]** (~$80, 1 day) — *do agents interact?* If $F < 1$, optimize independently. Independence holds in all 6 tested two-agent feed-forward conditions.
2. **[[HeadroomTest|Headroom test]]** (~$5, 10 min) — *is the landscape worth optimizing?* Generate 10–20 candidate prompts; if best gain $< 2$ pts over zero-shot, use zero-shot.

The wiki's prior prompt-optimization successes ([[2406.11695-mipro|MIPRO]] wins on [[HotPotQAConditional]]; [[2507.19457-gepa|GEPA]]'s reflective mutation gains; [[2025-bionlp-archehr-qa-neural|Neural at ArchEHR-QA 2025]]'s 20-point jump over zero-shot) all align with the [[CanButDoesntPattern]] hypothesis — they are tasks with conditional-rule / citation-format / composite-reward output structure the model does not zero-shot default to. Zhang et al.'s coin-flip aggregate is consistent with the prior wiki gains being conditional on this structural property rather than universal.

## Connections

- [[OPRO]] / [[MIPROv2|MIPRO]] / [[ModuleLevelOPRO]] / [[GEPA]] / [[APE]] / [[EvoPrompt]] / [[PromptBreeder]] / [[ProTeGi]] / [[PROSEOptimizer]] — the optimizer family.
- [[TextGrad]] / [[GPTSwarm]] / [[Helix]] — joint-optimization tools whose premise [[2604.14585-prompt-optimization-coin-flip|Zhang et al. 2026]] audits.
- [[2025-bionlp-archehr-qa-neural]] — clinical-QA application of MIPROv2.
- [[2604.14585-prompt-optimization-coin-flip]] — the empirical audit; introduces the [[CompoundAIDiagnostic|two-stage diagnostic framework]].
- [[CoinFlipOptimization]] / [[CanButDoesntPattern]] / [[HeadroomTest]] / [[ANOVAVarianceDecomposition]] / [[ModelSpecificityShelfLife]] — the audit's concept tree.
- [[LMProgram]] / [[CompoundAISystem]] — the target object being optimized.
- [[DSPy]] — the framework these optimizers ship in.
- [[CreditAssignment]] — the structural sub-problem.
- [[BayesianOptimization]] / [[TreeStructuredParzenEstimator]] — the search-engine subroutines.
