---
title: "Prompt-Lookup Decoding"
type: concept
tags: [llm-engineering]
sources: [leh-ch08-inference-optimization]
last_updated: 2026-05-22
---

## Definition
Speculative decoding variant that drafts candidate tokens by matching prompt n-grams.

## In LLM Engineer's Handbook
Tokenizer-free variant of [[SpeculativeDecoding]] where candidate tokens are drawn from n-gram overlaps between prompt and current generation rather than a separate draft model. Particularly effective for input-grounded tasks (summarization, QA, [[rag]]). Enabled in `transformers` via `model.generate(..., prompt_lookup_num_tokens=N)`.
