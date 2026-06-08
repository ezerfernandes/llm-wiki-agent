---
title: "Kernel"
type: concept
tags: [operating-systems, kernel, privilege]
sources: [dis-13-1-booting-running]
last_updated: 2026-05-17
---

# Kernel

> Disambiguation: this page is the **operating-system** kernel. For the linear-algebra *kernel / null space* of a mapping, see [[NullSpace]]; for ML kernel methods, see [[KernelTrick]] / [[KernelFunction]].

The **kernel** is the core of the [[OperatingSystem|OS]] — the code that runs in [[KernelMode|kernel mode]], manages hardware, and services [[SystemCall|system-call]] and [[Interrupt|interrupt]] requests from user programs.

## Responsibilities (from [[dis-13-1-booting-running|DIS 13.1]])

- Initializes itself after the [[Bootloader|bootloader]] hands off control: discovers hardware resources and prepares system data structures.
- Launches user programs: allocates RAM, loads the binary executable from disk, creates [[Process|process]] state, initializes the [[CPU]] to begin execution.
- Runs **reactively** — DIS describes most OSes as **interrupt-driven**: the kernel sleeps until a hardware device or user program signals it.
- Handles [[Interrupt|interrupts]] (hardware) and traps ([[SystemCall|system-call]] software interrupts) in [[KernelMode|kernel mode]].
- Executes unrestricted instructions, accesses all memory, and controls hardware directly.

## Memory-mapping convention

To make [[ContextSwitch|context switching]] cheap, OSes traditionally map the kernel into the **top region of every process's address space**. Hardware-enforced [[UserMode|user-mode]] restrictions prevent user code from reading or writing this mapping. The Meltdown class of speculative-execution vulnerabilities pushed OSes toward stricter kernel-user memory separation at some performance cost.

## Connections

- [[OperatingSystem]] — the kernel is its privileged core.
- [[KernelMode]] / [[UserMode]] — the dual-mode CPU split that protects the kernel.
- [[SystemCall]] — the trap interface user programs use to call kernel services.
- [[Interrupt]] / [[ContextSwitch]] — the asynchronous entry into the kernel.
- [[Bootloader]] — what loads the kernel at boot.
- [[DiveIntoSystems]] · [[dis-13-1-booting-running]]
