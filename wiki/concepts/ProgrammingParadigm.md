---
title: "Programming Paradigm"
type: concept
tags: [programming-languages, paradigms, taxonomy]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Programming Paradigm

*"A programming paradigm is an approach to programming a computer based on a mathematical theory or a coherent set of principles. Each paradigm supports a set of concepts that makes it the best for a certain kind of problem."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

Defined by a set of [[ProgrammingConcept|programming concepts]], organized into a simple core language called the paradigm's **[[KernelLanguage|kernel language]]**. Different paradigms differ by adding or removing concepts.

## Van Roy's taxonomy (27 paradigms)

The chapter names 27 practically useful paradigms (Figure 2), organized by **observable nondeterminism** and **expressiveness of state** axes:

- **Pure declarative** (no observable nondeterminism, no named state): descriptive declarative, [[FirstClassProcedures|first-order functional]], **functional programming**, [[ConcurrentConstraintProgramming|concurrent constraint]], lazy / monotonic dataflow, [[FunctionalReactiveProgramming|functional reactive]], [[DiscreteSynchronousProgramming|discrete synchronous]], deterministic logic, relational & logic
- **Imperative** (named state, sequential): imperative programming, [[FirstClassProcedures|imperative ADT functional]], ADT imperative, guarded command (Dijkstra), imperative search
- **Concurrent with named state**: event-loop, multi-agent dataflow, [[MessagePassingConcurrency|message-passing concurrent]], [[SharedStateConcurrency|shared-state concurrent]], software transactional memory (STM), sequential object-oriented, stateful functional, concurrent object-oriented, active object
- **Logic / constraint**: deterministic logic, relational & logic, [[ConcurrentConstraintProgramming|constraint (logic)]], [[ConcurrentConstraintProgramming|concurrent constraint]], lazy concurrent constraint

## Two organizing properties

- **[[ObservableNondeterminism|Observable nondeterminism]]** — yes/no. Required to model real-world interaction (client/server) but should be limited; gives rise to [[RaceCondition|race conditions]] when combined with [[NamedState|named state]].
- **[[NamedState|Named state]]** — none / unnamed / named, with sub-axes deterministic-vs-nondeterministic and sequential-vs-concurrent. Required for **modularity** (extending a component without rewriting all callers).

## The combinatorial space

With $n$ concepts one can construct up to $2^n$ paradigms. Many are useless (the empty paradigm) or one-concept-only; many more emerge from carefully chosen combinations. *"Often two paradigms that seem quite different (for example, functional programming and object-oriented programming) differ by just one concept."* Functional programming is the most important seed because closure / lambda calculus is Turing complete and adds the minimum to construct any other paradigm via the [[CreativeExtensionPrinciple|creative extension principle]].

## In this wiki

Concept anchor for [[vanroy-programming-paradigms-for-dummies]]. The wiki's first PL-paradigm-taxonomy entry. Connects to the [[KernelLanguage]] / [[CreativeExtensionPrinciple]] / [[DualParadigmLanguage]] / [[DefinitiveLanguage]] axes Van Roy uses to navigate the design space.
