---
title: "Output Format (Prompt Component)"
type: concept
tags: [prompt-engineering, prompt-component, llm, structured-outputs]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Output Format (Prompt Component)

**The format the LLM should use to output the generated text.** One of the seven modular prompt components in [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]]:

> *"Format — The format the LLM should use to output the generated text. Without it, the LLM will come up with a format itself, which is troublesome in automated systems."* — Ch 6

The format component is the **specification of structure** (bullet points, JSON, table, paragraph), distinct from **[[InstructionPrompt|instruction]]** (*what to do*) and **[[ContextPrompt|context]]** (*why this matters*).

## Example (Ch 6's paper-summary prompt)

```python
data_format = "Create a bullet-point summary that outlines the method. Follow this up with a concise paragraph that encapsulates the main results.\n"
```

## Format specification is one of three [[OutputVerification|output-control]] methods

Ch 6 enumerates three ways to control generative output: **examples** (few-shot demonstrations of the target format), **grammar** ([[ConstrainedSampling|constrained sampling]] at token-selection time), and **fine-tuning** (deferred to Ch 12). The *format* prompt component is the **prompt-engineering surface** of the first method — specifying the format **in the instruction** rather than via examples. The most reliable approaches *combine* a format specification with examples (one-shot or few-shot) — Ch 6 demonstrates this via the RPG character JSON template.

## Why it matters for automation

Ch 6's framing: *"Without it, the LLM will come up with a format itself, which is troublesome in automated systems."* Downstream code parsing JSON / extracting fields / chaining outputs into the next prompt depends on the output being structured consistently. The Format component is the cheapest first defense; **grammar-constrained decoding** ([[GrammarConstrainedDecoding]]) is the strongest.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source.
- [[PromptEngineering]] — parent discipline.
- [[Persona]] / [[InstructionPrompt]] / [[ContextPrompt]] / [[AudiencePrompt]] / [[TonePrompt]] — sibling prompt components.
- [[OutputVerification]] — the broader goal Format-component specification serves.
- [[GrammarConstrainedDecoding]] / [[ConstrainedSampling]] — the stronger token-level alternative.
- [[StructuredOutputs]] — the broader capability family.
- [[FewShotLearning]] — the complementary examples-based approach.
- [[JSON]] — a common target format.
