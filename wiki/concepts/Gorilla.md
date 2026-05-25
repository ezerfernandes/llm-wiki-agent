---
title: "Gorilla"
type: concept
tags: [agents, tools, api, retrieval]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Gorilla

**Gorilla** (Patil et al. 2023) is the canonical **large-tool-inventory** agent — the paper that attempted to prompt agents to select the right API call among **1,645 APIs**. Cited in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as the large-inventory end of the spectrum, contrasted with [[Toolformer]] (5) and [[Chameleon]] (13).

## Why 1,645 is structurally different

At 1,645 APIs, the **tool descriptions cannot fit in any model's context**. Gorilla's contribution is the recognition that tool selection over a large inventory is itself a **retrieval problem**:

- Index all tool descriptions in a vector database.
- At query time, retrieve the most relevant tools first.
- Only surface those tools to the LM for selection.

This is a [[rag|RAG]] pattern applied to the tool inventory itself — *"RAG over tools"* — and it scales to inventories far larger than 1,645.

## Position relative to function-calling APIs

Most commercial function-calling APIs ([[openai|OpenAI]], [[anthropic|Anthropic]], [[google|Google]]) assume the tool inventory fits in the prompt. Gorilla's RAG-over-tools approach is the structural fix needed when inventory exceeds prompt budget — likely to become standard as agent ecosystems expand.

## Position relative to [[BerkeleyFunctionCallingLeaderboard]]

Gorilla is from the same UC Berkeley group ([[UCBerkeley]]) that built the [[BerkeleyFunctionCallingLeaderboard]] — the leading benchmark for tool-use agent evaluation Huyen cites.

## Connections

- [[Agent]] / [[ToolInventory]] — what Gorilla scales.
- [[Toolformer]] / [[Chameleon]] — peer agents at smaller inventory scales.
- [[rag]] — the retrieval pattern Gorilla applies to tools.
- [[BerkeleyFunctionCallingLeaderboard]] — sibling evaluation harness.
- [[UCBerkeley]] — institutional home.
- [[FunctionCalling]] — the API surface.
- [[ai-engineering-ch06-rag-agents]] — primary source.
