---
title: "Computation Space"
type: concept
tags: [programming-languages, concurrency, constraint-programming, semantics]
sources: [vol1000-oz-programming-model]
last_updated: 2026-05-22
---

# Computation Space

The central execution-context abstraction of the [[OPM|Oz Programming Model]]: *"a number of **tasks** connected to a shared **store**."* Computation advances by **reduction of tasks** — *"the reduction of a task can manipulate the store and create new tasks. When a task is reduced it disappears. Reduction of tasks is an atomic operation, and tasks are reduced one by one. Thus there is no parallelism at the abstraction level of OPM."*

## Structure

```
    Task    ...    Task
            |
          Store
```

The **store** has three compartments ([[OPM]]):

- [[ConstraintStore]] — satisfiable conjunction of basic constraints (the only place information about variable values lives)
- [[ProcedureStore]] — name-indexed procedures $\xi : z/E$
- [[CellStore]] — name-indexed mutable bindings $\xi : x$

## Reduction strategies

A **reduction strategy** picks the next reducible task. Required properties:

- **Fairness** — *"ensures that several groups of tasks can advance simultaneously"*
- **Reactivity** — *"one can create computations that react to outside events within foreseeable time bounds"*
- **Efficiency** — production-quality implementation

The naive strategy (FIFO queue of tasks) is fair but **inefficient** — Fibonacci would traverse its recursion tree in breadth-first order, taking exponential space. The efficient strategy organizes tasks into **threads** — nonempty stacks of tasks, where only the **topmost** task can reduce; fairness is guaranteed at the thread level. *"Tries to be as sequential as possible and as concurrent as necessary."*

## Encapsulated search via space distribution

A choice task `E_1 or E_2` is reducible only when no other task is reducible. Reduction **distributes** the computation space into two child spaces obtained by replacing the choice with $E_1$ and $E_2$ respectively. The resulting **search tree of computation spaces** can be explored with a suitable strategy; failed spaces are aborted; unfailed leaves contain solutions as bindings of certain variables.

The **search combinator** spawns a **subordinate** computation space; on distribution, the two alternative subordinate spaces are frozen and returned as **first-class procedures**. This encapsulates Prolog-style search into concurrent agents without polluting the top-level space — see [[EncapsulatedSearch]].

## Distribution (across machines)

OPM can be extended to distributed programming by assigning a **site** to every task and assuming the store is transparently distributed; new tasks inherit the creating task's site. Under distribution:

- **[[Agent|Agents]] are stationary** — messages served at the agent's creation site
- **[[OPMObject|Objects]] are mobile** — messages served at the application site

## In this wiki

Concept anchor for the central abstraction of [[OPM]] / [[Oz]]. Distinct from the wiki's existing process / thread / address-space vocabulary ([[Process]] / [[Thread]] / [[ProcessAddressSpace]] from [[DiveIntoSystems]] Ch 13–14) — a computation space is a **declarative store + reducible-task** abstraction, not a [[OperatingSystem|OS]]-level scheduling unit.
