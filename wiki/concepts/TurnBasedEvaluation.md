---
title: "Turn-Based Evaluation"
type: concept
tags: [evaluation, methodology, conversational-ai]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Turn-Based Evaluation

Evaluating an AI application **on the quality of each conversation turn**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Turn-based evaluation evaluates the quality of each output."

A "turn" can consist of multiple steps or messages — *"if a system takes multiple steps to generate an output, it's still considered a turn."*

## Position

Sibling to [[TaskBasedEvaluation|task-based evaluation]]. Per Ch 4: *"Given that what users really care about is whether a model can help them accomplish their tasks, task-based evaluation is more important."* But turn-based evaluation remains useful — it provides finer-grained signal and is easier to define boundaries for.

## Worked example

A Python debugging conversation:
- Turn 1: model asks for hardware info (good turn? helpful?).
- Turn 2: model asks for Python version.
- Turn 3: model finally suggests a fix.

Turn-based evaluation scores each turn independently. [[TaskBasedEvaluation|Task-based evaluation]] scores the whole sequence: *"did the chatbot fix the bug, and in how many turns?"*

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[TaskBasedEvaluation]] — sibling, more important but harder.
- [[PerComponentEvaluation]] — sibling at the system-internals level.
- [[EvaluationPipeline]] — parent process.
