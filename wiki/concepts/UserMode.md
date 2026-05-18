---
title: "User Mode"
type: concept
tags: [operating-systems, cpu, privilege, dual-mode]
sources: [dis-13-1-booting-running]
last_updated: 2026-05-17
---

# User Mode

**User mode** is the unprivileged [[CPU]] execution mode in which application code runs. [[dis-13-1-booting-running|DIS 13.1]] defines the **dual-mode** discipline: *"When OS code is run on the CPU, the system runs in kernel mode, and when user-level programs run on the CPU, the system runs in user mode."*

## Restrictions

- Executes only **permitted (non-privileged) instructions** — privileged hardware-control instructions trap.
- Accesses only **OS-authorized memory regions** — the kernel-mapped portion of the address space is hardware-protected.
- **No direct hardware access** — devices must be reached via [[SystemCall|system calls]].

## Escaping to the kernel

A user program escapes user mode via a **trap instruction** ([[SystemCall|system call]]) or by receiving a hardware [[Interrupt|interrupt]]. Either path lands the CPU in [[KernelMode|kernel mode]] running a handler in the [[Kernel|kernel]].

## Connections

- [[KernelMode]] — the privileged counterpart.
- [[SystemCall]] — the controlled escape hatch.
- [[Process]] — what runs in user mode.
- [[DiveIntoSystems]] · [[dis-13-1-booting-running]]
