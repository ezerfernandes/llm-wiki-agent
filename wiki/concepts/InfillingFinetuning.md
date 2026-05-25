---
title: "Infilling Finetuning"
type: concept
tags: [finetuning, code-models, masked-lm]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Infilling Finetuning

A [[SupervisedFinetuning|supervised finetuning]] variant that trains the model to **fill in blanks** — predict tokens given both **prefix** and **suffix** context, rather than just the prefix. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Similarly, with supervised finetuning, you can also finetune a model to predict the next token or fill in the blank. The latter, also known as infilling finetuning, is especially useful for tasks such as text editing and code debugging. You can finetune a model for infilling even if it was pre-trained autoregressively."

## Use cases (Ch 7)

- **Code debugging**: insert a fix between two existing code regions.
- **Text editing**: rewrite a middle paragraph while preserving the surrounding context.
- **Code completion** in the middle of a function — fill in code given the function signature and the rest of the body.

## How it works (sketch)

Modify the training data format to include both **before-cursor** and **after-cursor** context, with a special token marking where the model should generate. For example, "Fill-in-the-Middle" (FIM) training (Bavarian et al. 2022) splits sequences into three parts (prefix, middle, suffix) and trains the model to predict the middle given prefix + suffix.

## Compatibility

Ch 7 emphasizes: **you can finetune for infilling even if the base model was pre-trained autoregressively**. The infilling capability emerges from the finetuning, not the pre-training architecture.

## Canonical case: [[CodeLlama]]

Ch 7's worked example: the [[CodeLlama|Code Llama]] family (Rozière et al. 2024). Code Llama was finetuned from Llama 2 with multiple finetuning techniques including infilling — making it suitable for in-editor code-completion experiences where the cursor is in the middle of a function body.

## Connections

- [[FineTuning]] — parent operation.
- [[SupervisedFinetuning]] — the broader category.
- [[CodeLlama]] — Ch 7's canonical infilling-finetuned model.
- [[AutoregressiveModel]] — the base architecture infilling FT extends.
- [[ai-engineering-ch07-finetuning]] — primary source.
