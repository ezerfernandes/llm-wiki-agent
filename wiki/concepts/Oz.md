---
title: "Oz"
type: concept
tags: [programming-language, concurrent, constraint, multi-paradigm]
sources: [vol1000-oz-programming-model]
last_updated: 2026-05-22
---

# Oz

Concurrent high-level programming language designed at the [[DFKI]] Programming Systems Lab by [[GertSmolka]] and collaborators since 1991. Oz is the **concomitant programming language** of the [[OPM|Oz Programming Model]] — Oz is what OPM looks like as a programmer-facing surface syntax.

## Design intent

> *"Oz is designed as a concurrent high-level language that can replace sequential high-level languages such as Lisp, Prolog and Smalltalk. There is no other concurrent language combining a rich object system with advanced features for symbolic processing and problem solving."*

Application targets cited in [[vol1000-oz-programming-model|Smolka 1995]]: simulations, multi-agent systems, natural language processing, virtual reality, graphical user interfaces, scheduling, time-tabling, placement problems, and configuration.

## Features

- **Concurrent** by default (every composition $E_1 E_2$ is concurrent; thread sequencing is a derived discipline)
- **First-class procedures** with lexical scope
- **Logic variables** + constraint store; no static distinction between input and output arguments — *"the functionality offered by a procedure $\xi:z/E$ is simply the ability to spawn any number of tasks $E[y/z]$, where the variable $y$ replacing the formal argument $z$ can be chosen freely each time."*
- **Stateful cells** + atomic `Exchange` for concurrent state
- **Rich object system** (objects = procedures wrapping cells + serve procedures + `Self`; classes, inheritance, private attributes via names)
- **Constraint structures** beyond [[OPM|INP]] — Oz uses an extension of **CFT** (feature trees, possibly infinite records; Smolka & Treinen 1994; Backofen 1995)
- **Encapsulated search** via the search combinator — gets constraint logic programming *"out of its problem solving ghetto"* and into a lexically-scoped concurrent language
- **Threads** as reduction strategy — fair and reactive, *"as sequential as possible and as concurrent as necessary"*

## Implementation: DFKI Oz

Efficient, robust, interactive implementation for many Unix-based platforms. Components: programming interface based on GNU Emacs, concurrent browser, object-oriented Tcl/Tk interface for GUIs, powerful interoperability features, incremental compiler, runtime system with emulator and garbage collector. Freely available (1995) via `http://ps-www.dfki.uni-sb.de/`. Implementation techniques reported in Mehl, Scheidhauer & Schulte 1995 ("An Abstract Machine for Oz", PLILP'95).

## Lineage

- **Influenced by AKL** (Andorra Kernel Language; Janson & Haridi, SICS, 1991) — *"the first concurrent constraint language with encapsulated search"*
- **Extends CCP** (Saraswat 1993) with first-class procedures and cells
- **First appearance of name-based procedure interface**: Fresh (Smolka 1986)
- **Successor**: Mozart/Oz (later distributed implementation, 1999+); referenced in CTM (van Roy & Haridi, *Concepts, Techniques, and Models of Computer Programming*, MIT Press 2004)

## In this wiki

Concept anchor for [[vol1000-oz-programming-model]]. Contrasts with the wiki's existing language coverage: Oz is the first **constraint-logic + functional + OO + concurrent** language anchored; prior corpora cover [[CLanguage|C]] (imperative, sequential), [[RustLanguage|Rust]] (imperative + ownership), [[Python]] (multi-paradigm but not concurrent-by-default), and the ML / Lisp / Prolog tradition only via reference.
