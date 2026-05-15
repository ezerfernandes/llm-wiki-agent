---
title: "SentencePiece"
type: concept
tags: [concept, tokenization, subword]
sources: [1910.10683-t5]
last_updated: 2026-05-10
---

# SentencePiece

A language-agnostic subword tokenizer (Kudo & Richardson, 2018) that operates directly on raw Unicode text, treating whitespace as just another symbol (specifically `▁` U+2581). This contrasts with [[wordpiece]] tokenizers that pre-tokenize on whitespace before applying subword splitting, and makes SentencePiece naturally suitable for languages without explicit word boundaries (Chinese, Japanese, Thai).

Used by [[t5]] in [[1910.10683-t5]]: a 32k WordPiece-style vocabulary trained on a 10:1:1:1 mixture of English / German / French / Romanian C4 — chosen so the single tokenizer covers all three translation targets without requiring language-specific tokenizers.

## See also

- [[1910.10683-t5]] — source paper that uses it.
- [[wordpiece]] — predecessor subword tokenizer used by [[bert]].
- [[t5]] — model that uses this tokenizer.
