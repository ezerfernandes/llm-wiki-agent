---
title: "LMQL"
type: entity
tags: [tool, library, llm, structured-output, query-language, open-source]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# LMQL

Open-source **declarative query language for constraining LLM outputs** — [LMQL](https://lmql.ai/) — combining SQL-like syntax with constraints, regex, and type specifications that the LMQL runtime enforces at decoding time. Beck et al., ETH Zürich. Named in [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]] alongside [[Guidance]] and [[Guardrails]] as the canonical Python packages for **constrain-and-validate** LLM output:

> *"Packages have been rapidly developed to constrain and validate the output of generative models, like Guidance, Guardrails, and LMQL."* — Ch 6

## What it does

LMQL is a **superset of Python** — you write a query in LMQL-flavored Python that wraps prompts and output constraints:

```python
argmax
    "Tell me a joke about [SUBJECT] involving [PROFESSION]."
where
    SUBJECT in set(["cats", "dogs"]) and
    len(PROFESSION) < 20
```

The runtime enforces:
- **Variable-binding constraints** — `SUBJECT in set(["cats", "dogs"])` masks the model's logits so only the listed values can be sampled.
- **Length constraints** — `len(PROFESSION) < 20` enforces token-count caps.
- **Regex constraints** — patterns enforced character-by-character during decoding.

## Position in the prompt-engineering toolchain

LMQL is a **partial-workflow [[PromptEngineeringTools|prompt-engineering tool]]** specialized for **structured / constrained output**, sibling to:

- [[Guidance]] — Microsoft's templating + constrained decoding.
- [[Guardrails]] — Guardrails AI's validation + structured output.
- [[Outlines]] — JSON / regex / context-free grammar / Pydantic schemas.
- [[Instructor]] — Pydantic-based for chat APIs.

Distinguished from the others by its **language-level abstraction**: where Guidance / Guardrails / Outlines / Instructor are Python libraries you call with strings and schemas, LMQL is a *language* with its own syntax and runtime.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source naming LMQL.
- [[Guidance]] / [[Guardrails]] — siblings in Ch 6's triad.
- [[Outlines]] / [[Instructor]] — additional siblings named by [[ai-engineering-ch02-foundation-models|Huyen Ch 2]] / [[ai-engineering-ch05-prompt-engineering|Ch 5]].
- [[ConstrainedSampling]] — the underlying mechanism.
- [[GrammarConstrainedDecoding]] — the chapter-level pattern.
- [[OutputVerification]] — the parent goal.
- [[StructuredOutputs]] — the broader capability family.
- [[PromptEngineeringTools]] — partial-workflow tools taxonomy.
