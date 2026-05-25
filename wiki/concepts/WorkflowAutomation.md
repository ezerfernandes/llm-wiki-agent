---
title: "Workflow Automation"
type: concept
tags: [use-case, ai-engineering, agents, automation]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# Workflow Automation

**The use case of automating tasks end-to-end** — one of the eight [[FoundationModelUseCases|foundation-model use case categories]] in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]]. The category most closely tied to **AI agents** as the technical mechanism.

## Consumer patterns

- Booking restaurants.
- Requesting refunds.
- Planning trips.
- Filling out forms.

## Enterprise patterns

- Lead management.
- Invoicing / reimbursements.
- Customer-request triage.
- Data entry.
- Data synthesis for self-improving training pipelines (Chapter 8 of the book).

## Agents as the mechanism

> *"Access to external tools is required to accomplish many tasks. To book a restaurant, an application might need permission to open a search engine to look up the restaurant's number, use your phone to make calls, and add appointments to your calendar. AIs that can plan and use tools are called agents."*

The chapter explicitly defines an agent as **an AI that plans and uses tools** — a practical engineering definition. *"The level of interest around agents borders on obsession, but it's not entirely unwarranted. AI agents have the potential to make every person vastly more productive and generate vastly more economic value."*

Agents are the central topic of Chapter 6 of the book.

Note: this is a narrower agent definition than the wiki's existing [[AgenticAI]] formalization (Liao et al.'s topology-graph $\Psi = (\mathcal{G}, \mathcal{F}, \Lambda)$). Both are compatible — Huyen's engineering-flavored definition is what gets implemented; [[AgenticAI]] is the theoretical-paradigm framing.

## Self-improvement loop

One especially noteworthy enterprise pattern from Ch 1:

> *"One especially exciting use case is using AI models to synthesize data, which can then be used to improve the models themselves. You can use AI to create labels for your data, looping in humans to improve the labels."*

This loops [[DatasetEngineering|dataset engineering]] and workflow automation into a single closed-loop self-improvement cycle.

## Connections

- [[FoundationModelUseCases]] — parent category.
- [[Agent]] / [[AgenticAI]] / [[llmagents]] — the agent paradigm Ch 1 sketches and the wiki's existing formalization.
- [[InformationAggregation]] / [[DataOrganization]] — natural pairing categories ([[Instacart|Instacart's]] Fast Breakdown is the bridge).
- [[DatasetEngineering]] — data synthesis loops back here.
- [[humanintheloop]] — for label-improvement loops.
- [[ai-engineering-ch01-intro]] — primary source.
