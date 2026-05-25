---
title: "SentencePiece"
type: concept
tags: [concept, tokenization, subword]
sources: [1910.10683-t5, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# SentencePiece

A language-agnostic subword tokenizer (Kudo & Richardson, 2018) that operates directly on raw Unicode text, treating whitespace as just another symbol (specifically `▁` U+2581). This contrasts with [[wordpiece]] tokenizers that pre-tokenize on whitespace before applying subword splitting, and makes SentencePiece naturally suitable for languages without explicit word boundaries (Chinese, Japanese, Thai).

Used by [[t5]] in [[1910.10683-t5]]: a 32k WordPiece-style vocabulary trained on a 10:1:1:1 mixture of English / German / French / Romanian C4 — chosen so the single tokenizer covers all three translation targets without requiring language-specific tokenizers.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 uses [[FLANT5|Flan-T5]] as the canonical SentencePiece example in its tokenizer tour. **Vocabulary size: 32,100.** [[SpecialToken|Special tokens]]: `<unk>`, `<pad>`, `</s>`.

Ch 2 notes SentencePiece *"supports BPE and the unigram language model"* (the latter described in Kudo's *"Subword regularization: Improving neural network translation models with multiple subword candidates"*). Two failure modes the chapter observes in Flan-T5's SentencePiece tokenizer:

- **No newline or whitespace tokens** — *"this would make it challenging for the model to work with code."*
- **`<unk>` on emoji + Chinese characters** — *"making the model completely blind to them."*

Despite these failures on Ch 2's contrived test string, SentencePiece's **language-agnostic, no-pre-tokenization** design remains the preferred choice for multilingual models — its whitespace-as-symbol approach (the U+2581 `▁`) avoids the language-specific word-segmentation assumptions that trip up [[WordPiece]].

## See also

- [[1910.10683-t5]] — source paper that uses it.
- [[wordpiece]] — predecessor subword tokenizer used by [[bert]].
- [[t5]] — model that uses this tokenizer.
- [[FLANT5]] — uses SentencePiece via Ch 2's comparative tour.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 deep-dive on tokenization.
