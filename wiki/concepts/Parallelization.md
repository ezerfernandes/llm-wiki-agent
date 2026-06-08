---
title: "Parallelization (Agentic Pattern)"
type: concept
tags: [agentic-design-patterns, agents, parallelization, concurrency, async, fan-out-fan-in, scatter-gather, control-flow]
sources: [agentic-design-patterns-ch03-parallelization, agentic-design-patterns-ch07-multi-agent]
last_updated: 2026-06-07
---

# Parallelization (Agentic Pattern)

**Parallelization** is the third of the 21 [[AgenticDesignPattern|agentic design patterns]] in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]]. It is the **control-flow pattern for executing independent workflow components — LLM calls, tool usages, or entire sub-agents — concurrently** rather than one after another, so a workflow's wall-clock time approaches its slowest branch instead of the sum of all branches.

> *"Parallelization involves executing multiple components, such as LLM calls, tool usages, or even entire sub-agents, concurrently."* — Ch 3

This is the **agentic-orchestration** sense of parallelization (overlapping independent agent/LLM/tool steps), distinct from the hardware/HPC sense covered by [[ParallelComputing]], [[ConcurrencyVsParallelism]], and the GPU/training-parallelism pages ([[DataParallelism]], [[TensorParallelism]], [[PipelineParallelism]]). Those are cross-references, not the same concept.

## Where it sits among the control-flow patterns
Parallelization completes the core control-flow trio the book builds in its first three chapters:

| Pattern | Shape | Chapter |
|---|---|---|
| [[PromptChaining]] | **Sequential** — each step's output feeds the next | Ch 1 |
| [[Routing]] | **Conditional** — dynamically branch to one path | Ch 2 |
| **Parallelization** | **Concurrent** — run independent paths at once, then join | Ch 3 |

The chapter stresses these compose: *"integrating parallel processing with sequential (chaining) and conditional (routing) control flows"* yields sophisticated, high-performance agent systems.

## How it works — fan-out / fan-in
The canonical structure is **fan-out → parallel execution → fan-in**:

1. **Identify independent sub-tasks** — parts of the workflow that do not depend on each other's immediate outputs.
2. **Fan-out**: dispatch them concurrently (a [[ScatterGather|scatter]] / [[MapReduce|map]] over sub-tasks).
3. **Fan-in / synthesis**: a *typically sequential* join step waits for all branches to finish, then aggregates their results.

Gulli's worked illustration: an agent researching a topic runs *Search A* **and** *Search B* simultaneously, then *Summarize A* **and** *Summarize B* simultaneously, and finally synthesizes both summaries (the synthesis waits for the parallel steps to complete).

## Why it matters in agentic systems
- **Latency hiding for I/O-bound work.** The pattern is *"particularly effective when dealing with external services (like APIs or databases) that have latency, as you can issue multiple requests concurrently"* — see [[Latency]] / [[LatencyHiding]]. A purely sequential agent pays the **sum** of all task durations; a parallel one pays roughly the **max**.
- **Throughput and responsiveness.** It is the book's fundamental optimization technique for complex agent workflows, making them more performant and responsive.
- **Concurrency, not necessarily parallelism.** The chapter is explicit that `asyncio` provides *concurrency, not parallelism*: a single-thread event loop interleaves tasks while one awaits I/O, giving the *effect* of simultaneous progress, but the code runs on one thread under Python's GIL. True multi-core parallelism needs multi-threading/multi-processing. This is the same distinction the wiki's [[ConcurrencyVsParallelism]] page formalizes — the agentic pattern primarily exploits **concurrency to overlap I/O waits**.

## Sub-shapes and techniques
- **Fan-out/fan-in (scatter-gather)** — dispatch N independent calls, collect N results, join. Maps to [[ScatterGather]] at the orchestration level.
- **Map-reduce over sub-tasks** — run the same analysis over many segments (e.g. sentiment + keyword + category extraction across a batch), then reduce; the agentic analogue of [[MapReduce]].
- **Sectioning** — decompose a task into *different* independent sub-tasks run in parallel (e.g. generate a marketing email's subject line, body, image, and CTA concurrently; multi-modal text+image analysis).
- **Voting / multiple-options generation** — run the *same* task multiple times (varied prompts/models) to generate variants, then select the best — an A/B-style selection ([[ABTesting]]) related to [[ModelEnsemble|ensembling]] and [[selfconsistency|self-consistency]].

## Practical applications (Ch 3)
Information gathering & research (multi-source lookups at once); data processing & analysis (concurrent analysis techniques over a batch); multi-API/tool interaction (a travel planner querying flights, hotels, events, restaurants concurrently); content generation with multiple components; validation & verification (parallel independent checks); multi-modal processing (text + image of one input); and A/B testing / multiple-options generation.

## Framework support
- **[[LangChain]] (LCEL)** — `RunnableParallel` runs the contained runnables concurrently; combine in a dict/list construct and use `RunnablePassthrough` to thread the original input through. The `|` pipe is sequential; the dict form is parallel. Runs on [[asyncio]] (`ainvoke`, `asyncio.run`).
- **[[LangGraph]]** — parallelism is a property of graph topology: multiple nodes with no direct sequential dependency are launched from one common node as **parallel branches**, then converge at a downstream aggregation node.
- **[[GoogleADK|Google ADK]]** — a `ParallelAgent` natively orchestrates concurrent execution of its `sub_agents`, finishing only when all have written results to shared **session state** (`output_key`); a downstream merger `LlmAgent` reads that state. ADK can also parallelize via **LLM-driven delegation** from a coordinator.
- **[[CrewAI]]** — peer framework for orchestrating multiple agents (named across the book).

## Trade-offs
The chapter's caution: *"the adoption of a concurrent or parallel architecture introduces substantial complexity and cost, impacting key development phases such as design, debugging, and system logging."* **Rule of thumb:** use parallelization when a workflow contains multiple genuinely independent operations (fetching from several APIs, processing distinct data chunks, generating multiple pieces for later synthesis) — not for inherently sequential logic.

## Connections
- [[AgenticDesignPatterns]] — book hub (Pattern #3 of 21).
- [[PromptChaining]] / [[Routing]] — the sequential and conditional control-flow siblings; parallelization composes with both.
- [[ScatterGather]] / [[MapReduce]] — CS fan-out/fan-in and map-reduce shapes this pattern instantiates at the agent level (cross-reference).
- [[ConcurrencyVsParallelism]] — the OS/CS distinction the GIL/asyncio note relies on (cross-reference; the multi-core hardware sense, kept distinct from this agentic-orchestration sense).
- [[ParallelComputing]] — the broader HPC concept (cross-reference, not the same as this pattern).
- [[asyncio]] — the Python concurrency substrate of the LangChain example.
- [[Latency]] / [[LatencyHiding]] — the I/O latency this pattern hides by overlapping waits.
- [[AgentHandoff]] / [[multiagentsystems]] — ADK's `ParallelAgent` + merger is concurrent multi-agent collaboration.
- [[MultiAgentCollaboration]] / [[agentic-design-patterns-ch07-multi-agent]] — Ch 7 names **Parallel Processing** as a collaboration *form*, reusing ADK's `ParallelAgent` (`data_gatherer` running `weather_fetcher` + `news_fetcher` concurrently).
- [[ABTesting]] / [[ModelEnsemble]] / [[selfconsistency]] — the multiple-options / voting sub-shape.
- [[LangChain]] / [[LangGraph]] / [[GoogleADK]] / [[CrewAI]] — frameworks providing parallel-execution constructs.
- [[AntonioGulli]] — author.
- [[agentic-design-patterns-ch03-parallelization]] — source.
</content>
