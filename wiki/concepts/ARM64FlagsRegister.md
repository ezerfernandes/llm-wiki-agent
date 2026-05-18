---
title: "ARM64 NZCV Flag Register (PSTATE Condition Flags)"
type: concept
tags: [arm64, armv8, assembly, flags, condition-codes, nzcv, pstate, register]
sources: [dis-9-4-1-arm64-preliminaries, dis-9-3-arm64-arithmetic]
last_updated: 2026-05-17
---

# ARM64 NZCV Flag Register

The **NZCV condition-flag register** is the [[ARM64|AArch64]] ALU side-channel that records single-bit results of comparison and arithmetic operations. The four flags live inside `PSTATE` (Processor State), [[ARM64]]'s aggregate processor-state register — they are read-modify-written via the dedicated `MRS` / `MSR` instructions when needed, but ordinarily consumed implicitly by the [[ARM64ConditionalBranch|`b.cond`]] family and [[ARM64ConditionalSelect|`csel`]]. Per [[dis-9-4-1-arm64-preliminaries|Ch 9.4.1 of *[[DiveIntoSystems]]*]].

## The four flags

- **N (Negative)** — set to **1** if the result is negative (MSB = 1 under [[TwosComplement|two's complement]]). Mirrors the result's [[SignBit|sign bit]]. Analog of [[X86FlagsRegister|x86 SF]].
- **Z (Zero)** — set to **1** if the result equals 0. Analog of [[X86FlagsRegister|x86 ZF]].
- **C (Carry)** — set to **1** if unsigned-arithmetic carry-out (on add) / **borrow == 0** (on subtract) of the MSB. Analog of [[X86FlagsRegister|x86 CF]], but with **inverted borrow polarity on subtract** — the reason [[ARM64ArithmeticInstructions|`adc` / `sbc` / `ngc`]] consume `~C` rather than `C` for the borrow case.
- **V (Overflow)** — set to **1** if signed-integer overflow occurs. Analog of [[X86FlagsRegister|x86 OF]].

## How NZCV is set

Three distinct mechanisms set the flags — **flag-setting is opt-in**, unlike [[X86FlagsRegister|x86]] where most ALU ops set flags by default:

- **`s`-suffixed arithmetic** (`adds` / `subs` / `ands` / `bics` / ...) — per [[dis-9-3-arm64-arithmetic|Ch 9.3]], appending `s` to a base arithmetic / bitwise mnemonic inlines the flag-setting side-effect. The non-`s` form (`add` / `sub` / `and`) leaves NZCV unchanged.
- **[[ARM64Cmp|`cmp` / `cmn` / `tst`]]** — flag-only siblings of `subs` / `adds` / `ands`. *Their entire purpose is to set NZCV* — they discard the arithmetic result.
- **Carry-variant** (`adcs` / `sbcs`) — set flags while propagating C through extended-precision arithmetic.

## Who reads NZCV

- The **[[ARM64ConditionalBranch|`b.cond`]] conditional-branch family** (`b.eq` / `b.ne` / `b.lt` / `b.gt` / `b.le` / `b.ge` / `b.hi` / `b.lo` / `b.hs` / `b.ls` / `b.cs` / `b.cc` / `b.vs` / `b.vc` / `b.mi` / `b.pl`).
- The **[[ARM64ConditionalSelect|`csel`]] / `cset` / `csinc` / `csinv` / `csneg`** conditional data-flow instructions.

## Condition-code suffix table

| Suffix | Meaning | Flag test |
|---|---|---|
| `eq` | equal | Z == 1 |
| `ne` | not equal | Z == 0 |
| `lt` | signed less | N != V |
| `le` | signed less-or-equal | Z == 1 OR N != V |
| `gt` | signed greater | Z == 0 AND N == V |
| `ge` | signed greater-or-equal | N == V |
| `lo` (a.k.a. `cc`) | unsigned lower | C == 0 |
| `ls` | unsigned lower-or-same | C == 0 OR Z == 1 |
| `hi` | unsigned higher | C == 1 AND Z == 0 |
| `hs` (a.k.a. `cs`) | unsigned higher-or-same | C == 1 |
| `mi` | minus / negative | N == 1 |
| `pl` | plus / non-negative | N == 0 |
| `vs` | overflow set | V == 1 |
| `vc` | overflow clear | V == 0 |

The **signed vs unsigned split** is encoded in the **consumer suffix**, not in the [[ARM64Cmp|comparison]] that preceded it — the same `cmp` sets all four flags.

## Signed vs unsigned interpretation

[[TwosComplement|Two's complement]] makes the underlying bit-pattern arithmetic identical for signed and unsigned operands — the **same `cmp` or `subs` instruction sets all four flags**, and the **consumer picks the interpretation** by choosing a signed-suffixed branch (`lt` / `le` / `gt` / `ge` — consume **N + V**) or unsigned-suffixed branch (`lo` / `ls` / `hi` / `hs` — consume **C**, with `ls` / `hi` also folding in **Z**).

## Comparison to x86 FLAGS

| Dimension | [[X86FlagsRegister|x86 FLAGS]] | [[ARM64FlagsRegister|ARM64 NZCV]] |
|---|---|---|
| Register | `%eflags` / `%rflags` (32 / 64-bit dedicated register) | Four bits in `PSTATE` |
| Headline flags | ZF / SF / OF / CF | Z / N / V / C |
| Default flag-setting | Most arithmetic ops set flags implicitly | **Only `s`-suffixed ops** set flags |
| Comparison instructions | [[CmpInstruction|`cmp`]] / [[TestInstruction|`test`]] | [[ARM64Cmp|`cmp`]] / `cmn` / `tst` |
| Borrow polarity | C = 1 on borrow | C = 0 on borrow (inverted) |
| Branch family | [[X86JumpInstructions|`jXX`]] (`je` / `jne` / `jg` / ...) | [[ARM64ConditionalBranch|`b.cond`]] (`b.eq` / `b.ne` / `b.gt` / ...) |

## Connections

- [[ConditionCode]] — the individual single-bit flag concept (shared across ISAs).
- [[ARM64Cmp]] — the flag-only `cmp` / `cmn` / `tst` family.
- [[ARM64ConditionalBranch]] — `b.cond` family that consumes NZCV.
- [[ARM64ConditionalSelect]] — `csel` family that consumes NZCV.
- [[X86FlagsRegister]] — the x86 analog (different layout, different default policy).
- [[ARM64]] / [[CpuRegister]] / [[TwosComplement]] / [[SignBit]] / [[IntegerOverflow]] — supporting concepts.
- [[dis-9-4-1-arm64-preliminaries]] / [[dis-9-3-arm64-arithmetic]] — sources.
