---
title: "Calling Convention"
type: concept
tags: [abi, calling-convention, x86-64, assembly, system-v]
sources: [dis-7-5-x86-64-functions]
last_updated: 2026-05-17
---

# Calling Convention

A **calling convention** is the **ABI contract** between a caller and callee at a function-call boundary — which registers hold which arguments, which register holds the return value, who is responsible for preserving which registers, and how the stack is laid out around the call. Per [[dis-7-5-x86-64-functions|Ch 7.5]]:

> "The first six parameters are passed in registers `%rdi`, `%rsi`, `%rdx`, `%rcx`, `%r8`, and `%r9`. Additional parameters are successively loaded into the call stack based on their size."

## System V AMD64 (the [[X86_64|x86-64]] convention)

The convention covered by Ch 7.5 is **System V AMD64** — used by every mainstream Unix-like OS on x86-64 (Linux, macOS, the BSDs, Solaris). Windows uses a **different** convention (Microsoft x64) — first four args in `%rcx` / `%rdx` / `%r8` / `%r9`, plus a 32-byte *shadow space* on the stack.

### Argument-passing registers (System V)

| Position | Register |
|---|---|
| 1st | `%rdi` |
| 2nd | `%rsi` |
| 3rd | `%rdx` |
| 4th | `%rcx` |
| 5th | `%r8` |
| 6th | `%r9` |
| 7th + | call stack |

The order is **fixed** — `%rdi` is *always* the first parameter, never the second. Floating-point arguments use `%xmm0`–`%xmm7` (covered in later chapters).

### Return-value register

`%rax` holds the return value (or a sub-register per the [[OperandSize|operand-size]] table — `%eax` for `int`, `%ax` for `short`, `%al` for `char` / `bool`). Wide return values (128-bit) use `%rax`:`%rdx`.

### Register preservation partition

Every general-purpose register falls into exactly one of two ownership classes across a [[CallInstruction|`callq`]] boundary:

- **[[CallerSavedRegister|Caller-saved]]** (`%rax`, `%rcx`, `%rdx`, `%rsi`, `%rdi`, `%r8`–`%r11`) — the **caller** owns preservation; the callee may freely clobber. If the caller needs any of these values after the call, it must spill them first.
- **[[CalleeSavedRegister|Callee-saved]]** (`%rbx`, `%rbp`, `%r12`–`%r15`, plus `%rsp` implicitly) — the **callee** owns preservation; must save+restore around any use. The caller can rely on these surviving the call.

## Why a convention is needed

Without a convention, every function would need to be compiled knowing the exact register usage of every function it calls — making **separate compilation** impossible and **linking against pre-compiled libraries** unworkable. The convention is the **standardized interface** that lets compilers, assemblers, and linkers produce composable code modules: any caller can call any callee that follows the same convention, regardless of who compiled either side.

## Variations

- **System V AMD64** — covered by Ch 7.5; standard on Linux / macOS / BSD x86-64.
- **Microsoft x64** — Windows x86-64; first four args in `%rcx` / `%rdx` / `%r8` / `%r9` + 32-byte shadow space.
- **IA32 cdecl** — 32-bit x86; all arguments on stack; covered by Ch 8 of [[DiveIntoSystems]].
- **ARM AAPCS64** — ARMv8-A; first eight args in `x0`–`x7`; covered by Ch 9.

## Connections

- [[dis-7-5-x86-64-functions]] — **introducing source**; defines the System V AMD64 calling convention at the [[X86_64|x86-64]] level.
- [[CallInstruction]] — the instruction that participates in the convention at the call site; argument registers must hold the correct values at the moment `callq` executes.
- [[RetInstruction]] — `%rax` must hold the return value at the moment `retq` executes.
- [[CallerSavedRegister]] — half of the register-preservation partition.
- [[CalleeSavedRegister]] — the other half.
- [[StackPointer]] — the convention specifies the stack must be 16-byte aligned at the moment of `callq` (a constraint Ch 7.5 does not emphasize but the System V ABI requires).
- [[FramePointer]] — optional under the convention (compilers may omit at higher optimization levels).
- [[StackFrame]] — the data structure the convention shapes.
- [[GeneralPurposeRegister]] — the 16 GPRs the convention partitions into role classes (arg / return / caller-saved / callee-saved / stack-management).
- [[X86_64]] — the ISA the System V AMD64 convention targets.
- [[ABI]] — the broader concept the calling convention is one component of.
