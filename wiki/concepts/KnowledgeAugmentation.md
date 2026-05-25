---
title: "Knowledge Augmentation"
type: concept
tags: [agents, tools, rag, retrieval]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Knowledge Augmentation

**Knowledge augmentation** is the first of [[ChipHuyen|Huyen]]'s three tool categories in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]: tools that **give the agent access to information** it doesn't have in its weights. Sister categories: [[CapabilityExtension]] (tools that compensate for model deficiencies) and [[WriteAction|write actions]] (tools that mutate state).

## Examples

- **Text retriever** — the canonical [[rag|RAG]] retriever.
- **Image retriever** — the [[MultimodalRAG]] counterpart.
- **SQL executor** — for [[RAGOverTabularData|tabular data]].
- **Internal people search**, inventory API, Slack retrieval, email reader — enterprise-internal knowledge.
- **[[WebBrowsingTool|Web browsing]]** — public internet access; *"prevents a model from going stale"* (training cutoff workaround).

## Why this category exists

Per Ch 6: *"I hope that this book, so far, has convinced you of the importance of having the relevant context for a model's response quality. An important category of tools includes those that help augment your agent's knowledge."*

Knowledge augmentation is the **agent-pattern realization** of the [[ContextConstruction]] umbrella Ch 5 introduces: where [[rag|RAG]] is the pre-attached form, knowledge-augmentation tools are the tool-mediated form.

## Position relative to the rest of the chapter

A [[rag|RAG]] system is, in agent terms, *"an agent with a knowledge-augmentation tool inventory of one: the retriever."* This is why Ch 6 treats RAG and agents as a single chapter — RAG is the simplest non-trivial agent.

## Connections

- [[Agent]] / [[ToolInventory]] — what knowledge augmentation is a category within.
- [[CapabilityExtension]] / [[WriteAction]] — sibling tool categories.
- [[rag]] — the canonical knowledge-augmentation application.
- [[ContextConstruction]] — the Ch 5 umbrella.
- [[WebBrowsingTool]] — a specific knowledge-augmentation tool family.
- [[RAGOverTabularData]] / [[TextToSQL]] — the SQL-executor variant.
- [[ai-engineering-ch06-rag-agents]] — primary source.
