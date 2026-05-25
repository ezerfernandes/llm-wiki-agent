---
title: "Context (Prompt Component)"
type: concept
tags: [prompt-engineering, prompt-component, llm]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Context (Prompt Component)

**Additional information describing the context of the problem or task.** One of the seven modular prompt components in [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]]:

> *"Context — Additional information describing the context of the problem or task. It answers questions like 'What is the reason for the instruction?'"* — Ch 6

The context complements **[[Persona|persona]]** (*who to be*) and **[[InstructionPrompt|instruction]]** (*what to do*) by supplying *why and what background matters*.

## Example (Ch 6's paper-summary prompt)

```python
context = "Your summary should extract the most crucial points that can help researchers quickly understand the most vital information of the paper.\n"
```

The context explains the *purpose* of the summary so the model can prioritize content choices appropriately.

## Distinct from [[ContextConstruction|context construction]] / [[rag|RAG]]

The Ch 6 *"context"* prompt component is the **narrative reason / framing** for the task, distinct from the larger [[ContextConstruction|context-construction]] discipline ([[ai-engineering-ch06-rag-agents|Huyen Ch 6]]) which encompasses [[rag|retrieval-augmented generation]], tool outputs, and memory. The Ch 6 component is *one ingredient* of the prompt; [[ContextConstruction|context construction]] is the broader practice of *what data flows into the prompt window* and from where.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source.
- [[PromptEngineering]] — parent discipline.
- [[Persona]] / [[InstructionPrompt]] / [[OutputFormat]] / [[AudiencePrompt]] / [[TonePrompt]] — sibling prompt components.
- [[ContextConstruction]] — broader RAG / tool-output / memory discipline.
- [[rag|RAG]] — operationalizes dynamic context insertion.
- [[SystemPrompt]] — context often lives in the system prompt.
