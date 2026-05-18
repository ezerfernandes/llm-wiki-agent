---
title: "General-Purpose Register (GPR)"
type: concept
tags: [register, x86-64, isa, cpu, low-level]
sources: [dis-7-1-x86-64-basics]
last_updated: 2026-05-17
---

# General-Purpose Register (GPR)

A **general-purpose register** is a [[CpuRegister|CPU register]] available to ordinary programs for holding **integer values, addresses, or function arguments** — distinct from special-purpose registers (stack pointer, instruction pointer, status flags) that are reserved for fixed architectural roles. The count, width, and naming of GPRs are part of the [[ISA]] contract.

## The 16 x86-64 GPRs ([[dis-7-1-x86-64-basics|Ch 7.1]])

[[X86_64|x86-64]] provides **16 64-bit GPRs**:

| Register | Conventional use (System V ABI) |
|---|---|
| `%rax` | **Return value** from a function |
| `%rdi` | 1st function argument |
| `%rsi` | 2nd function argument |
| `%rdx` | 3rd function argument |
| `%rcx` | 4th function argument |
| `%r8` | 5th function argument |
| `%r9` | 6th function argument |
| `%rbx`, `%r10`, `%r11`, `%r12`, `%r13`, `%r14`, `%r15` | scratch / callee-saved per ABI |

Per [[dis-7-1-x86-64-basics|Ch 7.1]]: *"Compilers typically store the first six parameters in registers `%rdi`, `%rsi`, `%rdx`, `%rcx`, `%r8` and `%r9`, respectively. Register `%rax` stores the return value from a function."*

## Subregister access — same physical register, four widths

Every x86-64 GPR exposes its lower 8 / 16 / 32 / 64 bits under distinct names so a single instruction can operate on whichever width matches the C type:

- **First eight GPRs** (`%rax`, `%rbx`, `%rcx`, `%rdx`, `%rdi`, `%rsi`, `%rsp`, `%rbp`) — **letter substitution**: `%rax` → `%eax` (32) → `%ax` (16) → `%al` (low 8) / `%ah` (high byte of the low 16).
- **Last eight GPRs** (`%r8`–`%r15`) — **suffix**: `%r8` → `%r8d` (32) → `%r8w` (16) → `%r8b` (8).

Compiler rule ([[dis-7-1-x86-64-basics|Ch 7.1]]): *"the 64-bit registers when dealing with 64-bit values (e.g., pointers or long types) and the 32-bit component registers when dealing with 32-bit types (e.g., int)."*

## GPR vs special-purpose

The same chapter draws the boundary by **counterexample**: `%rsp` (stack pointer, *"reserved by the compiler"*), `%rbp` (frame/base pointer, *"reserved by the compiler"*), and `%rip` (instruction pointer, *"cannot be written directly"*) are **not** general-purpose — they have architecturally fixed roles. The 16 GPRs above can hold any value the program needs.

## Why 16 GPRs?

The original [[IA32|32-bit x86]] [[ISA]] had only **eight** GPRs (`%eax` / `%ebx` / `%ecx` / `%edx` / `%edi` / `%esi` / `%esp` / `%ebp`) — a long-criticized scarcity that forced frequent [[RegisterSpill|register spills]] to the stack. [[X86_64|x86-64]] doubled the count to 16 by adding `%r8`–`%r15`, reducing spill pressure substantially.

By contrast, [[ARM|AArch64]] has 31 GPRs and [[RISCV|RISC-V]] has 31 (with `x0` hardwired to zero) — both significantly more than x86-64.

## Connections

- [[dis-7-1-x86-64-basics]] — promoting source; supplies the 16-register list and subregister-naming rules.
- [[CpuRegister]] — the umbrella concept GPR specializes.
- [[X86_64]] — the [[ISA]] defining the 16-register set.
- [[IA32]] — the 32-bit predecessor with only 8 GPRs.
- [[InstructionPointer]] — `%rip`; an example of a **non**-GPR (read-only, special-purpose).
- [[RegisterSpill]] — the mechanism the GPR shortage forces in IA32; mitigated by x86-64's expanded set.
- [[CPrimitiveType]] — the C type widths that determine which subregister width the compiler selects.
- [[OperandSize]] — the instruction-suffix mechanism that names the subregister width at the instruction level.
