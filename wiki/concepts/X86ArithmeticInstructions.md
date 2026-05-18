---
title: "x86-64 Arithmetic Instructions (add / sub)"
type: concept
tags: [x86-64, assembly, instruction, arithmetic, add, sub]
sources: [dis-7-2-x86-64-common, dis-7-1-x86-64-basics]
last_updated: 2026-05-17
---

# `add` / `sub` — Arithmetic

The **`add` and `sub` instructions** are [[X86_64|x86-64]]'s integer-arithmetic primitives — both two-operand, both [[AtAndTSyntax|AT&T order]] source-first, both writing the result into the destination operand. Per [[dis-7-2-x86-64-common|Ch 7.2]]:

```
add S, D    # D ← D + S
sub S, D    # D ← D − S    (not S − D)
```

## Operand structure

Same three-type operand taxonomy as [[X86MovInstruction|`mov`]] — source may be [[Constant|constant]] / [[CpuRegister|register]] / [[MemoryOperand|memory]]; destination may be register or memory; **destination is also a source** (the result overwrites it). The [[dis-7-1-x86-64-basics|Ch 7.1]] *"at most one memory operand"* rule still applies — memory-to-memory `add` is illegal.

## Size variants — `addl` / `addq` / `subl` / `subq`

Per the [[OperandSize|operand-size suffix]] table — `b` / `w` / `l` / `q` select 1 / 2 / 4 / 8-byte widths. The [[dis-7-2-x86-64-common|Ch 7.2 `adder2` trace]] uses `add $0x2, %eax` — a 32-bit add of the immediate `2` into the 32-bit return-value register `%eax`. The instruction also implicitly sets the condition codes in `%eflags` (zero / sign / carry / overflow flags) — the foundation for subsequent conditional branches.

## Subtraction asymmetry — source-first surprise

`sub` is the one place AT&T's source-first ordering becomes counterintuitive: `sub %ebx, %eax` computes `%eax = %eax − %ebx`, **not** `%ebx − %eax`. Reading mechanically as "subtract source from destination" is the safe rule. (Intel syntax has the same semantics under reversed operand order, so the human-language description is identical — only the textual operand order differs.)

## Connection to `mov`

`add` / `sub` are structurally `mov`-shaped — same operand types, same size-suffix discipline, same one-memory-operand rule — but with a read-modify-write semantics where `mov` is pure write. This regularity is part of x86's [[CISC|CISC]] character: arithmetic instructions can directly read from / write to memory (no separate load-arithmetic-store dance required), in contrast to RISC ISAs like [[ARM]] / [[RISCV]] that confine arithmetic to register-register form.

## Connections

- [[dis-7-2-x86-64-common]] — **introducing source**; the `add` / `sub` definitions and the `adder2` `add $0x2, %eax` instance.
- [[dis-7-1-x86-64-basics]] — operand-type and size rules that constrain `add` / `sub`.
- [[X86_64]] — the ISA the pair belongs to.
- [[X86MovInstruction]] — sibling primitive with identical operand structure.
- [[X86StackInstructions]] — specialized `add`/`sub` against `%rsp` are functionally what `push` / `pop` do.
- [[Operand]] / [[OperandSize]] / [[AtAndTSyntax]] — the operand framework.
- [[BinaryAddition]] / [[BinarySubtraction]] — the bit-level mechanics [[dis-4-4-1-addition|Ch 4.4.1]] and [[dis-4-4-2-subtraction|Ch 4.4.2]] supplied for these instructions.
- [[CISC]] — the design-style that allows memory operands directly in arithmetic instructions.
