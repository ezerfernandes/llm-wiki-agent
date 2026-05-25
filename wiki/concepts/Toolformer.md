---
title: "Toolformer"
type: concept
tags: [agents, tools, finetuning]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Toolformer

**Toolformer** (Schick et al. 2023) is one of the earliest demonstrations that a small open-source LM can be **finetuned to use external tools**. Cited in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as the **5-tool** anchor on the inventory-size spectrum — the small end, contrasted with [[Chameleon]] (13) and [[Gorilla]] (1,645).

## What it did

Finetuned **GPT-J** to use 5 tools (the paper's set includes a calculator, calendar, search engine, translation, and Q&A). The contribution was the **self-supervised finetuning recipe**: generate tool-use traces with a seed prompt, filter for ones that improve the model's loss, finetune on the filtered traces.

## Position relative to [[FunctionCalling|function-calling]] APIs

When Toolformer was published (Feb 2023), modern function-calling APIs didn't exist yet. The Toolformer recipe — finetune the model to *emit* tool calls in a special format the runtime can parse — is the conceptual precursor to today's function-calling protocols. The function-calling API surface generalizes Toolformer's idea by standardizing the tool-call format across providers.

## Connections

- [[Agent]] / [[ToolInventory]] — what Toolformer demonstrates.
- [[FunctionCalling]] — the modern API generalization.
- [[Chameleon]] / [[Gorilla]] — peer agents at different inventory scales.
- [[FineTuning]] — Toolformer's training approach.
- [[ai-engineering-ch06-rag-agents]] — primary source.
