---
title: "Observable Nondeterminism"
type: concept
tags: [programming-languages, semantics, concurrency, nondeterminism]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Observable Nondeterminism

A property of a [[ProgrammingParadigm|paradigm]]: *"nondeterminism is when the execution of a program is not completely determined by its specification"* — and **observable** if *"a user can see different results from executions that start at the same internal configuration."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

Van Roy treats this as the **first key paradigm-classification axis** (Figure 2 — paradigms with observable nondeterminism are drawn with a heavy border).

## When it appears

- During execution, the choice made by the run-time scheduler may produce different observable results across runs.
- Combined with [[NamedState|named state]], observable nondeterminism produces **[[RaceCondition|race conditions]]**: *"the result of a program depends on precise differences in timing between different parts of a program (a 'race')."*

## When it is unavoidable

Observable nondeterminism is *needed* to **model real-world interaction**:

- A client/server application with two clients is inherently nondeterministic since the server cannot know which client's next command will arrive first.
- But: **the nondeterminism is at the boundary**, not inside the components. *"The client and server implementations can themselves be completely deterministic."*

## When it should be avoided

For most internal computation, observable nondeterminism is **undesirable**. *"This is highly undesirable. A typical effect is a race condition."* Van Roy recommends limiting observable nondeterminism to those parts of the program that really need it, and choosing a paradigm that **cannot express** observable nondeterminism for the rest.

Four [[ConcurrencyParadigm|concurrent paradigms]] have no observable nondeterminism (Table 2): [[DeclarativeConcurrency]], [[ConcurrentConstraintProgramming|constraint programming]], [[FunctionalReactiveProgramming|functional reactive programming]], and [[DiscreteSynchronousProgramming|discrete synchronous programming]]. [[MessagePassingConcurrency|message-passing concurrency]] ([[Erlang]], [[E_Language|E]]) has races possible and nondeterministic inputs.

## In this wiki

The first paradigm-axis concept anchored. The wiki's existing concurrency vocabulary ([[Pthreads]] / [[Mutex]] from [[DiveIntoSystems]], shared-state / message-passing from [[TheEmbeddedRustBook]]) operates entirely in the **observable-nondeterminism = yes** half of Van Roy's taxonomy; this concept is the structural reason those paradigms are hard to reason about.
