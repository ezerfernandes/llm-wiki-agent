---
title: "Kernel Mode"
type: concept
tags: [operating-systems, cpu, privilege, dual-mode]
sources: [dis-13-1-booting-running]
last_updated: 2026-05-17
---

# Kernel Mode

**Kernel mode** is the privileged [[CPU]] execution mode in which the [[Kernel|OS kernel]] runs. [[dis-13-1-booting-running|DIS 13.1]]: *"When OS code is run on the CPU, the system runs in kernel mode, and when user-level programs run on the CPU, the system runs in user mode."*

## Properties

- Executes **unrestricted** instructions — including privileged hardware-control instructions forbidden in [[UserMode|user mode]].
- Accesses **all memory**, including OS data structures and the kernel-mapped portion of every process's address space.
- Controls hardware directly.

## Transition

The CPU enters kernel mode on:

- A **trap instruction** issued by a user program ([[SystemCall|system call]]).
- A **hardware [[Interrupt|interrupt]]** signalled on the interrupt bus.

After the handler runs, the CPU returns to [[UserMode|user mode]] at the interrupted instruction — a [[ContextSwitch|context switch]].

## Connections

- [[UserMode]] — the unprivileged counterpart.
- [[Kernel]] — what runs in this mode.
- [[SystemCall]] / [[Interrupt]] / [[ContextSwitch]] — the entry mechanisms.
- [[DiveIntoSystems]] · [[dis-13-1-booting-running]]
