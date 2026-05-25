---
title: "Chao et al. 2023 — PAIR"
type: entity
tags: [paper, jailbreak, automated-attack, safety]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Chao et al. 2023 — PAIR

The paper introducing **[[PAIR|Prompt Automatic Iterative Refinement]]** — a [[Jailbreak|jailbreak]] method in which an **attacker LLM** iteratively refines its prompts against a target LLM. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the canonical AI-powered automated prompt-attack technique.

## The headline result

> "In their experiment, PAIR often requires fewer than twenty queries to produce a jailbreak." — Ch 5

20 queries is the data point that mattered: it transforms jailbreaking from a *manual prompt engineering* problem into an *automated search* problem. Attackers running PAIR can mass-produce jailbreaks at low cost.

## Algorithm

1. The attacker LLM generates a prompt aimed at eliciting a specific objectionable behavior.
2. The prompt is sent to the target LLM.
3. The attacker LLM observes the response and refines the prompt.
4. Repeat until success (or budget exhausted).

## Position

PAIR is the bridge between manual jailbreaks ([[DANJailbreak]], [[GrandmaExploit]]) and the modern DSPy-optimizer-based jailbreak research ([[2603.19247-prompt-optimization-jailbreaking|Shamsi et al. 2026]]) — both formalize the idea that *"AI optimizes attack prompts against an AI target."*

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PAIR]] — the concept.
- [[Jailbreak]] / [[PromptAttack]] — attack classes.
- [[AdversarialPromptSearch]] — broader category.
- [[2603.19247-prompt-optimization-jailbreaking]] — DSPy-optimizer successor work.
