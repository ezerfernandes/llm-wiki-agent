---
title: "x86-64 `test` Instruction"
type: concept
tags: [x86-64, assembly, comparison, condition-codes, control-flow, bitwise]
sources: [dis-7-4-1-x86-64-preliminaries]
last_updated: 2026-05-17
---

# x86-64 `test` Instruction

The **`test` instruction** is [[X86_64|x86-64]]'s **flag-only sibling of [[X86BitwiseInstructions|`and`]]**: it evaluates a bitwise AND of two operands **purely to set the [[X86FlagsRegister|FLAGS register]]**, discarding the result so no register or memory location is written. Per [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1 of *[[DiveIntoSystems]]*]]: *"`test R1, R2` performs the bitwise AND of R1 and R2 ... [and] a common usage of the `test` instruction is to test whether a register value is 0."*

## Form and semantics

```
test R1, R2   ; evaluates (R1 AND R2); sets ZF, SF; writes nothing
```

## The canonical idiom: `test %reg, %reg`

```
test %rax, %rax
```

Since `x AND x = x` for any bit-pattern `x`, **`x AND x = 0` if and only if `x = 0`** — so this single instruction sets [[ConditionCode|ZF = 1]] iff `%rax` holds zero. A following `je` / `jz` then branches on "register is zero" / `jne` / `jnz` on "register is nonzero".

This is the standard compilation pattern for [[CLanguage|C]]'s implicit-boolean tests:

```c
if (ptr == NULL) { ... }    // test %rdi, %rdi ; je L_null
if (x) { ... }              // test %eax, %eax ; jne L_then
```

## Distinction from [[CmpInstruction|`cmp`]]

| | [[CmpInstruction|`cmp R1, R2`]] | `test R1, R2` |
|---|---|---|
| Operation | Subtraction `R2 − R1` | Bitwise AND `R1 AND R2` |
| Sibling of | [[X86ArithmeticInstructions|`sub`]] | [[X86BitwiseInstructions|`and`]] |
| Typical use | General comparison | Zero-test / bit-mask test |

## Connections

- [[X86FlagsRegister]] — the register `test` writes.
- [[ConditionCode]] — ZF is the headline output for the register-zero idiom.
- [[CmpInstruction]] — subtraction-based sibling for general comparisons.
- [[X86BitwiseInstructions]] — `and` is `test`'s value-producing sibling.
- [[X86JumpInstructions]] — the consumers (`je` / `jne` / `jz` / `jnz`).
- [[NullPointer]] — `test %reg, %reg` + `je` is the standard `if (ptr == NULL)` compilation.
