---
title: "RoleLLM"
type: concept
tags: [benchmark, evaluation, roleplaying, instruction-following]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# RoleLLM

A **[[Roleplaying|roleplaying]] benchmark** by Wang et al. (2023) — *"evaluates a model's ability to emulate a persona using both carefully crafted similarity scores (how similar the generated outputs are to the expected outputs) and AI judges."* Discussed in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]].

## The AI-judge prompt

Ch 4 quotes the beginning of RoleLLM's AI-judge prompt to give a sense of what scoring roleplay looks like:

> System Instruction: You are a role-playing performance comparison assistant. You should rank the models based on the role characteristics and text quality of their responses.
>
> User Prompt: The models below are to play the role of "{role_name}". The role description of "{role_name}" is "{role_description_and_catchphrases}". I need to rank the following models based on the two criteria below:
> 1. Which one has more pronounced role speaking style, and speaks more in line with the role description. The more distinctive the speaking style, the better.
> 2. Which one's output contains more knowledge and memories related to the role; the richer, the better.

## Position

Sibling to [[CharacterEval]] (which uses human annotators + a reward model + 5-point scale instead of similarity + AI judges).

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Roleplaying]] — what it measures.
- [[CharacterEval]] — sibling roleplay benchmark.
- [[LLMAsAJudge]] — methodology used.
- [[InstructionFollowingCapability]] — parent capability.
