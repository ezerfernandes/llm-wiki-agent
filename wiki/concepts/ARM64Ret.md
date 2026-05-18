---
title: "ARM64 `ret` Instruction"
type: concept
tags: [arm64, armv8, assembly, control-flow, function-return, calling-convention]
sources: [dis-9-5-arm64-functions]
last_updated: 2026-05-17
---

# ARM64 `ret`

**`ret`** is the **[[ARM64]] function-return instruction** — the [[RISC]] analog of [[X86_64|x86]]'s [[RetInstruction|`retq`]]. Per [[dis-9-5-arm64-functions|DIS Ch 9.5]], `ret` *"sets `pc = x30`"* — pure register-to-register transfer, no memory access. Covered jointly with [[ARM64BranchAndLink|`bl`]] on the [[ARM64BranchAndLink]] page; this page focuses on `ret`-specific semantics.

## Semantics

```
pc = x30        ; or pc = xN if `ret xN` form
```

- **No operand form** (`ret`) — defaults to [[LinkRegister|`x30`]].
- **Explicit form** (`ret xN`) — branch to the address in `xN`.
- **No stack manipulation** — `sp` is unchanged by `ret` itself.
- **No side effects** on flags or other registers.

## The "no stack pop" structural delta

[[X86_64|x86]]'s [[RetInstruction|`retq`]] **pops** the return address off the stack — combining a load with the jump. [[ARM64]]'s `ret` is **pure jump** — the load happens **separately** in the [[ARM64FunctionPrologue|epilogue]] via `ldp x29, x30, [sp], #N`.

The standard non-leaf-function epilogue pattern:

```asm
ldp  x29, x30, [sp], #N   ; load fp+lr from stack, sp += N
ret                       ; pc = x30
```

For leaf functions, the `ldp` is omitted entirely — `x30` still holds the value [[ARM64BranchAndLink|`bl`]] wrote at entry.

## Return value via `x0`

By [[ARM64CallingConvention|AAPCS64]] convention, the function's return value lives in [[AArch64Registers|`x0`]] (or `w0` for 32-bit returns) at the moment `ret` executes. `ret` itself does not handle the return value — it's a contract the function body must satisfy before reaching `ret`.

## Hint encoding

`ret` is technically an **alias of `br x30`** with a return-prediction hint set in the encoding — branch-predictor implementations can use the hint to populate the return-address-prediction stack more efficiently than for a generic `br xN`.

## Connections

- [[dis-9-5-arm64-functions]] — introducing source.
- [[ARM64BranchAndLink]] — the paired `bl` instruction; full call-instruction family treatment.
- [[LinkRegister]] — `x30`; the register `ret` reads.
- [[ARM64FunctionPrologue]] — the epilogue's `ldp` that restores `x30` before `ret` executes.
- [[ARM64CallingConvention]] — AAPCS64 specifies `x0` as the return-value register at the `ret` boundary.
- [[RetInstruction]] — [[X86_64|x86]] structural analog (`retq`).
- [[CallStack]] / [[StackFrame]] / [[ExecutionStack]] — the runtime substrate.
- [[ARM64]] / [[InstructionPointer]].
