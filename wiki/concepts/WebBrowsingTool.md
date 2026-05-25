---
title: "Web Browsing Tool"
type: concept
tags: [agents, tools, knowledge-augmentation]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Web Browsing Tool

**Web browsing** is the [[KnowledgeAugmentation|knowledge-augmentation]] tool family that gives an agent **internet access** — *"an umbrella term to cover all tools that access the internet, including web browsers and specific APIs such as search APIs, news APIs, GitHub APIs, or social media APIs such as those of X, LinkedIn, and Reddit."* ([[ai-engineering-ch06-rag-agents|Huyen Ch 6]]).

## Why it's the most-anticipated tool

> *"Web browsing was among the earliest and most anticipated capabilities to be incorporated into chatbots like ChatGPT. Web browsing prevents a model from going stale."*

A model's training data has a cutoff. Anything that happened after the cutoff is unreachable from internal knowledge — weather, news, upcoming events, stock prices, flight status. Web browsing is the universal **post-cutoff fallback**.

## The risk

> *"While web browsing allows your agent to reference up-to-date information to generate better responses and reduce hallucinations, it can also open up your agent to the cesspools of the internet. Select your Internet APIs with care."*

This is a euphemism for two concrete attack surfaces:

- **[[IndirectPromptInjection|Indirect prompt injection]]** — pages on the open internet can carry malicious instructions that hijack the agent (see Ch 5).
- **Misinformation amplification** — the agent ingests low-quality sources as ground truth.

Production agents typically restrict to **curated** APIs (search APIs over filtered indexes, allowlisted domains) rather than open-web browsing.

## Connections

- [[KnowledgeAugmentation]] — the tool family this belongs to.
- [[Agent]] / [[ToolInventory]] — parent abstractions.
- [[rag]] — the alternative way to inject up-to-date information.
- [[IndirectPromptInjection]] — the load-bearing security risk.
- [[ai-engineering-ch06-rag-agents]] — primary source.
