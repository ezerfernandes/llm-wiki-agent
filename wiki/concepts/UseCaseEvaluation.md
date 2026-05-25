---
title: "Use Case Evaluation"
type: concept
tags: [planning, ai-engineering, business, framework]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# Use Case Evaluation

**The "why are we building this?" question that should precede every AI application.** Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], use case evaluation is the first step of [[AIEngineering|AI engineering]] planning — *"it's easy to build a cool demo with foundation models. It's hard to create a profitable product."*

## Three risk/opportunity levels (high → low)

1. **Existential threat**: *"If you don't do this, competitors with AI can make you obsolete."* — incorporating AI must be the highest priority. In Gartner's 2023 study, 7% of 2,500 executives cited *business continuity* as their reason for embracing AI. Common in document-processing, financial analysis, insurance, advertising, web design, image production.

2. **Missed opportunity**: *"If you don't do this, you'll miss opportunities to boost profits and productivity."* — the most common motivation. AI cheapens user acquisition (better copywriting, product descriptions), improves retention (better support + customization), helps with sales lead generation, internal communication, market research.

3. **Hedging**: *"You're unsure where AI will fit into your business yet, but you don't want to be left behind."* — Huyen's cue list: *cue Kodak, Blockbuster, and BlackBerry.* For bigger companies, this is R&D-budget territory; smaller startups usually can't afford a "look around" role.

## Build vs. buy

Once a use case is justified, the next question: do you build it in-house or buy from a vendor?

- **Existential-threat tier** → favor in-house (don't outsource your moat to a competitor).
- **Opportunity tier** → buy-options are usually faster and cheaper at higher quality.

## What to consider once you've decided to build

Ch 1's planning checklist (each is a separate wiki page):
- **The role of AI in the product** — [[CriticalOrComplementary]], [[ReactiveOrProactive]], [[DynamicOrStatic]].
- **The role of humans** — [[humanintheloop|HITL]], [[CrawlWalkRun|Crawl-Walk-Run]] automation ladder.
- **[[AIProductDefensibility|Defensibility]]** — tech / data / distribution moats.
- **[[UsefulnessThreshold|Usefulness thresholds]]** — quality, latency, cost, fairness metric bars.
- **Milestone planning** including the [[LastMileChallenge|last-mile problem]].
- **Maintenance** under the fast-moving FM landscape.

## Connections

- [[AIEngineering]] — discipline this framework serves.
- [[CriticalOrComplementary]] / [[ReactiveOrProactive]] / [[DynamicOrStatic]] — the role-of-AI axes.
- [[AIProductDefensibility]] / [[UsefulnessThreshold]] / [[LastMileChallenge]] — downstream planning concepts.
- [[CrawlWalkRun]] / [[humanintheloop]] — role-of-humans frameworks.
- [[ai-engineering-ch01-intro]] — primary source.
