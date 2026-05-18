---
title: "Alignment Rule (x86-64)"
type: concept
tags: [x86-64, memory-alignment, abi, compiler, hardware]
sources: [dis-7-9-x86-64-structs]
last_updated: 2026-05-17
---

# Alignment Rule (x86-64)

The **x86-64 alignment rule** is the platform-level policy that **every primitive data type must reside at an address that is a multiple of its size**. Per [[dis-7-9-x86-64-structs|Ch 7.9]]: *"x64's alignment policy requires that two-byte data types (i.e., `short`) reside at a two-byte-aligned address, four-byte data types (i.e., `int`, `float`, and `unsigned`) reside at four-byte-aligned addresses, and larger data types (`long`, `double`, and pointer data) reside at eight-byte-aligned addresses."*

## The rule table

| Type | Size (bytes) | Alignment (bytes) |
|---|---|---|
| `char` | 1 | 1 (any address) |
| `short` | 2 | 2 |
| `int`, `float`, `unsigned` | 4 | 4 |
| `long`, `double`, pointer | 8 | 8 |

**Size = alignment** for every primitive — the rule's defining feature.

## Why the rule exists

- **Hardware efficiency.** [[CPU|CPUs]] fetch data from memory in fixed-size aligned chunks. An aligned access is a single memory transaction; a misaligned access either takes extra cycles (x86-64) or faults outright ([[ARM]] before v6, see [[SIGBUS]]).
- **Atomicity guarantees.** Aligned word reads/writes are atomic on most ISAs; misaligned ones often are not.
- **Cache-line interaction.** An aligned 8-byte object never straddles two 64-byte cache lines; the alignment rule preserves single-cache-line access for word-sized objects.

## Consequences for compilers

- **[[StructPadding|Struct padding]]** — the [[CCompiler|compiler]] inserts padding bytes between [[StructMember|struct fields]] so each field satisfies its alignment requirement.
- **Stack frame alignment** — the [[CallingConvention|System V AMD64]] ABI requires `%rsp` to be 16-byte aligned at every `callq` site (a stricter rule than the per-type rule above).
- **[[StructLayout|Struct layout]] depends on declaration order** — same fields in different orders can produce different total sizes via [[SizeOf|`sizeof`]].

## Connections

- [[MemoryAlignment]] — the general hardware principle that this rule instantiates on x86-64.
- [[StructPadding]] — the compiler mechanism that enforces this rule inside structs.
- [[StructLayout]] — the layout that this rule shapes.
- [[X86_64]] — the ISA whose policy this is.
- [[CStruct]] / [[StructMember]] — the source-level aggregates the rule affects most visibly.
- [[CallingConvention]] — adds the **16-byte stack-alignment** requirement at function boundaries.
- [[ARM]] — has stricter alignment requirements historically; misaligned access raises [[SIGBUS]].
- [[CCompiler]] — the agent that enforces the rule on the programmer's behalf.
- [[dis-7-9-x86-64-structs]] — chapter of origin.
