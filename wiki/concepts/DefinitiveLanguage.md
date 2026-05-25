---
title: "Definitive Language"
type: concept
tags: [programming-languages, design, multiparadigm, layered-architecture]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Definitive Language

A programming language whose design is **good enough that researchers move on to work at higher levels of abstraction**. *"At some point in time, language research will give solutions that are good enough that researchers will move on to work at higher levels of abstraction. This has already arrived for many subareas of language design, such as assembly languages and parsing algorithms."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

## The four converging projects (Table 1)

Van Roy reports the surprising empirical finding that **four independent research projects, solving four very different problems, all converged on the same four-layer language architecture** — *"Convergence in Language Design: A Case of Lightning Striking Four Times in the Same Place"* (Van Roy 2006, FLOPS).

| Layer | [[Erlang]] | [[E_Language|E]] | [[DistributedOz|Distributed Oz]] | [[CTM|Didactic Oz]] |
|---|---|---|---|---|
| **Functional core** | A process is a recursive function in its own thread, with closures for hot-code update | An object is a recursive function with a local state | Functions, procedures, classes, components are closures with efficient distribution protocols | Closures are the foundation of all paradigms |
| **Deterministic concurrency** | (not supported) | Deterministic execution of all objects in one vat (process) | Dataflow concurrency with efficient protocol for [[DataflowVariable|dataflow variables]] | Concurrency is as easy as functional programming, no race conditions |
| **Message-passing concurrency** | Fault tolerance by isolation; fault detection with messages | Security by isolation; messages between objects in different vats | Asynchronous message protocols to hide latency | Multi-agent programming is expressive and easy to program |
| **Shared-state concurrency** | Global database (Mnesia) keeps consistent states | (not supported) | Coherent global state protocols; transactions for latency and fault tolerance | Named state for modularity |

## The four projects

1. **[[Erlang]]** (Armstrong & Ericsson Computer Science Lab, 1986+) — programming highly available embedded systems for telecommunications. Stable implementation 1991. Isolated lightweight processes + messages + Mnesia replicated database. Used commercially by Ericsson and others (AXD-301 ATM switch — >1M LOC).
2. **[[E_Language|E]]** (Dennis & Van Horn capability model 1965 → Hewitt Actor model 1973 → concurrent logic programming → E by Barnes, Miller et al.) — programming secure distributed systems with multiple users and multiple security domains. Isolated single-threaded **vats** hosting active objects + asynchronous messages between vats; deterministic concurrency *inside* a vat (because nondeterminism can support a covert channel).
3. **[[DistributedOz|Distributed Oz]]** (PERDIO project at [[DFKI]], 1995; Smolka, Schulte, Van Roy) — making network-transparent distributed programming practical. Realized in the [[MozartProgrammingSystem|Mozart Programming System]] (first released 1999).
4. **[[CTM|Didactic Oz]]** (Van Roy & Haridi 2004 [[CTM]] textbook) — teaching programming as a unified discipline covering all popular paradigms. Used in the second-year [[UCL]] FSAB1402 course since 2005.

## Conclusions Van Roy draws from the convergence

1. **Declarative programming is at the core** of programming languages. Already well-known; this study reinforces.
2. **Declarative programming will stay at the core** for the foreseeable future, because distributed / secure / fault-tolerant programming are essential topics that need declarative support.
3. **Deterministic concurrency is an important form of concurrent programming that should not be ignored.** *"Deterministic concurrency is an excellent way to exploit the parallelism of multi-core processors because it is as easy as functional programming and it cannot have race conditions."*
4. **Message-passing concurrency is the correct default for general-purpose concurrent programming instead of shared-state concurrency.**

## In this wiki

The wiki's anchor for **convergent language design** as an empirical question. Anchored by [[vanroy-programming-paradigms-for-dummies]]. Sibling concept: [[DualParadigmLanguage]] (two-paradigm minimum for non-toy programs). Connects to [[CTM]] / [[Erlang]] / [[DistributedOz]] / [[MozartProgrammingSystem]].
