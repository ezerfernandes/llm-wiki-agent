---
title: "Constrained Sampling"
type: concept
tags: [sampling, structured-outputs, inference, llm]
sources: [ai-engineering-ch02-foundation-models, hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Constrained Sampling

A technique for **guiding LLM generation toward a target format** by **filtering the logit vector at each generation step** to only the tokens that meet the constraints. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "At a high level, to generate a token, the model samples among values that meet the constraints. ... Constrained sampling filters this logit vector to keep only the tokens that meet the constraints. It then samples from these valid tokens."

## How it works

For each decode step:
1. The model computes a logit vector (one logit per vocabulary token).
2. **A grammar specifies which tokens are valid given the partial output so far.**
3. Logits for invalid tokens are masked out (set to −∞).
4. Softmax + sampling is performed only over valid tokens.

## Worked example

JSON grammar rules:
- After `{`, you can't have another `{` unless it's part of a string (`{"key": "{{string}}"}`).
- After a key like `"name":`, you need a value (string, number, object, array, etc.).
- After a closing `}` at the top level, you need EOS.

Each of these constraints becomes a token-filter rule the sampler applies at the corresponding step.

## Cost

Per Ch 2:
- **Generalizability**: Limited. Each output format (JSON, YAML, regex, CSV...) needs its own grammar.
- **Latency**: Grammar verification can add generation latency (Brandon T. Willard 2024).
- **Tooling dependency**: Use is limited to formats whose grammars are supported by external tools or built by your team.

## The opposing argument

> "Some are against constrained sampling because they believe the resources needed for constrained sampling are better invested in training models to become better at following instructions." — Ch 2

This is the *finetuning-over-grammars* school of thought.

## Where it fits in the structured-outputs stack

Per Ch 2's five-layer ranking:
1. Prompting (lightest)
2. Post-processing
3. Test-time compute
4. **Constrained sampling** ← here
5. Finetuning (heaviest)

Constrained sampling is "intensive treatment" — used when prompting and post-processing don't get to the required validity rate.

## Frameworks

Ch 2 names **guidance**, **outlines**, **instructor**, **llama.cpp** as frameworks that implement constrained sampling.

## Connections
- [[StructuredOutputs]] — the parent enforcement family.
- [[SemanticParsing]] — primary task class needing constrained sampling.
- [[FineTuning]] — the alternative "intensive treatment" path.
- [[Logprobs]] / [[Softmax]] — the substrate constrained sampling operates on.
- [[StoppingCondition]] — interacts because constrained sampling may need extended generation to complete a valid output.
- [[ai-engineering-ch02-foundation-models]] — primary source (Huyen Ch 2).
- [[hands-on-llm-ch06-prompt-engineering]] — operational source (Alammar & Grootendorst Ch 6).

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 elaborates the mechanism with an explicit sentiment-classification example:

> *"When sampling tokens, we can define a number of grammars or rules that the LLM should adhere to when choosing its next token. For instance, if we ask the model to either return 'positive,' 'negative,' or 'neutral' when performing sentiment classification, it might still return something else. By constraining the sampling process, we can have the LLM only output what we are interested in. Note that this is still affected by parameters such as top_p and temperature."* — Ch 6

### The wiki's first runnable demonstration

Ch 6's worked code is the **wiki's first runnable constrained-sampling demonstration** — `llama-cpp-python` with [[GGUF]]-quantized [[Phi3Mini|Phi-3]]:

```python
from llama_cpp.llama import Llama
llm = Llama.from_pretrained(
    repo_id="microsoft/Phi-3-mini-4k-instruct-gguf",
    filename="*fp16.gguf",
    n_gpu_layers=-1, n_ctx=2048, verbose=False,
)
output = llm.create_chat_completion(
    messages=[{"role": "user", "content": "Create a warrior for an RPG in JSON format."}],
    response_format={"type": "json_object"},
    temperature=0,
)["choices"][0]["message"]["content"]
import json; json.loads(output)  # parses without error
```

The `response_format={"type": "json_object"}` parameter is an **OpenAI-API-compatible** option that `llama-cpp-python` honors by applying a JSON grammar under the hood. The output validates as proper JSON containing the RPG character `Eldrin Stormbringer / Warrior / level 10 / Ironclad Armor / Steel Greatsword`. See [[GrammarConstrainedDecoding]] for the dedicated page.

### Toolchain Ch 6 names

Ch 6's named set is **[[Guidance]] / [[Guardrails]] / [[LMQL]]** — partially overlapping with Huyen Ch 2's *guidance / outlines / instructor / llama.cpp*. The wiki's full picture (combining both):

| Library | Source | Notes |
|---|---|---|
| [[Guidance]] | Huyen Ch 2 + Ch 6 | Microsoft's templating + constrained decoding. |
| [[Outlines]] | Huyen Ch 2 | JSON / regex / CFG / Pydantic schemas. |
| [[Instructor]] | Huyen Ch 2 | Pydantic-based for chat APIs. |
| [[Guardrails]] | Ch 6 | Guardrails AI's validation + structured-output library. |
| [[LMQL]] | Ch 6 | Declarative query language for constrained outputs. |
| [[llamacpp]] | Huyen Ch 2 + Ch 6 | Has built-in JSON grammar via `response_format`. |
