---
title: "Sequential Decomposition"
type: concept
tags: [agentic-design-patterns, agents, prompt-engineering, prompt-chaining, divide-and-conquer]
sources: [agentic-design-patterns-ch01-prompt-chaining]
last_updated: 2026-06-07
---

# Sequential Decomposition

**Sequential decomposition** is the divide-and-conquer mechanic at the heart of [[PromptChaining|prompt chaining]]: breaking a complex, multifaceted task into a sequence of smaller, focused sub-problems, each handled by a dedicated step, where each step's output becomes the next step's input. Named and formalized in [[agentic-design-patterns-ch01-prompt-chaining|Chapter 1]] of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) under the heading *"Enhanced Reliability Through Sequential Decomposition."*

## How it works
The original "daunting" problem is restructured into a focused, sequential workflow. [[agentic-design-patterns-ch01-prompt-chaining|Ch 1]]'s worked example takes the monolithic request *"analyze a market research report, summarize findings, identify trends with data points, and draft an email"* and decomposes it into three dependent steps:

1. **Summarization** — *"Summarize the key findings of the following report: [text]."* (sole focus → higher accuracy)
2. **Trend identification** — *"Using the summary, identify the top three emerging trends and extract the specific data points: [output from step 1]."* (more constrained; builds on a validated output)
3. **Email composition** — *"Draft a concise email outlining the following trends and supporting data: [output from step 2]."*

Each step can be assigned a **distinct role** — e.g., "Market Analyst," then "Trade Analyst," then "Expert Documentation Writer."

## Why it matters in agentic systems
A single monolithic prompt overloads the model and triggers failure modes — instruction neglect, contextual drift, error propagation, context-window pressure, and hallucination from cognitive load. Sequential decomposition mitigates these by making each step **simpler, less ambiguous, and individually optimizable**, which is *"analogous to a computational pipeline where each function performs a specific operation before passing its result to the next."* This modularity also makes the workflow **easier to debug** (you can inspect each intermediate output) and lets deterministic logic, validation, and conditional branching be inserted between model calls. It is the foundational structuring principle for building reliable multi-step agents.

## Relation to parallelization
Decomposition is not always purely sequential. [[agentic-design-patterns-ch01-prompt-chaining|Ch 1]] notes that complex pipelines often **combine parallel processing** for independent sub-tasks (e.g., extracting key info from many articles at once — [[Parallelization]]) **with sequential chaining** for the dependent synthesis and refinement steps.

## Connections
- [[PromptChaining]] — the pattern this mechanic implements.
- [[ContextHandoff]] — the structured passing of each step's output to the next.
- [[Parallelization]] — the complementary pattern for independent sub-tasks.
- [[Pipeline]] — the computational-pipeline analogy Ch 1 draws on.
- [[PromptDecomposition]] — the *Hands-On LLMs*/Huyen vocabulary for the same idea.
- [[ContextEngineering]] — engineering each step's focused context.
- [[agentic-design-patterns-ch01-prompt-chaining]] — source.
