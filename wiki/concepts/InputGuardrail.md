---
title: "Input Guardrail"
type: concept
tags: [llm-security, defense, guardrail, prompt-attack]
sources: [ai-engineering-ch05-prompt-engineering, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Input Guardrail

**An application-layer filter that inspects user inputs *before* they reach the model, blocking or flagging suspicious requests.** One of two paired application-layer guardrail types named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] — the sibling is [[OutputGuardrail]].

## Implementation patterns

Ch 5 lists three implementation tactics, ordered by sophistication:

1. **Block-list of keywords** — naive but cheap. Filter out inputs containing predefined phrases associated with [[OutOfScopeTopics|out-of-scope topics]] (e.g., *"immigration"*, *"antivax"* for a customer-support chatbot).
2. **Known-attack-pattern matching** — match inputs against a catalog of known [[PromptInjection|prompt injection]] / [[Jailbreak|jailbreak]] templates ([[DANJailbreak|DAN]], grandma-exploit phrasing, *"ignore the above"* patterns).
3. **Model-based suspicious-request detection** — *"more advanced algorithms use AI to understand the user's intent by analyzing the entire conversation, not just the current input"* — possibly an [[AnomalyDetection|anomaly-detection]] algorithm flagging unusual prompts, possibly routing high-suspicion requests to human operators.

## Why input filtering alone is insufficient

> "Inputs that appear harmless can produce harmful outputs, so it's important to have output guardrails, as well." — Ch 5

Input filtering catches *known* attack shapes but is blind to (a) novel attacks the catalog doesn't cover, (b) inputs whose harmfulness only manifests in the output, and (c) [[IndirectPromptInjection|indirect prompt injection]] where the malicious instruction arrives via tool output, not user input.

## Pairing with output guardrails

Input + output guardrails form a **defense-in-depth pair**: input blocks the obvious, output catches what slipped through and what the model itself produces unprompted.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[OutputGuardrail]] — paired application-layer filter.
- [[Guardrail]] — parent concept; the broader defensive infrastructure.
- [[OutOfScopeTopics]] — content-filter input case.
- [[PromptInjection]] / [[Jailbreak]] / [[IndirectPromptInjection]] — the attacks input guardrails partially defend against.
- [[UsagePatternMonitoring]] — behavior-over-time complement to single-input filtering.
- [[LlamaGuard]] / [[NeMoGuardrails]] / [[GuardrailsAI]] — production input-guardrail implementations.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 reframes input guardrails around **two risks specific to API-fronted apps**:

### Risk 1: Leaking private information to external APIs

When prompts cross your organization's boundary to a third-party model API, sensitive data can leak in three common ways:

1. An employee pastes secrets / customer data into a prompt.
2. An application developer puts company policies or data into the system prompt.
3. A tool retrieves private information from an internal database and adds it to context.

Ch 10's footnote names the canonical incident: *"a Samsung employee put Samsung's proprietary information into ChatGPT, accidentally leaking the company's secrets."*

Mitigation: automated PII detection plus the **[[PIIReverseDictionary|PII reverse dictionary]]** masking pattern — replace sensitive values with placeholders before egress, restore from a reverse map on the response side.

### Risk 2: Executing bad prompts that compromise the system

The Ch 5 attack-surface lineage: prompt injection, jailbreaks, indirect prompt injection. Input guardrails partially defend; *"while you can mitigate risks, they can never be fully eliminated."*

### Sensitive-data classes Ch 10 enumerates

- **Personal information** — ID numbers, phone numbers, bank accounts.
- **Human faces** — for multimodal inputs.
- **Specific keywords / phrases** — company IP, codenames, privileged information.

### The two policy choices on detection

> *"If a query is found to contain sensitive information, you have two options: block the entire query or remove the sensitive information from it."* — Ch 10

The first kills user workflow; the second (via reverse dictionary) preserves it at the cost of detection-tool quality risk.

### Operational tradeoff

Like all guardrails, input guardrails add latency. Self-hosted models reduce the input-guardrail budget materially because data doesn't leave the org boundary.
