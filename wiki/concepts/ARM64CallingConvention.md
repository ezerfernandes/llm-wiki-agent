---
title: "AAPCS64 (ARM64 Calling Convention)"
type: concept
tags: [abi, calling-convention, arm64, armv8, aapcs64, assembly]
sources: [dis-9-5-arm64-functions]
last_updated: 2026-05-17
---

# AAPCS64 — Procedure Call Standard for the Arm 64-bit Architecture

**AAPCS64** is the **[[ARM64|AArch64]] calling convention** — the ABI contract every well-formed [[ARM64]] function-call boundary follows. Per [[dis-9-5-arm64-functions|DIS Ch 9.5]]:

> "The first eight parameters to a function are stored in registers `x0`…​`x7`."

## Argument-passing registers

| Position | Register |
|---|---|
| 1st | `x0` |
| 2nd | `x1` |
| 3rd | `x2` |
| 4th | `x3` |
| 5th | `x4` |
| 6th | `x5` |
| 7th | `x6` |
| 8th | `x7` |
| 9th + | call stack |

The order is **fixed** — `x0` is always the first parameter. Floating-point arguments use the SIMD/FP register file (`s0`–`s7` for `float`, `d0`–`d7` for `double`) — disjoint from the GPR argument bank. **Doubles** [[SystemVCallingConvention|System V AMD64]]'s six-register fast path (`%rdi`/`%rsi`/`%rdx`/`%rcx`/`%r8`/`%r9`) and **fully eliminates** [[CdeclCallingConvention|cdecl]]'s stack-only argument passing — the [[RISC]] design tradeoff for the larger [[AArch64Registers|31-GPR]] register file.

## Return-value register

[[ARM64Ret|`x0`]] holds the return value (or `w0` for 32-bit returns — `int` / `unsigned`). Wide returns (128-bit) use the `x0`:`x1` pair. Floating-point returns use `s0` / `d0`.

## Link register and frame pointer

- **[[LinkRegister|`x30`]] (Link Register, LR)** — holds the return address. [[ARM64BranchAndLink|`bl`]] writes `pc + 4` here; [[ARM64Ret|`ret`]] reads `pc` from here. **Single register** — non-leaf functions must spill to the stack in the [[ARM64FunctionPrologue|prologue]].
- **[[FramePointer|`x29`]] (Frame Pointer, FP)** — base of the current [[StackFrame|stack frame]]; saved alongside `x30` in the canonical `stp x29, x30, [sp, #-N]!` prologue idiom.
- **[[StackPointer|`sp`]]** — top of the stack; must be **16-byte aligned** at every function-call boundary (a strict ABI constraint — frames are allocated in 16-byte multiples).

## Register preservation partition

- **Caller-saved (volatile)** — `x0`–`x18` (argument registers + temporaries). The callee may freely clobber; caller must spill anything it needs after the call.
- **Callee-saved (non-volatile)** — `x19`–`x28` (general-purpose preserved). The callee must save+restore if used.
- **Special-role** — `x29` (FP — preserved via stp/ldp), `x30` (LR — preserved via stp/ldp), `sp` (preserved implicitly), `xzr` (read-only zero).

## Variations and cross-ISA comparison

| Convention | ISA | Argument registers | Return | Stack alignment |
|---|---|---|---|---|
| **AAPCS64** | [[ARM64]] | `x0`–`x7` (8 GPRs) | `x0` | 16 bytes |
| [[SystemVCallingConvention\|System V AMD64]] | [[X86_64]] | `%rdi`/`%rsi`/`%rdx`/`%rcx`/`%r8`/`%r9` (6 GPRs) | `%rax` | 16 bytes |
| Microsoft x64 | [[X86_64]] | `%rcx`/`%rdx`/`%r8`/`%r9` (4 GPRs + 32B shadow) | `%rax` | 16 bytes |
| [[CdeclCallingConvention\|cdecl]] | [[IA32]] | stack only | `%eax` | 4 bytes |

## Connections

- [[dis-9-5-arm64-functions]] — **introducing source**; defines AAPCS64 at the [[ARM64]] level.
- [[LinkRegister]] — `x30`-as-return-address discipline.
- [[ARM64FunctionPrologue]] — the `stp x29, x30, [sp, #-N]!` / `ldp x29, x30, [sp], #N` pair that implements AAPCS64's frame protocol.
- [[ARM64BranchAndLink]] / [[ARM64Ret]] — the two instructions that participate in the convention at the call boundary.
- [[CallingConvention]] — umbrella concept; AAPCS64 is the [[ARM64]] variant.
- [[SystemVCallingConvention]] / [[CdeclCallingConvention]] — cross-ISA siblings ([[X86_64]] / [[IA32]]).
- [[StackFrame]] / [[FramePointer]] / [[StackPointer]] / [[AArch64Registers]] — the substrate AAPCS64 partitions.
- [[ARM64]] / [[ABI]].
