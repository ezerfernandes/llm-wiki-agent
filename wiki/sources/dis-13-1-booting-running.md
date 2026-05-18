---
title: "Dive into Systems — 13.1 Booting and Running the OS"
type: source
tags: [textbook, operating-systems, kernel, boot, interrupts, system-calls]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C13-OS/impl.html
---

## Summary

**First leaf of Ch 13 *The Operating System*** in [[DiveIntoSystems]]. Section 13.1 explains how the [[OperatingSystem|OS]] itself gets started ([[Booting]] via [[Firmware|firmware]] like [[BIOS]] / [[UEFI]]), how it loads and launches user programs, and the **interrupt-driven architecture** that lets the OS sleep until a hardware device or user program needs service. Codifies the **dual-mode CPU** ([[KernelMode]] vs [[UserMode]]) and the **[[SystemCall|system-call]] trap** as the controlled gateway between them, with the [[Kernel|kernel]] mapped into the top of every process's address space to keep [[ContextSwitch|context switching]] cheap.

## Key Claims

- A running program requires the OS to (1) allocate RAM, (2) load the binary executable from disk into RAM, (3) create and initialize OS [[Process|process]] state, (4) initialize the [[CPU]] to start executing the process's instructions.
- The OS itself is initialized at power-up by [[Firmware|firmware]] stored in non-volatile memory — [[BIOS]] or [[UEFI]] — which performs minimal hardware setup, loads the OS [[Bootloader|boot block]] from disk into memory, and transfers CPU control to the OS.
- *"Most operating systems are implemented as interrupt-driven systems"* — the OS does not run until some entity (hardware device or user program) wakes it.
- Two interrupt sources: **hardware [[Interrupt|interrupts]]** (devices signal via an interrupt bus) and **traps / software interrupts** ([[SystemCall|system calls]] issued by user programs).
- A user program invokes a [[SystemCall|system call]] by placing the call number in a known CPU register (location is [[ISA]]-specific) and issuing a **trap instruction**. The trap transitions the CPU into [[KernelMode|kernel mode]] and runs the OS handler; on return, execution resumes at the instruction after the trap.
- **Dual-mode execution**: in [[UserMode|user mode]] a program executes only permitted instructions and accesses only OS-authorized memory; in [[KernelMode|kernel mode]] the OS runs unrestricted instructions, accesses all memory, and controls hardware directly.
- On interrupt, the [[CPU]] switches user → kernel mode, runs the handler, then returns to user mode at the interrupted instruction — a [[ContextSwitch|context switch]].
- To make context switching cheap, OSes traditionally map [[Kernel|kernel]] code into the **top region of every process's address space**; hardware-enforced mode restrictions protect kernel memory from user code.
- Modern speculative-execution vulnerabilities (e.g., **Meltdown**) prompted stricter kernel-user memory separation at some performance cost.

## Key Quotes

> "the OS allocates a portion of RAM for the running program, loads the program's binary executable from disk into RAM, creates and initializes OS state for the process associated with this running program, and initializes the CPU to start executing the process's instructions." — program-startup sequence.

> "Most operating systems are implemented as interrupt-driven systems, meaning that the OS doesn't run until some entity needs it to do something — the OS is woken up (interrupted from its sleep) to handle a request." — interrupt-driven architecture.

> "When an application wants to invoke a system call, it places the desired call's number in a known location (the location varies according to the ISA) and issues a trap instruction to interrupt the OS." — system-call mechanism.

> "When OS code is run on the CPU, the system runs in kernel mode, and when user-level programs run on the CPU, the system runs in user mode." — dual-mode execution.

## Connections

- [[DiveIntoSystems]] — opening leaf of Ch 13 *The Operating System*; **118th ingested DIS chapter**.
- [[OperatingSystem]] — the abstraction this chapter implements; previously named throughout the book, now mechanistically opened.
- [[Bootloader]] — firmware-loaded boot block that brings the OS into RAM.
- [[Firmware]] / [[BIOS]] / [[UEFI]] — the non-volatile-storage code that runs before the OS.
- [[Kernel]] — the OS code that runs in privileged mode.
- [[KernelMode]] / [[UserMode]] — the dual-mode CPU privilege split.
- [[SystemCall]] — the trap-based gateway from user mode to kernel mode.
- [[Interrupt]] — the hardware + software signalling mechanism that drives the OS.
- [[ContextSwitch]] — the user→kernel→user transition triggered by every interrupt.
- [[Process]] — the OS state container for a running program.

## Contradictions

- None. Extends prior [[DiveIntoSystems]] references to [[OperatingSystem]] as an abstraction layer into concrete mechanism. Consistent with [[ComputerSystem]] = hardware + OS framing from [[dis-0-introduction|Ch 0]].
