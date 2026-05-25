---
title: "European AI Act"
type: entity
tags: [regulation, eu, ai-governance, policy]
sources: [hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# European AI Act

The European Union's comprehensive AI regulation (Regulation (EU) 2024/1689) — the world's first horizontal AI law, adopted in 2024. Establishes a **risk-based classification** of AI systems (unacceptable risk, high risk, limited risk, minimal risk) and introduces explicit obligations for providers and deployers of **general-purpose AI models** (foundation models / LLMs), including transparency, copyright compliance, and — for models above a compute threshold — systemic-risk evaluations.

Cited in [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]] under "Responsible LLM Development and Usage" as the canonical example of foundation-model-regulating legislation:

> "Due to the enormous impact of LLMs, governments are starting to regulate commercial applications. An example is the European AI Act, which regulates the development and deployment of foundation models including LLMs." — Ch 1 (p. 28)

## Why it matters here

The Act is the first major legal regime that treats **foundation models** as a regulated artifact in their own right — the wiki's [[FoundationModel|foundation-model]] concept page lifts directly onto the Act's "general-purpose AI model" category. Practitioner-facing implications include training-data copyright documentation, model-card-style transparency obligations, and (for the largest models) post-market monitoring.

## Connections

- [[FoundationModel]] — the regulated artifact class.
- [[LargeLanguageModel]] / [[GenerativeModel]] — concrete instances.
- [[Hallucination]] — one of the safety risks the Act's transparency obligations aim to surface.
- [[HandsOnLLM]] / [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1 cites the Act in its responsibility section.
