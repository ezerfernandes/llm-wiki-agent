---
title: "LLMChain"
type: concept
tags: [langchain, chains, composition, prompt-template]
sources: [hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# LLMChain

**`langchain.LLMChain`** is the [[LangChain]] **named-output chain primitive** — wraps a `(llm, prompt, output_key)` triple into a composable unit that produces a named result. The substrate for multi-step sequential chains like Ch 7's three-stage story-generation worked example.

## Worked example: the three-stage story generation chain

```python
from langchain import LLMChain, PromptTemplate

title_template = """<s><|user|>Create a title for a story about {summary}. Only return the title.<|end|>
<|assistant|>"""
title_prompt = PromptTemplate(template=title_template, input_variables=["summary"])
title = LLMChain(llm=llm, prompt=title_prompt, output_key="title")

character_template = """<s><|user|>Describe the main character for a story called {title} about {summary}.<|end|>
<|assistant|>"""
character_prompt = PromptTemplate(template=character_template, input_variables=["summary", "title"])
character = LLMChain(llm=llm, prompt=character_prompt, output_key="character")

story_template = """<s><|user|>Create a story about {summary} called {title} starring {character}.<|end|>
<|assistant|>"""
story_prompt = PromptTemplate(template=story_template, input_variables=["summary", "title", "character"])
story = LLMChain(llm=llm, prompt=story_prompt, output_key="story")

llm_chain = title | character | story
llm_chain.invoke("a girl that lost her mother")
# → {"summary": ..., "title": " \"Whispers of Loss: A Journey Through Grief\"", "character": ..., "story": ...}
```

Each `LLMChain` consumes its declared `input_variables` and emits its `output_key` — values accumulate in a dict that the next stage's prompt reads from.

## Why LLMChain matters

Ch 7's framing on multi-prompt benefits:

- **Smaller, more manageable prompts per step** — each prompt is narrower than a single mega-prompt would be.
- **Independent components** — *"we now have access to these individual components. We can easily extract the title; that might not have been the case if we were to use a single prompt."*
- **Different parameters per call** — different `temperature`, `max_tokens`, or even different LLMs per stage.
- **The operationalization of [[PromptChaining|chain prompting]] / [[PromptDecomposition|prompt decomposition]] in [[LangChain]].**

## LLMChain vs LCEL

`LLMChain` and the [[LCEL|LCEL pipe operator]] (`prompt | llm`) are LangChain's two composition primitives:

| Primitive | Use case |
|---|---|
| `prompt | llm` (LCEL) | Single-step chain; no named output |
| `LLMChain(llm, prompt, output_key)` | Multi-step chain; explicit named output for downstream consumption |

Both can be combined with the pipe operator (`title | character | story` is three LLMChains piped together).

## Connections

- [[LangChain]] — the framework.
- [[PromptTemplate]] — the prompt LLMChain wraps.
- [[LCEL]] — the pipe-operator composition primitive used together with LLMChain.
- [[PromptChaining]] / [[PromptDecomposition]] — the conceptual patterns LLMChain operationalizes.
- [[hands-on-llm-ch07-advanced-text-generation]] — primary source.

## From Hands-On LLMs Ch 7

Ch 7's named-output chain primitive. The chapter introduces it as the **sequential-composition** answer to the question *"how do I decompose a complex generation task into smaller steps?"* — the runnable LangChain implementation of [[hands-on-llm-ch06-prompt-engineering|Ch 6's]] *writing stories* use case from the chain-prompting taxonomy. The named-output mechanism (`output_key="title"`) is what makes the three-stage chain composable — every downstream stage can refer to `{title}` by name in its own prompt template.
