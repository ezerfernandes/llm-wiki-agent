---
title: "garak"
type: entity
tags: [entity, tool, llm-security, red-team, open-source]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# garak

**garak** (`leondz/garak`) is an **open-source LLM vulnerability scanner**, named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as one of four automated security-probing tools for LLM applications.

> "Tools that help automate security probing include Azure/PyRIT, leondz/garak, greshake/llm-security, and CHATS-lab/persuasive_jailbreaker." — Ch 5

## What it does

garak runs a target LLM against a battery of probes covering [[Jailbreak|jailbreaks]], [[PromptInjection|prompt injections]], [[TrainingDataExtraction|training-data leakage]], [[Hallucination|hallucination]], toxicity, and other security-relevant failure modes. Often described as "nmap for LLMs" — a structured scanner that fingerprints vulnerabilities and outputs a report.

## Role in the defense ecosystem

garak is part of the **automated red-teaming layer** of [[DefensivePromptEngineering|defensive prompt engineering]]. It sits alongside [[AzurePyRIT|PyRIT]] as a tool a defender runs *before* deployment and *continuously* during operation to catch new vulnerabilities introduced by model or prompt updates.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[LLMRedTeaming]] — discipline this tool implements.
- [[AzurePyRIT]] / [[GreshakeLLMSecurity]] / [[CHATSPersuasiveJailbreaker]] — sibling automated red-team tools named alongside.
- [[Jailbreak]] / [[PromptInjection]] / [[PromptAttack]] / [[TrainingDataExtraction]] — the attack families probed.
- [[AdvBench]] / [[PromptRobustnessBenchmark]] — benchmarks garak-style tools draw probes from.
