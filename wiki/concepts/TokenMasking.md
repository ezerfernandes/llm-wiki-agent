---
title: "Token Masking"
type: concept
tags: [pretraining, mlm, masked-language-modeling, training-objective]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Token Masking

**Token masking** is the default [[MaskedLanguageModel|MLM]] masking strategy: randomly mask **15% of WordPiece tokens** in each sequence, regardless of word boundaries. Subword tokens may be masked independently from the rest of the word they belong to.

Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"With token masking, we randomly mask 15% of the tokens in a sentence. It might happen that part of a word will be masked."*

## Trade-off vs whole-word masking

- **Token masking** (Ch 11's default) — *"faster convergence"*; each masked position is partially predictable from the surrounding subtokens of the same word, making each prediction easier.
- **[[WholeWordMasking|Whole-word masking]]** — when one subtoken of a word is selected, all subtokens of that word are masked. *"Predicting whole words tends to be more complicated than tokens, which makes the model perform better as it needs to learn more accurate and precise representations during training. However, it tends to take a bit more time to converge."*

## Implementation

Provided by [[DataCollatorForLanguageModeling]] with `mlm_probability=0.15`:

```python
from transformers import DataCollatorForLanguageModeling
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)
```

## The 80/10/10 split (inherited from BERT)

Of the 15% masked positions, **80%** become `[MASK]`, **10%** become a random token, **10%** are left unchanged. Mitigates the **pre-train / fine-tune mismatch** caused by `[MASK]` never appearing during fine-tuning. See [[MaskedLanguageModel]] for the full BERT recipe.

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[MaskedLanguageModel]] — the parent training objective.
- [[WholeWordMasking]] — the more-difficult alternative.
- [[DataCollatorForLanguageModeling]] — implementation.
- [[ContinuedPretraining]] — Ch 11's primary use case.
- [[WordPiece]] — the subword tokenizer that makes the distinction matter.
