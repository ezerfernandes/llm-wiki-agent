---
title: "Roleplaying"
type: concept
tags: [evaluation, instruction-following, roleplaying, characters, npc]
sources: [ai-engineering-ch04-evaluate-ai-systems, ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Roleplaying

**Asking the model to assume a fictional character or persona.** One of the most common types of real-world LM instructions per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]] — the **8th most common use case** in LMSYS's million-conversation analysis (Zheng et al. 2023).

## Two purposes

1. **Roleplay-as-product** — character interactions for users, usually entertainment (games, interactive storytelling, AI companions).
2. **Roleplay-as-prompt-technique** — assigning a persona to improve output quality (e.g. *"You are an expert Python developer"*). Covered in Ch 5.

## Why it matters in production

> "Roleplaying is especially important for AI-powered NPCs (non-playable characters) in gaming, AI companions, and writing assistants."

[[Convai]] is the canonical example — 3D NPCs whose entire product surface is roleplay.

## Evaluation

Roleplaying is hard to automate. Two benchmarks Ch 4 names:

- **[[RoleLLM]]** (Wang et al. 2023) — similarity scores + AI judges. Has a multi-step ranking-AI-judge prompt: rank models on (1) style adherence and (2) role-specific knowledge.
- **[[CharacterEval]]** (Tu et al. 2024) — human annotators + a reward model on a 5-point scale.

For simple cases, heuristics work — a quiet character's outputs should be short on average.

## The "negative knowledge" problem

A roleplay model should not say things the character doesn't know. Ch 4's footnote example:

> "If Jackie Chan doesn't speak Vietnamese, you should check that the roleplaying model doesn't speak Vietnamese. The 'negative knowledge' check is very important for gaming. You don't want an NPC to accidentally give players spoilers."

This is a [[GuardRail|guardrail]] problem in disguise.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[InstructionFollowingCapability]] — parent capability.
- [[RoleLLM]] / [[CharacterEval]] — public benchmarks.
- [[Convai]] / [[Inworld]] — canonical NPC-product surfaces.
- [[PromptEngineering]] — the alternative use of roleplay (persona = prompt technique).
- [[Guardrail]] — what enforces "negative knowledge."

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Ch 5 introduces the **dual-use nature** of roleplaying explicitly. Where Ch 4 framed roleplaying as a [[GenerationCapability|generation capability]] for products (NPCs, AI companions), Ch 5 reframes it as **both** a prompt technique *and* a jailbreak vector:

**Constructive use** — the [[Persona|persona]] prompt-engineering technique. Ch 5: *"A persona can help the model to understand the perspective it's supposed to use to generate responses."* The first-grade-teacher essay-scoring example: shifting the persona shifts the scoring lens.

**Adversarial use** — roleplay as the **most versatile** family of manual [[Jailbreak|jailbreaks]]. Ch 5: *"The third approach, which is versatile, is roleplaying. Attackers ask the model to pretend to play a role or act out a scenario."* Named exemplars:
- [[DANJailbreak|DAN]] — *"Do Anything Now"* (Reddit 2022).
- [[GrandmaExploit|Grandma exploit]] — loving grandma tells bedtime stories about dangerous topics.
- NSA-agent-with-secret-code.
- Simulation-without-restrictions.
- *Filter Improvement Mode* with restrictions off.

This dual-use means [[Roleplaying]] sits at the intersection of [[GenerationCapability|generation capability]] (Ch 4), [[PromptEngineering|prompt engineering]] (Ch 5 constructive), and [[Jailbreak|jailbreaking]] (Ch 5 adversarial) — the same mechanism powers all three.
