---
title: "The Oz Programming Model"
type: source
tags: [paper, programming-languages, concurrency, constraint-programming, logic-programming, foundational]
date: 1995-07-01
source_file: raw/papers/vol1000-oz-programming-model.pdf
---

## Summary

**Gert Smolka (DFKI Programming Systems Lab, July 1995; appeared in *Computer Science Today*, J. van Leeuwen ed., LNCS Vol. 1000, pp. 324–343, Springer-Verlag).** Informal exposition of the **[[OPM|Oz Programming Model]]** — a concurrent programming model subsuming higher-order functional and object-oriented programming as facets of a single general model, designed alongside the concurrent high-level language **[[Oz]]** at [[DFKI]] since 1991. OPM extends the [[ConcurrentConstraintProgramming|concurrent constraint]] model of [[VijaySaraswat|Saraswat]] with **[[FirstClassProcedures|first-class procedures]]** and stateful **[[Cell|cells]]**, and admits a conservative extension for [[EncapsulatedSearch|encapsulated search]] that generalizes constraint logic programming. Computation takes place in a **[[ComputationSpace|computation space]]** hosting tasks connected to a shared store (constraint store + procedure store + cell store); tasks **synchronize** on the store via **logic entailment** of their guards. The first wiki source from the **programming-language-theory** corpus and the first to anchor concurrent constraint programming, the [[Oz]] language, and Smolka's research program.

## Key Claims

- **OPM is concurrent but nonparallel.** *"Concurrency means that one can create several simultaneously advancing computations ... Parallelism means that the execution of several hardware operations overlaps in time."* OPM admits parallel implementation but the semantics does not depend on it.
- **Synchronization = logic entailment.** A task with guard $C$ becomes reducible only once the constraint store entails $C$. Synchronization is **monotonic**: *"a reducible task stays reducible if other tasks are reduced before it."*
- **Store has three compartments.** (i) [[ConstraintStore|Constraint store]] — a satisfiable conjunction of [[BasicConstraint|basic constraints]]; (ii) [[ProcedureStore|procedure store]] — finitely many procedures $\xi : z/E$ indexed by [[Name|names]]; (iii) [[CellStore|cell store]] — finitely many mutable bindings $\xi : x$ of names to variables. *"The constraint store is the exclusive place where information about the values of variables is stored."*
- **OCC sublanguage.** Concurrent constraint kernel with four expression forms: constraint $C$, composition $E_1 \wedge E_2$, conditional `if C then E_1 else E_2`, declaration `local x in E`. The conditional synchronizes on **both entailment and disentailment** of its guard.
- **First-class procedures via names.** A procedure $\xi : z/E$ is a triple: name, formal argument, body. *"The idea to interface variables and procedures through freshly chosen names appeared first in Fresh."* Procedures enable functional / higher-order programming as a facet of OPM.
- **Cells enable many-to-one communication.** A [[Cell|cell]] is a mutable binding of a name to a variable. **Exchange** combines read and write into a single atomic operation, providing mutual exclusion and indeterminism — *"this atomic combination turns out to be expressive since one can write a new variable into a cell whose value will be computed only afterwards from the value of the old variable in the cell."*
- **Ports, agents, objects are higher-order abstractions over cells.** A [[Port|port]] = procedure connected to a stream (incrementally constrained list); an [[Agent|agent]] = port + serve procedure processing messages with internal state; an [[OPMObject|object]] = procedure $\{Object\ Message\}$ wrapping cell + serve procedure with `Self`. *"Agents are stationary and objects are mobile"* — under distribution, an agent serves messages at its creation site; an object serves at the application site.
- **Incremental tell.** Telling a constraint $T$ as a single atomic step blocks other tells; incremental tell advances the store to a slightly stronger $S'$ entailed by $S \wedge T$ in many small steps via tell reductions $\to_T$. Required for parallel implementation.
- **[[Propagator|Propagators]] handle expressive constraints.** Nonbasic constraints (e.g., $x + y = z$, $\textit{less}(x, y, z)$) cannot be in the store (entailment must be cheap — *"the typical complexity should be constant time, and the worst-case complexity should be quadratic or better"*; for nonlinear integer constraints satisfiability is undecidable — Hilbert's Tenth). Instead they live as **tasks** waiting until the store contains enough information to reduce to basic constraints.
- **Threads as reduction strategy.** Naive breadth-first reduction makes `{Fib 5 M}` take exponential space. A **thread** is a nonempty stack of tasks; only the topmost task reduces; threads guarantee fair progress. *"Tries to be as sequential as possible and as concurrent as necessary."*
- **Encapsulated search via choice + search combinator.** A choice $E_1$ **or** $E_2$ distributes a computation space into two alternatives, producing a search tree. The **search combinator** spawns a subordinate computation space and returns the two alternative local spaces as first-class procedures on distribution — encapsulating Prolog-style search into concurrent agents without polluting the top-level space. *"Oz gets constraint logic programming out of its problem solving ghetto."*

## Key Quotes

> "Computer systems are undergoing a revolution. Twenty years ago, they were centralized, isolated, and expensive. Today, they are parallel, distributed, networked, and inexpensive. However, advances in software construction have failed to keep pace with advances in hardware." — opening framing for the entire concurrent-programming research agenda

> "OPM is a concurrent programming model that subsumes higher-order functional and object-oriented programming as facets of a general model. This is particularly interesting for concurrent object-oriented programming, for which no comprehensive formal model existed until now."

> "The reason for making OPM concurrent but not parallel is the desire to make things as simple as possible for programmers. In OPM, the semantics of programs does not depend on whether they run on a sequential or parallel implementation."

> "The constraint store is the exclusive place where information about the values of variables is stored. Dynamically created values called names interface the constraint store with the procedure and the cell store. This way OPM realizes an orthogonal combination of first-order constraints with first-class procedures and stateful cells."

> "Oz gets constraint logic programming out of its problem solving ghetto and integrates it into a concurrent and lexically scoped language with first-class procedures and state. This integration eliminates the need for Prolog's ad hoc constructs and also increases the expressivity of the problem solving constructs."

## Connections

- [[GertSmolka]] — author, DFKI Programming Systems Lab
- [[DFKI]] — German Research Center for Artificial Intelligence, Saarbrücken; institutional home of Oz / OPM
- [[OPM]] — the model itself (concept anchor)
- [[Oz]] — the concomitant language; this paper is its semantic-model companion to *The Oz Primer* (Smolka 1995) and *The Definition of Kernel Oz* (Smolka 1995)
- [[ConcurrentConstraintProgramming]] — Saraswat's framework; OPM extends it with first-class procedures and cells
- [[ComputationSpace]] — execution context (tasks + store); central abstraction
- [[ConstraintStore]] — declarative logic-formula compartment of the store
- [[FirstClassProcedures]] — Scheme / SML / Haskell feature here lifted into a concurrent constraint setting
- [[Cell]] — mutable name-to-variable bindings; basis for stateful concurrent abstractions
- [[Port]] — stream-based agent communication primitive
- [[Agent]] — active object pattern; stationary under distribution
- [[OPMObject]] — concurrent-OOP model from procedures + cells + names
- [[Propagator]] — task-based accommodation of expressive constraints (e.g., arithmetic)
- [[EncapsulatedSearch]] — search combinator + choice combinator yielding constraint-logic-programming capability as concurrent agents
- [[ConcurrencyVsParallelism]] — existing wiki page; this paper provides the canonical *"concurrent but not parallel"* framing
- Related but not pulled into the wiki yet: Prolog II (Colmerauer / Kanoui / Caneghem, 1983) — first appearance of synchronization on a constraint store via `freeze`; AKL (Janson & Haridi, 1991) — first concurrent constraint language with encapsulated search; CCS (Milner, 1980) and π-calculus (Milner, 1992) — well-founded concurrent models OPM positions against; Obliq (Cardelli, POPL'95) — distributed scope with first-class procedures and concurrent state, cited as kindred work; CFT (Smolka & Treinen 1994; Backofen 1995) — feature-tree constraint structure Oz extends.

## Contradictions

- None — first paper in the wiki on programming-language theory / concurrent constraint programming. **Live tension** with the wiki's existing concurrency vocabulary, which is grounded in shared-memory POSIX [[Pthreads]] (from [[DiveIntoSystems]] Ch 14) and bare-metal [[Concurrency]] + [[Mutex]] (from [[TheEmbeddedRustBook]]): both prior corpora treat the **mutex / semaphore / barrier** family as the synchronization primitive; OPM replaces those with **logic entailment of guards over a declarative constraint store** — a fundamentally different (declarative, monotonic, lexically-scoped) discipline. Not a contradiction in claims, a contrast in design space; flagged for future synthesis on *"what shared-memory threading and concurrent constraint programming would learn from each other."*
