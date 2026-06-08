---
title: "Graph of Debates (GoD)"
type: concept
tags: [reasoning, multi-agent, agentic-design-patterns, debate, graph]
sources: [agentic-design-patterns-ch17-reasoning]
last_updated: 2026-06-07
---

# Graph of Debates (GoD)

**Graph of Debates (GoD)** is an advanced agentic reasoning framework that **reimagines discussion as a dynamic, non-linear network rather than a simple chain**. It is documented in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] as one of the [[ReasoningTechniques|Reasoning Techniques]] ([[agentic-design-patterns-ch17-reasoning|Ch 17]]), generalizing [[ChainOfDebates|Chain of Debates (CoD)]].

## How it works

In GoD, **arguments are individual nodes connected by edges that signify relationships** like `supports` or `refutes`, reflecting the multi-threaded nature of real debate. This structure lets new lines of inquiry **dynamically branch off, evolve independently, and even merge over time**.

A conclusion is reached **not at the end of a sequence, but by identifying the most robust and well-supported cluster of arguments** within the entire graph. In this context, "well-supported" refers to knowledge that is firmly established and verifiable, including:
- **Ground truth** — information considered inherently correct and widely accepted as fact.
- **Search-grounded factual evidence** — information validated against external sources and real-world data (see [[RAG]] / search grounding).
- **Multi-model consensus** — a high degree of agreement and confidence reached by multiple models during a debate.

## Why it matters in agentic systems

This comprehensive approach provides a more **holistic and realistic model for complex, collaborative AI reasoning** — a more robust and reliable foundation for the information being discussed than a linear chain of arguments can offer. It is the graph-structured analogue of how [[TreeOfThoughts|Tree-of-Thought]] generalizes the linear [[ChainOfThought|Chain-of-Thought]]: GoD is to [[ChainOfDebates|CoD]] what ToT is to CoT.

> Note: The chapter names this *Graph of Debates*. It is conceptually adjacent to the research-literature *Graph-of-Thoughts* (which structures a single model's thoughts as a graph); GoD applies the graph structure to a *multi-agent* debate rather than one model's thoughts.

## Connections
- [[agentic-design-patterns-ch17-reasoning]] — source (Ch 17).
- [[ReasoningTechniques]] — the chapter's parent pattern.
- [[ChainOfDebates]] — the linear debate framework GoD generalizes.
- [[TreeOfThoughts]] — the tree-structured single-model analogue.
- [[multiagentsystems]] / [[MultiAgentCollaboration]] — the multi-agent paradigm.
- [[RAG]] — search grounding as one source of "well-supported" evidence.
- [[LLMAsAJudge]] / [[SelfBiasJudge]] — consensus and cross-critique as bias mitigation.
