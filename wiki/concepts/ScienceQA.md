---
title: "ScienceQA"
type: concept
tags: [benchmark, qa, multimodal, science]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# ScienceQA

**ScienceQA** is a multimodal science question-answering benchmark Huyen names in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as the headline benchmark on which the [[Chameleon]] agent (Lu et al. 2023) demonstrates the power of **tool augmentation**: a 13-tool [[GPT|GPT-4]] agent **improves the best published few-shot result by +11.37%** on ScienceQA.

## What it covers

ScienceQA spans grade-school science questions across natural sciences, social sciences, and language sciences, with rich multimodal context (text + images + tables). The benchmark rewards systems that can **integrate retrieved knowledge, parse images, and reason** — which is why it became the canonical multi-tool agent benchmark.

## Why it favors knowledge-augmentation tools

Per Lu et al. (quoted in Ch 6): *"ScienceQA, the science question answering task, relies much more on knowledge retrieval tools than TabMWP, a tabular math problem-solving task."* This is the **tool-task affinity** observation that [[ToolInventory|tool selection]] must respect.

## Position relative to [[TabMWP]]

The two benchmarks together form the empirical backbone of the [[Chameleon]] paper:

| Benchmark | What it tests | Chameleon's gain |
|---|---|---|
| **ScienceQA** | Science QA — favors knowledge retrieval | +11.37% over best few-shot |
| **[[TabMWP]]** | Tabular math word problems — favors math tools | +17% accuracy |

## Connections

- [[Chameleon]] — the agent that scored the +11.37% gain.
- [[TabMWP]] — sibling benchmark.
- [[KnowledgeAugmentation]] — the tool category most relevant to ScienceQA.
- [[QuestionAnswering]] — parent task family.
- [[MultimodalLLM]] — what ScienceQA tests in multimodal settings.
- [[ai-engineering-ch06-rag-agents]] — primary source.
