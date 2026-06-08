---
title: "AlphaEvolve"
type: entity
tags: [google, ai-agent, evolutionary-algorithm, gemini, self-improvement, algorithm-discovery]
sources: [agentic-design-patterns-ch09-learning-adaptation, agentic-design-patterns-ch21-exploration]
last_updated: 2026-06-07
---

# AlphaEvolve

**AlphaEvolve** is an AI agent developed by [[google|Google]] designed to **discover and optimize algorithms**. It combines an ensemble of [[gemini|Gemini]] models, automated evaluation systems, and an **evolutionary-algorithm framework** to advance both theoretical mathematics and practical computing. It is the flagship "advanced self-improvement" example of the [[LearningAndAdaptation|Learning and Adaptation]] pattern in [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli, Ch 9).

## How it works

AlphaEvolve employs an ensemble of [[gemini|Gemini]] models: **Flash** generates a wide range of initial algorithm proposals (breadth), while **Pro** provides in-depth analysis and refinement (depth). Proposed algorithms are automatically evaluated and scored against predefined criteria; this feedback drives iterative, evolutionary improvement toward optimized and novel algorithms.

## Demonstrated results

**Practical computing (deployed in Google's infrastructure):**
- **0.7% reduction in global compute resource usage** via improved data-center scheduling.
- Hardware design contributions — suggested optimizations for **Verilog code in upcoming [[TPU|Tensor Processing Units]]**.
- **23% speed improvement** in a core kernel of the [[gemini|Gemini]] architecture.
- Up to **32.5% optimization** of low-level GPU instructions for **FlashAttention**.

**Fundamental research:**
- Discovered new algorithms for **matrix multiplication**, including a method for **4×4 complex-valued matrices using 48 scalar multiplications**, surpassing previously known solutions.
- **Rediscovered SOTA solutions to 50+ open problems in 75% of cases** and **improved on existing solutions in 20% of cases** — including advances on the **kissing-number problem**.

## As an Exploration and Discovery system

Although introduced under Ch 9 (Learning and Adaptation), AlphaEvolve is also a canonical instance of the [[ExplorationAndDiscovery|Exploration and Discovery]] pattern (Ch 21): its evolutionary "propose → evaluate/score → refine" loop is a discovery-by-evolution engine that uncovers *novel* algorithms (e.g. faster matrix multiplication, the kissing-number problem) rather than merely optimizing within a fixed space. It is a sibling of the Ch 21 exemplars [[GoogleCoScientist|Google AI Co-Scientist]] and [[AgentLaboratory|Agent Laboratory]] — all three use generate-evaluate-evolve loops with automated scoring to expand the space of known solutions.

## Connections
- [[ExplorationAndDiscovery]] — the discovery-by-evolution pattern it also exemplifies (Ch 21).
- [[GoogleCoScientist]] / [[AgentLaboratory]] — sibling autonomous-discovery systems (Ch 21).
- [[google|Google]] — developer; [[googledeepmind|Google DeepMind]] context.
- [[gemini|Gemini]] — the Flash + Pro model ensemble powering proposals and refinement.
- [[OpenEvolve]] — the open-source evolutionary coding agent that mirrors AlphaEvolve.
- [[SelfImprovingCodingAgent]] — peer self-improving system in the same chapter.
- [[LearningAndAdaptation]] — the Ch 9 pattern it exemplifies.
- [[recursiveselfimprovement]] — broader self-improvement framing.
- [[TPU]] — AlphaEvolve optimized Verilog for upcoming TPUs.
- [[AgenticDesignPatterns]] — Chapter 9; [[AntonioGulli]].
- [[agentic-design-patterns-ch09-learning-adaptation]] — source page.
