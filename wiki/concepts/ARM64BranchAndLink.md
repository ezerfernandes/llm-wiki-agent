---
title: "ARM64 `bl` (Branch and Link) / `ret` Instructions"
type: concept
tags: [arm64, armv8, assembly, control-flow, function-call, calling-convention]
sources: [dis-9-5-arm64-functions]
last_updated: 2026-05-17
---

# ARM64 `bl` (Branch and Link) and `ret`

The **two [[ARM64]] instructions that implement structured function call and return** — the [[RISC]] analog of [[X86_64|x86]]'s [[CallInstruction|`callq`]] / [[RetInstruction|`retq`]] pair. Per [[dis-9-5-arm64-functions|DIS Ch 9.5]]:

| Instruction | Semantics | Cross-ISA analog |
|---|---|---|
| **`bl addr`** | `x30 = pc + 4; pc = addr` — save return address into [[LinkRegister\|`x30`]] **then** jump | [[CallInstruction\|`callq`]] / [[X86_64]] |
| **`ret`** | `pc = x30` — read return address from [[LinkRegister\|`x30`]] **then** jump | [[RetInstruction\|`retq`]] / [[X86_64]] |

## Key structural difference from x86 `callq` / `retq`

[[X86_64|x86]]'s [[CallInstruction|`callq`]] **pushes** the return address onto the stack; [[RetInstruction|`retq`]] **pops** it. [[ARM64]]'s `bl` / `ret` move the return address through the **[[LinkRegister|link register `x30`]]** — no memory access. This eliminates two stack accesses per call for **leaf functions** (functions with no nested calls) — the [[RISC]] design tradeoff for the larger [[AArch64Registers|31-GPR]] register file.

**Non-leaf functions** must spill `x30` to the stack in the [[ARM64FunctionPrologue|prologue]] (`stp x29, x30, [sp, #-N]!`) — recreating the same stack-resident return-address discipline [[X86_64|x86]] has by default.

## `bl` semantics in detail

`bl addr` is a **single atomic instruction** that:

1. Writes `pc + 4` (the address of the instruction **after** `bl`) into [[LinkRegister|`x30`]].
2. Sets `pc = addr` (the callee's entry point).

The encoded `addr` is a **±128 MB PC-relative offset** (26-bit signed). For longer-range calls, the compiler emits a chained-branch idiom or uses **`blr xN`** (branch-and-link to register — same effect, but the target is in a register, no range limit).

## `ret` semantics in detail

`ret` (with no operand) is a hint-form alias of `br x30` — branch to the address in [[LinkRegister|`x30`]]. **No stack manipulation** — `sp` is unchanged by `ret` itself. The standard [[ARM64FunctionPrologue|epilogue]] `ldp x29, x30, [sp], #N` reloads `x30` from its spilled slot **before** `ret` executes; for leaf functions, `x30` still holds the value `bl` wrote at entry.

`ret xN` (with explicit register) is the general form — branches to the address in `xN`. The unadorned `ret` defaults to `x30` — the [[ARM64CallingConvention|AAPCS64]] convention.

## Variants in the family

- **`bl addr`** — branch-and-link to PC-relative immediate.
- **`blr xN`** — branch-and-link to register (indirect call; same semantics, target from register).
- **`b addr`** — branch (no link) — unconditional jump, **does not write `x30`**. Used for tail calls and goto-style transfers.
- **`br xN`** — branch to register (no link) — indirect tail call.
- **`ret`** / **`ret xN`** — return.

## Connections

- [[dis-9-5-arm64-functions]] — introducing source.
- [[LinkRegister]] — `x30`; the register `bl` writes and `ret` reads.
- [[ARM64FunctionPrologue]] — the stack-spill discipline that recreates [[X86_64|x86]]-style stack-resident return addresses for non-leaf functions.
- [[ARM64CallingConvention]] — AAPCS64 specifies the `bl` / `ret` protocol.
- [[CallInstruction]] / [[RetInstruction]] — [[X86_64|x86]] structural analogs.
- [[ARM64ConditionalBranch]] — the conditional-jump family `b.cond` (no link).
- [[CallStack]] / [[StackFrame]] / [[ExecutionStack]] — the runtime substrate.
- [[ARM64]] / [[InstructionPointer]] / [[LoadStoreArchitecture]].
