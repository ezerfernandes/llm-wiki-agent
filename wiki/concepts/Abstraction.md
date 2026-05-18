---
title: "Abstraction"
type: concept
tags: [systems, software-engineering, design]
sources: [dis-0-introduction]
last_updated: 2026-05-17
---

# Abstraction

In systems programming, an **abstraction** is a simplified, stable interface that hides the underlying implementation of a resource so that code above can be written without depending on physical details.

## The OS as abstraction provider

[[DiveIntoSystems]] Ch 0 frames the [[OperatingSystem|OS]] as the canonical abstraction provider: it exposes processes (over CPUs), virtual address spaces (over RAM), and files (over disks). Programs above use these abstractions; the OS enforces them with policies and mechanisms ([[ComputerSystem]]).

The book's thesis — *"understanding what a computer system is and how it runs your programs can help you to design code that runs efficiently"* — is essentially an argument for **peeking through** the OS's abstractions. The abstractions are necessary for productivity, but performance comes from knowing which physical details they hide and when those details matter (e.g. the [[MemoryHierarchy]]).

## Abstraction in the embedded world

The embedded-Rust corpus ([[TheEmbeddedRustBook]]) shows the dual case: when there is no OS, abstraction is provided by **trait-based** [[HardwareAbstractionLayer|HALs]] compiled in rather than syscalls dispatched at runtime. Same architectural role, different mechanism.

## Connections

- [[OperatingSystem]] — primary abstraction provider in the [[ComputerSystem|general-purpose-computer world]].
- [[HardwareAbstractionLayer]] — the embedded dual.
- [[ComputerSystem]] — the context this concept operates in.
- [[MemoryHierarchy]] — a layer where abstractions famously leak (latency/bandwidth differences are visible).
- [[ZeroCostAbstraction]] — the Rust ideal of an abstraction that compiles away to no runtime overhead.
- [[dis-0-introduction]] — source.
