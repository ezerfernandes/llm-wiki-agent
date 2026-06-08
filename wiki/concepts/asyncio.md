---
title: "asyncio (Python)"
type: concept
tags: [python, concurrency, async, event-loop, agentic-design-patterns]
sources: [agentic-design-patterns-ch03-parallelization]
last_updated: 2026-06-07
---

# asyncio (Python)

**`asyncio`** is Python's standard-library framework for writing concurrent code with the `async`/`await` syntax. It runs coroutines on a single-thread **event loop** that switches between tasks whenever one is idle (e.g. awaiting network I/O), which is why it is the substrate of choice for orchestrating concurrent LLM/tool calls in agentic frameworks.

## Role in agentic parallelization
[[AgenticDesignPatterns|*Agentic Design Patterns*]] [[agentic-design-patterns-ch03-parallelization|Ch 3 (Parallelization)]] runs its [[LangChain]] LCEL example on asyncio: the parallel `RunnableParallel` block is invoked with `await full_parallel_chain.ainvoke(topic)`, and the program entry point uses `asyncio.run(run_parallel_example(test_topic))` (the standard way to run an async function since Python 3.7+).

## Concurrency, not parallelism
The chapter is emphatic about a distinction the wiki formalizes in [[ConcurrencyVsParallelism]]:

> *"Note that asyncio provides concurrency, not parallelism. It achieves this on a single thread by using an event loop that intelligently switches between tasks when one is idle (e.g., waiting for a network request). This creates the effect of multiple tasks progressing at once, but the code itself is still being executed by only one thread, constrained by Python's Global Interpreter Lock (GIL)."* — Ch 3

So asyncio **overlaps I/O-bound waits** — exactly the case (API/database latency) where the [[Parallelization|parallelization pattern]] pays off — without delivering true multi-core parallel execution. For CPU-bound parallelism Python falls back to `multiprocessing`.

## Connections
- [[Parallelization]] — the agentic pattern asyncio implements at the LLM-orchestration level.
- [[ConcurrencyVsParallelism]] — the OS/CS distinction (event loop = concurrency; multi-core = parallelism).
- [[LangChain]] — LCEL's `ainvoke` / `RunnableParallel` run on asyncio.
- [[Latency]] / [[LatencyHiding]] — the I/O latency asyncio hides by interleaving awaits.
- [[agentic-design-patterns-ch03-parallelization]] — source.
</content>
