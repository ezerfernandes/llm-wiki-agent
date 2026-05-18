---
title: "SIGBUS (Bus Error Signal)"
type: concept
tags: [posix, signal, alignment, memory, c-debugging, fault]
sources: [dis-3-4-gdb-advanced]
last_updated: 2026-05-17
---

# SIGBUS (Bus Error Signal)

[[OperatingSystem|POSIX]] [[Signal|signal]] (10 on macOS/BSD, 7 on Linux) delivered when a [[Process|process]] makes a **misaligned memory access** or accesses a **memory-mapped region that no longer has backing storage**. Default action: **terminate + core dump**. *"If a program tries to access memory with a misaligned memory address for the type it is accessing, it receives a `SIGBUS` signal"* ([[dis-3-4-gdb-advanced|DIS Ch 3.4]]).

## SIGBUS vs SIGSEGV

| | [[SIGBUS]] | [[SegmentationFault|`SIGSEGV`]] |
|---|---|---|
| **Cause** | Valid address, **wrong alignment** for the access type; or `mmap`'d file shorter than access. | **Invalid** address — unmapped page, wrong permission, null deref. |
| **Architecture sensitivity** | Common on [[ARMCortexM|ARM]] / SPARC / RISC-V (strict alignment); rare on x86 (forgiving). | Universal — every architecture. |
| **Typical C bug** | Reading `int *` from an unaligned `char *` cast. | Dereferencing [[NullPointer|`NULL`]], use-after-free, off-end-of-array. |

The corpus's first **alignment-fault** entry — distinct from the [[SegmentationFault|`SIGSEGV`]] entry that earlier debugging chapters covered.

## Canonical reproducer

```c
char buf[8];
int *p = (int *)(buf + 1);   // off by 1 from alignment boundary
*p = 42;                     // on ARM / SPARC: SIGBUS; on x86: usually slow but works
```

x86 makes most misalignment **silently expensive** (split-load microcode); strict-alignment ISAs ([[ARMCortexM|ARM]], SPARC, MIPS) fault.

## Debugging with GDB

`handle SIGBUS stop` is on by default — [[GDB]] halts at the faulting instruction. Use [[GdbInfo|`info registers`]] to read the faulting address (`$pc` / faulting operand) and [[GdbExamineMemory|`x/i $pc`]] to disassemble the offending instruction. The fix is usually a [[Memcpy|`memcpy`]] for unaligned reads, or fixing the cast / struct packing.

## Related

- [[Signal]] — parent mechanism.
- [[GdbSignalControl]] — `handle SIGBUS stop` to halt on bus errors.
- [[SegmentationFault]] — sibling fatal-memory-fault signal — distinct cause (invalid vs misaligned).
- [[ARMCortexM]] — strict-alignment ISA where [[SIGBUS]] is common.
- [[Memcpy]] — alignment-safe alternative for unaligned reads.
