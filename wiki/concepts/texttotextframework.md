---
title: "Text-to-Text Framework"
type: concept
tags: [concept, framework, transfer-learning, prompting]
sources: [1910.10683-t5]
last_updated: 2026-05-10
---

# Text-to-Text Framework

A unified interface for NLP tasks in which **every** task — translation, classification, regression, question answering, summarization — is cast as *string in, string out*. The model is fed an input string (typically prefixed by a task identifier such as `"translate English to German:"` or `"cola sentence:"`) and trained, via maximum likelihood with teacher forcing, to produce an output string. Introduced for [[t5]] in [[1910.10683-t5]].

## What it replaces

Prior transfer-learning approaches in NLP attached task-specific heads to a shared pre-trained encoder:
- **[[bert]]-style classification.** A `[CLS]` token's final hidden state is fed to a task-specific MLP that emits class logits.
- **Span prediction.** Two extra heads predict start/end positions over the input.
- **Translation/summarization.** A separate decoder is trained for generative tasks.

The text-to-text framework collapses all of these into a single loss (cross-entropy over output tokens) and a single decoding procedure (greedy or beam) — at the cost of slightly higher inference cost for classification (the model must emit a multi-token label string).

## Concrete examples (from T5 §2.4)

| Task | Input | Target |
|---|---|---|
| Translation | `"translate English to German: That is good."` | `"Das ist gut."` |
| CoLA | `"cola sentence: The course is jumping well."` | `"not acceptable"` |
| STS-B | `"stsb sentence1: ... sentence2: ..."` | `"3.8"` (regression cast as 21-class via rounded literal string) |
| MNLI | `"mnli premise: I hate pigeons. hypothesis: My feelings toward pigeons are filled with animosity."` | `"entailment"` |
| Summarization | `"summarize: state authorities dispatched emergency crews ..."` | `"six people hospitalized after a storm in attala county."` |

## Why it matters

- **One model, one loss, one decoder for all tasks.** Enables clean ablation across architectures and objectives — the methodological precondition for [[1910.10683-t5]]'s systematic empirical study.
- **No task-specific heads** means classification benefits from the decoder's generative capacity (e.g. predicting target words with semantic content, not arbitrary class indices).
- **Prompts become first-class.** T5's task-prefix prompts ("summarize:", "translate English to German:") are the direct ancestor of GPT-3-style in-context prompting and modern instruction-following LLMs.

## Predecessors

- **Natural Language Decathlon** (McCann et al., 2018) — unifies 10 NLP tasks as question answering, but requires training on all tasks simultaneously.
- **Span extraction** (Keskar et al., 2019) — unifies tasks as span selection by appending output choices to the input.
- **GPT-2 zero-shot** (Radford et al., 2019) — feeds a prefix (`TL;DR:`) to elicit a behavior, but evaluates without fine-tuning.

T5 differs from these by (1) allowing task-specific fine-tuning, (2) using short task prefixes rather than full questions, and (3) supporting generative tasks (translation, summarization) where output choices cannot be enumerated.

## See also

- [[1910.10683-t5]] — source paper.
- [[t5]] — the model family.
- [[c4]] — corpus used to pre-train the framework.
- [[spancorruption]] — pre-training objective compatible with the framework.
