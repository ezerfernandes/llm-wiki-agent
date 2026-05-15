---
title: "Neuro-Symbolic AI"
type: concept
tags: [neuro-symbolic, planning, reasoning, framing]
sources: [2402.01817-llm-modulo]
last_updated: 2026-05-10
---

# Neuro-Symbolic AI

Umbrella term for architectures that combine **neural** components (typically learned, sub-symbolic, approximate) with **symbolic** components (typically logical, formally defined, sound).

## Two failure modes per [[2402.01817-llm-modulo]]
1. **LLM as glorified solver front-end** — pipelining NL → PDDL/SAT, then handing to a back-end symbolic solver (LLM+P, Logic-LM, Xie et al.). The paper notes this has been called *neuro-symbolic architecture* but argues the badge is undeserved: such systems inherit the **expressivity and search-complexity** limits of the back-end solver. Footnote 2: *"In some circles, this unidirectional pipeline has been given the undeserved badge of neuro-symbolic architecture."*
2. **Loosely pipelined LLM + symbolic component** — the paper criticizes this as weaker than tight bi-directional integration.

## The LLM-Modulo position
[[LLMModuloFramework]] is offered as a **tighter, bi-directional neuro-symbolic integration**: the LLM is *not* a translator to a back-end planner — it's a *front-end generator* that proposes candidates against a *back-end bank of critics* in a Generate-Test-Critique loop. The compound system is sound by inheritance from the hard critics, but the LLM retains its generative leverage. Polanyi's Revenge ([[PolanyisRevenge]]) supplies the knowledge-engineering bridge.

## Connections
- [[LLMModuloFramework]] — proposed tight integration pattern
- [[PDDL]] — symbolic-side representation
- [[Planning]] — primary application domain
- [[PolanyisRevenge]] — the framing that makes cheap-but-approximate neural knowledge useful to symbolic systems
- [[2402.01817-llm-modulo]] — source
