---
title: "Code Back-Translation"
type: concept
tags: [dataset-engineering, synthetic-data, code, llama]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Code Back-Translation

**A [[Backtranslation|back-translation]] variant applied to code: generate explanation/documentation from code → regenerate code from the explanation → verify faithfulness to the original.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], this was one of three AI-data-synthesis techniques used to train [[Llama|Llama 3]].

## The pipeline

1. Start with a code snippet.
2. Use AI to generate an explanation + documentation for the code.
3. Use AI to **regenerate code** from the explanation + documentation.
4. Compare the regenerated code with the original.
5. **Only if the regenerated code is faithful to the original** is the explanation + documentation used as finetuning data.

## Why it works

The explanation + documentation pass forces the AI to compress the code into natural language. If the compression is faithful, AI can rebuild the original code from it; if not, the regenerated code diverges. This gives a **functional-correctness signal** on the synthetic data.

## Llama 3 context

Per Dubey et al. (2024), back-translation was one of three synthesis methods used to generate **2.7 million synthetic coding examples** for Llama 3.1 SFT. The three methods combined:

1. **Code generation** — AI generates programming problem descriptions and solutions.
2. **Code translation** — AI translates code across programming languages.
3. **Code back-translation** — AI generates explanations and documentation, then verifies via regeneration.

## Why verification is the hottest topic in synthetic data

Per Ch 8: "Most of the synthetic data used to train Llama 3 is coding-related" — because coding is **functionally verifiable**. Code back-translation is the verification scheme for the documentation-and-explanation side of code data.

## Connections

- [[Backtranslation]] — parent technique.
- [[AIPoweredDataSynthesis]] — parent category.
- [[Llama|Llama 3]] — the canonical case study.
- [[FactualConsistency]] — the more general consistency-check paradigm.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
