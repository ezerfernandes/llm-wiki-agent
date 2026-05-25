---
title: "Constraint Store"
type: concept
tags: [programming-languages, concurrency, constraint-programming, semantics]
sources: [vol1000-oz-programming-model]
last_updated: 2026-05-22
---

# Constraint Store

The compartment of a [[ComputationSpace|computation space]] that *"holds a constraint in a special compartment"* — a **satisfiable conjunction** $\textbf{true} \wedge C_1 \wedge C_2 \wedge \cdots \wedge C_n$ where each $C_i$ is a constraint **told** so far.

> *"The constraint store is the exclusive place where information about the values of variables is stored."* — [[vol1000-oz-programming-model|Smolka 1995]]

## Operations

- **Tell** $C$: if $S \wedge C$ is satisfiable, advance store from $S$ to $S \wedge C$; otherwise announce **failure** (handled by ignore / abort / exception).
- **Ask / synchronize on $C$**: a task with guard $C$ becomes reducible iff $S \vdash C$ (constraint store entails $C$).
- **Disentailment ask**: a conditional task `if C then E_1 else E_2` synchronizes on **both** entailment and disentailment ($S \vdash \neg C$) — *"the incremental algorithms for checking entailment automatically also check for disentailment."*

## Properties

- **Monotonic** — *"the information in the constraint store increases monotonically with every further constraint told"*. A reducible task stays reducible.
- **Order-independent** — *"the order in which constraints are told is insignificant as far as the information in the store is concerned (conjunction is an associative and commutative operation)."*
- **Modulo logic equivalence** — *"it suffices to represent the constraint store modulo logic equivalence ... the synchronization mechanism is completely declarative."*
- **Always satisfiable** — *"it is impossible to tell a constraint store $S$ a constraint $C$ if the conjunction $S \wedge C$ is unsatisfiable."*

## Constraint structures

The constraint store admits **[[BasicConstraint|basic constraints]]** from a chosen **constraint structure**. Examples used in [[OPM]] / [[Oz]]:

- **INP** — integers + names + pairs. Primitive constraints: $x = n$, $x = \xi$, $x = y \mid z$ (pair), $x = y$.
- **CFT** — feature trees (possibly infinite records). Used by Oz (extension thereof). References: Smolka & Treinen 1994 *"Records for Logic Programming"*; Backofen 1995 *"A Complete Axiomatization of a Theory with Feature and Arity Constraints"*.

## Efficiency constraint

Algorithms for telling and checking entailment/disentailment of basic constraints **must be efficient**: *"the typical complexity should be constant time, and the worst-case complexity should be quadratic or better in the size of the guard and the constraint store."* Consequently, **expressive nonbasic constraints** like $x + y = z$ or $x \cdot y = z$ **cannot be in the store** — for nonlinear constraints over integers, satisfiability is **undecidable** (Hilbert's Tenth Problem). Such constraints are accommodated as [[Propagator|propagators]] — tasks waiting until the store contains enough information to reduce them to basic constraints.

## Incremental tell

Single-step atomic tell blocks all other tells (telling $x = y$ may scan the entire store). **Incremental tell** advances the store from $S$ to a slightly stronger $S'$ entailed by $S \wedge T$ in many small **tell-reduction** steps $S \to_T S' \to_T S'' \to_T \cdots$, repeating until the store entails $T$. Required for parallel implementation. Implementations: Aït-Kaci, Podelski & Smolka 1994 (feature-based); Smolka & Treinen 1994 (records).

## In this wiki

Concept anchor for the declarative-shared-memory mechanism of [[OPM]] / [[Oz]] / [[ConcurrentConstraintProgramming]]. Contrasts with imperative shared memory ([[SharedMemory]], [[ProcessAddressSpace]]) — the constraint store can only grow (monotonic), values are partial (a variable may be only partially constrained), and synchronization is on **logical entailment** rather than acquisition of a [[Mutex|lock]].
