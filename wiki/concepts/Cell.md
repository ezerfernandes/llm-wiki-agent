---
title: "Cell (Oz)"
type: concept
tags: [programming-languages, concurrency, state, oz]
sources: [vol1000-oz-programming-model]
last_updated: 2026-05-22
---

# Cell

In the [[OPM|Oz Programming Model]]: a **mutable binding** $\xi : x$ of a [[Name|name]] $\xi$ to a logic variable $x$, held in the [[ComputationSpace|computation space's]] **cell store**. Cells are *"OPM's third and final compartment"* of the store (alongside [[ConstraintStore|constraint store]] and procedure store). They are *"a mutable binding of a name to a variable"* enabling stateful and concurrent data structures and the *"communication medium between concurrent agents."*

## Operations

- **`{NewCell X Y}`** — choose fresh name $\xi$, tell $Y = \xi$, write the new cell $\xi : X$ into the cell store. Once entered, a cell **cannot be retracted**.
- **`{Exchange X Y Z}`** — wait until the cell store contains $\xi : u$ with $X = \xi$; **atomically** update the cell to host $Z$ and tell $Y = u$ (so the variable $Y$ becomes bound to the *old* hosted variable $u$).

## Properties

- **Atomic exchange** combines read and write into a single non-interruptible step — provides mutual exclusion and indeterminism *"as needed for many-to-one communication."*
- **Different from imperative assignable variables** — Exchange's atomicity matters because, in the presence of logic variables, *"one can write a new variable into a cell whose value will be computed only afterwards from the value of the old variable in the cell. This cannot be obtained in an imperative setting since it requires that consumers of a variable are automatically synchronized on the event that the value of the variable becomes known."*

## What cells enable

- [[Port|Ports]] — message queues built on a stream + private cell
- [[Agent|Agents]] — port + serve procedure + initial state
- [[OPMObject|Objects]] — procedures wrapping cell + serve procedure + Self for concurrent OOP

## In this wiki

Concept anchor from [[vol1000-oz-programming-model]]. Distinct from the [[CellRust]] / [[RefCell]] / [[UnsafeCell]] family in the [[RustLanguage|Rust]] [[TheEmbeddedRustBook|embedded]] corpus (those provide interior mutability under [[Borrow|borrow]]-checking discipline; OPM cells provide concurrent atomic exchange under logic-variable discipline) and from the [[MemoryCell]] [[MemoryHierarchy|memory-hierarchy]] concept (hardware storage unit).
