---
title: "AGIEval"
type: concept
tags: [benchmark, evaluation, microsoft, mcq, human-exam]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# AGIEval

[[microsoft|Microsoft]]'s 2023 **human-exam-derived [[MultipleChoiceQuestion|MCQ]] benchmark** covering subjects from SAT/GRE/Gaokao/bar exams. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "AGIEval's authors explained that they excluded open-ended tasks on purpose to avoid inconsistent assessment."

## Significance

One of the canonical examples of the **MCQ-dominance pattern** in FM evaluation — together with [[mmlu|MMLU]] and [[ARCC]], part of the 75% of [[lm-evaluation-harness]] tasks that are multiple-choice (April 2024).

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[microsoft|Microsoft]] — author.
- [[MultipleChoiceQuestion]] — format.
- [[CloseEndedTask]] — design rationale (close-ended for consistency).
- [[mmlu|MMLU]] / [[ARCC]] — sibling MCQ benchmarks.
