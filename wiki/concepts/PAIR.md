---
title: "PAIR — Prompt Automatic Iterative Refinement"
type: concept
tags: [llm-security, adversarial, jailbreak, automated-attack]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# PAIR — Prompt Automatic Iterative Refinement

**An algorithmic [[Jailbreak|jailbreak]] method that uses an AI model as an *attacker* against a target AI.** Introduced by [[ChaoEtAl2023|Chao et al. 2023]] and cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the canonical example of an AI-powered automated prompt attack.

## How it works

PAIR runs an attacker LLM in a three-step loop:

1. **Generate a prompt** intended to elicit a target objectionable behavior from the victim model.
2. **Send the prompt** to the target AI.
3. **Based on the response, revise the prompt** until the objective is achieved.

The attacker LLM is given an objective like *"elicit instructions for making a Molotov cocktail"* and the rest is closed-loop optimization.

## The headline result

> "In their experiment, PAIR often requires fewer than twenty queries to produce a jailbreak." — Ch 5

This is the data point that makes PAIR notable. Twenty queries is **cheap** — a determined attacker can run thousands of PAIR sessions per day per dollar. The economics of defending against PAIR-style attacks therefore shift: it's no longer enough to defeat a single human attempt; the defender must defeat an automated search.

## Position in the attack ladder

Ch 5 places PAIR midway up the sophistication ladder:

| Tier | Examples |
|---|---|
| **Manual** | Direct prompt hacking (obfuscation, output-format manipulation, roleplaying — [[DANJailbreak|DAN]], [[GrandmaExploit|grandma exploit]]) |
| **Automated** | [[ZouEtAl2023]] adversarial-suffix search; **PAIR** ([[ChaoEtAl2023]]); brainstorm-new-attacks-given-existing-attacks (X user @haus_cole) |
| **Indirect** | [[IndirectPromptInjection]] |

## Relationship to DSPy-based jailbreak research

The PAIR attacker-LLM pattern is conceptually the predecessor to [[2603.19247-prompt-optimization-jailbreaking|Shamsi et al. 2026]]'s DSPy-optimizer approach to jailbreak generation — both are "AI optimizes attack prompts against an AI target." The 2026 work formalizes the reward signal ([[DangerScore|continuous danger score]] from an LLM judge) and replaces hand-tuned attacker logic with general-purpose DSPy optimizers ([[MIPROv2]], [[GEPA]], [[SIMBA]]).

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[ChaoEtAl2023]] — the paper.
- [[Jailbreak]] — parent attack family.
- [[PromptAttack]] — umbrella.
- [[AdversarialPromptSearch]] — broader automated-attack family.
- [[ZouEtAl2023]] — sibling automated-attack technique (substring substitution).
- [[2603.19247-prompt-optimization-jailbreaking]] — DSPy-optimizer-based successor work.
- [[AttackSuccessRate]] — metric for evaluating PAIR's effectiveness.
