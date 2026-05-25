---
title: "Declarative Concurrency"
type: concept
tags: [programming-languages, concurrency, deterministic, dataflow, oz]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Declarative Concurrency

A **concurrent paradigm with no observable nondeterminism** — confluent like [[FunctionalProgramming|functional programming]] but supporting threads and asynchronous data production / consumption. Also called **monotonic dataflow programming**. *"Declarative concurrency has the main advantage of functional programming, namely confluence, in a concurrent model. This means that all evaluation orders give the same result, or in other words, it has no race conditions."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

## Two added concepts (vs functional programming)

- **[[Thread|Threads]]** — `{NewThread P}` creates a new thread executing the 0-argument procedure `P`. A thread defines a sequence of instructions executed independently of other threads.
- **[[DataflowVariable|Dataflow variables]]** — single-assignment variables with `NewVar` / `Bind` / `Wait` primitives. All language operations are extended to **wait on data availability**, making the model declarative.

## Properties

- **Deterministic** — same inputs always give the same output; *"any part of a correct program can be executed concurrently without changing the results"*
- **No race conditions** — race conditions require [[NamedState|named state]] + concurrent unsynchronized writes; dataflow variables are single-assignment, no such race exists
- **Concurrent inputs must be deterministic** — *"if there are multiple input streams, they must be deterministic, i.e., the program must know exactly what input elements to read to calculate each output (for example, there could be a convention that exactly one element is read from each input stream)"*
- **Lazy extension stays declarative** — [[LazyDeclarativeConcurrency|lazy declarative concurrency]] adds `WaitNeeded` for by-need synchronization; still confluent

## Languages

[[Oz]] [50, 34], [[Alice]] [38]. Also: [[CTM]] Chapter 4 uses declarative concurrency as the primary teaching paradigm for concurrent programming.

## Why this matters for multi-core

> *"Declarative concurrency is a good paradigm for parallel programming [53]. This is because it combines concurrency with the good properties of functional programming. ... Any correct program can be parallelized simply by executing its parts concurrently on different cores. Paradigms that have named state (variable cells) make this harder because each variable cell imposes an order."*

Van Roy's policy recommendation: **declarative concurrency as the default for parallel programming**; named state only where required. Common idiom: *"concurrent agents connected by streams ... can be parallelized simply by partitioning the agents over the cores, which gives a pipelined execution."*

## Position in Table 2 (no-observable-nondeterminism paradigms)

| Paradigm | Races possible? | Nondeterministic input? | Languages |
|---|---|---|---|
| **Declarative concurrency** | No | No | [[Oz]], [[Alice]] |
| [[ConcurrentConstraintProgramming|Constraint programming]] | No | No | [[Gecode]], [[Numerica]] |
| [[FunctionalReactiveProgramming|Functional reactive programming]] | No | Yes | [[FrTime]], [[Yampa]] |
| [[DiscreteSynchronousProgramming|Discrete synchronous programming]] | No | Yes | [[Esterel]], [[Lustre]], [[Signal]] |
| Message-passing (for contrast) | Yes | Yes | [[Erlang]], [[E_Language|E]] |

Declarative concurrency is **the strictest** of the four no-nondeterminism paradigms — it requires inputs themselves to be deterministic. The next paradigms relax this constraint.

## In this wiki

The wiki's first paradigm anchor for **deterministic concurrent programming**. Built on [[DataflowVariable|dataflow variables]] (the load-bearing primitive) and [[Thread|threads]]. Realized in [[Oz]] / [[Alice]] / [[CTM]] (didactic version). Contrasts with the wiki's existing [[Pthreads]] / [[Mutex]] (shared-memory imperative, observable nondeterminism) and [[MPI]] (distributed-memory message passing, observable nondeterminism) vocabulary — declarative concurrency is a strict alternative occupying a different paradigm-space quadrant.
