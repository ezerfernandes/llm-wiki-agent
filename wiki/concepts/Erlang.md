---
title: "Erlang"
type: concept
tags: [programming-languages, concurrency, message-passing, telecom, fault-tolerance]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Erlang

Concurrent programming language designed by **Joe Armstrong** and colleagues at the **Ericsson Computer Science Laboratory** starting in 1986. First efficient and stable implementation completed 1991. Designed for **programming highly available embedded systems for telecommunications**. *"An Erlang program consists of isolated named lightweight processes that send each other messages."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

## Language properties

- **[[MessagePassingConcurrency|Asynchronous message passing]]** — sender does not wait; receiver buffers
- **Functional programming** — programs are recursive functions; closures for hot code update
- **Isolated processes** — each process has its own heap; messages are copied between heaps; no shared mutable state across processes
- **Lightweight processes** — millions of processes per node are practical
- **Fault tolerance by isolation** — process crashes don't propagate; supervisor trees restart failed processes
- **Mnesia** — replicated distributed database for global coherent state ([[NamedState|named state]] layer)

## Position in the [[DefinitiveLanguage|definitive-language]] convergence (Table 1)

Erlang implements three of the four layers (missing **deterministic concurrency**):

| Layer | Erlang's realization |
|---|---|
| Functional core | A process is a recursive function in its own thread, with closures for hot code update |
| Deterministic concurrency | **(not supported)** |
| Message-passing concurrency | Fault tolerance by isolation; fault detection with messages |
| Shared-state concurrency | Global database (Mnesia) keeps consistent states |

## Why it works at scale

> *"Erlang programs can be run almost unchanged on distributed systems and multi-core processors."* — because the language has no shared mutable state across processes, scaling is **a topology problem**, not a synchronization problem.

> *"The Erlang language implements all these abilities directly with closures. This is practical and scalable: successful commercial products with more than one million lines of Erlang code have been developed (e.g., the AXD-301 ATM switch)."*

## OTP (Open Telecom Platform)

Erlang's **programming platform** — a library of generic concurrency / fault-tolerance patterns implemented as higher-order functions taking behavior-defining closures as arguments. Examples: `gen_server` (generic client/server), `gen_event` (generic event handler), supervisors. *"Used successfully in commercial systems by Ericsson and other companies"* (Ericsson 1996; Wiger 2001).

## Closure-as-fault-tolerance illustration

> *"For example, Erlang has a function that implements a generic fault-tolerant client/server. It is called with a function argument that defines the server's behavior. Aspect-oriented programming in object-oriented languages is explained in the chapter by Pierre Cointe [9]. It is usually done by syntactic transformations (called 'weaving') that add aspect code to the original source. The AspectJ language is a good example of this approach. Weaving is difficult to use because it is fragile: it is easy to introduce errors in the program (changing the source code changes the semantics of the program). Using closures instead makes it easier to preserve correctness because the source code is not changed."*

A clean illustration of [[Closure|closures]] as a **separation-of-concerns** mechanism without source-code transformation.

## In this wiki

The wiki's anchor for **Erlang as a definitive language** — production-deployed message-passing concurrency at million-LOC scale. Distinct from the wiki's existing concurrency vocabulary (mostly C / Rust / MPI). Anchored by [[vanroy-programming-paradigms-for-dummies]]; reachable from [[MessagePassingConcurrency]] / [[Closure]] / [[DefinitiveLanguage]].
