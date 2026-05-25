---
title: "STORM (Synthesis of Topic Outlines through Retrieval and Multi-perspective question asking)"
type: concept
tags: [system, multi-agent, long-form-generation, llm-application]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# STORM

**STORM** — *Synthesis of Topic Outlines through Retrieval and Multi-perspective question asking* — is the Wikipedia-style long-form article generation system introduced by [[YijiaShao|Shao]] et al. ([[Shao2024]], NAACL 2024 — *Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models*, arXiv 2402.14207). Built at [[StanfordOVAL]]; the **direct predecessor** of [[CoSTORM|Co-STORM]] ([[2408.15232-co-storm]]).

## What it does

Given an arbitrary topic, STORM:

1. Retrieves background information via a search engine.
2. Generates a list of **perspectives** ($p_1, ..., p_N$) representing different stakeholder/expert viewpoints on the topic.
3. Simulates **multi-perspective question-asking** — an LM-played expert per perspective asks questions, retrieves answers, and assembles structured information.
4. Produces an **outline** for a Wikipedia-style article.
5. Generates the article **section by section**, each section grounded in retrieved sources.

The output is a **static cited long-form report** — a high-quality first draft of a Wikipedia-like article.

## Limitations of STORM (that motivated Co-STORM)

Per [[2408.15232-co-storm|Co-STORM §1]]:

> *"STORM does not support any user interaction which is crucial in complex information seeking where there is no single, gold query, but queries evolve dynamically towards a goal."*

— i.e. STORM treats the topic as **the** query, and the output as **the** answer. There is no mechanism for the user to interject, redirect, or follow up. Co-STORM addresses this by wrapping STORM-style multi-perspective question-asking with a moderator agent + a mind map + a turn-management protocol that lets the user observe and participate.

## Connections

- **Predecessor of [[CoSTORM|Co-STORM]]** — same lab, same DSPy substrate, same You.com search backend, same Wikipedia *Reliable sources* filter.
- Cited as the [[STORM]]+QA **baseline** in Co-STORM's evaluation (STORM generates the report; the user can ask follow-up questions answered by retrieval).
- The [[Shao2024]] reference is also invoked in the [[2406.11695-mipro|MIPRO]] / [[2407.10930-better-together|BetterTogether]] / [[2507.19457-gepa|GEPA]] [[DSPy]]-optimizer line — STORM is a canonical *expensive multi-stage LM program* that benefits from automated optimization.
- The **perspective-guided question-asking** mechanism is inherited unchanged by Co-STORM as the [[PerspectiveGuidedExpert]] role.

## See also
- [[CoSTORM]] · [[YijiaShao]] · [[MonicaLam]] · [[StanfordOVAL]] · [[PerspectiveGuidedExpert]]
