---
title: "x86-64 `cmp` Instruction"
type: concept
tags: [x86-64, assembly, comparison, condition-codes, control-flow]
sources: [dis-7-4-1-x86-64-preliminaries]
last_updated: 2026-05-17
---

# x86-64 `cmp` Instruction

The **`cmp` instruction** is [[X86_64|x86-64]]'s **flag-only sibling of [[X86ArithmeticInstructions|`sub`]]**: it evaluates a subtraction **purely to set the [[X86FlagsRegister|FLAGS register]]**, discarding the arithmetic result so no register or memory location is written. Per [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1 of *[[DiveIntoSystems]]*]]: *"`cmp R1, R2` compares R2 with R1 (i.e., evaluates R2 - R1) without modifying the values of either register."*

## Form and semantics

```
cmp R1, R2   ; evaluates (R2 - R1); sets ZF, SF, OF, CF; writes nothing
```

In [[AtAndTSyntax|AT&T syntax]] the **source-first ordering** makes this counterintuitive: `cmp %rbx, %rax` sets flags as if you computed `%rax − %rbx`. (Reversed in [[IntelSyntax|Intel syntax]], where the destination-first ordering reads more naturally.)

After `cmp R1, R2`:

- **ZF = 1** iff `R2 == R1` — consumed by `je` (jump if equal).
- **SF, OF** encode the **signed** ordering of `R2` vs `R1` — consumed by `jg` / `jge` / `jl` / `jle`.
- **CF** encodes the **unsigned** ordering — consumed by `ja` / `jae` / `jb` / `jbe`.

## Compiling C comparisons

The [[CLanguage|C]] expression `a < b` (with `a`, `b` typed `int`) compiles to roughly:

```
cmp %rsi, %rdi   ; assume %rdi = a, %rsi = b — evaluates (b - a) ... wait, AT&T: cmp src, dst = dst - src
                 ; so cmp %rsi, %rdi = (%rdi - %rsi) = (a - b)
jl  L_then       ; jump if a < b (signed)
```

The **operand-order trap** is the chapter's chief reading hazard: the source-first ordering of [[AtAndTSyntax|AT&T]] inverts the natural "compare X with Y" reading.

## Distinction from [[X86ArithmeticInstructions|`sub`]]

| | `sub S, D` | `cmp S, D` |
|---|---|---|
| Computes | `D ← D − S` | `D − S` (discarded) |
| Writes destination | Yes | **No** |
| Sets FLAGS | Yes (side effect) | Yes (sole purpose) |

`sub` is used when you want both the difference and the flags; `cmp` is used when you want **only** the flags.

## Connections

- [[X86FlagsRegister]] — the register `cmp` writes.
- [[ConditionCode]] — the individual flags it sets.
- [[TestInstruction]] — sibling flag-only instruction based on bitwise AND (`and`) rather than subtraction.
- [[X86JumpInstructions]] — the consumers of the flags `cmp` sets.
- [[X86ArithmeticInstructions]] — `sub` is `cmp`'s value-producing sibling.
- [[AtAndTSyntax]] / [[IntelSyntax]] — operand-order trap.
- [[TwosComplement]] — interpretation-invariance lets the same instruction serve signed and unsigned comparisons.
