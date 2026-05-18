---
title: "Memory Alignment"
type: concept
tags: [memory, hardware, architecture, abi]
sources: [dis-7-9-x86-64-structs]
last_updated: 2026-05-17
---

# Memory Alignment

**Memory alignment** is the general hardware-level principle that data items should reside at memory addresses that are multiples of a natural unit — typically the item's own size, the machine word, or a cache line. On [[X86_64|x86-64]] the principle is codified by the [[AlignmentRule|alignment rule]] *"each primitive data type must reside at an address that is a multiple of its size"* ([[dis-7-9-x86-64-structs|Ch 7.9]]).

## Why hardware cares

- **Single-transaction memory access.** A [[CPU|CPU]] reads memory in fixed-width aligned chunks (typically 4 or 8 bytes). An aligned object fits in one such chunk; a **misaligned** object straddles two and requires two reads fused together.
- **Atomicity.** Aligned word-sized reads and writes are atomic on most ISAs; misaligned ones are not, so concurrent code on a misaligned field can observe torn values.
- **Cache-line non-straddling.** An aligned 8-byte object never crosses a 64-byte cache-line boundary, preserving single-cache-miss access cost.
- **Stricter ISAs fault.** [[ARM|ARMv6-]] (and many embedded MCUs) **trap** on misaligned access — the program receives [[SIGBUS]] rather than a slow access.

## Where it shows up in the wiki

- **[[StructPadding|Struct padding]]** — the [[CCompiler|compiler]] inserts padding bytes inside [[CStruct|C structs]] so each [[StructMember|field]] is aligned per the [[AlignmentRule|x86-64 alignment rule]].
- **[[StructLayout|Struct layout]]** — declaration order shapes how much padding the compiler must insert, making total [[SizeOf|`sizeof`]] order-dependent.
- **[[CallingConvention|System V AMD64 ABI]]** — requires `%rsp` to be 16-byte aligned at every `callq` site (a coarser, frame-level alignment requirement).
- **Heap allocators ([[Malloc|`malloc`]])** — return pointers aligned to the maximum-alignment requirement of any standard type (`alignof(max_align_t)`, typically 16 bytes on x86-64).

## Connections

- [[AlignmentRule]] — the specific x86-64 instantiation of the general principle.
- [[StructPadding]] — the compiler mechanism enforcing it inside structs.
- [[StructLayout]] — the layout outcome.
- [[X86_64]] — the ISA whose alignment policy [[dis-7-9-x86-64-structs|Ch 7.9]] codifies.
- [[ARM]] — historically stricter; misaligned access faults.
- [[SIGBUS]] — the signal raised by hard alignment faults.
- [[CPU]] / [[CacheMemory]] — the hardware layers that benefit from alignment.
- [[CallingConvention]] — the function-boundary alignment companion rule.
- [[Malloc]] — heap allocator aligning returned pointers.
- [[dis-7-9-x86-64-structs]] — chapter of origin.
