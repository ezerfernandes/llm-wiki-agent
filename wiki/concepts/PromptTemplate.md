---
title: "Prompt Template"
type: concept
tags: [prompt-engineering, llm, application-development]
sources: [ai-engineering-ch05-prompt-engineering, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Prompt Template

**An application-developer-defined parameterized prompt-text, hydrated with task-specific data at runtime.** Distinct from a [[ChatTemplate|chat template]] (which is model-developer-defined and wraps system/user prompts into the model's expected wire format).

> "A prompt template can be defined by any application developer." — [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]]

## Anatomy

A prompt template typically contains:

- **The static instruction** — task description, persona, output format spec.
- **Placeholder variables** — `{{disclosure}}`, `{{user_question}}`, `{{retrieved_context}}`.
- **Optional metadata** (in more sophisticated catalog formats): model endpoint URL, sampling params (temperature, top-p), input schema, expected output schema.

Ch 5 shows the [[Dotprompt|Google Firebase Dotprompt]] format as a representative example:

```yaml
---
model: vertexai/gemini-1.5-flash
input:
  schema:
    theme: string
output:
  format: json
  schema:
    name: string
    price: integer
    ingredients(array): string
---
Generate a menu item that could be found at a {{theme}} themed restaurant.
```

## Why separate prompts from code

Ch 5's *Organize and Version Prompts* section names four reasons:

| Advantage | Why |
|---|---|
| **Reusability** | Multiple applications can reuse the same prompt. |
| **Testing** | Code and prompts can be tested separately. |
| **Readability** | Both code and prompts are easier to read. |
| **Collaboration** | Subject-matter experts can edit prompts without touching code. |

## Two storage strategies

1. **Git-versioned with code.** Simple; couples prompt version to code version — *"if multiple applications share the same prompt and this prompt is updated, all applications dependent on this prompt will be automatically forced to update."*
2. **External [[PromptCatalog|prompt catalog]].** Decouples prompt version from code version; supports search, metadata, dependency tracking. Production-grade approach.

## File formats in the wild

- [[Dotprompt]] (Google Firebase)
- [[Humanloop]]
- [[ContinueDev]] (Continue.dev)
- [[Promptfile]]

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[hands-on-llm-ch07-advanced-text-generation]] — operationalizes prompt templates as the first chain link in LangChain.
- [[ChatTemplate]] — the model-side counterpart (different abstraction layer).
- [[PromptCatalog]] — the versioned storage layer for templates.
- [[PromptOrganization]] — parent practice.
- [[SystemPrompt]] / [[UserPrompt]] — the two roles a template populates.
- [[Dotprompt]] / [[Humanloop]] / [[ContinueDev]] / [[Promptfile]] — file-format implementations.
- [[PromptEngineering]] — parent discipline.

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

Ch 7 of *Hands-On LLMs* is the wiki's first runnable demonstration of prompt templates as the **building block of LangChain chains**. The chapter operationalizes Huyen's prompt-template concept via:

```python
from langchain import PromptTemplate
template = """<s><|user|>
{input_prompt}<|end|>
<|assistant|>"""
prompt = PromptTemplate(template=template, input_variables=["input_prompt"])
basic_chain = prompt | llm  # LCEL pipe operator
basic_chain.invoke({"input_prompt": "Hi! My name is Maarten. What is 1 + 1?"})
```

**Three pedagogical moves Ch 7 makes**:

1. **A prompt template hides model-specific chat-template details**. Ch 7's worked example uses Phi-3's `<s><|user|>...<|end|><|assistant|>` template wrapping around an `{input_prompt}` placeholder — the application code no longer has to copy-paste the template each call. *"Instead of having to copy-paste the prompt template each time we use the LLM, we would only need to define the user and system prompts."*

2. **Templates compose with LLMs via the LCEL pipe operator** — `prompt | llm` is the canonical chain primitive. Ch 7's framing extends Huyen Ch 5's *"a prompt template can be defined by any application developer"* with a concrete composition surface: the template **is** the first link, and `|` is the connector.

3. **Templates can have multiple named variables** that are wired into multi-stage chains. The chapter's three-stage story-generation example uses three `PromptTemplate`s with `input_variables=["summary"]`, `["summary", "title"]`, and `["summary", "title", "character"]` respectively — each template's output named via `LLMChain(..., output_key="title")` becomes input to the next template.

The chapter's important caveat: with `transformers.pipeline`, chat-template processing happens implicitly (`apply_chat_template`); with [[LangChain]]'s `LlamaCpp` it does **not**. Without an explicit `PromptTemplate` wrapping Phi-3's `<|user|>` / `<|assistant|>` / `<|end|>` markers around the user input, the model returns empty output. This makes `PromptTemplate` not optional but **required** for LangChain + GGUF Phi-3 workflows.
