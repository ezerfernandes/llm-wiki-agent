---
title: "Instruction-Following Capability"
type: concept
tags: [evaluation, criteria, ai-engineering, instruction-following]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Instruction-Following Capability

The **third bucket** of evaluation criteria in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]'s taxonomy: *"how good is this model at following the instructions you give it? If the model is bad at following instructions, it doesn't matter how good your instructions are, the outputs will be bad."*

## Why it matters

- **Structured outputs.** Classifying as A/B/C but receiving "That's correct" breaks downstream.
- **Format constraints beyond structure.** *"If you ask a model to use only words of at most four characters, the model's outputs don't have to be structured, but they should still follow the instruction"* — Ello's reading-help startup uses this for kid-appropriate vocabulary.
- **InstructGPT lineage.** *"InstructGPT, the predecessor of ChatGPT, was named so because it was finetuned for following instructions."* Powerful models are generally better at this.

## The confounding problem

> "Instruction-following capability isn't straightforward to define or measure, as it can be easily conflated with domain-specific capability or generation capability. … When a model performs poorly, it can either be because the model is bad or the instruction is bad."

Vietnamese lục bát poem example: failure could be (a) doesn't know lục bát or (b) doesn't understand the instruction.

## Benchmarks

Ch 4 names two — both should inspire (not be) your private benchmark:

- **[[IFEval]]** (Zhou et al. 2023, [[google|Google]]) — 25 automatically-verifiable instruction types: keywords, length constraints, paragraph count, JSON format, language, etc.
- **[[INFOBench]]** (Qin et al. 2024) — broader: format + content constraints + linguistic guidelines + style rules; decomposed into yes/no questions answerable by humans or AI judges.

## Curating your own

> "You should curate your own benchmark to evaluate your model's capability to follow your instructions using your own criteria. If you need a model to output YAML, include YAML instructions in your benchmark. If you want a model to not say things like 'As a language model', evaluate the model on this instruction."

## Roleplaying as instruction-following

[[Roleplaying]] — *"asking the model to assume a fictional character or a persona"* — is the **8th most common LMSYS use case** (Zheng et al. 2023). Critical for NPCs, AI companions, writing assistants. Evaluated via [[RoleLLM]] and [[CharacterEval]]. Includes "negative knowledge" checks (Jackie Chan roleplay shouldn't speak Vietnamese if Jackie Chan doesn't).

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[DomainSpecificCapability]] / [[GenerationCapability]] / [[CostAndLatency]] — sibling buckets.
- [[IFEval]] / [[INFOBench]] — public benchmarks.
- [[Roleplaying]] / [[RoleLLM]] / [[CharacterEval]] — the roleplaying sub-area.
- [[StructuredOutputs]] — the most concrete instruction-following requirement.
- [[InstructionTuning]] / [[rlhf|RLHF]] — the training-side counterparts.
