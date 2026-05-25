---
title: "Concurrent Constraint Programming"
type: concept
tags: [programming-languages, concurrency, constraint-programming, logic-programming]
sources: [vol1000-oz-programming-model]
last_updated: 2026-05-22
---

# Concurrent Constraint Programming (CCP)

A concurrent programming model in which tasks **communicate and synchronize** through a shared **[[ConstraintStore|constraint store]]**, by **telling** constraints (asserting information) and **asking** whether constraints are **entailed** (deriving information). Formalized by **Vijay A. Saraswat** in his 1989 PhD thesis (*Concurrent Constraint Programming*, MIT Press 1993; cited as [18] in [[vol1000-oz-programming-model|Smolka 1995]]).

## Core mechanism

> *"We assume that a set of logic formulas, called constraints, is given ... We also assume that the store of a computation space holds a constraint in a special compartment, called the constraint store. The only way the constraint store can be updated is by telling it a constraint $C$, which means that the constraint store advances from $S$ to the conjunction $S \wedge C$. Finally, we assume that it is possible to synchronize a task on a constraint, called its guard. A synchronized task becomes reducible if its guard is entailed by the constraint store."*

Three primitive operations:

- **Tell** $C$: advance store $S$ to $S \wedge C$ (assert information).
- **Ask** $C$ (synchronization guard): block until $S \vdash C$ (consume information).
- **Disentailment ask**: block until $S \vdash \neg C$.

The synchronization mechanism is **monotonic** — a reducible task stays reducible as more constraints are told. The store grows monotonically; order of tells is irrelevant (conjunction is associative and commutative). *"It suffices to represent the constraint store modulo logic equivalence. This means that the synchronization mechanism is completely declarative."*

## Lineage

- **Prolog II** (Colmerauer, Kanoui & Van Caneghem 1983) — first synchronization on a constraint store, via the primitive `freeze` construct.
- **Maher 1987** — first to articulate synchronization as **entailment** of constraints.
- **Saraswat 1989/1993** — first complete CCP model: tell + ask + hiding + parallel composition over an arbitrary constraint system.
- **AKL** (Janson & Haridi 1991, SICS) — Andorra Kernel Language; first concurrent constraint language with encapsulated search; direct ancestor of Oz.

## Position in OPM

[[OPM]] adopts CCP as its kernel sublanguage ([[OPM|OCC]]) and extends it with:

- **[[FirstClassProcedures]]** — beyond CCP's pure constraint-based discipline
- **Stateful [[Cell|cells]]** — for many-to-one concurrent communication
- **[[EncapsulatedSearch|Encapsulated search]]** — via choice + search combinator, recovering constraint-logic-programming capability

## In this wiki

The wiki's first concurrent-programming-model anchor based on **declarative information propagation** rather than imperative message passing or shared-memory mutation. Contrasts with [[MessagePassing]] (CSP / actor / [[MPI]] style) and shared-memory [[Mutex]] / [[Semaphore]] / [[ConditionVariable]] disciplines covered elsewhere in the wiki. Anchored by [[vol1000-oz-programming-model]].
