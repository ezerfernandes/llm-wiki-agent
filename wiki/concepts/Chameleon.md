---
title: "Chameleon"
type: concept
tags: [agents, tools, multi-tool, benchmark]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Chameleon

**Chameleon** (Lu et al. 2023) is the canonical **13-tool agent** Huyen cites repeatedly in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] to demonstrate that **tool use can significantly boost a model's performance** beyond what prompting or finetuning alone can deliver.

## The headline result

A [[GPT|GPT-4]]-powered Chameleon agent with 13 tools outperforms GPT-4 alone on:

- **[[ScienceQA]]** (science question-answering): improves the best published few-shot result by **+11.37%**.
- **[[TabMWP]]** (Tabular Math Word Problems; Lu et al. 2022): improves accuracy by **+17%**.

## The 13 tools (named in Ch 6)

Examples Huyen names: knowledge retrieval, a query generator, an image captioner, a text detector, Bing search. The set spans [[KnowledgeAugmentation]] and [[CapabilityExtension]] categories.

## Two empirical observations from Lu et al.

Huyen quotes the paper:

1. **Different tasks require different tools.** [[ScienceQA]] relies much more on knowledge-retrieval tools than [[TabMWP]] (which is tabular-math-heavy).
2. **Different models have different tool preferences.** GPT-4 selects a wider set of tools than ChatGPT. ChatGPT favors image captioning; GPT-4 favors knowledge retrieval.

## The tool-transition contribution

Chameleon also introduces **tool transition** analysis — the conditional probability of using tool Y after tool X. Huyen names this as the basis for **AI-created composite tools**: *"If two tools are frequently used together, they can be combined into a bigger tool. If an agent is aware of this information, the agent itself can combine initial tools to continually build more complex tools."*

## Position relative to [[Toolformer]] and [[Gorilla]]

| Agent | Tools | Method |
|---|---|---|
| [[Toolformer]] (Schick et al. 2023) | 5 | Finetune GPT-J on tool-use traces |
| **Chameleon** (Lu et al. 2023) | 13 | Prompt GPT-4 |
| [[Gorilla]] (Patil et al. 2023) | 1,645 APIs | Retrieve over tool inventory |

Chameleon occupies the **middle**: medium inventory, prompted (not finetuned), benchmarked rigorously.

## Connections

- [[Agent]] / [[ToolInventory]] — what Chameleon is.
- [[Toolformer]] / [[Gorilla]] — peer agents at different inventory scales.
- [[KnowledgeAugmentation]] / [[CapabilityExtension]] — the tool categories Chameleon's 13 tools span.
- [[ScienceQA]] / [[TabMWP]] — Chameleon's benchmarks.
- [[ToolTransition]] — Chameleon's methodological contribution.
- [[PlanningGranularity]] — Chameleon's *program generator* corresponds to Huyen's natural-language-plan-with-translator approach.
- [[ai-engineering-ch06-rag-agents]] — primary source.
