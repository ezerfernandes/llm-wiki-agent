---
title: "Grammar-Constrained Decoding"
type: concept
tags: [sampling, structured-outputs, inference, llm, decoding]
sources: [hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Grammar-Constrained Decoding

**A decoding-time technique that filters the sampler's candidate-token set to only those allowed by a formal grammar (JSON / regex / context-free grammar / Pydantic schema).** The strongest of the three [[OutputVerification|output-control]] methods enumerated in [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]] — stronger than [[FewShotLearning|few-shot examples]] (prompt-level), weaker than fine-tuning (weight-level) in invasiveness but stronger than examples in guarantee strength.

> *"This process can be taken one step further and instead of validating the output we can already perform validation during the token sampling process. When sampling tokens, we can define a number of grammars or rules that the LLM should adhere to when choosing its next token."* — Ch 6

## Mechanism

For each decoding step:
1. The model produces a logit vector over the vocabulary.
2. The **grammar** specifies which tokens are valid given the partial output so far (e.g., after `{`, only string-keys or `}` are valid; after a JSON key, the next valid tokens are `:` or whitespace; etc.).
3. Invalid tokens are masked out (logits → −∞).
4. Softmax + sampling occurs only over valid tokens.

The full mechanism details live on [[ConstrainedSampling]]; this page is the **Ch 6 framing** that emphasizes the constraint is **at the token-sampling step**, not after-the-fact validation.

## Worked example (Ch 6)

Sentiment classification example: if we ask for `positive` / `negative` / `neutral`, *"it might still return something else."* By constraining the sampling process to only those three labels' token-IDs (and `<EOS>`), the LLM **can only emit one of the three valid answers**. *"Note that this is still affected by parameters such as top_p and temperature."*

## JSON-grammar worked code

Ch 6's runnable demonstration uses **[[llamacpp|`llama-cpp-python`]]** with a [[GGUF]]-quantized [[Phi3Mini|Phi-3]] and the OpenAI-compatible `response_format` parameter:

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
import json
json.loads(output)  # parses without error
```

This is the **wiki's first runnable demonstration** of grammar-constrained decoding producing valid JSON; previous wiki coverage on [[ConstrainedSampling]] (from [[ai-engineering-ch02-foundation-models|Huyen Ch 2]]) was conceptual-only.

## Frameworks (Ch 6's named set)

- **[[Guidance]]** — Microsoft's templating + constrained-decoding library.
- **[[Guardrails]]** — Guardrails AI's validation + structured-output library.
- **[[LMQL]]** — declarative query language for constrained LLM outputs.

The wiki's broader [[PromptEngineeringTools]] taxonomy also covers **[[Outlines]]** and **[[Instructor]]** — Outlines is the Python library most closely associated with this technique outside the llama.cpp ecosystem; Instructor is the Pydantic-based variant for chat APIs.

## When to use it

Per Ch 6 (and consistent with [[ai-engineering-ch02-foundation-models|Huyen Ch 2]]'s ranking): grammar-constrained decoding is **"intensive treatment"** — appropriate when prompting + post-processing don't reach the required validity rate, and when the cost (added latency, grammar-authoring effort, tooling dependency) is acceptable.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source.
- [[ConstrainedSampling]] — the broader mechanism / Huyen Ch 2 framing.
- [[OutputVerification]] — the parent goal.
- [[Guidance]] / [[Guardrails]] / [[LMQL]] / [[Outlines]] / [[Instructor]] — Python libraries implementing the technique.
- [[llamacpp]] — Ch 6's runtime for the JSON-grammar worked example.
- [[GGUF]] — the quantized model format Ch 6 uses.
- [[Phi3Mini]] — the model Ch 6 uses.
- [[JSON]] — the canonical target format.
- [[StructuredOutputs]] — the broader capability.
- [[FewShotLearning]] / [[OutputFormat]] — prompt-level alternatives.
- [[FineTuning]] — Ch 12's weight-level alternative.
- [[Softmax]] / [[Topp]] / [[Topk]] / [[Temperature]] — sampling parameters still active alongside the grammar.
