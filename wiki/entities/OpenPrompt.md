---
title: "OpenPrompt"
type: entity
tags: [tool, library, prompt-optimization, open-source]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# OpenPrompt

Open-source prompt-engineering toolkit introduced by Ding et al. 2021. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] alongside [[DSPy]] as a representative **full-workflow prompt-optimization tool**.

> "Tools that aim to automate the whole prompt engineering workflow include OpenPrompt (Ding et al., 2021) and DSPy (Khattab et al., 2023). At a high level, you specify the input and output formats, evaluation metrics, and evaluation data for your task. These prompt optimization tools automatically find a prompt or a chain of prompts that maximizes the evaluation metrics on the evaluation data." — Ch 5

The framing Ch 5 uses: these tools are *"similar to autoML (automated ML) tools that automatically find the optimal hyperparameters for classical ML models"* — autoPrompt by analogy.

## Position

OpenPrompt predates the modern wave of [[DSPy]]-family typed-pipeline tools. It is the historical bridge between hand-written prompts and the optimizer-driven future.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PromptEngineeringTools]] — parent category.
- [[DSPy]] — sibling full-workflow tool.
- [[PromptOptimization]] — the task.
- [[AutoPrompt]] — adjacent (similar name; distinct tool).
