---
title: "Crawl-Walk-Run"
type: concept
tags: [planning, automation, microsoft, hitl, ai-engineering]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# Crawl-Walk-Run

**Microsoft's three-stage framework for gradually increasing AI automation in products**, surfaced in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] (citing [[microsoft|Microsoft]] 2023). A practical [[humanintheloop|human-in-the-loop]] deployment ladder for [[AIEngineering|AI applications]].

## The three stages

1. **Crawl** — *human involvement is mandatory.* Every AI decision is reviewed/approved by a human before any external action.
2. **Walk** — *AI can directly interact with internal employees.* AI takes some actions autonomously, but only against internal users where the blast radius is contained.
3. **Run** — *increased automation, potentially including direct AI interactions with external users.* The product reaches full deployment.

## How the ladder progresses

Huyen's worked customer-support example:

- **Crawl**: AI shows several response suggestions; human agents reference them while writing.
- **Walk**: AI responds to simple requests; routes complex ones to humans.
- **Run**: AI responds to all requests directly, without human involvement.

Progression depends on **acceptance rate by humans**: e.g., *"if 95% of AI-suggested responses to simple requests are used by human agents verbatim, you can let customers interact with AI directly for those simple requests."*

## Why this matters

Crawl-Walk-Run is one of Ch 1's most reusable planning frameworks because it gives a **measurable graduation criterion** for moving up the automation ladder, rather than a one-shot "deploy or don't" decision. It pairs naturally with [[UsefulnessThreshold|usefulness thresholds]] — each stage has its own quality bar.

## Connections

- [[humanintheloop]] — parent concept; Crawl-Walk-Run is a concrete HITL deployment ladder.
- [[microsoft|Microsoft]] — framework originator.
- [[UseCaseEvaluation]] — Crawl-Walk-Run is a sub-framework of use-case planning.
- [[UsefulnessThreshold]] — the per-stage quality bar.
- [[AIEngineering]] — the discipline this framework serves.
- [[ai-engineering-ch01-intro]] — primary source.
