---
title: "x86-64 `leaveq` Instruction"
type: concept
tags: [x86-64, assembly, instruction, function-epilogue, stack-frame]
sources: [dis-7-5-x86-64-functions]
last_updated: 2026-05-17
---

# `leaveq` — Stack-Frame Teardown

The **`leaveq` instruction** is [[X86_64|x86-64]]'s **function-epilogue helper** — a single instruction that bundles the standard stack-frame teardown sequence. Per [[dis-7-5-x86-64-functions|Ch 7.5]]:

> "`leaveq` restores the stack and frame pointers — equivalent to `mov %rbp, %rsp` then `pop %rbp`."

## Semantics

```
leaveq    # %rsp ← %rbp;  %rbp ← (%rsp);  %rsp ← %rsp + 8
```

Equivalent two-instruction longhand:

```
mov %rbp, %rsp     # collapse local variable area — %rsp now points to saved-%rbp slot
pop %rbp           # restore caller's frame pointer; %rsp now points to saved return address
```

After `leaveq`, [[StackPointer|`%rsp`]] sits at the saved return address — exactly the precondition [[RetInstruction|`retq`]] requires.

## Why it exists

Function epilogue is the symmetric undo of the prologue:

```
# Prologue                  # Epilogue
push %rbp                   leaveq
mov  %rsp, %rbp             retq
sub  $N, %rsp               # (leaveq subsumes the next 2 lines)
                            # mov %rbp, %rsp
                            # pop %rbp
```

Since the same two-instruction teardown appears in every function compiled with a frame pointer, `leaveq` exists as a **specialized encoding** — tighter than the longhand, makes the epilogue a fixed two-instruction shape (`leaveq; retq`).

## When `leaveq` is omitted

Modern compilers with `-O1` or higher often **omit `%rbp` entirely** as a frame-pointer optimization — the function uses `%rsp` directly as the frame anchor, freeing `%rbp` for general use. In this case the epilogue is just `add $N, %rsp; retq` (or even just `retq` if the function had no locals) — no `leaveq` needed because there's no saved-`%rbp` to restore. Functions compiled this way are harder to walk in a debugger (no `%rbp` chain) but slightly faster.

## Connections

- [[dis-7-5-x86-64-functions]] — **introducing source**; the `leaveq` definition and its place in the canonical function epilogue.
- [[RetInstruction]] — the instruction that immediately follows `leaveq` in every textbook epilogue.
- [[X86MovInstruction]] — half of the longhand `leaveq` expands to (`mov %rbp, %rsp`).
- [[X86StackInstructions]] — the other half is a `pop %rbp`.
- [[StackPointer]] — the `%rsp` register `leaveq` restores via the `mov %rbp, %rsp` step.
- [[FramePointer]] — the `%rbp` register `leaveq` restores via the `pop %rbp` step.
- [[StackFrame]] — the activation record `leaveq` dismantles.
- [[X86_64]] — the ISA `leaveq` belongs to.
