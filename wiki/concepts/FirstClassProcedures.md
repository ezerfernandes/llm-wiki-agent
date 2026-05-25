---
title: "First-Class Procedures"
type: concept
tags: [programming-languages, functional-programming, higher-order]
sources: [vol1000-oz-programming-model]
last_updated: 2026-05-22
---

# First-Class Procedures

A programming-language property: procedures (functions) are values that can be passed as arguments, returned from other procedures, and stored in data structures, with **lexical scoping** of their global variables.

A language **provides first-class procedures if** ([[vol1000-oz-programming-model|Smolka 1995]]):

1. *"procedures can create new procedures"*
2. *"procedures can have lexically scoped global variables"*
3. *"procedures are referred to by first-class values"*

> *"First-class procedures are available in functional programming languages such as Scheme, SML or Haskell. They are typically not available in today's concurrent programming languages although they can provide crucial functionality for concurrent and distributed programming."* — Smolka 1995

## In OPM

[[OPM]] is the first concurrent-constraint model to integrate first-class procedures. A procedure is a triple $\xi : z/E$ — a [[Name|name]] $\xi$, formal argument $z$, body $E$. The **procedure store** (one of three [[ComputationSpace|computation-space]] compartments) holds finitely many procedures keyed by name; once entered, a procedure cannot be retracted. Information about a procedure's global variables lives in the [[ConstraintStore|constraint store]] — *"what we call a procedure is often called a closure in the literature."*

Two new expressions:

- **Definition** `proc {x z} E` — chooses fresh name $\xi$, tells $x = \xi$, writes $\xi : z/E$ into the procedure store. Always reducible.
- **Application** `{x y}` — waits until the procedure store contains $\xi : z/E$ such that $x = \xi$; then reduces to $E[y/z]$ (body with formal $z$ replaced by actual $y$, avoiding capture).

## Why it matters for concurrent programming

First-class procedures give OPM:

- **Lazy and eager higher-order functional programming** — e.g. `MkMap` builds a list-mapping procedure from a value-mapping procedure (Section 7).
- **Concurrent functions** — a procedure call spawns tasks that synchronize on its argument variables; *"since our model employs logic variables, there is no static distinction between input and output arguments."*
- **Abstract concurrent data types with state** — combined with [[Cell|cells]] and lexical scoping, [[Port|ports]] / [[Agent|agents]] / [[OPMObject|objects]] are derived abstractions, not primitives.
- **Distributed programming** — compute servers, mobile code, Cardelli's *Obliq* (POPL'95) cited as kindred work.

## First appearance of the design

> *"The idea to interface variables and procedures through freshly chosen names appeared first in Fresh."* — Smolka 1986, *"Fresh: A higher-order language with unification and multiple results"*

## In this wiki

The wiki's first concept anchor for **higher-order programming** as a language-design feature (rather than as a Python / Rust feature exercised in passing). Contrasts with: the [[CLanguage|C]] [[FunctionPointer|function pointer]] (callable but no closure / no lexical scope), [[Java]] methods (tied to classes, not first-class until lambdas), and Scheme / SML / Haskell (first-class but in *purely* sequential settings). [[OPM]] / [[Oz]] is the first integration into a concurrent constraint setting.
