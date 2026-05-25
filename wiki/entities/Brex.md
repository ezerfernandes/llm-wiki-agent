---
title: "Brex"
type: entity
tags: [company, fintech, ai-application]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Brex

American fintech company offering corporate credit cards, expense management, and treasury services. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] for its **Prompt Engineering Guide** (2023) — specifically Figure 5-10, where the guide demonstrates a model revealing a user's location even though it has been explicitly instructed not to.

The example is used by Ch 5 to illustrate that **context, not just system prompts, can be extracted** — extending [[PromptExtraction|prompt extraction]] beyond the obvious "leak the system prompt" framing into "leak the application-supplied context."

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PromptExtraction]] — the attack class Brex's example illustrates.
- [[PromptEngineering]] — discipline.
- [[DefensivePromptEngineering]] — Brex's guide is a practitioner-side resource.
