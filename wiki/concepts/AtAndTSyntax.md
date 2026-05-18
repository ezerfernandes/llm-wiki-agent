---
title: "AT&T Assembly Syntax"
type: concept
tags: [assembly, x86-64, ia32, syntax, gcc, gdb, linux]
sources: [dis-7-1-x86-64-basics, dis-2-9-7-c-to-assembly]
last_updated: 2026-05-17
---

# AT&T Syntax

**AT&T syntax** is one of two surface conventions for writing [[X86_64|x86-64]] and [[IA32]] [[AssemblyLanguage|assembly]] — the default for [[GCC|`gcc`]], [[GDB|`gdb`]], [[Objdump|`objdump`]], and the GNU [[AssemblyStage|assembler]] (`as`). Originated at AT&T Bell Labs for the Unix toolchain; competes with [[IntelSyntax|Intel syntax]] (used by Microsoft tools, NASM, and Intel's own reference manuals).

## The four conventions ([[dis-7-1-x86-64-basics|Ch 7.1]])

1. **Register names prefixed `%`** — `%rax`, `%rbp`, `%r8d`. Disambiguates from variable names in inline-assembly contexts.
2. **Immediate (constant) values prefixed `$`** — `$0x2` is hexadecimal 2, `$42` is decimal 42. Distinguishes a literal from a memory address.
3. **Source first, destination second** — `mov src, dst`. Reads left-to-right as **data flows** from source into destination. (Intel syntax is the opposite: `mov dst, src`.)
4. **Memory operands as `disp(base, index, scale)`** — see [[X86AddressingMode]]. The parentheses syntactically distinguish memory operands from arithmetic.

## Worked examples ([[dis-7-1-x86-64-basics|Ch 7.1]])

```asm
mov  $0x2, %eax           ; move immediate 2 into the low 32 bits of %rax
mov  -0x4(%rbp), %eax     ; load 32-bit word at address (%rbp - 4) into %eax
add  $0x2, %eax           ; %eax = %eax + 2
mov  %eax, -0x4(%rbp)     ; store %eax into the local variable at offset -4 from %rbp
```

The third line is the canonical illustration of **source-then-destination**: `add` adds the source `$0x2` into the destination `%eax`.

## [[OperandSize|Size suffixes]] are part of the AT&T convention

Where [[IntelSyntax|Intel syntax]] writes `mov dword ptr [rbp-4], 2` and infers the operand size from operand annotations, AT&T encodes the size **in the mnemonic itself** — `movl $2, -4(%rbp)` uses the `l` suffix to specify a 32-bit (`long`) operand. The full table: `b` (1B), `w` (2B), `l` (4B int), `s` (4B float), `q` (8B long/pointer), `d` (8B double) — see [[OperandSize]].

## Why two syntaxes?

The [[X86_64|x86-64]] [[ISA]] has one binary encoding but two human-readable surface forms — a historical accident of competing toolchain ecosystems:

| | AT&T | Intel |
|---|---|---|
| Default in | [[GCC]], [[GDB]], `objdump`, Linux | MSVC, NASM, Intel manuals |
| Register prefix | `%rax` | `rax` |
| Immediate prefix | `$0x2` | `0x2` |
| Operand order | `mov src, dst` | `mov dst, src` |
| Memory operand | `disp(base, index, scale)` | `[base + index*scale + disp]` |
| Size info | suffix on mnemonic (`movl`) | annotation on operand (`dword ptr`) |

Same instructions, same encoded bytes, different assembly text. [[Objdump|`objdump -M intel`]] disassembles in Intel syntax; without the flag it defaults to AT&T on Linux.

## Connections

- [[dis-7-1-x86-64-basics]] — promoting source; the syntax conventions and worked examples.
- [[dis-2-9-7-c-to-assembly]] — earlier appearance of AT&T syntax in the corpus (via [[IA32]] / `gcc -S`).
- [[AssemblyLanguage]] — the umbrella concept; AT&T is one of its two x86 surface forms.
- [[IntelSyntax]] — the contrasting syntax.
- [[X86_64]] / [[IA32]] — the ISAs AT&T syntax describes.
- [[GCC]] / [[GDB]] / [[Objdump]] — the toolchain that defaults to AT&T on Linux.
- [[OperandSize]] — the suffix mechanism that is part of the AT&T convention.
- [[X86AddressingMode]] — the `disp(base, index, scale)` memory-operand form.
- [[Operand]] — the operand-type taxonomy whose syntactic forms AT&T encodes.
