---
title: "Sign Bit"
type: concept
tags: [systems, binary, data-representation, signed-integers]
sources: [dis-4-3-signed]
last_updated: 2026-05-17
---

# Sign Bit

The **sign bit** is the [[MostSignificantBit|most-significant bit]] (MSB) of a [[SignedInteger|signed-integer]] bit pattern — the bit that signals whether the encoded value is non-negative or negative. Per [[dis-4-3-signed|DIS Ch 4.3]], both signed encoding schemes use the MSB as a sign indicator, but they assign it **different semantics**:

## Two Roles, Two Schemes

| Scheme | Sign-bit role | Negation |
|---|---|---|
| [[SignMagnitude\|Sign-magnitude]] | **Pure flag** — 0 means non-negative, 1 means negative. The remaining $N-1$ bits encode the absolute magnitude. | Flip just the sign bit. |
| [[TwosComplement\|Two's complement]] | **Dual role** — both a sign indicator (0 → non-negative, 1 → negative) **and** a place-value digit with **negative weight** $-2^{N-1}$ in the value formula. | Flip all bits, then add 1 (cannot flip the sign bit alone). |

In both schemes the **direction** of the sign-bit convention is the same — `0b0xxx…` is non-negative and `0b1xxx…` is negative — making the sign-bit *test* (just inspect the MSB) identical regardless of encoding. What differs is what the *other bits* mean when the sign bit is 1.

## The Convention Is Universal

Modern hardware uniformly uses [[TwosComplement|two's complement]], so in practice "sign bit" means *"the MSB of a two's-complement integer."* CPU flags registers expose this directly — e.g., the x86 [[CpuRegister|SF (sign flag)]] mirrors the MSB of the last ALU result, and conditional-branch instructions like `JS` / `JNS` test it. Sign-aware instructions ([[GdbDisassemble|`movsx`]], shift-arithmetic-right [[GdbStepi|`sar`]]) propagate it; sign-unaware ones (`movzx`, `shr`) zero-extend instead.

## Visual

8-bit signed cell — sign bit is the leftmost bit:

```
  S  6  5  4  3  2  1  0   ← bit positions
  |
  +-- sign bit (MSB)
```

- `0b0000_0001` → +1 (S=0)
- `0b1111_1111` → −1 in [[TwosComplement|two's complement]] (S=1)
- `0b1000_0000` → **−128** in two's complement (the unique extreme negative), but `−0` in sign-magnitude (the pathological duplicate zero)

## Connections

- [[SignedInteger]] — the umbrella concept the sign bit makes possible.
- [[TwosComplement]] — the dominant scheme; sign bit doubles as the negative-weight place-value digit.
- [[SignMagnitude]] — the historical scheme; sign bit is a pure flag.
- [[MostSignificantBit]] — the physical bit position the sign bit occupies.
- [[SignExtension]] — the width-widening operation that replicates the sign bit.
- [[BinaryNumber]] — the underlying encoding.
- [[CpuRegister]] — exposes sign-flag state on x86 / ARM CPUs.
- [[dis-4-3-signed]] — source.
