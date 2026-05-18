---
title: "Link Register (x30)"
type: concept
tags: [arm64, armv8, assembly, calling-convention, return-address, aapcs64]
sources: [dis-9-5-arm64-functions, dis-9-6-arm64-recursion, dis-9-10-arm64-buffer-overflow]
last_updated: 2026-05-17
---

# Link Register — `x30`

The **link register (LR)** — register **`x30`** on [[ARM64|AArch64]] — is the **dedicated GPR that holds the return address** during an active function call. Per [[dis-9-5-arm64-functions|DIS Ch 9.5]], [[ARM64BranchAndLink|`bl addr`]] *"sets `x30 = pc + 4` and sets `pc = addr`"* — atomically saving the post-call return address into `x30` and transferring control. The inverse [[ARM64Ret|`ret`]] instruction *"sets `pc = x30`"* — pure register-to-register transfer, no memory access.

## Why a dedicated register

[[ARM64]] is a **[[RISC]] [[LoadStoreArchitecture|load/store architecture]]** — minimizing memory accesses is a structural design goal. By putting the return address in a register rather than on the stack (as [[X86_64|x86]] / [[IA32]] do via [[CallInstruction|`callq` / `call`]]), [[ARM64]] eliminates a memory access for **leaf functions** (functions that make no nested calls) — the return-address fast path is **register-only**.

## Tradeoff: single register vs nested calls

The dedicated-register design is **only optimal for leaf functions**. Because `x30` is a **single register**, any nested [[ARM64BranchAndLink|`bl`]] would overwrite the caller's return address — so **non-leaf functions must spill `x30` to the stack** in the [[ARM64FunctionPrologue|prologue]] via the canonical `stp x29, x30, [sp, #-N]!` idiom. Once spilled, the stack-resident saved-`x30` slot is **structurally equivalent** to [[X86_64|x86]]'s stack-resident return address — including its vulnerability to [[BufferOverflow|buffer-overflow]]-driven [[ReturnAddressOverwrite|return-address overwrite]] (per [[dis-9-10-arm64-buffer-overflow|Ch 9.10]]).

## Cross-ISA comparison

| ISA | Return address location | Saved by |
|---|---|---|
| **[[ARM64]]** | Register `x30` (leaf) / stack via `stp` (non-leaf) | [[ARM64BranchAndLink\|`bl`]] writes `x30`; non-leaf prologue spills to stack |
| [[X86_64]] | Stack | [[CallInstruction\|`callq`]] pushes onto stack |
| [[IA32]] | Stack | [[CallInstruction\|`call`]] pushes onto stack |
| [[RISCV]] | Register `ra` (= `x1`) | `jal` writes `ra`; non-leaf prologue spills |
| MIPS | Register `$ra` (= `$31`) | `jal` writes `$ra`; non-leaf prologue spills |

The register-resident return address is a **[[RISC]] family invariant** — [[ARM64]], [[RISCV]], MIPS all use it. [[CISC]] families ([[X86_64]] / [[IA32]]) push to the stack.

## Buffer-overflow attack-surface delta

Per [[dis-9-10-arm64-buffer-overflow|Ch 9.10]]: **leaf functions are structurally immune** to the canonical [[ReturnAddressOverwrite|return-address overwrite]] exploit — their return address never touches memory. **Non-leaf functions** are equivalent to [[X86_64]] / [[IA32]] post-spill: the saved-`x30` stack slot is overwriteable just like a [[X86_64|x86]] saved-`%rip`. A partial structural mitigation, not a complete defense.

## Other uses of `x30`

Outside the immediate `bl` → `ret` pair, `x30` is a **general-purpose register** — the compiler may use it as a scratch register inside a leaf function (where no `ret` is pending). Inside non-leaf functions after the prologue save, the spilled stack slot at `[sp, #8]` (or wherever) is the **active** return-address copy; `x30` itself is free for re-use until the epilogue's `ldp` restores it.

## Connections

- [[dis-9-5-arm64-functions]] — **introducing source**; defines `bl` / `ret` against `x30`.
- [[dis-9-6-arm64-recursion]] — demonstrates the **mandatory spill** in the recursive case.
- [[dis-9-10-arm64-buffer-overflow]] — explains the **attack-surface tradeoff** (leaf immunity vs non-leaf vulnerability post-spill).
- [[ARM64BranchAndLink]] / [[ARM64Ret]] — the two instructions that read/write `x30`.
- [[ARM64FunctionPrologue]] — the `stp x29, x30, [sp, #-N]!` idiom that spills `x30` to the stack.
- [[ARM64CallingConvention]] — AAPCS64 specifies `x30`'s role.
- [[AArch64Registers]] — the 31-GPR file `x30` is the last of.
- [[ReturnAddressOverwrite]] / [[BufferOverflow]] — the security context (post-spill vulnerability).
- [[ARM64]] / [[LoadStoreArchitecture]] / [[RISC]].
