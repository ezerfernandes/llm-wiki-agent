---
title: "Condition Code (x86-64 Flag)"
type: concept
tags: [x86-64, assembly, flags, condition-codes]
sources: [dis-7-4-1-x86-64-preliminaries]
last_updated: 2026-05-17
---

# Condition Code

A **condition code** is a single-bit slot within the [[X86FlagsRegister|FLAGS register]] that encodes one specific aspect of the most recent ALU result. Per [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1 of *[[DiveIntoSystems]]*]], condition codes are the **side-channel** through which arithmetic / logic / comparison instructions communicate with downstream conditional-jump instructions — the mechanism by which [[CLanguage|C]] comparisons (`==` / `!=` / `<` / `<=` / `>` / `>=`) are realized in [[X86_64|x86-64]] [[AssemblyLanguage|assembly]].

## The four covered in Ch 7.4.1

| Flag | Name | Set to 1 when... | Consumed by |
|---|---|---|---|
| **ZF** | Zero Flag | Result equals zero | `je` / `jne` / `jz` / `jnz` |
| **SF** | Sign Flag | Result is negative (MSB = 1 / [[SignBit|sign bit]] = 1) | Signed jumps (with OF) |
| **OF** | Overflow Flag | **Signed** integer overflow occurred | Signed jumps `jg` / `jge` / `jl` / `jle` |
| **CF** | Carry Flag | **Unsigned** arithmetic carry-out of MSB occurred | Unsigned jumps `ja` / `jae` / `jb` / `jbe` |

## The signed/unsigned split

The **same** ALU operation sets **all four flags**. The split between signed and unsigned interpretation lives **in the consumer** (the conditional jump mnemonic), not in the producer (the comparison). Per [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1]]: *"SF and OF guide signed comparisons, while CF handles unsigned operations."*

This realises the bit-pattern-interpretation-invariance from [[dis-4-3-signed|Ch 4.3]] and [[dis-4-5-overflow|Ch 4.5]] at the assembly-instruction surface.

## Connections

- [[X86FlagsRegister]] — the register that holds the codes.
- [[CmpInstruction]] / [[TestInstruction]] — the **flag-only** producers.
- [[X86ArithmeticInstructions]] / [[X86BitwiseInstructions]] — arithmetic / logic producers that update flags as a side effect.
- [[X86JumpInstructions]] — the consumers.
- [[TwosComplement]] / [[SignBit]] / [[IntegerOverflow]] — the bit-pattern semantics that SF / OF / CF encode.
