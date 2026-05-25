---
title: "StarCoder2"
type: entity
tags: [model, llm, code-llm, open-weight]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# StarCoder2

A **15-billion-parameter** open-weights LLM focused on **code generation**, described in *"StarCoder 2 and the Stack v2: The Next Generation"* (Lozhkov et al., 2024). Continues the original StarCoder line (*"StarCoder: May the source be with you!"*).

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 uses StarCoder2 as the **canonical example of a code-tokenization-optimized model** in its comparative tokenizer tour.

**Tokenization details:**
- **Method**: [[BPE]] (byte pair encoding).
- **Vocabulary size**: 49,152.
- **[[SpecialToken|Special tokens]]**:
  - `<|endoftext|>` — end of generation.
  - **[[FillInTheMiddle|Fill-in-the-middle]] tokens**: `<fim_prefix>`, `<fim_middle>`, `<fim_suffix>`, `<fim_pad>`.
  - **Repository / file context tokens**: `<filename>`, `<reponame>`, `<gh_stars>` — used to disambiguate cross-file code references during pretraining on multi-file repos. *"One file might make a function call to a function that is defined in a different file. So the model needs some way of being able to identify code that is in different files in the same code repository, while making a distinction between code in different repos."*

**Two distinctive tokenization choices:**

1. **Whitespace-runs as single tokens** — similar to [[GPT4|GPT-4]], runs of consecutive whitespace are encoded as a single token. Important for representing Python-style indentation efficiently.

2. **Per-digit tokenization** — *"A major difference here to everything we've seen so far is that each digit is assigned its own token (so 600 becomes 6 0 0). The hypothesis here is that this would lead to better representation of numbers and mathematics."* Contrast with [[GPT2|GPT-2]], where `870` is one token and `871` is two (`8` + `71`) — an inconsistency that can confuse the model's number representation. Per-digit tokenization buys consistency at the cost of slightly more tokens for numeric content.

## Connections

- [[Galactica]] — sibling specialized model (scientific), also per-digit + whitespace-run tokens.
- [[FillInTheMiddle]] — the training objective StarCoder2's special tokens implement.
- [[GPT4]] — peer code-aware tokenizer (whitespace-run tokens, but not per-digit).
- [[BPE]] — the tokenization method.
- [[HandsOnLLM]] / [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 surveys StarCoder2's tokenizer.
- [[GitHubCopilot]] — a peer code-completion system that uses FIM-style training.
- [[HuggingFace]] — model hub host.
