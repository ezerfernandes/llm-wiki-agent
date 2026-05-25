---
title: "Galactica"
type: concept
tags: [model, science-llm, meta]
sources: [2605.06651v2-ai-co-mathematician, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Galactica

[[meta|Meta]]'s **scientific-knowledge** LLM (Taylor et al. 2022, arXiv:2211.09085 — *"Galactica: A Large Language Model for Science"*), trained on scientific papers, reference materials, textbooks, encyclopedias, and knowledge bases. Briefly released as a public demo in November 2022, then withdrawn after public criticism of confidently-wrong scientific output — the model itself remained available via paper / weights.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 surveys Galactica in its comparative tokenizer tour as a **domain-tuned tokenizer**:

> "The Galactica model ... is focused on scientific knowledge and is trained on many scientific papers, reference materials, and knowledge bases. It pays extra attention to tokenization that makes it more sensitive to the nuances of the dataset it's representing." — Ch 2

**Tokenization details:**
- **Method**: [[BPE]] (byte pair encoding).
- **Vocabulary size**: 50,000.
- **Standard [[SpecialToken|special tokens]]**: `<s>`, `<pad>`, `</s>`, `<unk>`.

**Domain-specific special tokens** — the distinctive feature of Galactica's tokenizer:

- **Citations**: `[START_REF]` ... `[END_REF]` wrap citations. Example from the paper: *"Recurrent neural networks, long short-term memory `[START_REF]`Long Short-Term Memory, Hochreiter`[END_REF]`"*. The model is trained to emit these tokens when it should produce a citation, integrating citation generation into the language-modeling objective.
- **Reasoning**: `<work>` — *"an interesting token that the model uses for chain-of-thought reasoning."* A precursor of the structured-reasoning special tokens that later appear in chain-of-thought / reasoning-tuned models.
- Plus special tokens for **mathematics**, **amino acid sequences**, and **DNA sequences** (mentioned by category; not enumerated in Ch 2).

**Code-aware tokenization choices** (similar to [[StarCoder2]]):
- **Whitespace runs as single tokens** — consecutive whitespaces of various lengths each get one token.
- **Per-digit tokenization** — `600` → `6 0 0` (matching StarCoder2's hypothesis about better math representation).
- **Unique: per-tab tokens** — *"it also does that for tabs ... it's the only one that assigns a single token to the string made up of two tabs (`\t\t`)."*

## In the wiki

Previously a stub referenced from [[2605.06651v2-ai-co-mathematician]] (a math/science-LMs related-work mention). Ch 2 of *Hands-On LLMs* upgrades the page to a substantive treatment of Galactica's **tokenization design choices** — the first wiki source to document why a science-focused LLM needs different special tokens than a general-purpose one.

## Connections

- [[meta]] — publishing organization.
- [[BPE]] — the tokenization method.
- [[SpecialToken]] — the umbrella concept for `[START_REF]` / `[END_REF]` / `<work>`.
- [[StarCoder2]] — peer specialized model with similar code-aware tokenization choices (whitespace runs, per-digit).
- [[chainofthought]] — the reasoning paradigm Galactica's `<work>` token preempts.
- [[2605.06651v2-ai-co-mathematician]] — related-work mention.
- [[HandsOnLLM]] / [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 tokenizer survey.
- [[Minerva]] — peer scientific LLM.
