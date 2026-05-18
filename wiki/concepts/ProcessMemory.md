---
title: "Program Memory (Process Memory)"
type: concept
tags: [c-language, memory, operating-systems, address-space]
sources: [dis-2-1-scope-memory]
last_updated: 2026-05-17
---

# Program Memory (Process Memory)

**Program memory** (a.k.a. **process memory**) is the partitioned [[AddressSpace|address space]] a running [[CLanguage|C]] program occupies. Per [[dis-2-1-scope-memory|DIS Ch 2.1]], a C program's memory divides into **four named regions**:

| Region | What it holds | Lifetime |
|---|---|---|
| **[[CodeSection|Code section]]** | The program's [[BinaryExecutable|compiled]] instructions | Program lifetime |
| **[[DataSection|Data section]]** | [[GlobalVariable|Global variables]] | Program lifetime |
| **[[HeapSection|Heap]]** | [[DynamicMemoryAllocation|Dynamically allocated]] storage ([[Malloc|`malloc`]] / [[Free|`free`]]) | Programmer-controlled |
| **[[StackSection|Stack]]** | [[LocalVariable|Local variables]] + [[FunctionParameter|parameters]], one [[StackFrame|frame]] per active [[FunctionCall|call]] | Per call — push on call, pop on return |

This is the **headline picture** of Ch 2.1: it upgrades [[dis-1-4-functions|Ch 1.4]]'s "[[ExecutionStack|stack of frames]]" cartoon into the full *four-region* layout where the stack is one of four regions of the process's address space.

## Why it matters

Every variable in a C program lives in exactly one of these four regions, and *which* region determines its **lifetime** and **scope** properties:

- A [[GlobalVariable|global]] in the [[DataSection|data section]] is alive for the entire program.
- A [[LocalVariable|local]] on the [[StackSection|stack]] vanishes when its [[StackFrame|frame]] is popped.
- A heap allocation persists until the programmer calls [[Free|`free`]].
- Code-section bytes are typically read-only (modifying them is undefined behavior or a segfault).

## Hosted vs. bare-metal

The four-region picture assumes the hosted [[OperatingSystem|OS]] world — the [[OperatingSystem|OS]] sets up the address space when the process launches and reclaims it on exit. In the [[NoStd|`no_std`]] / bare-metal world ([[TheEmbeddedRustBook]], [[ARMCortexM|Cortex-M]]) there is **no process**: the linker script partitions on-chip RAM into stack / `.bss` / `.data` regions and the reset handler sets up the stack pointer at boot. Same four-region taxonomy, different mechanism — no OS in the loop.

## Pedagogical placement

Ch 2.1 introduces this picture *minimally* — it names the four regions and ties each to a kind of variable. Later [[DiveIntoSystems]] chapters open up:

- **Ch 2.4** — [[DynamicMemoryAllocation|`malloc` / `free`]] mechanics; the [[HeapSection|heap]] becomes mechanical not just nominal.
- **Ch 2.6** — [[BufferOverflow|buffer overflow]] / stack corruption; what goes wrong when a write *crosses regions*.
- Later assembly / OS chapters — the calling convention's use of the stack region, virtual memory's mapping of the address space to physical RAM.

## Connections

- [[dis-2-1-scope-memory]] — introducing source.
- [[AddressSpace]] — the abstract container these four regions partition.
- [[CodeSection]] / [[DataSection]] / [[HeapSection]] / [[StackSection]] — the four regions.
- [[GlobalVariable]] / [[LocalVariable]] / [[FunctionParameter]] — the variable classes that occupy data section / stack region respectively.
- [[StackFrame]] / [[ExecutionStack]] — the stack region's internal structure ([[dis-1-4-functions|Ch 1.4]]).
- [[DynamicMemoryAllocation]] — what populates the heap; mechanism deferred to Ch 2.4.
- [[CompilationProcess]] / [[BinaryExecutable]] — what produces the bytes in the [[CodeSection|code section]].
- [[OperatingSystem]] — sets up the four-region layout at process launch (hosted world).
- [[CLanguage]] / [[DiveIntoSystems]].
