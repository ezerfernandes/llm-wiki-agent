---
title: "Humanloop"
type: entity
tags: [tool, platform, prompt-management, llm-ops]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Humanloop

LLM-ops platform providing **prompt management** — including prompt catalog, versioning, evaluation, and team collaboration features. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as one of several tools that have proposed dedicated `.prompt` file formats for storing prompts separately from code.

> "Several tools have proposed special `.prompt` file formats to store prompts. See Google Firebase's Dotprompt, Humanloop, Continue Dev, and Promptfile." — Ch 5

## Position

Humanloop is one of several commercial offerings in the *prompt catalog / prompt management* space, providing the production-grade versioning and metadata Ch 5 recommends. Sibling entities cited in the same Ch 5 paragraph:

- [[Dotprompt]] (Google Firebase)
- [[ContinueDev]] (Continue.dev)
- [[Promptfile]]

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PromptCatalog]] — the concept Humanloop implements.
- [[PromptTemplate]] / [[PromptOrganization]] — adjacent concepts.
- [[Dotprompt]] / [[ContinueDev]] / [[Promptfile]] — sibling prompt-file-format tools.
