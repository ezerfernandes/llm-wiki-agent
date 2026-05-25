---
title: "Twenty Questions Task"
type: concept
tags: [benchmark, task-based-evaluation, conversational-ai, big-bench]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Twenty Questions Task

The **`twenty_questions` task in [[bigbench|BIG-bench]]**, used by [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]] as the canonical [[TaskBasedEvaluation|task-based-evaluation]] example.

## The setup

> "One instance of the model (Alice) chooses a concept, such as apple, car, or computer. Another instance of the model (Bob) asks Alice a series of questions to try to identify this concept. Alice can only answer yes or no. The score is based on whether Bob successfully guesses the concept, and how many questions it takes for Bob to guess it."

Example conversation (from Ch 4 / BIG-bench):

> Bob: Is the concept an animal? — Alice: No.
> Bob: Is the concept a plant? — Alice: Yes.
> Bob: Does it grow in the ocean? — Alice: No.
> Bob: Does it grow in a tree? — Alice: Yes.
> Bob: Is it an apple? [correct]

## Why it's an interesting benchmark

- **Multi-turn** — explicitly tests sustained interaction.
- **Two-model** — one model's outputs are the other's inputs.
- **Compositional score** — success rate × question efficiency.
- **Goal-directed** — Bob has a concrete task; success is binary.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[bigbench]] — parent benchmark suite.
- [[TaskBasedEvaluation]] — methodology this exemplifies.
- [[InstructionFollowingCapability]] — adjacent capability.
