---
title: "False Refusal Rate"
type: concept
tags: [metric, llm-security, prompt-attack, safety, helpfulness]
sources: [ai-engineering-ch05-prompt-engineering, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# False Refusal Rate

**How often a model refuses a query when it is possible to answer safely.** Defined in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the **paired counterpart of [[ViolationRate|violation rate]]** for evaluating a system's robustness against prompt attacks.

> "The false refusal rate measures how often a model refuses a query when it's possible to answer safely. Both metrics are necessary to ensure a system is secure without being overly cautious." — Ch 5

## Why pair it with violation rate

A system can drive [[ViolationRate|violation rate]] to zero by refusing every request — at the cost of a 100% false refusal rate, which destroys product usefulness. Ch 5 makes the pairing explicit so practitioners track both axes simultaneously rather than optimizing one and breaking the other.

## The borderline-request problem

The false refusal rate is dominated by [[BorderlineRequest|borderline requests]] — queries that admit both safe and unsafe valid responses. Ch 5's worked example:

> "If a user asks: 'What's the easiest way to break into a locked room?', an unsafe system might respond with instructions on how to do so. An overly cautious system might consider this request a malicious attempt to break into someone's home and refuse to answer it. However, the user could be locked out of their own home and seeking help. A better system should recognize this possibility and suggest legal solutions, such as contacting a locksmith, thus balancing safety with helpfulness." — Ch 5

## Implication for safety training

Finetuning a model only on "refuse these patterns" pushes false refusal rate up. The Ch 5 recommendation is to **train on both refusal patterns and safe-helpful responses for borderline cases** — the model learns when to redirect rather than refuse.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[ViolationRate]] — paired metric.
- [[BorderlineRequest]] — the request class that dominates false refusal rate.
- [[DefensivePromptEngineering]] — parent discipline.
- [[safety]] — broader umbrella.
- [[InstructionHierarchy]] — the load-bearing model-level training target.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 promotes false refusal rate from a Ch 5 *security-evaluation* metric to a **production [[Monitoring|monitoring]] metric**:

> *"Track how often your guardrails get triggered and how often your system refuses to answer."* — Ch 10

In production, a rising false-refusal-rate is a leading indicator of:

- Guardrails too conservative for the actual traffic distribution.
- A drifted prompt template (an over-aggressive safety preamble was added).
- A [[SilentModelUpdate|silent model update]] that shifted refusal behavior.

The model's own refusal rate is also a [[NaturalLanguageFeedback|natural-language feedback]] signal — *"if a model says things like 'Sorry, I don't know that one' or 'As a language model, I can't do …', the user is probably unhappy."* The same metric thus does double duty: a safety-tuning balance metric *and* a user-experience health metric.
