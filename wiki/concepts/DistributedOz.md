---
title: "Distributed Oz"
type: concept
tags: [programming-languages, distributed-systems, oz, network-transparency]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Distributed Oz

Network-transparent distributed programming for [[Oz]]: a program written for a single machine should run **almost unchanged** on a network of machines, with the runtime handling the transport, location, and consistency protocols. *"Making network-transparent distributed programming practical."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

## Origin

> *"This project started in 1995 in the **PERDIO project** at the DFKI with the realization that the well-factored design of the Oz language, first developed by Gert Smolka and his students in 1991 as an outgrowth of the ACCLAIM project, was a good starting point for making network transparent distribution practical. This resulted in the **[[MozartProgrammingSystem|Mozart Programming System]]** which implements Distributed Oz and was first released in 1999."*

Principal investigators: [[GertSmolka]] (DFKI), [[ChristianSchulte]] (DFKI), [[PeterVanRoy]] (joining DFKI from UCL).

## Why Oz lends itself to network transparency

The key challenge of network-transparent distribution is the **shared-state problem**: how do you make a variable look the same on multiple machines? Three Oz design choices make this tractable:

1. **[[DataflowVariable|Dataflow variables]] are single-assignment** — a variable on machine A and a reference to it on machine B agree as soon as the variable is bound; no concurrent-write reconciliation. The Distributed Oz protocol for dataflow variables is the load-bearing distribution mechanism.
2. **[[Cell|Cells]] are the only mutable state** — and a cell's atomic Exchange has well-defined distributed semantics (a single global ordering of exchanges per cell).
3. **[[FirstClassProcedures|Procedures]] are values** — they marshal across the network like any other value.

> *"Recent work has both simplified Mozart and increased its power for building fault-tolerance abstractions"* (Collet 2007 Ph.D. thesis, [[UCL]]).

## Position in the [[DefinitiveLanguage|definitive-language]] layering (Table 1)

Distributed Oz implements the **full four-layer architecture**:

- **Functional core** — *"Functions, procedures, classes, and components are closures with efficient distrib. protocols"*
- **Deterministic concurrency** — *"Dataflow concurrency with efficient protocol for dataflow variables"*
- **Message-passing concurrency** — *"Asynchronous message protocols to hide latency"*
- **Shared-state concurrency** — *"Coherent global state protocols; transactions for latency and fault tolerance"*

This is the most complete of the four converging definitive-language projects ([[Erlang]] is missing layer 2; [[E_Language|E]] is missing layer 4; [[CTM|Didactic Oz]] is the teaching variant of Distributed Oz).

## Limits of network transparency

Network transparency is **not** the same as ignoring distribution. Some realities (partial failure, latency, capacity) require explicit handling regardless of language support — Raphaël Collet's 2007 [[UCL]] Ph.D. dissertation, *The Limits of Network Transparency in a Distributed Programming Language*, formalizes where the abstraction necessarily leaks.

## In this wiki

Anchor for the **distributed-systems** branch of the [[Oz]] / [[OPM]] research line. Bridge between the 1995 [[vol1000-oz-programming-model|Smolka OPM]] formal model (single-machine), the 2009 [[vanroy-programming-paradigms-for-dummies|Van Roy paradigm chapter]] (programmer-facing survey), and the production [[MozartProgrammingSystem|Mozart implementation]] (released 1999, current 2008+). Anchored by [[vanroy-programming-paradigms-for-dummies]].
