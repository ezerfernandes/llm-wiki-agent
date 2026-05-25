---
title: "Middle Context Degradation"
type: concept
tags: [llm, long-context, prompt-engineering, evaluation]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Middle Context Degradation

**The empirical finding that LLMs are markedly worse at attending to information placed in the middle of a long prompt than at the beginning or end.** Sometimes called the *"lost in the middle"* effect. Documented in Liu et al. (2023) via [[NeedleInAHaystack|NIAH]] tests and discussed in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]].

## What the data shows

Across model families tested by Liu et al., retrieval accuracy as a function of needle position is **U-shaped**: high at position 0, high at the final position, sagging in the middle. The effect is robust across models, including frontier-tier proprietary models.

## Why it matters for prompt structure

Two practical implications:

1. **Put the most important instructions at the start or end of the prompt** — not in the middle. This is one reason the [[SystemPrompt|system prompt]] (which comes first) tends to be honored more reliably than user-prompt content nested inside long contexts.
2. **Most models prefer task descriptions at the beginning, but some don't.** Ch 5: *"Most models, including GPT-4, empirically perform better when the task description is at the beginning of the prompt. However, some models, including Llama 3, seem to perform better when the task description is at the end of the prompt."* The end-position bias is consistent with the U-shape; the head/tail relative ordering is model-specific.

## Why it happens (conjectural)

Common explanations:
- **Training-data bias** — instructions in human text tend to come at the start or end of paragraphs/sections.
- **[[selfattention|Self-attention]] mechanics** — positional encodings and attention sinks may not distribute attention uniformly.
- **Implicit length penalties** in the loss may penalize attention to middle tokens.

None of these is settled.

## Test for it before trusting context length

Ch 5: even when the advertised context length is 1M or 2M tokens, *"if the model's performance grows increasingly worse with a longer context, then perhaps you should find a way to shorten your prompts."* Run [[NeedleInAHaystack|NIAH]] or [[RULERBenchmark|RULER]] on your model to find the *practical* usable context length.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[NeedleInAHaystack]] — the test method.
- [[RULERBenchmark]] — broader successor.
- [[ContextLength]] — the substrate; advertised context length ≠ usable context length.
- [[selfattention|Self-attention]] — mechanistic suspect.
- [[PromptEngineering]] — informs prompt-position decisions.
