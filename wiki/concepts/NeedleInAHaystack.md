---
title: "Needle in a Haystack (NIAH)"
type: concept
tags: [evaluation, long-context, llm, benchmark]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Needle in a Haystack (NIAH)

**A long-context evaluation test in which a small piece of information (the "needle") is inserted at different positions in a long prompt (the "haystack") and the model is asked to retrieve it.** Introduced by Liu et al. (2023) and used in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] to demonstrate the [[MiddleContextDegradation|"lost in the middle"]] phenomenon.

> "Research has shown that a model is much better at understanding instructions given at the beginning and the end of a prompt than in the middle (Liu et al., 2023). One way to evaluate the effectiveness of different parts of a prompt is to use a test commonly known as the needle in a haystack (NIAH)." — Ch 5

## The headline finding

Across all models tested by Liu et al., retrieval accuracy is **U-shaped** across prompt positions: high at the start, high at the end, low in the middle. This contradicts the naive expectation that long-context models give *uniform* attention to all tokens within their context length.

## Practitioner adaptations

Ch 5 names two extensions:

1. **Use real, private data** instead of randomly generated strings. A doctor-visit transcript with a real drug name embedded is a more realistic NIAH variant. [[ShreyaShankar]] published a practitioner-NIAH writeup for doctor visits in 2024. **The data must be private** — otherwise the model can answer from its pretraining memorization rather than from the haystack context, defeating the test.
2. **[[RULERBenchmark|RULER]]** (Hsieh et al. 2024) — a more comprehensive long-context benchmark that subsumes NIAH and adds variation tests.

## Operational use

If your application's NIAH score degrades sharply past a certain context length, **shorten your prompts** — through summarization, retrieval, or [[PromptDecomposition|prompt decomposition]] — rather than relying on the model's nominal context-length number. The advertised 1M-token context window is not the same as a *usable* 1M-token context window.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[MiddleContextDegradation]] — the phenomenon NIAH measures.
- [[ContextLength]] — the substrate.
- [[RULERBenchmark]] — successor benchmark.
- [[PromptEngineering]] — parent discipline; informs prompt-positioning decisions.
- [[ShreyaShankar]] — author of the doctor-visit NIAH writeup.
