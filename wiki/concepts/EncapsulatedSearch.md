---
title: "Encapsulated Search"
type: concept
tags: [programming-languages, constraint-programming, logic-programming, search]
sources: [vol1000-oz-programming-model]
last_updated: 2026-05-22
---

# Encapsulated Search

A mechanism for confining **constraint-logic-programming-style search** (Prolog-style backtracking, branch-and-bound, etc.) into a concurrent agent that does not pollute the top-level computation. Introduced in the [[OPM|Oz Programming Model]] context by [[GertSmolka]] and Christian Schulte; cited in [[vol1000-oz-programming-model|Smolka 1995]] (Section 18).

## Building blocks

**Nondeterministic choice combinator** — an expression

$$E_1 \mathbf{\ or\ } E_2$$

called a **choice**. A choice task is reducible **only if no other task is reducible** (deterministic computation has priority). Its reduction **distributes** the [[ComputationSpace|computation space]] into two spaces obtained by replacing the choice with $E_1$ and $E_2$ respectively. The resulting **search tree of spaces** is explored by a suitable strategy; failed leaves abort, unfailed leaves carry solutions as variable bindings.

**Problem**: distributing the **top-level** space is incompatible with concurrent computation — the whole world forks.

**Solution: the search combinator** — a primitive that spawns a **subordinate** computation space and reduces only once the subordinate space fails, becomes irreducible, or is distributed. On distribution, the two alternative local spaces are **frozen** and returned as **first-class procedures** (citizens of the parent space).

> *"What we would like to have are concurrent agents to which we can present a search strategy and a problem to be solved and from which we can request the solutions of the problem one by one. This means that the search agent should encapsulate search."* — [[vol1000-oz-programming-model|Smolka 1995]]

## Consequence

[[Oz]] integrates the full **problem-solving capability** of constraint logic programming into a **lexically scoped, concurrent, higher-order** language:

> *"Oz gets constraint logic programming out of its problem solving ghetto and integrates it into a concurrent and lexically scoped language with first-class procedures and state. This integration eliminates the need for Prolog's ad hoc constructs and also increases the expressivity of the problem solving constructs."*

## Lineage and references

- **AKL** (Janson & Haridi 1991, SICS) — *"the first concurrent constraint language with encapsulated search"* (cited as predecessor)
- Schulte & Smolka 1994, *"Encapsulated search in higher-order concurrent constraint programming"* (LP'94)
- Schulte, Smolka & Würtz 1994, *"Encapsulated search and constraint programming in Oz"* (PPCP'94)
- Müller, Popow, Schulte & Würtz 1994, *"Constraint programming in Oz"* (DFKI documentation)
- Smolka 1995, *"The Definition of Kernel Oz"* — formal calculus

## In this wiki

The wiki's first concept anchor for **search as a first-class language feature**. Distinct from search algorithms used in ML / RL ([[beamsearch]], [[mcts]], [[grpo|GRPO]] rollouts, [[2507.19457-gepa|GEPA]] reflective mutation): encapsulated search operates over a logical constraint space with sound backtracking semantics, not over a sampled action space with stochastic rewards. The intellectual ancestor of modern **finite-domain constraint solvers** (Gecode, Choco) and the *Mozart* programming system (the successor to DFKI Oz).
