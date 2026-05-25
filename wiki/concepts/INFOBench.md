---
title: "INFOBench"
type: concept
tags: [benchmark, evaluation, instruction-following]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# INFOBench

A broad **[[InstructionFollowingCapability|instruction-following]] benchmark** by Qin et al. (2024) discussed in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]. Where [[IFEval]] focuses on automatically-verifiable format instructions, INFOBench evaluates:

- **Format** — same as IFEval.
- **Content constraints** — *"discuss only climate change."*
- **Linguistic guidelines** — *"use Victorian English."*
- **Style rules** — *"use a respectful tone."*

## The yes/no decomposition

Many INFOBench criteria can't be automatically verified directly, so authors decompose each instruction into a list of yes/no questions. Example from Ch 4: the instruction *"Make a questionnaire to help hotel guests write hotel reviews"* decomposes into:

1. Is the generated text a questionnaire?
2. Is the generated questionnaire designed for hotel guests?
3. Is the generated questionnaire helpful for hotel guests to write hotel reviews?

## Scoring

Per-instruction score = fraction of yes/no criteria met. Total score = number of criteria met / total number of criteria. Each yes/no can be answered by a human OR an AI judge.

## GPT-4 as evaluator

Per Ch 4:

> "In their experiment, the INFOBench authors found that GPT-4 is a reasonably reliable and cost-effective evaluator. GPT-4 isn't as accurate as human experts, but it's more accurate than annotators recruited through Amazon Mechanical Turk."

This is one of the chapter's stronger data points for **AI judges out-grading [[AmazonMechanicalTurk|Mechanical Turk]] workers**.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[InstructionFollowingCapability]] — parent capability.
- [[IFEval]] — sibling benchmark (narrower format-only scope).
- [[LLMAsAJudge]] — methodology for scoring the yes/no questions.
- [[AmazonMechanicalTurk]] — beaten by GPT-4 on this benchmark.
