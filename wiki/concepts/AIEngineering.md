---
title: "AI Engineering"
type: concept
tags: [discipline, ai-engineering, foundation-models, ml-engineering]
sources: [ai-engineering-chip-huyen, ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# AI Engineering

**The process of building applications on top of foundation models.** Defined by [[ChipHuyen|Chip Huyen]] in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] as a discipline distinct from — but evolved out of — traditional [[MLOps|ML engineering]]. The defining shift: whereas ML engineering develops models from scratch, AI engineering **leverages models that someone else has already trained** ([[FoundationModel|foundation models]] available via API or open weights) and focuses on [[ModelAdaptation|adapting]] and [[Evaluation|evaluating]] them.

## Why now (Huyen's three factors)

1. **General-purpose AI capabilities.** Foundation models can do more tasks than task-specific predecessors — they expand the set of feasible applications, vastly increasing demand and user base.
2. **[[AIInvestmentBoom|Increased AI investments]].** Goldman Sachs estimated $100B (US) / $200B (global) AI investment by 2025; 1 in 3 S&P 500 companies mentioned AI in Q2 2023 earnings calls (3× the prior year). [[Scribd|Scribd's]] applied-research lead reported AI cost dropped two orders of magnitude April 2022 → April 2023.
3. **Low entry barrier.** [[ModelAsAService|Model-as-a-service]] APIs (popularized by [[openai|OpenAI]]) eliminate the need to host models; AI itself can write the surrounding code; natural-language prompts replace programming languages for many tasks.

## Why the term "AI Engineering"?

Huyen rejects competing terms: **ML engineering** is too narrow because foundation-model work differs in important ways (adaptation > development, evaluation harder, inference economics central); all the **"Ops"** terms (MLOps, LLMOps, AIOps) put operational concerns ahead of engineering judgment, which Huyen argues is backward. She surveyed 20 people building foundation-model applications; most preferred "AI engineering."

## Three ways AI engineering differs from ML engineering

(See [[AIEngineeringVsMLEngineering]] for the full comparison.)

1. **You use someone else's pretrained model.** Focus shifts from modeling/training to [[ModelAdaptation|adaptation]].
2. **Models are bigger** — more compute, higher latency, more pressure on [[InferenceOptimization|inference optimization]] and on engineers who can work with large GPU clusters.
3. **Outputs are open-ended** — [[Evaluation|evaluation]] becomes harder; classical ground-truth metrics break down.

## Tools growth

Within two years of [[ChatGPT|ChatGPT]]'s launch, four open-source AI engineering tools ([[AutoGPT]], [[StableDiffusion]] Web UI, [[LangChain]], [[Ollama]]) had each surpassed Bitcoin in GitHub stars — on track to surpass React and Vue. A LinkedIn survey (August 2023) showed professionals adding "Generative AI", "ChatGPT", "Prompt Engineering", "Prompt Crafting" to their profiles grew on average 75% per month. ComputerWorld declared "teaching AI to behave is the fastest-growing career skill."

## Connections

- [[FoundationModel]] — the substrate.
- [[AIEngineeringStack]] — the three-layer (application / model / infrastructure) stack.
- [[AIEngineeringVsMLEngineering]] — the comparison taxonomy.
- [[ModelAdaptation]] — the umbrella discipline.
- [[PromptEngineering]] / [[rag|RAG]] / [[FineTuning|finetuning]] — the three core adaptation techniques.
- [[Evaluation]] — the hardest problem in AI engineering (per Huyen's preface).
- [[InferenceOptimization]] — first-class engineering constraint.
- [[DatasetEngineering]] — replacement for classical ML feature engineering.
- [[AIInterface]] — the UX surface.
- [[ai-engineering-chip-huyen]] / [[ai-engineering-ch01-intro]] — primary sources.
