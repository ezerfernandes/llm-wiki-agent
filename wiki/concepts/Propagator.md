---
title: "Propagator (Oz)"
type: concept
tags: [programming-languages, concurrency, constraint-programming, oz]
sources: [vol1000-oz-programming-model]
last_updated: 2026-05-22
---

# Propagator

In the [[OPM|Oz Programming Model]]: a task accommodating a **nonbasic constraint** — one too expressive to live in the [[ConstraintStore|constraint store]] under the efficient-entailment-check discipline. Cited in [[vol1000-oz-programming-model|Smolka 1995]] Section 15.

## Why nonbasic constraints can't be in the store

Algorithms for telling and checking entailment of basic constraints must be efficient — *"the typical complexity should be constant time, and the worst-case complexity should be quadratic or better in the size of the guard and the constraint store."* Expressive constraints like

$$x + y = z, \quad x \cdot y = z$$

cannot meet this bar. Worse: *"for nonlinear constraints over integers satisfiability is undecidable (Hilbert's Tenth Problem)."*

## Accommodation strategy

Nonbasic constraints are accommodated as **tasks that wait** until the constraint store contains enough information that they can be **equivalently replaced with basic constraints**. Example: a propagator task $x + y = z$ may wait until the store entails $x = n \wedge y = m$ for integers $n, m$; once it does, the task reduces to the basic constraint $z = k$ where $k = n + m$.

## Another worked example: Boolean order test

$$\text{less}(x, y, z) \equiv (x < y \Leftrightarrow z = \text{True}) \wedge (z = \text{True} \vee z = \text{False})$$

This propagator reduces to $z = \text{True}$ or $z = \text{False}$ as soon as the constraint store contains sufficient information about $x$ and $y$ (lower bounds for one and upper bounds for the other suffice for many cases).

## Role in finite-domain constraint solving

Propagators are the foundational mechanism by which **finite-domain constraint solvers** (CSP solvers, [[ConstraintLogicProgramming|CLP]] over FD, modern *Gecode* / *Choco*) reduce expressive problems to a propagation-and-search loop: propagators monotonically tighten variable domains until either (i) all variables are determined (success), (ii) a domain becomes empty (failure), or (iii) propagation reaches a fixed point with multiple values remaining — at which point **[[EncapsulatedSearch|encapsulated search]]** distributes the space via a choice.

## In this wiki

Concept anchor for the *"constraints too expressive to be told as-is"* mechanism. The bridge from the **declarative** [[ConstraintStore|constraint store]] (basic constraints only, efficient entailment) to the **operational** [[EncapsulatedSearch|search engine]] (choice + distribute + propagate until fixed point). Predecessor of every modern finite-domain CSP solver's "propagator API."
