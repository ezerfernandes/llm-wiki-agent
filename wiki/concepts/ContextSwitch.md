---
title: "Context Switch"
type: concept
tags: [operating-systems, scheduling, performance, kernel, interrupts]
sources: [parproc-appA-systems-issues, dis-13-1-booting-running]
last_updated: 2026-05-17
---

# Context Switch

A **context switch** is the OS operation of suspending one process and resuming another by saving and restoring CPU register state. It is the mechanical core of [[Timesharing]].

## Mechanism

When a quantum expires (or a process voluntarily yields), a timer interrupt transfers control to the OS. The OS:

1. Saves all register values of the outgoing process — including the Program Counter (PC/instruction pointer) and the EFLAGS register — into the process' entry in the *process table*.
2. Loads the saved register values of the incoming process from its process table entry.
3. Jumps to the loaded PC value, causing the CPU to resume the incoming process exactly where it was suspended.

The CPU itself is unaware that any switch occurred; it simply executes instructions at whatever address the PC holds.

## Cost

Context switches are not free. Each switch invalidates or pollutes CPU caches and the [[TranslationLookasideBuffer]] (TLB), since a new process has different memory mappings. On multicore hardware, migrating a process between cores adds additional cache-cold overhead. For this reason, parallel programs that generate many short-lived threads may pay significant context-switch overhead.

## Mode-switch flavor ([[dis-13-1-booting-running|DIS 13.1]])

A narrower sense of *context switch* — the **[[UserMode|user-mode]] → [[KernelMode|kernel-mode]] → user-mode** round-trip triggered by every [[Interrupt|interrupt]] or [[SystemCall|trap]] — operates on the same machinery but **does not change the running [[Process|process]]**. The CPU saves user-mode register state, switches privilege, runs the [[Kernel|kernel]] handler, then restores user state and resumes the interrupted instruction.

**Kernel-in-every-address-space optimization**: to make this transition cheap, OSes traditionally map the [[Kernel|kernel]]'s code into the **top region of every process's address space**, so the handler is reachable without changing page tables. Hardware-enforced [[UserMode|user-mode]] memory restrictions keep the region inaccessible to user code. The **Meltdown** speculative-execution vulnerability undermined this isolation and drove OSes toward stricter kernel-user separation at some performance cost.

## Connections

- [[parproc-appA-systems-issues]] — §A.1; primary process-switch source.
- [[Timesharing]] — the scheduling mechanism that triggers process context switches.
- [[TranslationLookasideBuffer]] — flushed or partially invalidated on a context switch, adding re-warm cost.
- [[MemoryHierarchy]] — cache state is disrupted by context switches.
- [[Interrupt]] / [[SystemCall]] — trigger the narrower mode-switch flavor.
- [[KernelMode]] / [[UserMode]] / [[Kernel]] — the modes/code involved.
- [[DiveIntoSystems]] · [[dis-13-1-booting-running]] — OS mode-switch treatment.
