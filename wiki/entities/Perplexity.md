---
title: "Perplexity"
type: entity
tags: [product, conversational-search, startup, foundation-model-app]
sources: [ai-engineering-ch01-intro, ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag, hands-on-llm-ch12-fine-tuning-generation-models, agentic-design-patterns-ch17-reasoning]
last_updated: 2026-06-07
---

# Perplexity

Conversational-search product (Perplexity AI). Cited in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] alongside [[ChatGPT]] as a canonical example of a **standalone-web-app AI interface** — contrasted with [[GitHubCopilot]] (plug-in), [[Grammarly]] (browser extension), and [[Midjourney]] (chat-app embedded).

Note: distinct from the [[Perplexity|Perplexity metric]] in language modeling (the wiki's existing `concepts/Perplexity.md` page covers the evaluation metric; this entity page covers the product).

## Connections

- [[AIInterface]] — standalone web-app interface category.
- [[FoundationModelUseCases]] — information aggregation use case.
- [[ChatGPT]] — peer standalone product.
- [[ai-engineering-ch01-intro]] — Ch 1 source.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

Ch 6 cites Perplexity's CEO [[AravindSrinivas|Aravind Srinivas]] for the **load-bearing BM25 quote** that anchors Huyen's framing of term-based retrieval as a *"formidable baseline"*:

> *"Aravind Srinivas, the CEO of Perplexity, tweeted that 'Making a genuine improvement over BM25 or full-text search is hard.'"*

This positions Perplexity as a structurally interesting evidence point: as a **frontier conversational-search company** whose product is RAG-grade retrieval at scale, Perplexity's CEO's BM25 endorsement carries weight as engineering-from-the-trenches commentary — not classical-IR-researcher commentary. This is why Huyen footnotes the tweet in Ch 6 instead of relying on academic citations alone.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 cites Perplexity as one of three canonical **[[GenerativeSearch|generative search]]** product examples:

> *"More search engines are incorporating an LLM to summarize results or answer questions submitted to the search engine. Examples include Perplexity, Microsoft Bing AI, and Google Gemini."* — Ch 8

This positions Perplexity as **the standalone-startup representative** of the three-product generative-search category (vs Microsoft Bing AI's traditional-search-plus-overlay model and Gemini's search-engine-plus-AI-chat model). Perplexity was also one of the **four commercial systems** evaluated in the [[NelsonFLiu|Liu]] / Zhang / [[PercyLiang|Liang]] 2023 verifiability paper Ch 8 cites — alongside Bing Chat, NeevaAI, and YouChat — which is the source of the *"only 51.5% of generated sentences are fully supported by citations"* benchmark.

## Note on Hands-On LLMs Ch 12 disambiguation

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] of *Hands-On LLMs* references `[[Perplexity]]` in the context of **the language-modeling evaluation metric** (Jelinek et al. 1977), **not** the company. The metric coverage lives on the [[Perplexity|concepts/Perplexity.md]] page, which records the Ch 12 use. This entity page (the company / product) is preserved unchanged for that purpose; Ch 12 does not add new content about the company.

## From [[agentic-design-patterns-ch17-reasoning|Agentic Design Patterns Ch 17]]

[[AntonioGulli|Gulli]]'s Reasoning Techniques chapter names **Perplexity AI** as one of the major platforms in the [[DeepResearch|Deep Research]] space — *"AI Agentic tools designed to act as tireless, methodical research assistants"* — alongside [[gemini|Google Gemini]]'s research capabilities and [[openai|OpenAI]]'s advanced ChatGPT functions. This extends Perplexity's earlier wiki framing (conversational/generative search) to the **agentic deep-research** category: given a complex query and a few-minute "time budget," the tool autonomously explores, reasons, refines, and synthesizes a detailed report. See [[DeepResearch]] and [[ReasoningTechniques]].
