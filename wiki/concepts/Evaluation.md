---
title: "Evaluation"
type: concept
tags: [evaluation, ai-engineering, methodology]
sources: [ai-engineering-ch01-intro, ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Evaluation

**The discipline of measuring AI-system quality, behavior, and risks.** Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] and the book's preface, evaluation is *"one of the hardest, if not the hardest, challenges of AI engineering"* — [[ChipHuyen|Huyen]] dedicates **Chapters 3 and 4** of the book to it (more than any other topic). This page collects the Ch 1 framing; Chs 3–4 source pages will expand it.

## Why evaluation is harder for foundation models

From Ch 1:

> *"AI engineering works with models that can produce open-ended outputs. Open-ended outputs give models the flexibility to be used for more tasks, but they are also harder to evaluate. This makes evaluation a much bigger problem in AI engineering."*

Two specific challenges:

1. **No enumerable ground truth.** In classical close-ended ML (fraud detection, spam classification), there's a clear expected output. For an open-ended chatbot, *"there are so many possible responses to each prompt that it is impossible to curate an exhaustive list of ground truths."*

2. **Adaptation amplifies evaluation difficulty.** A model that performs poorly with one [[PromptEngineering|prompt engineering]] technique may perform well with another (see the [[gemini|Gemini]] MMLU CoT@32 vs 5-shot anecdote). The evaluator must take the **entire adaptation stack** into account, not just the base model.

## What evaluation is needed for

Per Ch 1, evaluation is needed throughout the [[ModelAdaptation|adaptation]] lifecycle:

- **Selecting models** — choose between competing FMs.
- **Benchmarking progress** — track improvement during development.
- **Deployment readiness** — decide whether a model meets the [[UsefulnessThreshold|usefulness threshold]].
- **Production monitoring** — detect drift, regressions, and new opportunities.

## Stack-comparison verdict

| Category | Traditional ML | Foundation models |
|---|---|---|
| Evaluation | Important | **More important** |

Evaluation lives at the **application-development layer** of the [[AIEngineeringStack|AI engineering stack]] (Ch 5 onward applies it), but is also shared with model development.

## Chapters 3-4 preview

- **Ch 3 — Evaluation Methodology**: language modeling metrics, exact evaluation, AI-as-judge, comparative evaluation.
- **Ch 4 — Evaluate AI Systems**: evaluation criteria, model selection, designing an evaluation pipeline.

## Connections

- [[AIEngineering]] / [[AIEngineeringStack]] — discipline-level home.
- [[UsefulnessThreshold]] — the per-product evaluation target.
- [[PromptEngineering]] — prompt format profoundly affects evaluation.
- [[Hallucination]] — a primary failure mode evaluation must detect.
- [[GenerativeAI]] — open-endedness is the structural reason evaluation is hard.
- [[LLMAsAJudge]] / [[SemanticF1]] / [[BERTScore]] / [[Perplexity]] / [[mmlu]] — concrete evaluators referenced throughout the wiki.
- [[ai-engineering-ch01-intro]] — primary source.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 applies the methodology to AI systems. Three pillars:

1. **[[EvaluationDrivenDevelopment|Evaluation-driven development]]** — define criteria before building. *"I believe that evaluation is the biggest bottleneck to AI adoption. Being able to build reliable evaluation pipelines will unlock many new applications."*
2. **Four-bucket criteria taxonomy** — [[DomainSpecificCapability]] / [[GenerationCapability]] (factual consistency + safety) / [[InstructionFollowingCapability]] / [[CostAndLatency]].
3. **[[EvaluationPipeline|Evaluation pipeline]] design** — six steps: per-component / per-turn / per-task; unambiguous [[EvaluationGuideline|guideline]]; [[ScoringRubric|scoring rubrics]] with examples; [[BusinessMetric|business-metric]] mapping; method selection (mix-and-match cheap + expensive); [[DataSlicing|sliced]] evaluation sets sized by [[BootstrapEvaluation|bootstrap]].

The chapter is the wiki's first systematic treatment of: [[FactualConsistency|factual consistency]] (local vs global; [[SelfCheckGPT]] / [[SAFEEvaluator|SAFE]]); [[Safety|safety]] (six harm categories; [[LlamaGuard]] / [[PerspectiveAPI]]); [[InstructionFollowingCapability|instruction-following]] ([[IFEval]] / [[INFOBench]]); [[ModelSelectionWorkflow|model selection]] ([[HardModelAttribute|hard]] vs [[SoftModelAttribute|soft]] attributes, [[ModelBuildVsBuy|build-vs-buy]] axes); and [[Leaderboard|leaderboards]] ([[OpenLLMLeaderboard]] / [[HELMLite]] / [[BenchmarkCorrelation]] / [[MeanWinRate]]).
