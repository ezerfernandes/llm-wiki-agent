---
title: "x86-64 Jump Instructions (`jmp` and conditional jumps)"
type: concept
tags: [x86-64, assembly, control-flow, branch, condition-codes]
sources: [dis-7-4-1-x86-64-preliminaries]
last_updated: 2026-05-17
---

# x86-64 Jump Instructions

The **jump-instruction family** is [[X86_64|x86-64]]'s **control-flow primitive** — every instruction in the family writes a new value into the [[InstructionPointer|`%rip` instruction pointer]], redirecting execution to a target label or address. Per [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1 of *[[DiveIntoSystems]]*]], the family splits into **unconditional** (`jmp`, always taken) and **conditional** (`je` / `jne` / ... — taken only when specific [[X86FlagsRegister|FLAGS]] bits hold the required values).

This is the **indirect channel** through which `%rip` changes — restating the [[dis-7-1-x86-64-basics|Ch 7.1]] rule that `%rip` is *"read-only — cannot be written directly"*. Jump instructions are how it moves.

## Unconditional jumps

| Form | Effect |
|---|---|
| `jmp L` | `%rip ← address(L)` — transfer control to label `L` |
| `jmp *addr` | `%rip ← *addr` — indirect jump through a memory operand (jump tables, computed gotos, indirect calls) |

The indirect form `jmp *` compiles [[SwitchStatement|`switch`]] statements with dense case ranges (the compiler builds a jump table indexed by the switch value).

## Conditional jumps

Each conditional jump tests a specific [[ConditionCode|condition-code combination]] left by the most recent flag-setting instruction (typically [[CmpInstruction|`cmp`]] or [[TestInstruction|`test`]]). Mnemonic-suffix vocabulary: **e** = equal, **n** = not, **z** = zero, **g** = (signed) greater, **l** = (signed) less, **a** = (unsigned) above, **b** = (unsigned) below.

### Equality (sign-agnostic)

| Mnemonic | Synonym | Flag test | C operator |
|---|---|---|---|
| `je`  | `jz`  | ZF = 1 | `==` |
| `jne` | `jnz` | ZF = 0 | `!=` |

### Signed ordering (consume SF + OF)

| Mnemonic | Synonyms | C operator |
|---|---|---|
| `jg`  | `jnle` | `>`  (signed) |
| `jge` | `jnl`  | `>=` (signed) |
| `jl`  | `jnge` | `<`  (signed) |
| `jle` | `jng`  | `<=` (signed) |

### Unsigned ordering (consume CF)

| Mnemonic | Synonyms | C operator |
|---|---|---|
| `ja`  | `jnbe` | `>`  (unsigned) |
| `jae` | `jnb`  | `>=` (unsigned) |
| `jb`  | `jnae` | `<`  (unsigned) |
| `jbe` | `jna`  | `<=` (unsigned) |

The **signed/unsigned split lives entirely in the jump mnemonic** — the preceding [[CmpInstruction|`cmp`]] sets all four flags, and the choice of `jg` vs `ja` (or `jl` vs `jb`) determines which interpretation the branch takes.

## Compilation pattern

A typical `if (a < b)` compiles to:

```
cmp  %rsi, %rdi   ; (a - b) — AT&T source-first
jl   L_then       ; signed less-than: branch if a < b
... fall-through (else) ...
L_then:
... then-branch ...
```

The next chapters operationalize this:

- [[dis-7-4-x86-64-conditional-loops|Ch 7.4]] hub introduces the family.
- Ch 7.4.2 *If Statements* will use these mnemonics to compile [[IfStatement|`if`]] / [[ElseStatement|`else`]].
- Ch 7.4.3 *Loops* will use them for the backward-branch pattern that implements [[WhileLoop|`while`]] / [[ForLoop|`for`]] / [[DoWhileLoop|`do`–`while`]].

## Connections

- [[X86FlagsRegister]] — the register conditional jumps read.
- [[ConditionCode]] — the individual bits (ZF / SF / OF / CF) decoded by the jump mnemonic.
- [[CmpInstruction]] / [[TestInstruction]] — the flag-setters that almost always precede a conditional jump.
- [[InstructionPointer]] — what every jump writes (`%rip`).
- [[X86_64]] / [[AtAndTSyntax]] — host ISA / syntax.
- [[TwosComplement]] — the bit-pattern-invariance that lets one `cmp` serve both signed and unsigned interpretations.
- [[IfStatement]] / [[WhileLoop]] / [[ForLoop]] / [[DoWhileLoop]] / [[SwitchStatement]] — the [[CLanguage|C]] constructs these jumps compile.
