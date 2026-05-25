---
title: "greshake/llm-security"
type: entity
tags: [entity, tool, llm-security, red-team, prompt-injection, open-source]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# greshake/llm-security

**`greshake/llm-security`** is an **open-source repository of LLM security tooling and example attacks**, maintained by Kai Greshake — the first author of the [[IndirectPromptInjection|Indirect Prompt Injection]] paper ([[GreshakeEtAl2023]]). Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as one of four automated security-probing tools for LLM applications.

> "Tools that help automate security probing include Azure/PyRIT, leondz/garak, greshake/llm-security, and CHATS-lab/persuasive_jailbreaker." — Ch 5

## What it contains

The repository is the practitioner companion to the Greshake et al. 2023 paper — it surfaces:

- Worked [[IndirectPromptInjection|indirect prompt injection]] examples (web pages, GitHub repos, retrieved documents poisoned with malicious instructions).
- Demonstrations of the attack against real LLM-integrated applications.
- Tooling for testing whether a given application is vulnerable to indirect injection patterns.

## Significance

Because the author is the same researcher who **named indirect prompt injection as a category**, the repository is treated as a canonical reference for that attack family. Ch 5's defensive-engineering recommendations on tool-output sanitization and the [[InstructionHierarchy|instruction hierarchy]]'s "tool outputs lowest priority" rule are direct responses to the attacks demonstrated in this repository.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[GreshakeEtAl2023]] — the paper this repo accompanies.
- [[IndirectPromptInjection]] — the attack family this repo specializes in.
- [[LLMRedTeaming]] — discipline this tool implements.
- [[AzurePyRIT]] / [[GarakLLMScanner]] / [[CHATSPersuasiveJailbreaker]] — sibling automated red-team tools.
- [[PromptInjection]] / [[PromptAttack]] — broader attack family.
- [[InstructionHierarchy]] — the model-level defense designed to neutralize these attacks.
