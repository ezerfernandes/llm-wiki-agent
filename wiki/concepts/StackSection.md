---
title: "Stack Section (C Program Memory)"
type: concept
tags: [c-language, memory, stack, address-space, calling-convention]
sources: [dis-2-1-scope-memory]
last_updated: 2026-05-17
---

# Stack Section

The **stack** is the region of a [[CLanguage|C]] program's [[ProcessMemory|address space]] that holds [[LocalVariable|local variables]] and [[FunctionParameter|parameters]] — one [[StackFrame|frame]] per active [[FunctionCall|call]]. Per [[dis-2-1-scope-memory|DIS Ch 2.1]]:

> "Local variables and parameters reside in the portion of memory for the *stack*."

This is the **same stack** as [[dis-1-4-functions|Ch 1.4]]'s [[ExecutionStack|execution stack]], now placed inside the four-region [[ProcessMemory|program-memory]] picture: the stack of [[StackFrame|frames]] occupies one region of the address space; the [[CodeSection|code]] / [[DataSection|data]] / [[HeapSection|heap]] regions sit elsewhere.

## Properties

- **LIFO discipline** — frames push on [[FunctionCall|call]], pop on [[ReturnStatement|return]] ([[ExecutionStack]] page).
- **Per-call lifetime** — a [[LocalVariable|local]]'s bytes are valid only while its frame is on the stack; once the function returns, those bytes are *reclaimed* (and any [[Pointer|pointer]] still holding the address points into the abyss).
- **Bounded** — the OS reserves a fixed stack-size limit at process launch (typically a few MB); blowing past it is **stack overflow** — typically from unbounded recursion or huge stack-allocated arrays.
- **Grows downward (conventionally)** — on x86-64 Linux and most modern targets, the stack grows from high addresses toward low addresses; new frames sit at *lower* addresses than older ones. (Convention, not language requirement.)

## Stack vs. execution stack vs. stack frame

| Term | Scope |
|---|---|
| **[[StackSection|Stack section]]** | A *region of the address space* — a range of addresses reserved for the stack |
| **[[ExecutionStack|Execution stack]]** | The *LIFO stack data structure* that lives in the stack section — the tower of frames |
| **[[StackFrame|Stack frame]]** | A *single record* on the execution stack — one activation of one function |

[[dis-2-1-scope-memory|Ch 2.1]] surfaces the *section* layer; [[dis-1-4-functions|Ch 1.4]] surfaced the *execution-stack* and *frame* layers. Same underlying mechanism, three resolution levels.

## Hosted vs. bare-metal

In the hosted [[OperatingSystem|OS]] world the OS reserves the stack region at process launch and grows it on demand (some kernels grow on page fault). In the [[NoStd|`no_std`]] / bare-metal world ([[TheEmbeddedRustBook]], [[ARMCortexM|Cortex-M]]) the **linker script** reserves a stack region in on-chip RAM and the reset handler loads the [[ARMCortexM|Cortex-M]] main-stack pointer at boot — different mechanism, same region role.

## Connections

- [[dis-2-1-scope-memory]] — introducing source.
- [[ProcessMemory]] / [[AddressSpace]] — the container.
- [[CodeSection]] / [[DataSection]] / [[HeapSection]] — the other three regions.
- [[ExecutionStack]] — the LIFO structure that lives in this region.
- [[StackFrame]] — the per-call record.
- [[LocalVariable]] / [[FunctionParameter]] — what frames hold.
- [[FunctionCall]] / [[ReturnStatement]] — push and pop the frames.
- [[OperatingSystem]] — reserves the stack region at process launch (hosted world).
- [[ARMCortexM]] — sibling treatment in the embedded world.
- [[CLanguage]] / [[DiveIntoSystems]].
