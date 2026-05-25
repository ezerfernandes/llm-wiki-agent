---
title: "Prompt Structure"
type: concept
tags: [prompt-engineering, llm]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Prompt Structure

**The three-part anatomy that [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] uses as the canonical breakdown of an effective prompt:**

| Part | What it contains |
|---|---|
| **Task description** | What you want the model to do, including the role you want the model to play and the output format. |
| **Example(s)** | Demonstrations of how to do the task — e.g., for toxicity detection, a few examples of toxic vs non-toxic text. |
| **The task** | The concrete input — the specific question to answer or document to summarize. |

> "A prompt generally consists of one or more of the following parts: Task description / Example(s) of how to do this task / The task." — Ch 5

## How it maps to [[SystemPrompt|system]] / [[UserPrompt|user]] prompts

Typical convention:

- **System prompt** ≈ task description (+ examples, sometimes).
- **User prompt** ≈ the task (+ retrieved context).

But Ch 5 explicitly licenses creative re-arrangement: *"You can also be creative and move instructions around, such as putting everything into the system prompt or user prompt."* The convention is a starting point, not a constraint.

## Position effects

Per the [[MiddleContextDegradation|"lost in the middle"]] effect:

- **Most models (including GPT-4)** perform better when the task description is at the **beginning**.
- **Some models (including Llama 3)** perform better with the task description at the **end**.

Test for your model rather than assume.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[SystemPrompt]] / [[UserPrompt]] — typical mapping of structure to model-API convention.
- [[PromptTemplate]] — the parameterized form.
- [[MiddleContextDegradation]] — the position-effect explanation.
- [[FewShotLearning]] / [[InContextLearning]] — the "example(s)" part is in-context learning.
- [[PromptEngineering]] — parent discipline.
