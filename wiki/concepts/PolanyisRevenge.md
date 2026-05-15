---
title: "Polanyi's Revenge"
type: concept
tags: [framing, ai-history, knowledge-engineering]
sources: [2402.01817-llm-modulo]
last_updated: 2026-05-10
---

# Polanyi's Revenge

A framing coined by [[SubbaraoKambhampati]] (*Polanyi's Revenge and AI's New Romance with Tacit Knowledge*, CACM 64(2):31–32, 2021), invoked centrally in [[2402.01817-llm-modulo]].

## The original paradox
**Polanyi's paradox** (Michael Polanyi, *The Tacit Dimension*, 1966): *we know more than we can tell* — expert performance relies on tacit knowledge that resists explicit articulation. This is the famous wound at the heart of GOFAI knowledge engineering, where experts had to laboriously author rules/ontologies (e.g., PDDL domains) for AI systems to use.

## The "revenge"
LLMs make tacit knowledge **cheaply accessible** without forcing anyone to articulate it: the LLM has absorbed civilizational text and can produce *approximate* domain knowledge on demand. The revenge is that AI gets to use tacit knowledge **without** paying knowledge engineering's articulation cost — provided we relax the requirement that the knowledge be **correct** and instead route soundness through **external critics**.

## Why this matters for LLM-Modulo
[[LLMModuloFramework]] is the **principled cash-out** of Polanyi's Revenge: LLMs deliver cheap approximate models and candidates; external sound critics (hard model-based, e.g. VAL) supply the correctness guarantees that knowledge engineering used to provide via painfully-authored symbolic models. The framework explicitly preserves a **human-in-the-outer-loop** role to sign off on extracted domain models (Guan et al. 2023), but humans are kept out of the inner planning loop.

## Connections
- [[LLMModuloFramework]] — operationalizes the framing
- [[PDDL]] — the kind of domain knowledge once authored by hand, now extracted via LLM + human sign-off
- [[NeuroSymbolicAI]] — Polanyi's Revenge is the bridge: approximate symbolic models from LLMs feeding sound symbolic solvers
- [[Planning]] — the immediate target application
- [[SubbaraoKambhampati]] — coined the framing
- [[2402.01817-llm-modulo]] — source citing it
