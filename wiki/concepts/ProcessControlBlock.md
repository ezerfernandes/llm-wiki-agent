---
title: "Process Control Block (PCB)"
type: concept
tags: [operating-systems, processes, kernel-data-structure]
sources: [dis-13-2-processes]
last_updated: 2026-05-17
---

# Process Control Block (PCB)

The **process control block** (PCB) — *"process control struct"* in [[dis-13-2-processes|DIS Ch 13.2]] — is the kernel data structure the [[OperatingSystem|OS]] maintains **per [[Process|process]]** to track everything it needs to manage that process: identity, memory layout, register snapshot, resources, and current life-cycle state.

## Contents (from DIS 13.2)

- **[[ProcessID|Process ID (PID)]]** — unique integer identifier.
- **Address-space information** — where the process's [[ProcessMemory|memory regions]] live and how they map to physical RAM.
- **Execution state** — saved [[CpuRegister|CPU register]] values (PC, [[StackPointer|stack pointer]], general-purpose registers, condition codes), enough to resume the process after a [[ContextSwitch|context switch]].
- **Allocated resources** — open files, sockets, locks, etc.
- **Current [[ProcessState|process state]]** — Ready / Running / Blocked / Exited; determines [[Scheduler|scheduling]] eligibility.

The kernel keeps PCBs in a **process table** (often a linked list or array of these structs); the [[Scheduler|scheduler]] walks the table to choose the next Ready process.

## Why it exists

When a [[ContextSwitch|context switch]] occurs, the OS must (1) save the outgoing process's CPU + memory state somewhere stable across CPU reuse and (2) restore the incoming process's state from a similar place. The PCB **is** that place. Without it the CPU snapshot would have nowhere to live during the time another process owns the registers.

The PCB also makes the [[ProcessState|state machine]] explicit: a process **is** Blocked because its PCB's state field reads `BLOCKED`, not because of any property of the CPU at that moment.

## Connections

- [[dis-13-2-processes]] — primary source.
- [[Process]] — the entity each PCB describes.
- [[ProcessState]] — the field tracking life-cycle phase.
- [[ProcessID]] — the identifier inside the PCB.
- [[ContextSwitch]] — the operation that reads/writes register state from/to PCBs.
- [[Scheduler]] — consumer of PCB state fields.
- [[ProcessMemory]] — the address-space half of the per-process record.
- [[Kernel]] — owner of the data structure.
