---
title: "Dotprompt"
type: entity
tags: [tool, format, prompt-management, google, firebase]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Dotprompt

[[google|Google]] Firebase's `.prompt` file format. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as a representative implementation of the dedicated-file-format approach to prompt storage.

## The format

Ch 5's reproduced example:

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

Frontmatter encodes: target model, input schema (with [[Pydantic|Pydantic]]-like typing), output schema, output format. Body is the parameterized prompt with `{{theme}}` placeholders.

## Position

Dotprompt is one of several `.prompt` file formats that emerged in 2023–2024 ecosystem. Sibling tools cited in the same Ch 5 paragraph:

- [[Humanloop]]
- [[ContinueDev]] (Continue.dev)
- [[Promptfile]]

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[google|Google]] / Firebase — origin.
- [[PromptOrganization]] / [[PromptTemplate]] — concepts implemented.
- [[Humanloop]] / [[ContinueDev]] / [[Promptfile]] — sibling formats.
- [[gemini|Gemini]] — the model family the example targets.
