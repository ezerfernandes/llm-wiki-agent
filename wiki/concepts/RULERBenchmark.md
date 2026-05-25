---
title: "RULER Benchmark"
type: concept
tags: [benchmark, long-context, evaluation, llm]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# RULER Benchmark

**Long-context evaluation benchmark (Hsieh et al. 2024) that extends [[NeedleInAHaystack|NIAH]] with multiple task variants for testing how well a model processes long prompts.** Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] alongside NIAH as the practitioner tool for confirming whether a model's *advertised* context length is also a *usable* context length.

## Position in the long-context evaluation stack

| Test | Scope | Cost |
|---|---|---|
| [[NeedleInAHaystack\|NIAH]] | Single fact retrieval at varied positions | Cheap |
| **RULER** | Multiple task variants (retrieval, multi-hop, aggregation, etc.) | Medium |

The Ch 5 advice — *"if the model's performance grows increasingly worse with a longer context, then perhaps you should find a way to shorten your prompts"* — applies to either test, but RULER produces more decision-relevant signal because it covers retrieval *plus* reasoning over long context.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[NeedleInAHaystack]] — predecessor test.
- [[MiddleContextDegradation]] — the phenomenon both benchmarks surface.
- [[ContextLength]] — substrate.
- [[PromptEngineering]] — informs prompt-construction decisions for long contexts.
