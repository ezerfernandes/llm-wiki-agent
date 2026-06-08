---
title: "Content Moderation"
type: concept
tags: [cs324, llm, safety, guardrails, agentic-design-patterns]
sources: [cs324-harms-2, agentic-design-patterns-ch18-guardrails]
last_updated: 2026-06-07
---

Content moderation is the dual-use detection and governance of harmful online content. LLM-based classifiers can assist moderation at scale, though the same generative capabilities can also produce the harmful content being moderated.

## As a guardrail layer (Agentic Design Patterns Ch 18)
[[AntonioGulli|Gulli's]] [[AgenticDesignPatterns|*Agentic Design Patterns*]] [[agentic-design-patterns-ch18-guardrails|Ch 18 (Guardrails/Safety Patterns)]] names **External Moderation APIs** as one of the six stages of the [[Guardrail|guardrails]] pattern, and **Social Media Content Moderation** as a flagship use case (auto-identify and flag hate speech, misinformation, graphic content). Its [[crewai|CrewAI]] example *"includes utilizing content moderation APIs to detect inappropriate prompts."* For ambiguous/borderline cases, Gulli pairs moderation with confidence-gated [[HumanInTheLoop|human-in-the-loop]] escalation. Off-the-shelf moderation tools the wiki catalogs: [[OpenAIModeration|OpenAI Moderation]], [[PerspectiveAPI|Perspective API]], [[LlamaGuard|Llama Guard]]. See [[Guardrail]] / [[safety|Safety]].

## Connections
- [[Toxicity]] — a primary category of moderated content
- [[Guardrail]] / [[safety]] — moderation as a guardrail/safety layer in agentic systems
- [[OpenAIModeration]] / [[PerspectiveAPI]] / [[LlamaGuard]] — moderation/safety classifier tools
- [[cs324-harms-2]] — discussed in this CS324 lecture
- [[agentic-design-patterns-ch18-guardrails]] — Gulli's guardrails chapter
