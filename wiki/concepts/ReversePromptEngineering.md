---
title: "Reverse Prompt Engineering"
type: concept
tags: [llm-security, adversarial, safety, reverse-engineering]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Reverse Prompt Engineering

**The practitioner term for [[PromptExtraction|prompt extraction]]** — deducing the system prompt of a deployed application by analyzing its outputs or tricking the model into emitting its instructions. Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]].

> "Reverse prompt engineering is the process of deducing the system prompt used for a certain application. Bad actors can use the leaked system prompt to replicate your application or manipulate it into doing undesirable actions — much like how knowing how a door is locked makes it easier to open." — Ch 5

## Two methods

1. **Analyze application outputs** — examine the model's behavior under varied inputs to infer the system prompt's constraints.
2. **Trick the model into repeating its prompt** — see [[PromptExtraction|prompt extraction]] for the canonical *"Ignore the above..."* pattern.

## Why it's "fashionable"

Ch 5: *"The more secretive companies are about their prompts, the more fashionable reverse prompt engineering becomes."* Some attempts are malicious; many are recreational — people reverse-engineer ChatGPT's system prompt just for fun.

## See [[PromptExtraction]] for the full treatment.

## Connections

- [[PromptExtraction]] — primary page; this is the practitioner-term alias.
- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[SystemPrompt]] — the target.
- [[PromptAttack]] — parent family.
