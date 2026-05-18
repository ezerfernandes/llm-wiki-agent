---
title: "Control Bus"
type: concept
tags: [computer-architecture, von-neumann, interconnect]
sources: [dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Control Bus

The **control bus** is one of the three classical [[Bus|system buses]] in the [[VonNeumannArchitecture|von Neumann architecture]] — it carries **command and control signals** (read vs write, interrupt request, bus-grant, clock, ready/busy) between the [[CPU]], [[RAM|memory]], and [[IODevice|I/O devices]] ([[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]]).

Distinct from its siblings: the [[AddressBus|address bus]] carries the **where**, the [[DataBus|data bus]] carries the **what**, and the control bus carries the **how / when**.

## Connections

- [[Bus]] — parent umbrella.
- [[AddressBus]] / [[DataBus]] — sibling buses.
- [[ControlUnit]] — the bus's primary commander.
- [[CPU]] / [[RAM]] / [[IODevice]] — endpoints.
- [[FetchDecodeExecuteCycle]] — control-bus traffic distinguishes the phases.
- [[dis-5-2-von-neumann]] — source.
