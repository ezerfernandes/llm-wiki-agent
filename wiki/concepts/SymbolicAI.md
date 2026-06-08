---
title: "Symbolic AI"
type: concept
tags: [ai-history, mlsysbook, foundations]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# Symbolic AI

The first era of AI engineering (1950s–1970s) that attempted to reduce intelligence to **manipulation of logical rules and symbols.** Covered in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) as the era that hit the **logic bottleneck**: hand-coded rules cannot capture real-world ambiguity, and the rule base grows exponentially until unmaintainable.

Originating at the 1956 **Dartmouth Conference** (where John McCarthy coined "artificial intelligence"), exemplars include Daniel Bobrow's **STUDENT** (1964), which parsed English word problems into algebra. A minor phrasing variation ("Tom's client count") would break it. **Moravec's Paradox** emerged here: high-level reasoning (chess) needs little compute while low-level perception (seeing, walking, grasping) needs massive parallelism — foreshadowing the accelerator revolution.

The engineering lesson: explicit logic cannot scale to real-world ambiguity. This motivated the [[ExpertSystems|expert-systems]] pivot and, ultimately, the data-driven paradigm.

## Connections

- [[ExpertSystems]] — the successor era (knowledge bottleneck).
- [[BitterLesson]] — the pattern this era's failure validates.
- [[NeuroSymbolicAI]] / [[SymbolicProgramming]] — modern descendants in the wiki.
- [[DeepLearning]] — the paradigm that dissolved hand-crafted representations.
- [[mlsysbook-ch01-introduction]] — source.
