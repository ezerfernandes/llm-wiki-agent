---
title: "Greshake et al. 2023 — Indirect Prompt Injection"
type: entity
tags: [paper, prompt-injection, safety, llm-security]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Greshake et al. 2023 — Indirect Prompt Injection

The paper introducing **[[IndirectPromptInjection|indirect prompt injection]]** — *"Not What You've Signed Up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection"* (Greshake et al. 2023). Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the foundational work for the most-powerful family of prompt attacks.

## The contribution

Demonstrated that malicious instructions don't have to be in the user prompt — they can live in any data source the LLM is integrated with: public web pages, GitHub repositories, retrieved documents, emails, SQL data. The model retrieves the malicious payload as part of its normal operation and treats it as if it were a legitimate instruction.

This generalized [[PromptInjection|direct prompt injection]] into a class of attacks that scales with **every** model-tool integration.

## Why it's the dominant attack surface for agents

[[Agent|Agentic]] systems and [[rag|RAG]] systems multiply the indirect-prompt-injection surface area by the number of tools and data sources. Every new tool integration is a new injection vector. Ch 5 names two example forms:

- **Passive phishing** — leave the payload in public spaces; wait for AI assistants to find it.
- **Active injection** — send the payload directly to the target (e.g., via email).

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[IndirectPromptInjection]] — the concept.
- [[PromptInjection]] / [[PromptAttack]] / [[Jailbreak]] — broader family.
- [[Agent]] / [[rag|RAG]] — the deployment patterns most affected.
- [[InstructionHierarchy]] / [[WallaceEtAl2024]] — the model-level defense.
