---
title: "Operand (x86-64 Assembly)"
type: concept
tags: [assembly, x86-64, isa, syntax]
sources: [dis-7-1-x86-64-basics]
last_updated: 2026-05-17
---

# Operand

An **operand** is an input or output location that an assembly instruction reads or writes. In [[X86_64|x86-64]] [[AssemblyLanguage|assembly]], every instruction is built from an [[OpCode|opcode]] plus zero or more operands. Per [[dis-7-1-x86-64-basics|Ch 7.1]], an instruction's operands appear in **source-then-destination order** in [[AtAndTSyntax|AT&T syntax]].

## The three operand types ([[dis-7-1-x86-64-basics|Ch 7.1]])

1. **Constant (immediate)** — a literal value baked into the instruction. Prefixed `$` in [[AtAndTSyntax|AT&T syntax]]: `$0x2` is hexadecimal 2, `$42` is decimal 42. Constants are **read-only**: they can only appear as source operands, never destinations.
2. **Register** — a [[GeneralPurposeRegister|GPR]] name (or one of the special-purpose registers). Prefixed `%`: `%rax`, `%eax`, `%r8d`, `%al`. Can be both source and destination.
3. **Memory** — an [[X86AddressingMode|addressing-mode expression]] that names a location in [[RAM]]. The CPU dereferences the expression and reads / writes the value at that address. AT&T form: `disp(base, index, scale)`.

## Two structural constraints ([[dis-7-1-x86-64-basics|Ch 7.1]])

- *"Constant forms cannot serve as destination operands."* — you cannot store into an immediate; it has no addressable location.
- *"Memory forms cannot serve as both the source and destination operand in a single instruction."* — at most one operand may be a memory reference. This is a fundamental [[X86_64|x86-64]] [[ISA]] constraint: memory-to-memory moves do not exist as a single instruction. A `mov` between two memory locations requires going through a register.

The pure RISC alternative would be stricter still — `mov` instructions on RISC ISAs forbid memory operands entirely; only `load` and `store` touch memory. [[X86_64|x86-64]]'s CISC heritage permits **one** memory operand per instruction, blurring the load-store boundary.

## Worked examples

```asm
mov $0x5, %eax          ; const → register  (legal: const is source)
mov %eax, %ebx          ; register → register (legal)
mov %eax, -0x4(%rbp)    ; register → memory   (legal)
mov -0x4(%rbp), %eax    ; memory → register   (legal)
mov $0x5, -0x4(%rbp)    ; const → memory      (legal: one operand each side, const can be source)
mov -0x4(%rbp), -0x8(%rbp)  ; ILLEGAL — two memory operands
mov %eax, $0x5          ; ILLEGAL — destination cannot be a constant
```

## Operand types in [[IntelSyntax|Intel syntax]]

Same three types, different surface forms: immediates have no prefix (`5`), registers have no prefix (`eax`), memory uses brackets (`[rbp-4]`). Order is `dst, src` rather than `src, dst`.

## Connections

- [[dis-7-1-x86-64-basics]] — promoting source; supplies the three-type taxonomy and constraints.
- [[X86_64]] — the [[ISA]] whose operand grammar this page documents.
- [[AssemblyLanguage]] — the broader concept; operand is a structural element of every instruction.
- [[AtAndTSyntax]] / [[IntelSyntax]] — the two surface syntaxes that encode operands differently.
- [[GeneralPurposeRegister]] — the register operand type.
- [[X86AddressingMode]] — the memory-operand sub-grammar.
- [[OperandSize]] — the suffix mechanism that selects which width of an operand the instruction uses.
- [[OpCode]] — the other half of every instruction; together with operands, it specifies a complete operation.
- [[InstructionSet]] — the catalog the operand grammar is part of.
