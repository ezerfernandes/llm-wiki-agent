---
title: "LangChain Expression Language (LCEL)"
type: concept
tags: [langchain, composition, dsl, pipe-operator]
sources: [hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# LangChain Expression Language (LCEL)

**LCEL** is [[LangChain]]'s pipe-operator composition syntax for chaining components together. `prompt | llm` produces a chain that first hydrates the prompt template and then feeds the result to the LLM. **Composition is the chain.**

## Worked example (the chapter's signature one-liner)

```python
from langchain import PromptTemplate, LlamaCpp

template = """<s><|user|>
{input_prompt}<|end|>
<|assistant|>"""

prompt = PromptTemplate(template=template, input_variables=["input_prompt"])
llm = LlamaCpp(model_path="Phi-3-mini-4k-instruct-fp16.gguf", n_gpu_layers=-1, max_tokens=500, n_ctx=2048, seed=42, verbose=False)

basic_chain = prompt | llm
basic_chain.invoke({"input_prompt": "Hi! My name is Maarten. What is 1 + 1?"})
# → "The answer to 1 + 1 is 2. It's a basic arithmetic operation..."
```

The `|` is Python's bitwise-or operator that LangChain overloads to mean **"feed the left output into the right input"** — a fluent interface for building chains.

## Generalization to sequential chains

The `|` operator generalizes to multi-step chains. Ch 7's three-stage story-generation worked example:

```python
title = LLMChain(llm=llm, prompt=title_prompt, output_key="title")
character = LLMChain(llm=llm, prompt=character_prompt, output_key="character")
story = LLMChain(llm=llm, prompt=story_prompt, output_key="story")

llm_chain = title | character | story
llm_chain.invoke("a girl that lost her mother")
# → dict with three named outputs: {"title": ..., "character": ..., "story": ...}
```

The named outputs flow through the pipe — each downstream chain reads the upstream named outputs from its `input_variables`.

## Why LCEL matters

- **Composition primitive** — the `|` operator is the structural unit for building [[LangChain]] pipelines, complementing the [[PromptTemplate|PromptTemplate]] (data primitive) and `LLMChain` (named-output primitive).
- **Lego-block analog** — extends [[hands-on-llm-ch06-prompt-engineering|Ch 6's]] seven-component modular-prompt framing from "compose a prompt" to "compose a chain of prompts."
- **Provider-agnostic** — the same `prompt | llm` shape works for [[LangChainLlamaCpp|`LlamaCpp`]], `ChatOpenAI`, etc.

## Connections

- [[LangChain]] — the framework providing LCEL.
- [[PromptTemplate]] — the left operand in the canonical pattern.
- [[LangChainLlamaCpp]] / [[LLMChain]] — typical right operands.
- [[PromptChaining]] / [[PromptDecomposition]] — the conceptual pattern LCEL operationalizes.
- [[hands-on-llm-ch07-advanced-text-generation]] — primary source.

## From Hands-On LLMs Ch 7

Ch 7 introduces LCEL as the **canonical composition primitive** for LangChain. The `prompt | llm` one-liner appears in every code listing in the chapter — Model I/O, Chains, Memory, Agents all build on top of it. The chapter does not name it "LCEL" explicitly but uses the syntax throughout; this page records the LangChain-canonical name for forward reference. The chapter's broader thesis on composition — *"Each of these techniques has significant strengths by themselves but their true value does not exist in isolation. It is when you combine all of these techniques that you get an LLM-based system with incredible performance"* — is operationalized by LCEL at the code level.
