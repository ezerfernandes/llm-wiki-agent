---
title: "Output Verification"
type: concept
tags: [prompt-engineering, structured-outputs, validation, llm, safety]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Output Verification

**Verifying and controlling the output of generative models before downstream code consumes it.** The closing topic of [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]]:

> *"Systems and applications built with generative models might eventually end up in production. When that happens, it is important that we verify and control the output of the model to prevent breaking the application and to create a robust generative AI application."* — Ch 6

## The four motivations (Ch 6)

| Motivation | Why we care |
|---|---|
| **Structured output** | Most generative models produce free-form text; many use cases require JSON / YAML / table / etc. |
| **Valid output** | When constrained to a choice set ("positive" / "negative" / "neutral"), the model should not invent a fourth option. |
| **Ethics** | No PII, no profanity, no bias, no cultural stereotypes. Especially relevant for open-source models without RLHF guardrails. |
| **Accuracy** | Factual, coherent, free from [[Hallucination|hallucination]]. |

## The three control methods (Ch 6)

| Method | What it does |
|---|---|
| **Examples** | Provide [[FewShotLearning|few-shot]] demonstrations of the expected output format. |
| **Grammar** | Control token selection via [[GrammarConstrainedDecoding|grammar-constrained decoding]] — e.g., JSON grammar / regex / context-free grammar. |
| **Fine-tuning** | Train the model on data with the expected output format (Ch 12 — deferred). |

Ch 6 walks the first two; Ch 12 covers the third.

## Worked examples (Ch 6)

### Examples method — RPG character JSON
Without examples, the model produces verbose truncated JSON with unwanted fields. With a one-shot template:
```json
{
  "description": "A SHORT DESCRIPTION",
  "name": "THE CHARACTER'S NAME",
  "armor": "ONE PIECE OF ARMOR",
  "weapon": "ONE OR MORE WEAPONS"
}
```
the model output conforms exactly: `Lysandra Shadowstep / Leather Cloak of the Night / Dagger of Whispers`. *"It is still up to the model whether it will adhere to your suggested format or not. Some models are better than others at following instructions."*

### Grammar method — JSON via llama-cpp-python
```python
output = llm.create_chat_completion(
    messages=[{"role": "user", "content": "Create a warrior for an RPG in JSON format."}],
    response_format={"type": "json_object"},
    temperature=0,
)
```
The `response_format={"type": "json_object"}` parameter applies a JSON grammar under the hood. Output is valid JSON that `json.loads()` parses without error.

## The validation-loop pattern

Ch 6 also describes a **post-hoc validation** pattern: use a second LLM call (or a deterministic checker) to verify the first LLM's output against rules. *"The generative models retrieve the output as new prompts and attempt to validate it based on a number of predefined guardrails."* This is the family that **[[Guidance]] / [[Guardrails]] / [[LMQL]]** support.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source.
- [[GrammarConstrainedDecoding]] / [[ConstrainedSampling]] — the strongest control method (token-level).
- [[FewShotLearning]] — the examples-based control method (prompt-level).
- [[FineTuning]] — Ch 12's third control method.
- [[OutputFormat]] — the prompt component that specifies the target format.
- [[StructuredOutputs]] — the broader capability family.
- [[Hallucination]] — the accuracy-motivation failure mode.
- [[Guidance]] / [[Guardrails]] / [[Outlines]] / [[LMQL]] — Python packages in the validation-toolchain space.
- [[JSON]] — the canonical worked target format.
- [[llamacpp]] — Ch 6's runtime for the grammar-constrained worked example.
- [[GGUF]] — the quantized model format Ch 6's grammar example uses.
