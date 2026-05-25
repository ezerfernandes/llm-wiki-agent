---
title: "Prompt Iteration"
type: concept
tags: [prompt-engineering, methodology, evaluation, llm]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Prompt Iteration

**The systematic, evaluation-driven, version-controlled practice of refining prompts over time.** Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as one of the six prompt-engineering best practices, and the practice that justifies prompt engineering's claim to be *engineering* rather than fiddling.

> "Prompt engineering requires back and forth. As you understand a model better, you will have better ideas on how to write your prompts." — Ch 5

## What's prescribed

Ch 5's iteration discipline has five parts:

1. **Test changes systematically.** Don't change three things at once.
2. **Version your prompts.** Track which prompt produced which outputs.
3. **Use an experiment tracking tool.** Same rigor as any ML experiment.
4. **Standardize evaluation metrics and evaluation data.** Apples-to-apples comparison.
5. **Evaluate each prompt in the context of the whole system.** *"A prompt might improve the model's performance on a subtask but worsen the whole system's performance."*

## Each model has quirks

Iteration is also necessary because **models differ**:

> "One model might be better at understanding numbers, whereas another might be better at roleplaying. One model might prefer system instructions at the beginning of the prompt, whereas another might prefer them at the end. Play around with your model to get to know it."

A prompt optimized for GPT-4 is not necessarily optimized for Claude 3 — and rebenchmarking on every model change is part of the iteration loop.

## Relation to Ch 4's evaluation-driven development

Ch 5's iteration discipline is the prompt-engineering specialization of [[EvaluationDrivenDevelopment|evaluation-driven development]] (Ch 4): define the evaluation criteria first, then iterate the prompt against them. Without the evaluation pipeline, iteration degenerates into vibes-driven fiddling — Ch 5's stated reason prompt engineering acquired its negative reputation.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PromptEngineering]] — parent discipline.
- [[EvaluationDrivenDevelopment]] — Ch 4 prerequisite.
- [[PromptCatalog]] / [[PromptOrganization]] — where versioned prompts live.
- [[ai-engineering-ch04-evaluate-ai-systems]] — Ch 4 (evaluation methodology).
- [[ExperimentTracking]] — the broader ML practice prompt-iteration is a special case of.
