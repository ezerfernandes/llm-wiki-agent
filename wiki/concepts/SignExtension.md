---
title: "Sign Extension"
type: concept
tags: [systems, binary, data-representation, signed-integers, twos-complement]
sources: [dis-4-3-signed]
last_updated: 2026-05-17
---

# Sign Extension

**Sign extension** is the operation that widens a [[SignedInteger|signed-integer]] bit pattern from $N$ bits to $M > N$ bits while preserving both its sign and its numeric value. Per [[dis-4-3-signed|DIS Ch 4.3]]: when extending a [[TwosComplement|two's-complement]] value, **replicate the [[MostSignificantBit|high-order bit]]** into the new positions — *"non-negative numbers prepend zeros; negative numbers prepend ones."*

## The Rule

| Original $N$-bit value | Extended $M$-bit value (with $M > N$) |
|---|---|
| `0_???...?` (non-negative, MSB=0) | `0...0_???...?` (prepend $M-N$ zeros) |
| `1_???...?` (negative, MSB=1) | `1...1_???...?` (prepend $M-N$ ones) |

## Worked Examples

8-bit → 16-bit sign extension:

| 8-bit | Decimal | 16-bit (sign-extended) |
|---|---|---|
| `0000_0001` | +1 | `0000_0000_0000_0001` |
| `0111_1111` | +127 | `0000_0000_0111_1111` |
| `1111_1111` | **−1** | `1111_1111_1111_1111` (still −1) |
| `1000_0000` | **−128** | `1111_1111_1000_0000` (still −128) |

The unsigned dual operation is **zero extension** — always prepend zeros regardless of the source MSB. This is correct for [[UnsignedInteger|unsigned integers]] but **wrong** for signed: zero-extending `1111_1111` (−1 as 8-bit signed) to `0000_0000_1111_1111` (255 as 16-bit) silently turns −1 into 255.

## Why It Works (Two's Complement)

The two's-complement value of an $N$-bit pattern is $-(d_{N-1} \cdot 2^{N-1}) + \sum_{i=0}^{N-2} d_i \cdot 2^i$. When extending to $M$ bits, the new MSB at position $M-1$ has weight $-2^{M-1}$, and intermediate positions $N-1, N, \ldots, M-2$ have positive weights. Replicating the old MSB into all these positions exactly cancels them out (for negative numbers) or contributes nothing (for non-negative), preserving the original value. Formal identity: $-2^{M-1} + \sum_{i=N-1}^{M-2} 2^i = -2^{N-1}$.

## Hardware / ISA Manifestations

- **x86**: `movsx` / `movsxd` instructions sign-extend on load; `movzx` zero-extends.
- **ARM**: `SXTB` / `SXTH` (sign-extend byte / halfword), `UXTB` / `UXTH` (unsigned/zero-extend) — the [[GdbDisassemble|assembly]]-level primitives.
- **C**: implicit at type conversions — `(int)(signed char)0xFF` evaluates to `-1` (sign-extended), while `(int)(unsigned char)0xFF` is `+255` (zero-extended). The *"usual arithmetic conversions"* rule determines which kicks in for mixed-type arithmetic.
- **Shift-right**: arithmetic shift right (`sar` x86, `>>` on signed C types) sign-extends on each shift; logical shift right (`shr` x86, `>>` on unsigned C types) zero-extends.

## Connections

- [[SignedInteger]] — the umbrella; sign extension is the width-widening operation for this family.
- [[TwosComplement]] — the encoding for which sign extension's correctness derives.
- [[SignBit]] — the bit being replicated.
- [[MostSignificantBit]] — the physical position of the sign bit.
- [[UnsignedInteger]] — the dual case; unsigned values use zero extension instead.
- [[BinaryNumber]] — the underlying bit-level operation.
- [[CLanguage]] — implicit at signed-type widening (`signed char → int`, etc.).
- [[CpuRegister]] — sign-extension instructions live at the register-transfer level.
- [[dis-4-3-signed]] — source.
