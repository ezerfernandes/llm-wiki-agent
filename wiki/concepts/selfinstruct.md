---
title: "Self-Instruct"
type: concept
tags: [dataset-engineering, synthetic-data, instruction-tuning]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Self-Instruct

**Wang et al. 2022's seed-instruction synthesis approach** — generate new (instruction, response) pairs from a small set of human-written seed examples using a base LLM. Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], this is the seed dataset that powered [[AlpacaDataset|Stanford Alpaca]] — 175 seed (instruction, response) examples expanded to **52,000 synthetic examples** via text-davinci-003.

## The recipe

1. Hand-write a small set of high-quality seed (instruction, response) examples (Self-Instruct used 175 covering diverse uses).
2. For each iteration, sample seed examples + already-generated examples.
3. Ask an LLM to generate new (instruction, response) pairs that mirror the style and diversity.
4. Filter out low-quality examples (see heuristics below).
5. Append the filtered survivors to the dataset.
6. Repeat.

## Heuristic filters (Ch 8)

Self-Instruct authors filtered out:

- **Repetitive examples**
- **Instructions too long or too short**
- **Examples with same instruction but different responses**
- **Examples where the output is a repetition of the input**

## Why it mattered

Self-Instruct demonstrated that **a small seed set + a strong base model can produce a usable SFT dataset at low cost** — the foundational result behind every subsequent instruction-synthesis pipeline.

## Descendant datasets

- **[[AlpacaDataset|Alpaca]]** (Taori et al. 2023) — 175 Self-Instruct seeds → 52K examples via text-davinci-003.
- **[[UltraChat]]** (Ding et al. 2023) — extended to multi-turn conversations using ChatGPT topic trees.
- **[[EvolInstruct|Evol-Instruct]]** (WizardLM team) — extends Self-Instruct with depth and breadth evolution.

## Connections

- [[InstructionDataSynthesis]] — parent category.
- [[AIPoweredDataSynthesis]] — parent category.
- [[AlpacaDataset]] — direct descendant.
- [[UltraChat]] / [[EvolInstruct]] — sibling extensions.
- [[InstructDataset]] — the consumer of Self-Instruct-style output.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
