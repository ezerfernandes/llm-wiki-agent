---
title: "x86-64 Memory Addressing Modes"
type: concept
tags: [x86-64, assembly, memory, addressing-mode, isa, att-syntax]
sources: [dis-7-1-x86-64-basics]
last_invoked: 2026-05-17
last_updated: 2026-05-17
---

# x86-64 Addressing Modes

An **addressing mode** is a syntactic form for naming a memory location inside an instruction's [[Operand|memory operand]]. [[X86_64|x86-64]] supports a single unified addressing template that subsumes six concrete forms, all derived by zeroing out subsets of the four fields. In [[AtAndTSyntax|AT&T syntax]] the template is:

```
displacement(base, index, scale)
```

The CPU computes the **effective address** as:

$$
\mathrm{addr} = \mathrm{displacement} + \mathrm{base} + \mathrm{index} \times \mathrm{scale}
$$

and dereferences it. `base` and `index` are [[GeneralPurposeRegister|GPRs]]; `displacement` is a literal (typically signed); `scale` is restricted to **1, 2, 4, or 8** — the byte widths of [[CPrimitiveType|primitive C types]].

## The six forms in [[dis-7-1-x86-64-basics|Ch 7.1]]

| AT&T form | Effective address | Use case |
|---|---|---|
| `(%rax)` | `%rax` | Plain pointer dereference: `*p` |
| `0x8(%rax)` | `%rax + 8` | Struct field at offset 8: `s->field` |
| `(%rax, %rcx)` | `%rax + %rcx` | Array-by-pointer with byte index |
| `0x4(%rax, %rcx)` | `%rax + %rcx + 4` | Struct array element with field offset |
| `0x800(,%rdx,4)` | `0x800 + %rdx*4` | Global array `g[i]` where `g` is at `0x800` and elements are 4 bytes |
| `(%rax, %rdx, 8)` | `%rax + %rdx*8` | C array indexing `arr[i]` with 8-byte elements (pointers / `long`) |

Per [[dis-7-1-x86-64-basics|Ch 7.1]]: *"Scaling factors can be one of 1, 2, 4, or 8."*

## Why scale ∈ {1, 2, 4, 8}

These are precisely the [[CPrimitiveType|byte widths of primitive C types]]: 1 (`char`), 2 (`short`), 4 (`int` / `float`), 8 (`long` / `double` / pointer). Setting `scale = sizeof(T)` lets a single instruction compute `&arr[i]` directly when `arr` has element type `T` — without a separate shift-or-multiply step. This is the hardware support for the **constant-time array indexing** [[CLanguage|C]] promises.

## Why the form is universal

Any [[X86_64|x86-64]] instruction that takes a memory operand can use any of these six forms (with the [[OperandSize|operand-size]] suffix selecting the data width). A single `mov` instruction can therefore express:

- Pointer dereference (`(%rax)`)
- Struct field access (`0x10(%rax)`)
- Array indexing (`(%rdi, %rsi, 8)`)
- Mixed cases (`0x10(%rdi, %rsi, 8)` — `arr[i].field`)

The compiler emits **whichever form fits the C expression** without needing temporary registers for address arithmetic — one reason CISC's complex addressing modes still earn their keep on a modern superscalar core (the [[X86_64|x86-64]] front-end decodes the address-generation work into a single µop).

## Compare with [[IntelSyntax|Intel syntax]]

The same addressing modes in [[IntelSyntax|Intel syntax]] use bracket notation: `(%rax, %rdx, 8)` becomes `[rax + rdx*8]`, and `0x4(%rax, %rcx)` becomes `[rax + rcx + 4]`. Same six effective-address forms, different surface syntax.

## Operand constraints

Per [[Operand]]: a memory operand may appear as **source or destination** but **not both** in the same instruction. The `mov` example `mov src_mem, dst_mem` is illegal — at most one side can use any of the six addressing modes above.

## Connections

- [[dis-7-1-x86-64-basics]] — promoting source; lists the six forms and the scaling-factor constraint.
- [[X86_64]] — the [[ISA]] this template belongs to.
- [[AtAndTSyntax]] — the syntax this page uses (`disp(base, index, scale)`).
- [[IntelSyntax]] — the contrasting syntax (`[base + index*scale + disp]`).
- [[Operand]] — the operand-type taxonomy; memory operands are one of the three types.
- [[GeneralPurposeRegister]] — the base and index registers are GPRs.
- [[OperandSize]] — the suffix that selects the data width loaded or stored from the computed address.
- [[CPrimitiveType]] — the byte widths (1/2/4/8) that justify the scale-factor restriction.
- [[CArray]] — the C construct that the `(base, index, scale)` form directly expresses.
- [[Pointer]] — the C construct that the `disp(base)` form directly expresses.
- [[AssemblyLanguage]] — the umbrella concept.
