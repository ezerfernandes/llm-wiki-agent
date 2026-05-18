---
title: "x86-64 Stack Instructions (push / pop)"
type: concept
tags: [x86-64, assembly, instruction, stack, push, pop]
sources: [dis-7-2-x86-64-common, dis-7-1-x86-64-basics]
last_updated: 2026-05-17
---

# `push` / `pop` — Stack Management

The **`push` and `pop` instructions** are [[X86_64|x86-64]]'s specialized [[CallStack|call-stack]] primitives — single-operand convenience forms that bundle a stack-pointer adjustment with a memory move into one instruction. Per [[dis-7-2-x86-64-common|Ch 7.2]]:

```
push S    # %rsp ← %rsp − 8;  (%rsp) ← S
pop  D    # D ← (%rsp);       %rsp ← %rsp + 8
```

## Stack-grows-down convention

[[X86_64|x86-64]] stacks **grow toward lower addresses** — so `push` *decrements* the [[StackPointer|`%rsp`]] before writing, and `pop` *increments* `%rsp` after reading. The 8-byte step matches the 64-bit register width — every push/pop moves exactly one 64-bit word. The popped slot is **not zeroed** — `pop` only adjusts `%rsp`; the stale bytes remain in memory until overwritten by a future push.

## Equivalence to `mov` + `sub`/`add` against `%rsp`

`push %rbp` is semantically equivalent to:

```
sub $0x8, %rsp
mov %rbp, (%rsp)
```

And `pop %rbp` is equivalent to:

```
mov (%rsp), %rbp
add $0x8, %rsp
```

The instructions exist as **specialized encodings** because stack pushes and pops are so frequent — function prologues, epilogues, parameter passing beyond the first six args, and register-save sequences all use them. Tighter encoding, no register tied up holding `$8`, and the implicit `%rsp` operand keeps the code dense.

## Worked example — `adder2` frame management

The [[dis-7-2-x86-64-common|Ch 7.2 `adder2` trace]] uses `push` / `pop` as a matched pair for **frame-pointer management**:

```
push %rbp           # save caller's frame pointer
mov  %rsp, %rbp     # establish new frame
...                 # function body
pop  %rbp           # restore caller's frame pointer
retq                # return
```

Every `push` is paired with a `pop` — the **stack-discipline invariant** that *"restores the call stack to its original state when a function completes"* per [[dis-7-2-x86-64-common|Ch 7.2]]. Violating this discipline (extra pushes, missing pops, or pop-without-push) corrupts the caller's [[StackFrame|stack frame]] and almost always causes the function to return to the wrong address.

## Connections

- [[dis-7-2-x86-64-common]] — **introducing source**; the `push` / `pop` definitions and the `adder2` frame-pointer pair.
- [[dis-7-1-x86-64-basics]] — names `%rsp` as the [[StackPointer|stack pointer]] and `%rbp` as the [[FramePointer|frame pointer]].
- [[X86_64]] — the ISA the pair belongs to.
- [[X86MovInstruction]] — the underlying memory move `push` / `pop` specialize.
- [[X86ArithmeticInstructions]] — the underlying `sub` / `add` against `%rsp` that `push` / `pop` bundle in.
- [[CallStack]] — the data structure `push` / `pop` manipulate.
- [[StackFrame]] — the per-function record built/torn-down by the prologue/epilogue pair.
- [[StackPointer]] — the `%rsp` register adjusted by every `push` / `pop`.
- [[FramePointer]] — the `%rbp` register typically saved/restored by the function-prologue `push` / function-epilogue `pop` pair.
