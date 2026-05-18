---
title: "x86-64 Bitwise Logic Instructions (`and` / `or` / `xor` / `not`)"
type: concept
tags: [x86-64, assembly, instruction, bitwise, logic]
sources: [dis-7-3-x86-64-arithmetic]
last_updated: 2026-05-17
---

# `and` / `or` / `xor` / `not` — Bitwise Logic

Per [[dis-7-3-x86-64-arithmetic|Ch 7.3]], [[X86_64|x86-64]] supplies four **bitwise logic instructions** that map one-to-one onto the [[BitwiseOperator|C bitwise operators]] of [[dis-4-6-bitwise|Ch 4.6]]:

```
and S, D    # D ← S & D
or  S, D    # D ← S | D
xor S, D    # D ← S ^ D
not D       # D ← ~D       (single operand — bit flip)
```

Each operates per bit across the operand width (`b`/`w`/`l`/`q` per the [[OperandSize|suffix]] rule); each is **one cycle, no carry propagation** at the hardware level — the cheapest arithmetic-class ops in the ISA. Direct hardware homes of [[dis-5-3-gates|Ch 5.3]]'s [[AndGate|AND]] / [[OrGate|OR]] / [[XorGate|XOR]] / [[NotGate|NOT]] [[LogicGate|gates]] applied across full register width.

## `not` vs `neg` — the canonical confusion

Per [[dis-7-3-x86-64-arithmetic|Ch 7.3]]: *"remember that bitwise `not` is distinct from negation ([[X86NegInstruction|`neg`]]). The `not` instruction flips the bits but does not add 1."* The [[TwosComplement|two's-complement]] negation recipe (*flip all the bits and add one* — [[dis-4-3-signed|Ch 4.3]]) splits across exactly these two instructions: `not` does the flip; [[X86NegInstruction|`neg`]] does the flip-and-add-one. Hence `~x = -x - 1` at the bit-pattern level — the [[BitwiseNot|`~` identity]] from [[dis-4-6-bitwise|Ch 4.6]] surfacing at the assembly-instruction surface.

## `xor` as the canonical register-zero idiom

`xor %reg, %reg` is the **idiomatic register-zero** pattern in compiled x86 code — shorter encoding than `mov $0, %reg`, sets condition codes the same way zero-tests would, and was historically faster on register-renaming microarchitectures because the result is **independent of the source register's prior value**. The compiler's preferred way to emit a literal `0` into a register.

## Operand structure

Same three-type framework as the rest of the [[X86ArithmeticInstructions|arithmetic family]] — `S` may be [[Constant|constant]] / [[CpuRegister|register]] / [[MemoryOperand|memory]]; `D` is register or memory; at most one memory operand per instruction. Implicit `%eflags` condition-code update.

## Connections

- [[dis-7-3-x86-64-arithmetic]] — **introducing source**.
- [[X86_64]] — the ISA.
- [[X86NegInstruction]] — `neg` (the *full* negation) vs `not` (bit flip only) — the [[TwosComplement|two's-complement]] *flip-and-add-one* split.
- [[BitwiseOperator]] — [[CLanguage|C]]'s `&` / `|` / `^` / `~` operators these instructions realize.
- [[BitwiseAnd]] / [[BitwiseOr]] / [[BitwiseXor]] / [[BitwiseNot]] — per-operator C-level pages.
- [[LogicGate]] — the gate-level primitives (AND / OR / XOR / NOT) these instructions apply across register width.
- [[dis-4-6-bitwise]] — the [[CLanguage|C]]-level operator surface; [[dis-5-3-gates|Ch 5.3]] — the gate-level mechanics.
