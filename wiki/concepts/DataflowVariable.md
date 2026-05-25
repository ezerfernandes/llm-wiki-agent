---
title: "Dataflow Variable"
type: concept
tags: [programming-languages, concurrency, synchronization, single-assignment, oz]
sources: [vanroy-programming-paradigms-for-dummies, vol1000-oz-programming-model]
last_updated: 2026-05-22
---

# Dataflow Variable

*"A dataflow variable is a single-assignment variable that is used for synchronization."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]]. The synchronization primitive of **[[DeclarativeConcurrency|declarative concurrent programming]]** — together with [[Thread|threads]], the two concepts that turn functional programming into a confluent concurrent paradigm.

## Three primitive operations

```
{NewVar X}    % create new dataflow variable referenced by X
{Bind X V}    % bind X to V (a value, or another dataflow variable)
{Wait X}      % current thread waits until X is bound to a value
```

All language operations are extended to **automatically wait** until their arguments are available. For example, `Add` becomes:

```oz
proc {Add X Y Z}
    {Wait X} {Wait Y}
    local R in {PrimAdd X Y R} {Bind Z R} end
end
```

The call `Z = {Add 2 3}` causes `Z` to be bound to `5`. The same discipline applies to conditionals (the `if` waits until the condition is bound) and procedure calls (waits until the procedure variable is bound).

## Why it makes concurrency declarative

Once every operation **waits on data availability**, threads compose **confluently** — *"all evaluation orders give the same result"* — and there are **no race conditions**. The result is a paradigm that:

- Behaves like [[FunctionalProgramming|functional programming]] (deterministic, declarative)
- But supports [[Concurrency|concurrency]] (multiple threads, asynchronous data production / consumption)
- And can be made lazy with one more operation: **`{WaitNeeded X}`** — the current thread waits until another thread executes `Wait X`. This gives **[[LazyDeclarativeConcurrency|lazy declarative concurrency]]** (Section 6.2), *"the most general declarative paradigm based on functional programming known so far"* (constraint programming is more general but is based on relational programming).

## Relationship to logic variables

In [[Oz]] / [[OPM|the Oz Programming Model]], the dataflow variable is essentially the **logic variable** — a single-assignment variable held in the [[ConstraintStore|constraint store]]. Read this in two ways:

- **Dataflow view** (Van Roy): `X = V` is a *bind* operation, threads block on *waits*. Semantics emphasizes synchronization.
- **Constraint view** ([[vol1000-oz-programming-model|Smolka 1995]]): `X = V` is a *tell* of the equality constraint, threads block on *guards* that synchronize on entailment. Semantics emphasizes monotonic information accumulation.

Both views describe the same operational machinery. [[ConcurrentConstraintProgramming|Constraint programming]] (Section 7 of [[vanroy-programming-paradigms-for-dummies]]) **generalizes** the dataflow variable: a constraint `X = V` is a basic equality, but constraints can also be inequalities, domain restrictions, or arbitrary logical relations — and each constraint can execute in its own concurrent thread as a [[Propagator|propagator]].

## Parallel-programming consequence

> *"Any correct program can be parallelized simply by executing its parts concurrently on different cores. ... A common programming style is to have concurrent agents connected by streams. This kind of program can be parallelized simply by partitioning the agents over the cores, which gives a pipelined execution."*

Dataflow variables turn parallelization into a **scheduling problem**, not a synchronization-correctness problem.

## In this wiki

The **load-bearing primitive** behind [[DeclarativeConcurrency]], [[Oz]]'s killer feature, and the reason Van Roy and Smolka argue [[Oz]] / [[Mozart]] / [[CTM|CTM]]-Oz is the **easy** way to do multi-core programming. Anchored by [[vanroy-programming-paradigms-for-dummies]] and [[vol1000-oz-programming-model]]; the conceptual sibling of [[ConstraintStore|the constraint store]] from the prior ingest. Distinct from the wiki's existing variable / synchronization vocabulary ([[Mutex]] / [[Semaphore]] / [[ConditionVariable]] from [[DiveIntoSystems]] Ch 14; [[CellRust]] / [[Atomic]] from [[TheEmbeddedRustBook]]) — those primitives operate over imperative mutable state, dataflow variables operate over **single-assignment immutable bindings** with **blocking-on-unbound** semantics.
