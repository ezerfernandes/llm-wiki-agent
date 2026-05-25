---
title: "`[SEP]` Token"
type: concept
tags: [nlp, bert, tokenization, special-token]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# `[SEP]` Token

The **separator** [[SpecialToken|special token]] used by [[bert|BERT]] (WordPiece tokenizer, vocab IDs vary by variant). Marks segment boundaries in inputs that contain **two** texts — e.g., question/passage in question-answering, query/document in cross-encoder reranking, premise/hypothesis in [[NaturalLanguageInference|NLI]].

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

> "`[SEP]` stands for separator, as it's used to separate sentences in some applications that require passing two sentences to a model (For example, in Chapter 8, we will use a `[SEP]` token to separate the text of the query and a candidate result.)" — Ch 2

BERT's two-segment input pattern:

```
[CLS] tok_1 ... tok_n [SEP] tok_1' ... tok_m' [SEP]
```

The trailing `[SEP]` marks the end of the second segment. A learned **segment embedding** ($\mathbf{e}_A$ or $\mathbf{e}_B$) is added to every position to identify which sentence it belongs to.

## Connections

- [[SpecialToken]] — parent category.
- [[ClsToken]] / [[ClassificationToken]] — the companion `[CLS]` at the start.
- [[bert]] — the canonical model that uses `[SEP]`.
- [[WordPiece]] — the tokenization scheme `[SEP]` ships with.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — source page.
