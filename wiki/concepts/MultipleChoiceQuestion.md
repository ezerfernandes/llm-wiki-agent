---
title: "Multiple-Choice Question (MCQ)"
type: concept
tags: [evaluation, mcq, classification, benchmark-format]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Multiple-Choice Question (MCQ)

The dominant **[[CloseEndedTask|close-ended]] benchmark format** for foundation models. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]: *"In April 2024, 75% of the tasks in Eleuther's lm-evaluation-harness are multiple-choice."*

## Format

A question paired with 2+ labeled options, exactly one (or sometimes more) of which is correct. Example from MMLU (Ch 4):

> Question: One of the reasons that the government discourages and regulates monopolies is that
> (A) Producer surplus is lost and consumer surplus is gained.
> (B) Monopoly prices ensure productive efficiency but cost society allocative efficiency.
> (C) Monopoly firms do not engage in significant research and development.
> (D) Consumer surplus is lost with higher prices and lower levels of output.
> Label: (D)

## Why it dominates

- Easy to **create** — humans can write MCQs faster than they can grade open-ended outputs.
- Easy to **verify** — string match.
- Easy to **reproduce** — no judge variability.
- Easy to **compare against random baseline** — 4-option MCQ random = 25%.

## The big limitation

MCQs test **recognition**, not **generation**:

> "MCQs test the ability to differentiate good responses from bad responses (classification), which is different from the ability to generate good responses. MCQs are best suited for evaluating knowledge … and reasoning. … They aren't ideal for evaluating generation capabilities such as summarization, translation, and essay writing."

## The fragility limitation

Alzahrani et al. (2024) found MCQ scores can flip with cosmetic prompt changes:
- Adding an extra space between the question and answer.
- Adding an instructional phrase like *"Choices:"*.

This makes [[mmlu|MMLU]]-style benchmarks more prompt-sensitive than they look.

## Canonical MCQ benchmarks

- [[mmlu|MMLU]] (UC Berkeley, 2020) — 57 subjects.
- [[ARCC]] (AI2 Reasoning Challenge, 2018) — grade-school science.
- [[AGIEval]] (Microsoft, 2023) — human-exam-derived.
- [[HellaSwag]] (Zellers et al. 2019) — sentence completion for commonsense.
- [[WinoGrande]] (Sakaguchi et al. 2019) — pronoun resolution.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[CloseEndedTask]] — parent category.
- [[mmlu|MMLU]] / [[AGIEval]] / [[ARCC]] / [[HellaSwag]] / [[WinoGrande]] — canonical MCQ benchmarks.
- [[DomainSpecificCapability]] — the criteria bucket MCQs mostly evaluate.
