---
title: "Whole-Word Masking"
type: concept
tags: [pretraining, mlm, masked-language-modeling, training-objective]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Whole-Word Masking

**Whole-word masking (WWM)** is an [[MaskedLanguageModel|MLM]] masking variant in which **all subtokens of a word are masked together** when any of its subtokens is selected. The harder, slower-to-converge alternative to [[TokenMasking|token masking]].

Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"To enable masking of the entire word, we could apply whole-word masking. ... Generally, predicting whole words tends to be more complicated than tokens, which makes the model perform better as it needs to learn more accurate and precise representations during training. However, it tends to take a bit more time to converge."*

## Why it's harder

In [[TokenMasking|token masking]], when only one of `Ma + ##arte + ##n` is masked, the model gets the other two subtokens as cheap context — *"the word starts with Ma and ends with n, so probably this is Maarten."* Whole-word masking deletes all three subtokens at once, forcing the model to recover the word from sentence context alone.

## Implementation

Swap `DataCollatorForLanguageModeling` for `DataCollatorForWholeWordMask` in the [[ContinuedPretraining|continued-pretraining]] recipe:

```python
from transformers import DataCollatorForWholeWordMask

data_collator = DataCollatorForWholeWordMask(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)
```

## When to use which

| Use whole-word masking when... | Use token masking when... |
|---|---|
| You have plenty of compute / time | You want fast convergence |
| You want strongest representations | You want a quick domain-adaptation pass |
| Your domain has lots of multi-subword domain-specific terms | You're prototyping |

Ch 11 chooses **token masking** for the worked example to keep training-time short on Colab T4.

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[MaskedLanguageModel]] — the parent training objective.
- [[TokenMasking]] — the easier, faster default.
- [[DataCollatorForLanguageModeling]] / `DataCollatorForWholeWordMask` — implementations.
- [[ContinuedPretraining]] — the typical use case.
