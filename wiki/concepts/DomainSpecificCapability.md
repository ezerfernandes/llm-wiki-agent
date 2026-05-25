---
title: "Domain-Specific Capability"
type: concept
tags: [evaluation, criteria, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Domain-Specific Capability

The **first bucket** of evaluation criteria in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]'s four-bucket taxonomy: *"a model's domain-specific capabilities are constrained by its configuration (such as model architecture and size) and training data. If a model never saw Latin during its training process, it won't be able to understand Latin."*

## What gets measured

Capabilities a model needs for an application: code generation, code debugging, grade-school math, science knowledge, common sense, reasoning, legal knowledge, tool use, game playing, etc. Each tied to one or more public/private benchmarks.

## How it's measured

Mostly via [[ExactEvaluation|exact evaluation]]:

- **Code**: [[FunctionalCorrectness|functional correctness]] via [[HumanEval]], [[MBPP]], [[Spider]] / [[BIRDSQL]] / [[WikiSQL]] — [[PassAtK|`pass@k`]] over unit tests.
- **Math, science, knowledge, reasoning**: [[MultipleChoiceQuestion|MCQ]] benchmarks ([[mmlu|MMLU]], [[AGIEval]], [[ARCC]], [[GSM8K]]). *"In April 2024, 75% of the tasks in Eleuther's lm-evaluation-harness are multiple-choice."*

## The MCQ limitation

MCQs test *recognition* (can the model identify the correct answer from options?) not *generation* (can the model produce the correct answer?). *"MCQs are best suited for evaluating knowledge … and reasoning … They aren't ideal for evaluating generation capabilities such as summarization, translation, and essay writing."*

## Beyond functional correctness

For code, you might also care about:
- **Efficiency** — runtime, memory ([[BIRDSQL]] compares generated-query runtime to ground-truth runtime).
- **[[CodeReadability|Readability]]** — can a human maintain the code? No exact metric — falls back to [[LLMAsAJudge|AI judges]].

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[GenerationCapability]] / [[InstructionFollowingCapability]] / [[CostAndLatency]] — sibling buckets.
- [[CloseEndedTask]] / [[MultipleChoiceQuestion]] — the dominant evaluation framing.
- [[ExactEvaluation]] / [[FunctionalCorrectness]] / [[PassAtK]] — exact-eval primitives from Ch 3.
- [[mmlu|MMLU]] / [[GSM8K]] / [[ARCC]] / [[AGIEval]] / [[HumanEval]] / [[MBPP]] / [[Spider]] / [[BIRDSQL]] — canonical domain benchmarks.
