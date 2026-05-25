---
title: "Out-of-Scope Topics"
type: concept
tags: [llm-security, defense, prompt-engineering, content-filtering]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Out-of-Scope Topics

**Topics an application defines in advance as off-limits for the LLM to engage with**, regardless of user request. Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as a system-level defense for narrowing the application's behavior to its intended domain.

## Canonical example (Ch 5)

> "If your application is a customer support chatbot, it shouldn't answer political or social questions." — Ch 5

The customer-support chatbot's intended scope is order status, returns, billing. Out-of-scope topics include political opinions, medical advice, legal advice, financial advice, and any controversial social topic that could expose the brand to risk.

## Implementation tactics

| Tactic | How |
|---|---|
| **Keyword blocklist** | Filter inputs containing predefined controversial phrases — *"immigration"*, *"antivax"*, etc. |
| **Intent classifier** | Use a small model to classify the request's topic; block out-of-scope intents. |
| **Conversation-level intent analysis** | More advanced — analyze the *entire conversation*, not just the current input, for inappropriate intentions. Route flagged conversations to human operators. |
| **System-prompt instruction** | Embed the scope constraint in the system prompt: *"You are a customer support assistant. Do not discuss politics, religion, or controversial social topics."* |

## Why it's needed even with safety-trained models

A safety-trained model will refuse harmful requests but will *engage* with off-topic-but-not-harmful ones. That engagement is a **brand-risk** vector (Ch 5 examples: Google AI Overviews' 2024 "eat rocks" incident, Microsoft Tay 2016) even when the content is technically not unsafe.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[InputGuardrail]] — implementation surface.
- [[DefensivePromptEngineering]] — parent discipline.
- [[Guardrail]] — broader defensive infrastructure.
- [[safety]] — overlapping but distinct (safety covers harm, scope covers domain fit).
