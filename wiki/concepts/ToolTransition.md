---
title: "Tool Transition"
type: concept
tags: [agents, tools, analysis]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Tool Transition

**Tool transition** is the analysis of **which tools an agent calls in sequence** — the conditional probability `P(tool_Y | tool_X)`. Introduced by [[Chameleon]] (Lu et al. 2023) and named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as the methodological basis for:

1. **Tool-pair analysis** — which tools are routinely used together?
2. **Composite tool construction** — *"If two tools are frequently used together, they can be combined into a bigger tool."*
3. **AI-created tools** — feed tool-transition statistics back to the agent; the agent itself can compose new tools.

## Why it matters

Without tool-transition analysis, the tool inventory is treated as a **flat set**. With it, the inventory becomes a **graph** — nodes (tools) connected by transition probabilities. This graph reveals:

- **Bottlenecks**: tools always invoked early in successful plans.
- **Redundancy**: tools whose outputs are usually fed to the same downstream tool — candidates for composition.
- **Dead ends**: tools rarely followed by anything successful — candidates for removal.

## Position relative to [[VoyagerAgent|Voyager]]'s skill manager

[[Chameleon]] introduced tool transition as **analysis**. [[VoyagerAgent|Voyager]] (Wang et al. 2023) operationalized it: detect a successful transition pattern → package it as a coding program → add to the skill library. The conceptual chain: **observe transitions → identify useful pairs → mint composite tools**.

## Connections

- [[Chameleon]] — origin paper.
- [[VoyagerAgent]] — operationalization.
- [[ToolInventory]] — the abstraction tool transitions decorate.
- [[Agent]] — parent surface.
- [[CapabilityExtension]] — composite tools are a capability-extension instance.
- [[ai-engineering-ch06-rag-agents]] — primary source.
