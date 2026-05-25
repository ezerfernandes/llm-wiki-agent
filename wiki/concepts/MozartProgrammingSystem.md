---
title: "Mozart Programming System"
type: concept
tags: [programming-languages, implementation, oz, distributed-systems]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Mozart Programming System

The production implementation of **[[Oz]]** and **[[DistributedOz|Distributed Oz]]**. Developed by the Mozart Consortium (German Research Center for Artificial Intelligence ([[DFKI]] Saarbrücken), Swedish Institute of Computer Science (SICS), [[UCL]] Louvain-la-Neuve). **First released 1999.** Current as of [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]]: version 1.4.0 (July 2008). Website: `www.mozart-oz.org`.

## Lineage

- **1991** — [[GertSmolka]] and students at [[DFKI]] start the [[Oz]] language as an outgrowth of the ACCLAIM Esprit project.
- **1995** — **PERDIO** project (Persistent and Distributed Programming in Oz) at DFKI; principal investigators Smolka, Schulte, and [[PeterVanRoy|Van Roy]]. Funded by BMBF.
- **1999** — Mozart Programming System first public release, implementing **[[DistributedOz|Distributed Oz]]** (network-transparent distributed programming).
- **2007+** — Mozart simplification + fault-tolerance abstractions added (Collet 2007 Ph.D. thesis at UCL).

## What it implements

- **All [[OPM|OPM]] features** from [[vol1000-oz-programming-model|Smolka 1995]] — [[ComputationSpace|computation spaces]], [[ConstraintStore|constraint store]], [[FirstClassProcedures|first-class procedures]], [[Cell|cells]], [[EncapsulatedSearch|encapsulated search]] (via search combinator)
- **[[DataflowVariable|Dataflow variables]]** with efficient distribution protocol
- **[[Concurrency|Concurrent]] [[Thread|threads]]** with fair reduction strategy
- **[[DistributedOz|Distributed Oz]]** — network transparency for the full language including dataflow variables (the hard case)
- **Programming interface based on GNU Emacs**
- **Concurrent browser**
- **Object-oriented Tcl/Tk interface for GUIs**
- **Incremental compiler**

## Reference receipts in [[vanroy-programming-paradigms-for-dummies]]

> *"This is practical if threads are efficient, such as in Mozart [34]."* (Section 6.2, on [[LazyDeclarativeConcurrency|lazy declarative concurrency]])

> *"The call `Z = {LazyAdd 2 3}` delays the addition until the value of `Z` is needed. We say that it creates a **lazy suspension**."* — Mozart implements this efficiently because its thread scheduler is lightweight.

## In this wiki

Concept anchor for the **production [[Oz]] / [[DistributedOz]] / [[OPM]] implementation** that survived from the 1995 [[DFKI]] research line into the 21st century. Distinct from research prototypes (Kernel Oz formal calculus, *DFKI Oz* of the 1995 era) and from teaching variants (Didactic Oz in [[CTM]]). Anchored by [[vanroy-programming-paradigms-for-dummies]]; reachable from [[Oz]] / [[DistributedOz]] / [[OPM]] / [[GertSmolka]] / [[PeterVanRoy]] / [[DFKI]] / [[UCL]].
