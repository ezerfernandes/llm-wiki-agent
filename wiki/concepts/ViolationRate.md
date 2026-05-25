---
title: "Violation Rate"
type: concept
tags: [metric, llm-security, prompt-attack, safety]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Violation Rate

**The percentage of *successful* prompt attacks out of all attack attempts against an LLM-backed application.** Defined in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as one of the **two paired metrics** for evaluating a system's robustness against [[PromptAttack|prompt attacks]] — the other being [[FalseRefusalRate|false refusal rate]].

> "The violation rate measures the percentage of successful attacks out of all attack attempts." — Ch 5

## Relationship to ASR

Violation rate is the application-deployment-side framing of the same idea as [[AttackSuccessRate|Attack Success Rate (ASR)]] — but Ch 5 deliberately pairs it with [[FalseRefusalRate|false refusal rate]] to make the **safety-versus-usefulness trade-off** explicit.

## Why it can't be optimized alone

> "Imagine a system that refuses all requests — such a system may achieve a violation rate of zero, but it wouldn't be useful to users." — Ch 5

A system that returns `"I cannot help with that"` to every query has a violation rate of 0% and is useless. Both metrics must be tracked jointly; the joint Pareto frontier is what defines a deployable safety posture.

## Implication for borderline requests

Violation-rate optimization pushes the model toward refusing [[BorderlineRequest|borderline requests]] (queries with both safe and unsafe valid responses), inflating false refusal rate. Ch 5 argues the right model-level training target is **safe-helpful responses** — not refusal — for borderline cases.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[FalseRefusalRate]] — paired metric (the trade-off counterpart).
- [[AttackSuccessRate]] — research-side equivalent metric.
- [[PromptAttack]] / [[Jailbreak]] / [[PromptInjection]] — the attacks this measures.
- [[DefensivePromptEngineering]] — parent discipline.
- [[BorderlineRequest]] — the category where violation-rate optimization causes over-refusal.
