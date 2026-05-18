---
title: "Project Coordinator Agent"
type: concept
tags: [agent-role, agentic-ai, harness]
sources: [2605.06651v2-ai-co-mathematician]
last_updated: 2026-05-15
---

# Project Coordinator Agent

Top-level agent in the [[AICoMathematician|AI co-mathematician]] hierarchy ([[2605.06651v2-ai-co-mathematician]]). The user's primary interface: it formalizes intent through dialogue, defines the research question and goals, delegates per-goal [[WorkstreamCoordinator|Workstream Coordinators]], filters their low-level execution chatter, and surfaces alerts when uncertainty stalls a workstream (e.g. "Our initial implementation of the search is not efficient enough — do you have a mathematical intuition for a better pruning strategy?").

A key design choice: the Project Coordinator does **not** start working on a solution when asked. It first **opens a dialogue** — sounding board mode — to elicit the user's actual intent, refines proposed goals through chat, and only delegates downstream once the user formally approves the goal set.

## Connections
- [[AICoMathematician]]
- [[WorkstreamCoordinator]]
- [[ProgressiveDisclosure]]
- [[2605.06651v2-ai-co-mathematician]]
