---
title: "Azure PyRIT"
type: entity
tags: [entity, tool, llm-security, red-team, microsoft, open-source]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Azure PyRIT

**PyRIT (Python Risk Identification Toolkit)** is [[microsoft|Microsoft]]'s **open-source automated red-teaming toolkit for generative AI**, hosted at `Azure/PyRIT`. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as one of four named tools that help automate security probing for LLMs.

> "Tools that help automate security probing include Azure/PyRIT, leondz/garak, greshake/llm-security, and CHATS-lab/persuasive_jailbreaker. These tools typically have templates of known attacks and automatically test a target model against these attacks." — Ch 5

## What it does

PyRIT maintains a library of known prompt-attack templates and orchestrates running them against target LLM endpoints, scoring outcomes with [[AttackSuccessRate|ASR]] / [[ViolationRate|violation rate]] metrics. It's positioned as the Microsoft-blessed framework for institutionalized [[LLMRedTeaming|LLM red teaming]] — the structural counterpart to the [[microsoft|Microsoft]] LLM red-teaming write-up Ch 5 cites in the same paragraph.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[microsoft|Microsoft]] — parent organization.
- [[LLMRedTeaming]] — discipline this tool implements.
- [[GarakLLMScanner]] / [[GreshakeLLMSecurity]] / [[CHATSPersuasiveJailbreaker]] — sibling automated red-team tools named alongside.
- [[AdvBench]] / [[PromptRobustnessBenchmark]] — benchmarks PyRIT-style tools typically run against.
- [[Jailbreak]] / [[PromptInjection]] / [[PromptAttack]] — the attack families probed.
