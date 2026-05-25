---
title: "Instruction (Prompt Component)"
type: concept
tags: [prompt-engineering, prompt-component, llm]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Instruction (Prompt Component)

**The task itself in a prompt.** One of the seven modular prompt components in [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]]:

> *"Instruction — The task itself. Make sure this is as specific as possible. We do not want to leave much room for interpretation."* — Ch 6

The instruction is the *what to do*, complementing **[[Persona|persona]]** (*who to be*), **[[ContextPrompt|context]]** (*why this matters*), **[[OutputFormat|format]]** (*how to shape it*), **[[AudiencePrompt|audience]]** (*who reads it*), **[[TonePrompt|tone]]** (*how to sound*), and **data** (*what to operate on*).

## Ch 6's specificity rule

**The most important of the three instruction-prompting tips** (specificity, [[Hallucination|hallucination]] mitigation, order):

> *"Accurately describe what you want to achieve. Instead of asking the LLM to 'Write a description for a product' ask it to 'Write a description for a product in less than two sentences and use a formal tone.'"* — Ch 6

Without specificity, the model is forced to guess intent — *"if we were to skip the instruction 'in two to three sentences' it might generate complete paragraphs."*

## The two-/three-ingredient minimal prompt

Ch 6 introduces the minimal **instruction + data** prompt (two ingredients) and extends it with an **output indicator** (e.g., `Text:` / `Sentiment:` prefixes) as the third. The instruction is the load-bearing center of the minimal form — *"this extends the most basic prompt to one consisting of two components — the instruction itself and the data that relates to the instruction."*

## Order matters

Per Ch 6's third instruction-prompting tip:

> *"Either begin or end your prompt with the instruction. Especially with long prompts, information in the middle is often forgotten."*

This is the **[[lostinthemiddle|lost-in-the-middle]] phenomenon** (Liu et al. 2023) applied to instruction placement. **[[PrimacyEffect|Primacy effect]]** = beginning-of-prompt focus; **recency effect** = end-of-prompt focus. Both are stronger than middle-of-prompt focus.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source.
- [[PromptEngineering]] — parent discipline.
- [[Persona]] / [[ContextPrompt]] / [[OutputFormat]] / [[AudiencePrompt]] / [[TonePrompt]] — sibling prompt components.
- [[PromptStructure]] — Huyen Ch 5's three-part anatomy; instruction belongs to the *task description* half.
- [[SystemPrompt]] — instructions conventionally live in the system prompt (along with persona, format, audience, tone).
- [[UserPrompt]] — the data conventionally lives in the user prompt.
- [[Hallucination]] — Ch 6's second instruction-tip is the *"say 'I don't know'"* mitigation.
- [[lostinthemiddle]] / [[PrimacyEffect]] — explain why instruction position matters.
