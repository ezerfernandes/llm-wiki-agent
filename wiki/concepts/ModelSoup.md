---
title: "Model Soup"
type: concept
tags: [model-merging, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Model Soup

A simple [[ModelMerging|model-merging]] approach: **average the weights of multiple finetuned models** (often the same model finetuned with different hyperparameters or random seeds) into a single merged model. Introduced by [[Wortsman2022ModelSoups|Wortsman et al. (2022)]] — *"Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time."*

Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Model soups (Wortsman et al., 2022) showed how averaging the entire weights of multiple finetuned models can improve accuracy without increasing inference time."

## The "soup" recipe

1. Finetune the same base model multiple times with different hyperparameters / random seeds / data orderings.
2. Average the final weights — typically uniformly, sometimes weighted by validation performance ("greedy soup").
3. Serve the averaged model.

## Why it works

- **Loss-landscape geometry**: finetunes of the same base from the same starting point often end up in **the same loss basin**. Averaging within a basin yields a model close to the basin minimum.
- **Reduces variance** across random seeds — the soup is more stable than any individual finetune.
- **No retraining cost** beyond the original finetunes.

## When it doesn't work

- **Cross-basin averaging** — if finetunes land in *different* loss basins, averaging can produce a model worse than either constituent. This is why soups work best when all finetunes share the same base and don't diverge too far.

## Connection to broader model merging

Model soups are the simplest possible application of [[LinearCombinationMerging|linear combination merging]] — they don't even use [[TaskVector|task vectors]] (they merge raw weights directly because all soups share a single task).

## Connections

- [[ModelMerging]] — parent operation.
- [[LinearCombinationMerging]] — the underlying primitive.
- [[Wortsman2022ModelSoups]] — the paper.
- [[FineTuning]] — the operation whose outputs soups combine.
- [[ai-engineering-ch07-finetuning]] — primary source.
