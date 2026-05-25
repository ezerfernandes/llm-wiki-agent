---
title: "Prompt Catalog"
type: concept
tags: [prompt-engineering, application-development, versioning, llm, ops]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Prompt Catalog

**A versioned prompt store separate from code, allowing different applications to independently choose which prompt version they consume.** Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the production-grade alternative to Git-versioned prompts.

## The problem it solves

Ch 5: if prompts are versioned via Git alongside code, then any prompt change forces all dependent applications to update — *"it's very challenging for a team to choose to stay with an older version of a prompt for their application."*

The prompt catalog decouples prompt version from code version:

| Capability | Why it matters |
|---|---|
| **Explicit versioning per prompt** | App A can stay on v2; App B can move to v3 |
| **Metadata attached** | Search by model, application, creator, date |
| **Prompt search** | Discover existing prompts before writing new ones |
| **Dependency tracking** | Catalog knows which apps use which prompt versions |
| **Update notifications** | Application owners get notified when a new prompt version ships |

> "A well-implemented prompt catalog might even keep track of the applications that depend on a prompt and notify the application owners of newer versions of that prompt." — Ch 5

## Where it sits in the stack

A prompt catalog is part of the **[[AIEngineeringStack|application development layer]]** of the AI engineering stack. It is the *prompts equivalent* of an artifact store or feature store — a system whose only purpose is to manage versioning, discovery, and dependency tracking for a specific kind of asset.

## Relation to [[Instacart]]'s Prompt Exchange

Ch 5 names [[Instacart|Instacart's]] internal **Prompt Exchange** as a real-world example of this pattern at one organization. It's an internal marketplace where employees share and reuse their best prompts — similar in spirit to public marketplaces like [[PromptHero]], [[PromptBase]], and [[CursorDirectory]] but scoped to one company's needs.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PromptOrganization]] — the broader practice.
- [[PromptTemplate]] — the artifact stored.
- [[PromptIteration]] — what the catalog supports.
- [[Instacart]] — public example of an internal catalog (Prompt Exchange).
- [[Humanloop]] — third-party catalog implementation.
- [[AIEngineeringStack]] — application-layer position.
