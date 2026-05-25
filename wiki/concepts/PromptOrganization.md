---
title: "Prompt Organization"
type: concept
tags: [prompt-engineering, application-development, versioning, llm]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Prompt Organization

**The practice of separating prompts from application code, attaching metadata to them, and versioning them independently.** Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the *Organize and Version Prompts* best practice.

## Separation principle

Ch 5's basic recommendation:

```
# file: prompts.py
GPT4o_ENTITY_EXTRACTION_PROMPT = [YOUR PROMPT]

# file: application.py
from prompts import GPT4o_ENTITY_EXTRACTION_PROMPT
def query_openai(model_name, user_prompt):
    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": GPT4o_ENTITY_EXTRACTION_PROMPT},
            {"role": "user", "content": user_prompt}
        ]
    )
```

**Why this matters** (four reasons from Ch 5):

| Property | Mechanism |
|---|---|
| **Reusability** | Multiple applications can reuse the same prompt. |
| **Testing** | Code and prompts can be tested separately. |
| **Readability** | Both code and prompts are easier to read. |
| **Collaboration** | SMEs can contribute prompts without touching code. |

## Prompt metadata

Ch 5's [[Pydantic]]-style example:

```python
from pydantic import BaseModel

class Prompt(BaseModel):
    model_name: str
    date_created: datetime
    prompt_text: str
    application: str
    creator: str
```

A production prompt may also carry: model endpoint URL, sampling params (temperature, top-p), input schema, expected output schema.

## File-format options (`.prompt` files)

Several tools have proposed dedicated prompt-file formats:

- [[Dotprompt]] (Google Firebase)
- [[Humanloop]]
- [[ContinueDev]] (Continue.dev)
- [[Promptfile]]

The benefit: prompts live in a structured, schema-validated format alongside code.

## Git vs prompt catalog

The fundamental versioning tension Ch 5 names:

| Approach | Pro | Con |
|---|---|---|
| **Git-versioned prompts** | Simple, no extra system | If multiple apps share a prompt, all must update together |
| **[[PromptCatalog\|Prompt catalog]]** (separate store) | Apps choose their own prompt version; metadata-tagged; searchable; can notify owners of updates | More infrastructure |

For multi-application teams, the catalog is the production-grade choice.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PromptCatalog]] — the production-grade versioning layer.
- [[PromptTemplate]] — the unit organized.
- [[PromptIteration]] — the practice that makes organization necessary.
- [[Dotprompt]] / [[Humanloop]] / [[ContinueDev]] / [[Promptfile]] — file-format implementations.
- [[Pydantic]] — schema layer Ch 5 uses for prompt metadata.
