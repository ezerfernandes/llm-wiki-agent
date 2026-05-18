---
title: "x86-64 Bit-Shift Instructions (`shl` / `sal` / `shr` / `sar`)"
type: concept
tags: [x86-64, assembly, instruction, shift, bit-manipulation]
sources: [dis-7-3-x86-64-arithmetic]
last_updated: 2026-05-17
---

# `shl` / `sal` / `shr` / `sar` — Bit Shifts

Per [[dis-7-3-x86-64-arithmetic|Ch 7.3]], [[X86_64|x86-64]]'s four **bit-shift instructions** form a 2×2 grid along two axes — **direction** (left vs right) × **arithmetic vs logical** (signed-preserving vs unsigned-zero-fill):

```
sal v, D    # D ← D << v    (arithmetic left shift)
shl v, D    # D ← D << v    (logical left shift)
sar v, D    # D ← D >> v    (arithmetic right shift — sign-bit replicated)
shr v, D    # D ← D >> v    (logical right shift — zero fill)
```

## Left shifts collapse to one operation

`sal` and `shl` are **bit-pattern-identical** — both fill the vacated low bits with `0`, and both truncate at the high end. Arithmetic vs logical only diverges for **right** shifts, because left-shift's low-bit fill is unambiguous. The chapter lists both forms because some [[Assembler|assemblers]] / disassemblers prefer one mnemonic over the other; the encoded bytes are the same.

## Right shifts split — the wiki's central [[BitShift|shift]] distinction

`sar` replicates the [[SignBit|sign bit]] into the vacated high bits — preserves [[TwosComplement|two's-complement]] sign for signed integers ([[ArithmeticRightShift|arithmetic right shift]] from [[dis-4-6-bitwise|Ch 4.6]]); `shr` zero-fills — correct for [[UnsignedInteger|unsigned]] integers ([[LogicalRightShift|logical right shift]]). The [[CLanguage|C]] compiler's choice between `sar` and `shr` for the `>>` operator is dispatched by **operand type**: signed → `sar`; unsigned → `shr` — restating [[dis-4-6-bitwise|Ch 4.6]]'s claim that *"the C compiler automatically selects the appropriate shifting variant based on variable declaration"* at the assembly-instruction level.

## Shift-count constraint — `%cl` is the variable-shift register

Per [[dis-7-3-x86-64-arithmetic|Ch 7.3]]: *"the shift value `v` must either be a constant or stored in register `%cl`."* — second hidden-operand convention in Ch 7.3 (after [[X86DivInstruction|`idiv`]]'s `%rax`/`%rdx`). `%cl` is the low byte of `%rcx` per the [[GeneralPurposeRegister|GPR subregister naming]] of [[dis-7-1-x86-64-basics|Ch 7.1]] — the canonical variable-shift register inherited from [[IA32|32-bit x86]] and earlier. Other GPRs cannot supply the shift count.

## Compiler strength-reduction for power-of-two multiply / divide

The headline use-case payoff per [[dis-7-3-x86-64-arithmetic|Ch 7.3]]: *"to compute `77 * 4`, most compilers will translate this operation to `77 << 2` to avoid the use of an `imul` instruction"* — the [[CompilerOptimization|strength-reduction]] move that turns power-of-two [[X86MulInstruction|multiply]] into `shl` and power-of-two divide into `sar` / `shr`. Shifts execute in fewer cycles than `imul` / `idiv` on most microarchitectures — the *[[BitShift|shift-as-multiply]]* identity from [[dis-4-6-bitwise|Ch 4.6]] surfacing as a compiler shortcut.

## Connections

- [[dis-7-3-x86-64-arithmetic]] — **introducing source**.
- [[X86_64]] — the ISA.
- [[BitShift]] — the bit-level mechanics [[dis-4-6-bitwise|Ch 4.6]] supplied.
- [[BitwiseOperator]] — [[CLanguage|C]]'s `<<` / `>>` operators these instructions implement.
- [[ArithmeticRightShift]] / [[LogicalRightShift]] — the right-shift dispatch that maps onto `sar` / `shr`.
- [[SignExtension]] — `sar`'s sign-bit replication is the in-place form of sign extension.
- [[X86MulInstruction]] — `shl` is the power-of-two `imul` shortcut.
- [[CompilerOptimization]] — the *imul → shl* / *idiv → sar* strength-reduction pattern.
- [[GeneralPurposeRegister]] — `%cl` is the dedicated variable-shift register.
