---
title: "CHATS-lab/persuasive_jailbreaker"
type: entity
tags: [entity, tool, llm-security, red-team, jailbreak, open-source]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# CHATS-lab/persuasive_jailbreaker

**`CHATS-lab/persuasive_jailbreaker`** is an **open-source automated jailbreaking toolkit** that uses persuasive-rhetoric attack templates to elicit disallowed behavior from LLMs. Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as one of four automated security-probing tools for LLM applications.

> "Tools that help automate security probing include Azure/PyRIT, leondz/garak, greshake/llm-security, and CHATS-lab/persuasive_jailbreaker." — Ch 5

## What it does

The toolkit applies a taxonomy of **persuasion techniques** (authority appeal, social proof, urgency, reciprocity, etc.) to existing jailbreak prompts, generating variants that often succeed where direct attacks fail. The underlying premise: models trained on human conversational data inherit human susceptibility to persuasive framing.

## Position in the attack-sophistication ladder

In the Ch 5 [[PromptAttack|prompt-attack]] sophistication ladder, persuasive jailbreaking sits between **manual [[Roleplaying|roleplay]] attacks** ([[DANJailbreak|DAN]], [[GrandmaExploit|grandma exploit]]) and **fully automated attacks** like [[PAIR]]. It scales the roleplay/social-engineering approach via templates rather than manual creativity.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[Jailbreak]] / [[PromptAttack]] — the attack class this tool implements.
- [[Roleplaying]] / [[DANJailbreak]] / [[GrandmaExploit]] — manual antecedents to persuasive jailbreaking.
- [[PAIR]] — fully-automated attacker-LLM sibling.
- [[LLMRedTeaming]] — discipline this tool implements.
- [[AzurePyRIT]] / [[GarakLLMScanner]] / [[GreshakeLLMSecurity]] — sibling automated red-team tools.
- [[AttackSuccessRate]] / [[ViolationRate]] — reporting metrics.
