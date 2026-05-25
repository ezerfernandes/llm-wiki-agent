---
title: "Output Guardrail"
type: concept
tags: [llm-security, defense, guardrail, pii, toxicity]
sources: [ai-engineering-ch05-prompt-engineering, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Output Guardrail

**An application-layer filter that inspects model outputs *before* they reach the user, blocking or rewriting harmful content.** Paired with [[InputGuardrail|input guardrails]] in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] to form a defense-in-depth around the model.

## Why output filtering is non-optional

> "Inputs that appear harmless can produce harmful outputs, so it's important to have output guardrails, as well." — Ch 5

Even with strong [[InputGuardrail|input guardrails]], the model can:

- Produce **[[Hallucination|hallucinated]]** PII that wasn't in the input.
- Produce toxic or biased content from benign prompts.
- Leak training-data fragments via [[DivergenceAttack|divergence attacks]] the input filter doesn't recognize.
- Comply with [[IndirectPromptInjection|indirect prompt injection]] payloads embedded in tool outputs (which never passed through the user-input filter).

## Typical checks

Ch 5 names two canonical output checks:

- **PII detection** — block outputs containing names, emails, phone numbers, addresses.
- **Toxicity detection** — block outputs flagged by a [[safety|safety]] classifier.

Detailed treatment of guardrail implementations is deferred to Ch 10 of the book.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[InputGuardrail]] — paired application-layer filter.
- [[Guardrail]] — parent concept; the broader defensive infrastructure.
- [[Hallucination]] — failure mode output guardrails partially catch.
- [[safety]] — broader umbrella for toxicity / bias filtering.
- [[LlamaGuard]] / [[GuardrailsAI]] / [[NeMoGuardrails]] — production output-guardrail implementations.
- [[IndirectPromptInjection]] / [[DivergenceAttack]] — attacks where output-side filtering is the last line of defense.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 expands the Ch 5 sketch with two failure-mode taxonomies and a hard limit:

### Failure modes Ch 10 enumerates

- **Quality failures**: malformatted responses (invalid JSON), factually inconsistent / hallucinated content, generally bad responses.
- **Security failures**: toxicity, leaked PII, responses triggering remote tool/code execution, brand-risk content mischaracterizing the company or competitors.

### The stream-completion blind spot

> *"Output guardrails might not work well in the stream completion mode. … In the stream completion mode, new tokens are streamed to the user as they are generated, reducing the time the user has to wait to see the response. The downside is that it's hard to evaluate partial responses, so unsafe responses might be streamed to users before the system guardrails can determine that they should be blocked."* — Ch 10

A genuine limit of output guardrails: post-hoc evaluation requires having the full output, which streaming UIs do not provide. Mitigations include chunk-level scoring, optimistic streaming with redaction UIs, or accepting non-streamed responses for high-stakes flows.

### Failure-handling policies

Output guardrails also need a *policy* for what to do when they fire:

- **Retry** — fast and cheap when failures are stochastic (empty response, malformatted JSON); doubles latency in the worst case.
- **Parallel calls** — send the same query twice; pick the better. Higher cost, bounded latency.
- **Human fallback** — escalate to a human on sentiment-detected anger, on stuck-loop signals, or on sentinel phrases.

### [[FalseRefusalRate|False refusal rate]] tracking

Per Ch 5 (reiterated in Ch 10): *"For security measurements, it's important to track not only the security failures but also the false refusal rate. It's possible to have systems that are too secure, e.g., one that blocks even legitimate requests, interrupting user workloads and causing user frustration."* Output guardrails are a major source of false refusals.

### The [[PIIReverseDictionary|PII reverse dictionary]] pattern

Ch 10 names the canonical egress/ingress PII handling: mask values like phone numbers with placeholders (`[PHONE NUMBER]`) before sending to a third-party API, and use a reverse map to restore them in the response.
