---
title: "x86-64 FLAGS Register (`%eflags`)"
type: concept
tags: [x86-64, assembly, flags, condition-codes, register]
sources: [dis-7-4-1-x86-64-preliminaries]
last_updated: 2026-05-17
---

# x86-64 FLAGS Register

The **FLAGS register** (32-bit form `%eflags`; 64-bit form `%rflags`) is a special-purpose [[X86_64|x86-64]] register holding **single-bit [[ConditionCode|condition codes]]** that record side-effects of ALU operations. Per [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1 of *[[DiveIntoSystems]]*]]: *"the FLAGS register stores single-bit values that encode ALU operation results."*

## The four headline flags

Per [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1]]:

- **ZF (Zero Flag)** — set to **1** if the result of the previous instruction **equals zero**, else 0.
- **SF (Sign Flag)** — set to **1** if the result is **negative** (MSB = 1 under [[TwosComplement|two's complement]]), else 0. Directly mirrors the result's [[SignBit|sign bit]].
- **OF (Overflow Flag)** — set to **1** if **signed integer overflow** occurs.
- **CF (Carry Flag)** — set to **1** if **unsigned-arithmetic carry-out** of the MSB occurs.

## Who sets it

- [[X86ArithmeticInstructions|`add` / `sub`]] from [[dis-7-2-x86-64-common|Ch 7.2]] update flags as a side effect.
- [[X86BitwiseInstructions|`and` / `or` / `xor`]] from [[dis-7-3-x86-64-arithmetic|Ch 7.3]] update flags as a side effect.
- [[CmpInstruction|`cmp`]] and [[TestInstruction|`test`]] update flags **only** — they discard the arithmetic result. *Their entire purpose is to set FLAGS.*
- [[X86MovInstruction|`mov`]] does **not** affect flags.

## Who reads it

The [[X86JumpInstructions|conditional-jump family]] (`je` / `jne` / `jg` / `jge` / `jl` / `jle` / `ja` / `jae` / `jb` / `jbe`) and conditional-move / conditional-set instructions consume specific flag combinations.

## Signed vs unsigned interpretation

[[TwosComplement|Two's complement]] makes the underlying bit-pattern arithmetic identical for signed and unsigned operands — the **same `cmp` or `sub` instruction sets all four flags**, and the **consumer picks the interpretation** by choosing a signed-suffixed jump (`g`/`l` — consume **SF + OF**) or unsigned-suffixed jump (`a`/`b` — consume **CF**).

## Scope note

Ch 7.4.1 covers only the four headline flags. The full `%eflags` register also contains AF (auxiliary carry), PF (parity), DF (direction), IF (interrupt enable), TF (trap), and others — **out of scope** for the chapter.

## Connections

- [[ConditionCode]] — the individual single-bit slots within FLAGS.
- [[CmpInstruction]] — the flag-only sibling of [[X86ArithmeticInstructions|`sub`]].
- [[TestInstruction]] — the flag-only sibling of [[X86BitwiseInstructions|`and`]].
- [[X86JumpInstructions]] — flag consumers.
- [[X86_64]] / [[CpuRegister]] — host architecture / register class.
- [[SignBit]] / [[TwosComplement]] / [[IntegerOverflow]] — the bit-pattern foundations the flags express.
