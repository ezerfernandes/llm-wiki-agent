---
title: "Intel Assembly Syntax"
type: concept
tags: [assembly, x86-64, ia32, syntax, intel, microsoft, nasm]
sources: [dis-7-1-x86-64-basics, dis-2-9-7-c-to-assembly]
last_updated: 2026-05-17
---

# Intel Syntax

**Intel syntax** is one of two surface conventions for writing [[X86_64|x86-64]] and [[IA32]] [[AssemblyLanguage|assembly]] — the default for Microsoft tools (MASM, MSVC), NASM, and Intel's own architecture reference manuals. The contrasting convention is [[AtAndTSyntax|AT&T syntax]], used by [[GCC|`gcc`]] / [[GDB|`gdb`]] / [[Objdump|`objdump`]] on Linux.

## The four conventions (vs. [[AtAndTSyntax|AT&T]])

1. **No prefix on register names** — `rax`, `rbp`, `r8d`. ([[AtAndTSyntax|AT&T]]: `%rax`.)
2. **No prefix on immediates** — `2`, `0x2`, `42`. ([[AtAndTSyntax|AT&T]]: `$0x2`.)
3. **Destination first, source second** — `mov dst, src`. ([[AtAndTSyntax|AT&T]]: `mov src, dst`.) Mirrors the natural-language order *"store X into Y"* as `mov Y, X`.
4. **Memory operands in brackets** — `[base + index*scale + disp]`. ([[AtAndTSyntax|AT&T]]: `disp(base, index, scale)`.)

[[OperandSize|Operand size]] is annotated on the operand (`dword ptr [rbp-4]`) rather than encoded as a mnemonic suffix.

## Same instruction, two surfaces

The [[dis-7-1-x86-64-basics|Ch 7.1]] example `addl $0x2, %eax` ([[AtAndTSyntax|AT&T]]) renders in Intel syntax as `add eax, 2`:

| | AT&T | Intel |
|---|---|---|
| Add 2 to `%eax` | `addl $0x2, %eax` | `add eax, 2` |
| Move 5 into local at `-4(%rbp)` | `movl $0x5, -0x4(%rbp)` | `mov dword ptr [rbp-4], 5` |
| Load array element `arr[i]` (8-byte) | `movq (%rdi, %rsi, 8), %rax` | `mov rax, qword ptr [rdi + rsi*8]` |

Same encoded bytes, different text.

## Scope in [[dis-7-1-x86-64-basics|Ch 7.1]]

Ch 7.1 uses [[AtAndTSyntax|AT&T syntax]] exclusively — the GCC default. Intel syntax is the **implicit contrast** that the AT&T-specific conventions (`%` prefix, `$` prefix, `mov src, dst`) only make sense against. This wiki page documents Intel syntax to make the contrast explicit; the [[DiveIntoSystems|DIS]] corpus does not teach Intel syntax in Ch 7.1, though the surrounding chapters reference *"the syntax other tools use."*

## Connections

- [[dis-7-1-x86-64-basics]] — promoting source (covered implicitly as contrast to [[AtAndTSyntax|AT&T]]).
- [[AtAndTSyntax]] — the contrasting convention; [[GCC]] / [[GDB]] / [[Objdump]] default on Linux.
- [[AssemblyLanguage]] — the umbrella concept.
- [[X86_64]] / [[IA32]] — the ISAs Intel syntax describes.
- [[Objdump]] — `objdump -M intel` selects Intel syntax for disassembly.
- [[OperandSize]] — annotated on operands in Intel syntax (`dword ptr`), suffix-on-mnemonic in [[AtAndTSyntax|AT&T]].
- [[X86AddressingMode]] — same six addressing modes; Intel writes them in `[]` brackets.
