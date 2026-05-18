---
title: "ARM64 Shift Instructions"
type: concept
tags: [arm64, aarch64, assembly, shift, lsl, lsr, asr, ror, bitshift]
sources: [dis-9-3-arm64-arithmetic]
last_updated: 2026-05-17
---

# ARM64 Shift Instructions

The **bit-shift instruction family** on [[ARM64]] consists of **four instructions** per [[dis-9-3-arm64-arithmetic|Ch 9.3]] — three shifts (left, logical right, arithmetic right) plus one rotate. Like all [[ARM64]] computational instructions, these operate **only on registers and immediates** per the [[LoadStoreArchitecture|load/store rule]].

## The four instructions

| Instruction | Effect | Fill |
|---|---|---|
| `lsl D, R, #v` | Shift `R` left by `v` bits | Zero on the right; LSB padding |
| `lsr D, R, #v` | Logical shift `R` right by `v` bits | Zero on the left; MSB padding |
| `asr D, R, #v` | Arithmetic shift `R` right by `v` bits | **Sign bit** on the left; preserves signedness |
| `ror D, R, #v` | Rotate `R` right by `v` bits | Bits wrap from low end to high end; no fill |

The shift amount `v` is a **6-bit constant** (range `0`–`63` for 64-bit `x`-register operations, `0`–`31` for 32-bit `w`-register operations) or may be supplied via a register operand.

## Single left shift, two right shifts

There is **one left shift** but **two right shifts** because the choice of fill-bit determines whether signed quantities are preserved:

- `lsr` zero-fills the upper bits — correct for **unsigned** values, but turns negative two's-complement values into large positive ones.
- `asr` replicates the [[SignBit|sign bit]] into the upper bits — correct for **signed** values, preserves the sign of the result.

Left shift has no such ambiguity — the fill is always zero on the right regardless of signedness.

## Shift-instead-of-multiply

Per [[dis-9-3-arm64-arithmetic|Ch 9.3]]'s anti-premature-optimization caveat, **modern compilers automatically substitute shifts for multiplication / division by powers of two**:

| C operation | Compiler-generated shift |
|---|---|
| `x * 2` | `lsl D, x, #1` |
| `x * 4` | `lsl D, x, #2` |
| `x * 2^k` | `lsl D, x, #k` |
| `x / 2` (unsigned) | `lsr D, x, #1` |
| `x / 2` (signed) | `asr D, x, #1` |

The same substitution appears on [[X86_64|x86-64]] (see [[X86ShiftInstructions]]) and [[IA32]]. The standing recommendation across all three ISAs: *"premature optimization in source code is discouraged."*

## Rotate — `ror`

`ror` (rotate right) is **not** a multiplication/division shortcut — it is a bitwise reordering operation used by cryptographic primitives, hash functions, and bit-packing protocols. There is **no `rol`** mnemonic on [[ARM64]]; a left rotate by `k` is expressed as `ror D, R, #(N - k)` where `N` is the register width.

## Connections

- [[dis-9-3-arm64-arithmetic]] — promoting source.
- [[ARM64]] — the [[ISA]].
- [[LoadStoreArchitecture]] — the rule that confines these to register operands.
- [[ARM64ArithmeticInstructions]] — sibling family.
- [[ARM64BitwiseInstructions]] — sibling family.
- [[X86ShiftInstructions]] — contrasting [[CISC]] family; [[ARM64]] adds `ror` as a peer of the three shift instructions, where [[X86_64|x86]] keeps `rol`/`ror` separate from `shl`/`shr`/`sar`.
- [[BitShift]] — the cross-ISA concept; [[ARM64]] is the [[RISC]] instance.
- [[SignBit]] — the bit `asr` replicates to preserve signedness.
- [[TwosComplement]] — the signed encoding `asr` preserves.
- [[AssemblyLanguage]] — umbrella concept.
