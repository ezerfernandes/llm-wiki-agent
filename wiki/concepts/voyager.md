---
title: "Voyager"
type: concept
tags: [concept, agents, skills]
sources: [2604.27707-agentic-memory-is-a-memo, ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Voyager

Wang et al. (2023): Minecraft agent that accumulates skills as code in a vector database. Cited by Xu et al. as illustrating the substrate-mismatch problem — skills live in C while the composition rule combining them must come from θ.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

See [[VoyagerAgent]] for the deep dive of Ch 6's framing. [[ChipHuyen|Huyen]] cites Voyager as the canonical reference for **AI-created tools** — the agent's tool inventory can grow during operation via a **skill manager** that stores successful action-sequences as reusable code-tools in a vector-database skill library, retrieved later for new tasks. This complements the existing Xu et al. *substrate-mismatch* read with the agent-engineering read: Voyager shows that an agent's tool inventory need not be fixed at design time.
