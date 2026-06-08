---
title: "Chapter 3 — Parallelization (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, parallelization, concurrency, async, fan-out-fan-in, scatter-gather, control-flow]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 3 of [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] presents **[[Parallelization|parallelization]]** as the third of the 21 patterns: executing independent workflow components — LLM calls, tool usages, or whole sub-agents — *concurrently* rather than sequentially, so that the total execution time approaches the slowest branch rather than the sum of all branches. It frames parallelization as the efficiency-oriented complement to the sequential [[PromptChaining|prompt chaining]] (Ch 1) and conditional [[Routing|routing]] (Ch 2) control-flow patterns, most valuable when sub-tasks are I/O-bound (API/database latency). It closes with two hands-on examples — a [[LangChain]] LCEL `RunnableParallel` fan-out/fan-in over [[asyncio]], and a [[GoogleADK|Google ADK]] `ParallelAgent` nested inside a `SequentialAgent` that runs three researcher sub-agents concurrently then merges their state. (Agentic Design Patterns, PDF pp 50–64.)

## Key Claims
- **Parallelization executes multiple components concurrently** — LLM calls, tool usages, or entire sub-agents — instead of waiting for one step to finish before starting the next; this drastically reduces wall-clock time for tasks decomposable into independent parts.
- The core method is to **identify parts of a workflow that do not depend on each other's immediate outputs** and run them at the same time. It is *particularly effective with external services (APIs, databases) that have latency*, since multiple requests can be issued concurrently.
- The canonical shape is **fan-out → parallel execution → fan-in (synthesis)**: a research agent runs *Search A* and *Search B* simultaneously, then *Summarize A* and *Summarize B* simultaneously, and finally a *typically sequential* synthesis step that waits for all parallel branches to complete before aggregating ([[ScatterGather|scatter-gather]] / [[MapReduce|map-style]] fan-out with a reduce/merge join point).
- **Implementing parallelization requires frameworks supporting asynchronous execution or multi-threading/multi-processing.** Modern agentic frameworks ([[LangChain]], [[LangGraph]], [[GoogleADK|Google ADK]]) are designed with async operations in mind so steps can be declared parallel easily.
- In **[[LangChain]] Expression Language (LCEL)**, parallelism is achieved by combining runnables in a dictionary/list construct: `RunnableParallel` runs the contained runnables concurrently (with `RunnablePassthrough` threading the original input through), versus the `|` pipe operator for sequential composition; the example runs `summarize` / `questions` / `key_terms` chains in parallel and pipes the bundle into a synthesis prompt.
- In **[[LangGraph]]**, parallelism is a property of the graph topology: multiple nodes lacking direct sequential dependencies are initiated from a single common node, execute independently as **parallel branches**, then converge at a downstream aggregation node.
- In **[[GoogleADK|Google ADK]]**, a `ParallelAgent` natively orchestrates concurrent execution of its `sub_agents`, completing only once all of them have finished and written their results to shared **session state** (via `output_key`); a downstream "merger"/synthesis `LlmAgent` then reads that state. ADK can also achieve parallelism through **LLM-driven delegation**, where a coordinator's LLM identifies independent sub-tasks and dispatches them to specialized sub-agents.
- The chapter is careful that **asyncio provides concurrency, not parallelism**: a single-thread event loop interleaves tasks while one is idle (e.g. awaiting network I/O), giving the *effect* of simultaneous progress, but the code still runs on one thread constrained by Python's GIL — the agentic-orchestration sense of "parallel" is about overlapping I/O-bound waits, distinct from true multi-core [[ConcurrencyVsParallelism|parallel execution]].
- **Practical applications**: information gathering/research (multi-source lookups at once), data processing (sentiment + keywords + categorization concurrently), multi-API/tool interaction (travel planner hitting flights/hotels/events), multi-component content generation (subject line + body + image + CTA), validation/verification (email + phone + address + profanity checks), multi-modal processing (text + image of one input), and A/B-style multiple-options generation (three headline variants for selection).
- **Trade-off / rule of thumb**: adopting a concurrent or parallel architecture introduces substantial complexity and cost in design, debugging, and system logging; use the pattern when a workflow contains multiple genuinely independent operations (fetching from several APIs, processing distinct data chunks, generating multiple content pieces for later synthesis). Integrating parallelism with sequential ([[PromptChaining|chaining]]) and conditional ([[Routing|routing]]) flows yields sophisticated, high-performance systems.

## Key Quotes
> "Parallelization involves executing multiple components, such as LLM calls, tool usages, or even entire sub-agents, concurrently." — Parallelization Pattern Overview, p 1 (PDF p 50)

> "The core idea is to identify parts of the workflow that do not depend on the output of other parts and execute them in parallel. This is particularly effective when dealing with external services (like APIs or databases) that have latency, as you can issue multiple requests concurrently." — p 1 (PDF p 50)

> "Note that asyncio provides concurrency, not parallelism. It achieves this on a single thread by using an event loop that intelligently switches between tasks when one is idle (e.g., waiting for a network request)... the code itself is still being executed by only one thread, constrained by Python's Global Interpreter Lock (GIL)." — Hands-On Code Example (LangChain), p 7 (PDF p 56)

> "Google ADK provides robust, native mechanisms to facilitate and manage the parallel execution of agents, significantly enhancing the efficiency and scalability of complex, multi-agent systems." — p 2 (PDF p 51)

> "The adoption of a concurrent or parallel architecture introduces substantial complexity and cost, impacting key development phases such as design, debugging, and system logging." — Key Takeaways, p 14 (PDF p 63)

## Connections
- [[Parallelization]] — the chapter's named pattern (primary concept; created from this chapter).
- [[AgenticDesignPatterns]] — book hub; this is Chapter 3 of the 21 patterns.
- [[AgenticDesignPattern]] — the meta-concept of reusable agent design patterns.
- [[AntonioGulli]] — author (code examples credited to Marco Fago / MIT-licensed in the series).
- [[PromptChaining]] — Ch 1's sequential pattern; parallelization runs independent steps that chaining would serialize.
- [[Routing]] — Ch 2's conditional pattern; the chapter pairs all three (chaining + routing + parallelization) as the core control-flow trio.
- [[ScatterGather]] / [[MapReduce]] — the CS fan-out/fan-in and map-then-reduce shapes this pattern instantiates at the agentic-orchestration level (cross-reference; those pages are the HPC/data-engineering sense).
- [[ConcurrencyVsParallelism]] — the CS/OS distinction the chapter's GIL/asyncio note relies on (cross-reference; do not conflate the multi-core sense with the agentic sense).
- [[asyncio]] — the Python concurrency substrate the LangChain example runs on (`ainvoke`, `asyncio.run`).
- [[AgentHandoff]] / [[multiagentsystems]] — the ADK `ParallelAgent` + merger pattern is concurrent multi-agent collaboration.
- [[ABTesting]] — the "multiple options generation" use case (three headline variants) is an A/B-style selection.
- [[LangChain]] / [[LangGraph]] / [[GoogleADK]] / [[CrewAI]] — frameworks; LangChain `RunnableParallel`, LangGraph parallel branches, ADK `ParallelAgent`/`SequentialAgent` (entities augmented).
- [[openai|OpenAI]] — the LangChain example drives `gpt-4o-mini` via `langchain_openai.ChatOpenAI`.
- [[gemini|Gemini]] — the ADK example uses `gemini-2.0-flash` for its `LlmAgent` researchers and merger.
- [[ToolUse]] — ADK researchers call the `google_search` tool concurrently.
- [[Latency]] / [[LatencyHiding]] — the I/O-bound latency this pattern hides by overlapping waits.

## Contradictions
- None found. The chapter's agentic-orchestration sense of "parallelization" is consistent with — and deliberately distinguished from — the wiki's HPC/CS [[ConcurrencyVsParallelism]] and [[ParallelComputing]] pages (the GIL/asyncio note explicitly flags asyncio as concurrency, not true parallel execution). It complements [[PromptChaining]] and [[Routing]] as the third control-flow pattern rather than conflicting with them.
</content>
</invoke>
