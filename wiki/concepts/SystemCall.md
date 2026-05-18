---
title: "System Call"
type: concept
tags: [operating-systems, kernel, trap, software-interrupt]
sources: [dis-13-1-booting-running]
last_updated: 2026-05-17
---

# System Call

A **system call** (often abbreviated *syscall*) is the controlled mechanism by which a [[UserMode|user-mode]] program requests a service from the [[Kernel|OS kernel]]. It is implemented as a **trap** — a software [[Interrupt|interrupt]] that transitions the [[CPU]] from [[UserMode|user mode]] to [[KernelMode|kernel mode]].

## Invocation protocol (from [[dis-13-1-booting-running|DIS 13.1]])

> *"When an application wants to invoke a system call, it places the desired call's number in a known location (the location varies according to the ISA) and issues a trap instruction to interrupt the OS."*

1. User program loads the **system-call number** into a designated [[CpuRegister|register]] (location is [[ISA]]-specific).
2. User program executes a **trap instruction**.
3. CPU switches into [[KernelMode|kernel mode]] and jumps to the OS trap handler.
4. The kernel dispatches on the call number and runs the corresponding service routine.
5. On completion, execution resumes at the instruction following the trap, back in [[UserMode|user mode]].

## Why traps, not direct calls

The trap mechanism is what enforces the [[UserMode|user]] / [[KernelMode|kernel]] boundary: a user program **cannot** simply jump into kernel code, because the privilege transition is gated by the hardware trap instruction. This is the controlled gateway that makes the dual-mode discipline workable.

## Connections

- [[Interrupt]] — system calls are software interrupts (traps).
- [[KernelMode]] / [[UserMode]] — the modes the trap moves between.
- [[Kernel]] — the code that services the call.
- [[ContextSwitch]] — what the trap performs.
- [[DiveIntoSystems]] · [[dis-13-1-booting-running]]
