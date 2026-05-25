---
title: "Task-Based Evaluation"
type: concept
tags: [evaluation, methodology, conversational-ai]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Task-Based Evaluation

Evaluating an AI application **on whether a complete user task was accomplished**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Task-based evaluation evaluates whether a system completes a task. Did the application help you fix the bug? How many turns did it take to complete the task? It makes a big difference if a system is able to solve a problem in two turns or in twenty turns."

## Why it's the more important metric

> "Given that what users really care about is whether a model can help them accomplish their tasks, task-based evaluation is more important."

## Why it's harder

> "A challenge of task-based evaluation is it can be hard to determine the boundaries between tasks. Imagine a conversation you have with ChatGPT. You might ask multiple questions at the same time. When you send a new query, is this a follow-up to an existing task or a new task?"

Task boundaries are not always observable — they require user-intent inference or session-level user input.

## Worked example: twenty_questions

[[TwentyQuestionsTask|`twenty_questions`]] in [[bigbench|BIG-bench]] is the canonical task-based-evaluation benchmark — one model picks a concept, another asks yes/no questions to guess it. Score: success + number of questions used. Captures the multi-turn task notion directly.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[TurnBasedEvaluation]] — sibling, easier but less important.
- [[PerComponentEvaluation]] — sibling at the system-internals level.
- [[TwentyQuestionsTask]] — canonical benchmark.
- [[EvaluationPipeline]] — parent process.
