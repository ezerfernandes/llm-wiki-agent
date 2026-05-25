---
title: "Audience (Prompt Component)"
type: concept
tags: [prompt-engineering, prompt-component, llm]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Audience (Prompt Component)

**The target of the generated text and the level of the generated output.** One of the seven modular prompt components in [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]]:

> *"Audience — The target of the generated text. This also describes the level of the generated output. For education purposes, it is often helpful to use ELI5 ('Explain it like I'm 5')."* — Ch 6

The audience component specifies **who the output is for**, which shifts vocabulary, depth, examples, and assumed background knowledge. It is conceptually adjacent to **[[Persona|persona]]** (*who to be*) — together they form a producer-consumer pair: persona = speaker; audience = listener.

## Example (Ch 6's paper-summary prompt)

```python
audience = "The summary is designed for busy researchers that quickly need to grasp the newest trends in Large Language Models.\n"
```

The audience specification ("busy researchers") nudges the model toward concision and high-information-density phrasing rather than tutorial-style exposition.

## ELI5

The Explain-It-Like-I'm-5 idiom is the canonical concrete audience specification — it forces the model toward analogies and away from jargon. Other common audiences: *"a senior software engineer"*, *"a CEO without technical background"*, *"a graduate student in molecular biology"*.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source.
- [[PromptEngineering]] — parent discipline.
- [[Persona]] / [[InstructionPrompt]] / [[ContextPrompt]] / [[OutputFormat]] / [[TonePrompt]] — sibling prompt components.
- [[TonePrompt]] — closely related; audience often dictates tone.
