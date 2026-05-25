---
title: "User Prompt"
type: concept
tags: [prompt-engineering, llm, prompt-structure]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# User Prompt

**The portion of an LLM's input controlled by the end user** — typically the question, the task input, and any user-uploaded context. The complement of the [[SystemPrompt|system prompt]] in the modern model-API prompt-structure convention defined in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]].

> "You can think of the system prompt as the task description and the user prompt as the task." — Ch 5

## The split is conventional, not mechanical

Ch 5 is explicit: *"From the model's perspective, system prompts and user prompts are processed the same way."* They are concatenated under the hood into one final prompt and run through one [[ChatTemplate|chat template]]. The system/user split exists so application developers can structure their prompt construction — and so model providers can train the model to **privilege** the system half (see [[InstructionHierarchy]], [[WallaceEtAl2024]]).

## You can also be creative

Ch 5 notes that nothing forces a strict task-description-in-system / question-in-user split:

> "You can also be creative and move instructions around, such as putting everything into the system prompt or user prompt. You can experiment with different ways to structure your prompts to see which one works best."

## Adversarial relevance

The user prompt is the **attack surface**. The user can attempt [[PromptInjection|prompt injection]] (overriding the system prompt's instructions), [[PromptExtraction|prompt extraction]] (asking the model to reveal the system prompt), or [[Jailbreak|jailbreaking]] (bypassing safety filters). The [[InstructionHierarchy|instruction-hierarchy]] training scheme is the model-level countermeasure: train the model to refuse user-prompt instructions that conflict with system-prompt instructions.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[SystemPrompt]] — the complement.
- [[ChatTemplate]] — the wire-format wrapper.
- [[InstructionHierarchy]] — why system prompts are mechanically privileged.
- [[PromptInjection]] / [[Jailbreak]] / [[PromptExtraction]] — the three adversarial-use families.
- [[PromptEngineering]] — parent.
