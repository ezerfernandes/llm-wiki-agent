---
title: "Blocksworld"
type: concept
tags: [benchmark, planning, evaluation, classical-ai]
sources: [2402.01817-llm-modulo]
last_updated: 2026-05-10
---

# Blocksworld

Canonical AI-planning domain dating to the early 1970s (Winograd's SHRDLU): a robot arm stacks/unstacks labeled blocks on a table. Trivial preconditions/effects, well-understood plan complexity, **fully solvable** by classical planners. In [[PlanBench]] it's the headline domain used to stress-test LLM plan generation.

## Mystery BW (obfuscated Blocksworld)
A variant where action and object names are replaced with meaningless tokens (e.g., `attack`, `feast`, `succumb` instead of `pickup`, `stack`). **Logically identical** to standard BW — a real planner is indifferent — but human-readable surface form is destroyed.

## Why it matters
On 600 PlanBench BW instances, top LLMs solve **11–59%** zero-shot. On Mystery BW the same models drop to **0–4.3%**. This **collapse under semantic-preserving renaming** is the strongest single piece of evidence in [[2402.01817-llm-modulo]] that what LLMs do on BW is **approximate plan retrieval over web-scale corpora that mention blocks/pickup/stack**, not planning.

## LLM-Modulo result
With [[PDDL|VAL]] back-prompting in an [[LLMModuloFramework]] loop (≤15 rounds), GPT-4 reaches **82% on Blocksworld** — but still only ~10% on Mystery BW, because the LLM struggles to *propose* plausible candidates even though VAL would correctly verify them.

## Connections
- [[Planning]], [[PlanBench]], [[PDDL]] — classical planning context
- [[LLMModuloFramework]] — case study using BW + VAL
- [[2402.01817-llm-modulo]] — source
