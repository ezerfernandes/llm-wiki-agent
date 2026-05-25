---
title: "One-Shot Prompting"
type: concept
tags: [prompt-engineering, in-context-learning, llm]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# One-Shot Prompting

**Providing exactly one example in the prompt before asking the model to perform the task.** The middle point in the zero-shot / one-shot / few-shot continuum that [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]] codifies:

> *"Zero-shot prompting does not leverage examples, one-shot prompts use a single example, and few-shot prompts use two or more examples."* — Ch 6

## Worked example (Ch 6) — the made-up word *screeg*

```python
one_shot_prompt = [
    {"role": "user", "content": "A 'Gigamuru' is a type of Japanese musical instrument. An example of a sentence that uses the word Gigamuru is:"},
    {"role": "assistant", "content": "I have a Gigamuru that my uncle gave me as a gift. I love to play it at home."},
    {"role": "user", "content": "To 'screeg' something is to swing a sword at it. An example of a sentence that uses the word screeg is:"}
]
```

The chat-template-rendered prompt alternates `<|user|>` / `<|assistant|>` turns. The model produces:

> *"During the intense duel, the knight skillfully screeged his opponent's shield, forcing him to defend himself."*

A single example was sufficient to communicate the desired output pattern.

## Why one example sometimes suffices

The example carries **structural** information (the LLM should produce one sentence using the made-up word, not a definition or paragraph) that would be cumbersome to specify in natural language. The original [[GPT3|GPT-3]] paper (Brown et al. 2020) called this *"in-context learning"* — see [[InContextLearning]].

## When to scale to [[FewShotLearning|few-shot]]

Per Ch 6 — and consistent with [[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]] — *"the more examples you show a model, the better it can learn"* up to a context-length budget. The diminishing-returns crossover happens earlier for stronger models (Microsoft 2023: large few-shot effect on GPT-3, small effect on GPT-4).

One-shot is the right sweet spot when:
- **The task pattern is regular** — one example is structurally representative.
- **Tokens are scarce** — context windows are limited or per-call cost matters.
- **The model is strong** — instruction-tuned models often need only a single demonstration.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source.
- [[InContextLearning]] — parent concept (Brown et al. 2020).
- [[ZeroShotLearning]] — the zero-example endpoint.
- [[FewShotLearning]] — the multi-example endpoint.
- [[PromptEngineering]] — discipline.
- [[ChatTemplate]] — the `<|user|>` / `<|assistant|>` alternation needed for one-shot prompts.
- [[GPT3]] — the model where the few-shot result first dramatically appeared.
