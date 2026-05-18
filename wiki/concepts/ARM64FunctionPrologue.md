---
title: "ARM64 Function Prologue / Epilogue"
type: concept
tags: [arm64, armv8, assembly, calling-convention, stack-frame, aapcs64]
sources: [dis-9-5-arm64-functions, dis-9-6-arm64-recursion]
last_updated: 2026-05-17
---

# ARM64 Function Prologue / Epilogue

The **canonical [[ARM64]] function-entry/exit idiom** — the instruction pair that **allocates the stack frame, saves the [[FramePointer|frame pointer `x29`]] and [[LinkRegister|link register `x30`]], and (on exit) restores them while deallocating the frame**. Per [[dis-9-5-arm64-functions|DIS Ch 9.5]]:

```asm
; Prologue (function entry)
stp  x29, x30, [sp, #-N]!     ; pre-indexed: sp -= N, then store fp+lr at [sp]
mov  x29, sp                  ; (often elided) establish frame base

; ... function body ...

; Epilogue (function exit)
ldp  x29, x30, [sp], #N       ; post-indexed: load fp+lr from [sp], then sp += N
ret                           ; pc = x30
```

## Why this idiom

[[ARM64]] has **no `push` / `pop` instructions** — unlike [[X86StackInstructions|x86 `push`/`pop`]] which adjust `%rsp` by 8 implicitly. Stack growth/shrinkage is expressed through the **[[ARM64AddressingMode|pre-indexed]] (`[sp, #-N]!`) and [[ARM64AddressingMode|post-indexed]] (`[sp], #N`) addressing-mode forms** on [[ARM64DataMovement|`stp` / `ldp`]] — the [[LoadStoreArchitecture|load/store rule]] applied to the stack itself.

The **pair-load/store** `stp` / `ldp` from [[dis-9-2-arm64-common|Ch 9.2]] moves **two 64-bit values in one instruction** — collapsing what [[X86_64|x86-64]] expresses as three instructions (`sub $16, %rsp; push %rbp; ...`) into **one**.

## Frame size N

`N` must be a **multiple of 16** (AAPCS64 stack-alignment constraint). Common sizes:

- **`#-16`** — minimum frame; saves fp + lr only (16 bytes for the pair).
- **`#-32`** — fp + lr + 16 bytes of locals (e.g., [[dis-9-6-arm64-recursion|Ch 9.6]]'s `sumr`).
- **`#-N`** for larger N — additional local-variable / parameter-spill space.

## Why save `x30` to the stack

[[LinkRegister|`x30`]] is a **single register**. Any nested [[ARM64BranchAndLink|`bl`]] inside the function would overwrite the caller's return address — so non-leaf functions **must** spill `x30` to the stack in the prologue. **Leaf functions** (no nested `bl`) can skip the save entirely — an [[ARM64]]-specific optimization no [[X86_64|x86]] function gets (because [[CallInstruction|`callq`]] always pushes the return address).

## Why save `x29`

[[FramePointer|`x29`]] is **callee-saved** in [[ARM64CallingConvention|AAPCS64]] — the function must restore it before returning. Modern compilers often pair the fp+lr save into the same `stp` for code-density reasons even when `x29` isn't actively used as a frame base inside the function.

## Pre-indexed vs post-indexed asymmetry

The prologue uses **pre-indexed** (`!` suffix) to **decrement first, then store** — placing the saved pair at the new stack top. The epilogue uses **post-indexed** (no `!`, comma-immediate after `]`) to **load first, then increment** — reading the saved pair before deallocating its slot. The asymmetry is structural: you must allocate the slot **before** writing into it, and free it **after** reading from it.

## Connections

- [[dis-9-5-arm64-functions]] — introducing source for the canonical idiom.
- [[dis-9-6-arm64-recursion]] — operationalizes the prologue/epilogue in the recursive case — demonstrates *why* the `x30` save is mandatory for non-leaf functions.
- [[dis-9-2-arm64-common]] — supplied [[ARM64DataMovement|`stp` / `ldp` with pre-/post-indexed addressing]] — the underlying primitive.
- [[ARM64DataMovement]] / [[ARM64AddressingMode]] — the instruction family + addressing modes the idiom composes.
- [[LinkRegister]] — `x30` is the central save target.
- [[FramePointer]] — `x29` paired with `x30` in the canonical idiom.
- [[ARM64CallingConvention]] — AAPCS64 defines the alignment + save discipline.
- [[ARM64BranchAndLink]] / [[ARM64Ret]] — the call/return pair the prologue/epilogue brackets.
- [[StackFrame]] / [[StackPointer]] / [[CallStack]] — the runtime substrate.
- [[LoadStoreArchitecture]] — the [[RISC]] discipline that forces the addressing-mode-based stack manipulation (no dedicated `push`/`pop`).
