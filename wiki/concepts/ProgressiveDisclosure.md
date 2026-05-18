---
title: "Progressive Disclosure"
type: concept
tags: [ux, design-principle, agentic-ai, cognitive-load]
sources: [2605.06651v2-ai-co-mathematician]
last_updated: 2026-05-15
---

# Progressive Disclosure

UX design principle for multi-agent systems ([[2605.06651v2-ai-co-mathematician]] §2). The collaborative interface mirrors the agent hierarchy: by default, the user interacts only with the top-level [[ProjectCoordinatorAgent|Project Coordinator]], which filters out the low-level execution chatter of specialized sub-agents (e.g. *"We must verify measurability on line 40"*); the user can drill into any parallel agent's activity on demand.

Justification: long unstructured chats become unusable when high-level strategy (*"Try a fixed-point approach"*) is mixed with low-level execution logs from many parallel background agents. Filtering by hierarchy preserves cognitive bandwidth for steering decisions.

## Connections
- [[AICoMathematician]]
- [[ProjectCoordinatorAgent]] / [[WorkstreamCoordinator]]
- [[2605.06651v2-ai-co-mathematician]]
