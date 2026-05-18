---
title: "Caller-Saved Register"
type: concept
tags: [x86-64, assembly, register, calling-convention, abi]
sources: [dis-7-5-x86-64-functions]
last_updated: 2026-05-17
---

# Caller-Saved Register

A **caller-saved register** (a.k.a. *volatile* / *scratch* register) is one whose value the **caller** is responsible for preserving across a [[CallInstruction|`callq`]] boundary. The callee may freely overwrite it. Per [[dis-7-5-x86-64-functions|Ch 7.5]]: half of the register-preservation partition that the System V [[CallingConvention|calling convention]] imposes on the 16 [[GeneralPurposeRegister|GPRs]].

## The System V x86-64 caller-saved set

Nine registers are caller-saved under System V AMD64:

| Register | Role |
|---|---|
| `%rax` | return value |
| `%rcx` | 4th argument |
| `%rdx` | 3rd argument |
| `%rsi` | 2nd argument |
| `%rdi` | 1st argument |
| `%r8` | 5th argument |
| `%r9` | 6th argument |
| `%r10` | scratch |
| `%r11` | scratch |

Note the **overlap with the argument-passing registers** — every argument register is caller-saved, which is internally consistent: the caller is **already** writing these to set up arguments at the call site, so it already knows their pre-call values are gone.

## The contract from each side

**Caller's view**: *"Anything I want to keep across this call, I must spill to my own [[StackFrame|stack frame]] (or to a [[CalleeSavedRegister|callee-saved register]] I've taken responsibility for) **before** the [[CallInstruction|`callq`]]. After the call, these registers hold whatever the callee chose to leave there — typically garbage from the callee's intermediate computations."*

**Callee's view**: *"I can freely use these as scratch space without saving them first. The caller already knew that when it called me."*

## When to choose caller-saved vs callee-saved (compiler perspective)

A register allocator picks between caller-saved and [[CalleeSavedRegister|callee-saved]] registers based on the variable's **liveness across calls**:

- **No calls in the variable's live range** → use a **caller-saved** register (no save/restore overhead).
- **Variable lives across one or more calls** → use a **callee-saved** register (pay one save+restore at function entry/exit, but no per-call save+restore).

This is why short-lived temporaries land in `%rax`/`%rcx`/`%rdx` and long-lived induction variables tend to land in `%rbx`/`%r12`–`%r15`.

## The same register can be both — for different callers

The caller-saved / callee-saved partition is a **per-register classification**, not a per-use one. `%rax` is *always* caller-saved across *every* call — the convention is global. But a given **value** in `%rax` is either preserved (because the caller spilled it) or not (because the caller didn't need it past the call).

## Connections

- [[dis-7-5-x86-64-functions]] — **introducing source**; defines the caller-saved partition under the System V calling convention.
- [[CalleeSavedRegister]] — the **other half** of the register-preservation partition.
- [[CallingConvention]] — the convention that defines the caller-saved / callee-saved split.
- [[CallInstruction]] — the boundary across which the caller-saved promise applies.
- [[GeneralPurposeRegister]] — the 16-register inventory the convention partitions.
- [[StackFrame]] — where caller spills go when a value must survive a call.
- [[X86_64]] — the ISA whose System V convention defines this partition.
