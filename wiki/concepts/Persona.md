---
title: "Persona (Prompting Technique)"
type: concept
tags: [prompt-engineering, llm, roleplaying]
sources: [ai-engineering-ch05-prompt-engineering, hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Persona (Prompting Technique)

**Telling the model who to be in order to shape what it produces.** One of the six core prompt-engineering best practices in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]].

> "A persona can help the model to understand the perspective it's supposed to use to generate responses." — Ch 5

## Ch 5's worked example

Given the essay *"I like chickens. Chickens are fluffy and they give tasty eggs."*:

| Prompt | Model's score |
|---|---|
| Score this essay 1–5 | **2/5** |
| You are a first-grade teacher. Score this essay 1–5 | **4/5** |

The persona changes the *frame* (whose perspective and what standards) without changing the rubric (1–5).

## Why it works (proposed mechanisms)

Two non-mutually-exclusive hypotheses:

1. **Latent program activation** (per François Chollet's metaphor — see [[InContextLearning]]). The persona string activates a different region of the model's latent program-space.
2. **Bayesian-style prior shift.** The model's response distribution is conditioned on the persona token sequence — *"first-grade teacher"* shifts the prior toward charitable interpretation of beginner writing.

## Where it lives

Conventionally in the [[SystemPrompt|system prompt]]:

```
System: You are an experienced real estate agent. Your job is to read each
        disclosure carefully...
```

Anthropic explicitly recommends this — *"when assigning Claude a specific role or personality through a system prompt, it can maintain that character more effectively throughout the conversation"* (quoted in Ch 5).

## The dual-use problem

Persona prompting has both a **constructive** and an **adversarial** use:

| Use | Examples |
|---|---|
| **Constructive** (Ch 5 best practice) | "You are an expert Python developer", "Act like a first-grade teacher" |
| **Adversarial** ([[Jailbreak\|jailbreaking]]) | [[DANJailbreak\|DAN]] ("Do Anything Now"), the [[GrandmaExploit\|grandma exploit]], NSA-agent-with-secret-code |

Adversarial personas are the **most versatile** family of manual jailbreaks per Ch 5. The same mechanism that lets a productive persona shift the response distribution lets a malicious persona shift it past the safety boundary.

## Relation to [[Roleplaying]]

Persona prompting is a special case of [[Roleplaying|roleplaying]] focused on **shaping output quality** rather than **building a product around a character**. Ch 4's [[Roleplaying|Roleplaying]] page treats the product-side; Ch 5's persona discussion treats the technique-side.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[Roleplaying]] — the broader category Ch 4 develops.
- [[SystemPrompt]] — where personas usually live.
- [[PromptEngineering]] — parent discipline.
- [[Jailbreak]] / [[DANJailbreak]] / [[GrandmaExploit]] — adversarial-use of the same mechanism.
- [[InContextLearning]] — Chollet's "library of programs" framing.
- [[personadrivensynthesis]] — Ge et al. 2024 framework for persona-driven *data* synthesis (different scope but related).

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 names persona as the **first of seven modular prompt components** ([[Persona|persona]] / [[InstructionPrompt|instruction]] / [[ContextPrompt|context]] / [[OutputFormat|format]] / [[AudiencePrompt|audience]] / [[TonePrompt|tone]] / data):

> *"Persona — Describe what role the LLM should take on. For example, use 'You are an expert in astrophysics' if you want to ask a question about astrophysics."* — Ch 6

The Ch 6 framing is **structural** rather than best-practice-list: persona is one Lego block among seven that can be added, removed, and reordered when iterating a prompt. Ch 6's paper-summary worked example uses:

```python
persona = "You are an expert in Large Language models. You excel at breaking down complex papers into digestible summaries.\n"
```

The seven-component framework is **a finer decomposition** of Huyen Ch 5's three-part [[PromptStructure|prompt anatomy]] — persona + instruction + context + format + audience + tone all subdivide the *task description* half. Both framings are complementary, not contradictions.
