---
title: "OPM (Oz Programming Model)"
type: concept
tags: [programming-languages, concurrency, constraint-programming, logic-programming, model]
sources: [vol1000-oz-programming-model]
last_updated: 2026-05-22
---

# OPM — Oz Programming Model

A concurrent programming model designed by [[GertSmolka]] at [[DFKI]] in the early 1990s and exposed in [[vol1000-oz-programming-model|Smolka 1995]]. **OPM = [[ConcurrentConstraintProgramming|concurrent constraint kernel]] + [[FirstClassProcedures|first-class procedures]] + stateful [[Cell|cells]]**, with a conservative extension for [[EncapsulatedSearch|encapsulated search]] that yields the problem-solving capabilities of constraint logic programming.

## Core architecture

Computation takes place in a **[[ComputationSpace|computation space]]** — *"a number of tasks connected to a shared store"* — that advances by **reduction of tasks**. Tasks **synchronize** on the store via **logic entailment** of their guards (monotonic: a reducible task stays reducible). The store has three compartments:

| Compartment | Holds | Updated by |
|---|---|---|
| [[ConstraintStore]] | satisfiable conjunction of basic constraints | tell ($S \leftarrow S \wedge C$) |
| [[ProcedureStore]] | procedures $\xi : z/E$ keyed by [[Name|name]] | `proc {Name X} Body end` |
| [[CellStore]] | mutable bindings $\xi : x$ keyed by name | `{NewCell V C}`, `{Exchange C X Y}` |

Names interface the three compartments: a variable bound to a name $\xi$ in the constraint store can index a procedure or a cell in the other two compartments.

## Properties

- **Concurrent, not parallel** — semantics independent of sequential vs parallel execution. *"The complexities of parallelism need only concern the implementors of OPM, not the programmers."* See [[ConcurrencyVsParallelism]].
- **Monotonic synchronization** — the constraint store grows monotonically; tasks become reducible only by accumulation of information.
- **Lexically scoped** — `local x in E` binds fresh logic variables; lexical scoping of variables and names is the basis for encapsulation and access control.
- **Higher-order** — procedures are first-class values; cells can hold variables that later become bound to procedures, enabling abstract data types with state.
- **Declarative store** — *"the constraint store is the exclusive place where information about the values of variables is stored. Dynamically created values called names interface the constraint store with the procedure and the cell store."*

## Sublanguages and extensions

- **OCC** — concurrent constraint kernel (constraint $C$ / composition $E_1 \wedge E_2$ / conditional `if C then E_1 else E_2` / declaration `local x in E`); the [[VijaySaraswat|Saraswat]]-style core
- **+ first-class procedures** — `proc {x z} E` definition and `{x y}` application; functional / higher-order programming as a facet
- **+ cells** — `NewCell` and atomic `Exchange`; concurrent stateful abstractions ([[Port|ports]], [[Agent|agents]], [[OPMObject|objects]])
- **+ [[Propagator|propagators]]** — accommodate expressive constraints ($x + y = z$, $\textit{less}(x,y,z)$) as tasks that wait for store information sufficient to reduce them to basic constraints
- **+ threads** — reduction strategy for fairness and reactivity; only the topmost task of a thread reduces, making computation as sequential as possible
- **+ choice + search combinator** — yields [[EncapsulatedSearch]] generalizing constraint logic programming; problem solvers appear as concurrent agents encapsulating search and speculative computation with constraints

## Position relative to other models

| Model | Synchronization primitive | Concurrent? | First-class procedures? | State? |
|---|---|---|---|---|
| Lambda calculus | none | no | yes | no |
| CCS / π-calculus (Milner) | channel I/O | yes | no | via processes |
| CLP (constraint logic programming) | committed-choice + unification | partial | no | no |
| CCP (Saraswat 1993) | entailment of guards | yes | no | no |
| **OPM (Smolka 1995)** | **entailment of guards** | **yes** | **yes** | **via cells** |

OPM is the first model unifying all four columns. Calculi formalizing the major aspects are in *The Definition of Kernel Oz* (Smolka 1995) and *A Foundation for Higher-Order Concurrent Constraint Programming* (Smolka 1994).

## In this wiki

Anchored by [[vol1000-oz-programming-model|Smolka 1995]]. Realized as the language [[Oz]]. Contrasts with the wiki's existing shared-memory threading vocabulary ([[Pthreads]], [[Mutex]], [[Semaphore]], [[ConditionVariable]] from [[DiveIntoSystems]] Ch 14; [[Concurrency]] from [[TheEmbeddedRustBook]]): OPM replaces mutex / semaphore primitives with declarative logic entailment.
