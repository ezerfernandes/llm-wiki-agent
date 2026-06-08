---
title: "Automatic Prompt Engineering (APE)"
type: concept
tags: [prompt-optimization, prompt-engineering, agentic-design-patterns, dspy, llm]
sources: [agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# Automatic Prompt Engineering (APE)

**Automatic Prompt Engineering (APE)** is the technique of using **language models themselves to generate, evaluate, and refine prompts**, automating the otherwise complex, iterative, manual process of [[PromptEngineering|prompt design]]. Surveyed in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] [[agentic-design-patterns-appendix-a-prompting|Appendix A]] as an "Advanced Technique."

> This page is the **technique-level** treatment. For the specific Zhou et al. 2023 *Automatic Prompt Engineer* algorithm (the named single-prompt reranking baseline), see [[APE]].

## The meta-model idea

The core idea is a **"meta-model"** (or a process) that takes a task description and **generates multiple candidate prompts**. Each candidate is evaluated by the quality of the output it produces on a set of inputs — using metrics like **BLEU** or **ROUGE**, or human evaluation. The best-performing prompts are selected, optionally refined further, and used for the target task.

*Appendix A example:* a developer states "I need a prompt that can extract the date and sender from an email." An APE system generates several candidate prompts, tests them on sample emails, and selects the one that consistently extracts the correct information.

## Programmatic optimization with DSPy

Appendix A then generalizes APE into **programmatic prompt optimization**, notably promoted by the [[DSPy]] framework, which treats prompts **not as static text but as programmatic modules** that can be automatically optimized — moving beyond manual trial-and-error into a systematic, data-driven methodology. Two key components:

1. **A Goldset (high-quality dataset)** — a representative set of input/output pairs that defines what a successful response looks like (the "ground truth").
2. **An Objective Function (scoring metric)** — automatically scores the LLM's output against the corresponding "golden" output, returning a quality/accuracy score.

An optimizer (e.g. a **Bayesian optimizer**) then refines the prompt via two strategies, usable independently or together:

- **Few-shot example optimization** — programmatically sample combinations of examples from the goldset to find the set that most effectively guides the model (vs a developer hand-picking examples). See [[FewShotLearning]] and [[BootstrapFewShot]].
- **Instructional prompt optimization** — use an LLM as a meta-model to iteratively mutate and rephrase the prompt's core instructions, discovering wording/tone/structure that yields the highest objective-function scores.

The goal of both is to **maximize the objective-function score**, effectively "training" the prompt to consistently produce outputs close to the goldset — simultaneously optimizing *what instructions* to give and *which examples* to show.

## Why it matters in agentic systems

Manual prompt tuning does not scale across the many prompts in a multi-agent system, nor across frequent model updates. APE/programmatic optimization provides the **automated feedback loop** that keeps an agent's prompts performant — the same role [[ContextEngineering|context engineering]] assigns to systems like the [[GoogleCloudVertexAI|Vertex AI Prompt Optimizer]]. It is distinct from human-driven [[PromptIteration|iterative refinement]], which Appendix A treats as a separate, manual design loop.

## Connections
- [[agentic-design-patterns-appendix-a-prompting]] — source (Appendix A).
- [[APE]] — the specific Zhou et al. 2023 algorithm this technique generalizes.
- [[PromptOptimization]] — parent task; [[MIPROv2]] / [[GEPA]] / [[OPRO]] / [[EvoPrompt]] / [[PromptBreeder]] — related optimizers in the wiki.
- [[DSPy]] / [[DSPyOptimizers]] / [[BootstrapFewShot]] — the programmatic-optimization framework Appendix A cites.
- [[FewShotLearning]] — few-shot example optimization target.
- [[GoogleCloudVertexAI]] — the Vertex AI Prompt Optimizer as a managed instance.
- [[PromptEngineering]] / [[PromptIteration]] / [[ContextEngineering]] — the manual disciplines APE automates.
- [[AgenticDesignPatterns]] / [[AntonioGulli]] — book hub and author.
