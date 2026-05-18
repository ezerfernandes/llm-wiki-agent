---
title: "Dive into Systems — Ch 7.4.1 Preliminaries (x86-64 Conditional Control)"
type: source
tags: [book, dive-into-systems, x86-64, assembly, control-flow, condition-codes, flags]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/preliminaries.html
sources: []
last_updated: 2026-05-17
---

## Summary

**First leaf** of [[dis-7-4-x86-64-conditional-loops|Ch 7.4]] of *[[DiveIntoSystems]]*. Introduces the three mechanisms every conditional construct at the [[X86_64|x86-64]] assembly level rests on: the **[[X86FlagsRegister|FLAGS condition-code register]]** (the single-bit ALU side-channel that records *what just happened*), the **comparison instructions [[CmpInstruction|`cmp`]] and [[TestInstruction|`test`]]** (set flags **without writing a destination**), and the **[[X86JumpInstructions|jump-instruction family]]** (`jmp` unconditional + the signed/unsigned conditional jumps that consume the flags). Together they encode [[CLanguage|C]]'s comparison operators (`==` / `!=` / `<` / `<=` / `>` / `>=`) into branch-driven [[X86_64|x86-64]] [[AssemblyLanguage|assembly]]. **67th ingested DIS chapter.**

## Key Claims

- **The FLAGS register stores single-bit ALU side-effects** ([[X86FlagsRegister|FLAGS / `%eflags`]]) — most arithmetic / logic instructions update it as a side effect of their normal `D ← op(D, S)` semantics. Four headline flags: **[[ConditionCode|ZF]]** (zero — result equals 0), **[[ConditionCode|SF]]** (sign — result is negative, i.e. MSB = 1), **[[ConditionCode|OF]]** (overflow — signed integer overflow), **[[ConditionCode|CF]]** (carry — unsigned-arithmetic carry-out of the MSB).
- **Signed vs unsigned split is encoded in *which flags are consumed*, not in the arithmetic.** [[TwosComplement|Two's-complement]] makes the bit-pattern arithmetic identical; **SF + OF** guide signed comparisons, **CF** guides unsigned comparisons.
- **`cmp R1, R2` evaluates `R2 − R1`** *"without modifying the values of either register"* — sole purpose is to set the [[X86FlagsRegister|FLAGS]]. [[AtAndTSyntax|AT&T source-first ordering]] makes the operand order counterintuitive: `cmp %rbx, %rax` sets flags as if you computed `%rax − %rbx`.
- **`test R1, R2` performs bitwise AND** without writing a destination, just to set flags. The canonical pattern is **`test %rax, %rax`** — *"a common usage of the `test` instruction is to test whether a register value is 0"* — `x AND x = 0` iff `x = 0`, so the [[ConditionCode|ZF]] flag becomes a direct zero-test on the register.
- **Unconditional [[X86JumpInstructions|jump]] `jmp L`** transfers control to label `L` by writing `L` into the [[InstructionPointer|`%rip` instruction pointer]]; the indirect form **`jmp *addr`** jumps to a computed address (used to compile [[SwitchStatement|`switch`]] jump tables and indirect calls).
- **Conditional jumps consume specific flag combinations** — encoded in mnemonic suffix letters: `e` = equal, `n` = not, `z` = zero, `g`/`l` = signed greater/less, `a`/`b` = unsigned above/below. The signed/unsigned split is **encoded in the mnemonic**, not in the comparison that preceded it — the same `cmp` instruction sets all four flags, and the consumer chooses interpretation.

## Key Quotes

> "The FLAGS register stores single-bit values that encode ALU operation results."

> "ZF is set to 1 if the result equals zero. SF is set to 1 if the result is negative. OF is set to 1 if signed integer overflow occurs. CF is set to 1 if unsigned arithmetic carry occurs."

> "`cmp R1, R2` compares R2 with R1 (i.e., evaluates R2 - R1) without modifying the values of either register."

> "A common usage of the `test` instruction is to test whether a register value is 0."

> "`jmp L` jumps to the address indicated by label L by updating `%rip`."

## Connections

- [[DiveIntoSystems]] — host textbook; this is Ch 7.4.1, the **first leaf of [[dis-7-4-x86-64-conditional-loops|Ch 7.4]]** delivering the three mechanism families (flags + comparisons + jumps) that Ch 7.4.2 (if/else) and Ch 7.4.3 (loops) will compose into the [[IfStatement|`if`]] / [[WhileLoop|`while`]] / [[ForLoop|`for`]] / [[DoWhileLoop|`do`–`while`]] compilation patterns.
- [[X86FlagsRegister]] — the FLAGS / `%eflags` condition-code register: ZF, SF, OF, CF.
- [[ConditionCode]] — the individual single-bit flags within FLAGS.
- [[CmpInstruction]] — `cmp R1, R2` evaluates `R2 − R1`, sets flags, discards result.
- [[TestInstruction]] — `test R1, R2` evaluates `R1 AND R2`, sets flags, discards result; the `test %rax, %rax` register-zero idiom.
- [[X86JumpInstructions]] — `jmp` (unconditional) plus the signed (`je`/`jne`/`jg`/`jge`/`jl`/`jle`) and unsigned (`ja`/`jae`/`jb`/`jbe`) conditional-jump family.
- [[InstructionPointer]] — `%rip` is what `jmp` writes; restates [[dis-7-1-x86-64-basics|Ch 7.1]]'s read-only-by-direct-write rule (jumps are the indirect channel).
- [[X86ArithmeticInstructions]] — `add` / `sub` from [[dis-7-2-x86-64-common|Ch 7.2]] are the arithmetic instructions that **set** flags as a side effect; `cmp` is their flag-only sibling.
- [[X86BitwiseInstructions]] — `and` / `or` / `xor` from [[dis-7-3-x86-64-arithmetic|Ch 7.3]] also set flags; `test` is their flag-only sibling.
- [[TwosComplement]] — the bit-pattern-invariance from [[dis-4-3-signed|Ch 4.3]] that lets the **same** ALU and **same** flags serve both signed (SF + OF) and unsigned (CF) interpretations.
- [[SignBit]] — SF flag directly mirrors the result's MSB, the [[SignBit|sign bit]].
- [[IntegerOverflow]] — OF (signed) and CF (unsigned) are the hardware surface for the two overflow rules from [[dis-4-5-overflow|Ch 4.5]].

## Contradictions

None. Extends prior coverage:

- **Confirms [[dis-7-1-x86-64-basics|Ch 7.1]]'s** *"`%rip` is read-only — cannot be written directly"* rule by naming the **indirect** channel: jump instructions are how the instruction pointer changes.
- **Confirms [[dis-4-3-signed|Ch 4.3]] / [[dis-4-5-overflow|Ch 4.5]]'s** signed/unsigned interpretation-invariance at the bit-pattern level by showing the **same arithmetic instruction** sets **all four flags** and the consumer picks signed (SF, OF) vs unsigned (CF) interpretation through the **conditional-jump mnemonic**.
- **Confirms [[dis-7-2-x86-64-common|Ch 7.2]]'s** `add`/`sub` instructions and [[dis-7-3-x86-64-arithmetic|Ch 7.3]]'s `and`/`or`/`xor`: those already set flags as a side effect — Ch 7.4.1 names `cmp` / `test` as the **flag-only** siblings that discard the arithmetic result.
