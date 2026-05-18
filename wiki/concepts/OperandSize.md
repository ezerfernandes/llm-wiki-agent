---
title: "Operand Size (x86-64 Instruction Suffix)"
type: concept
tags: [x86-64, assembly, att-syntax, isa, data-width, type-system]
sources: [dis-7-1-x86-64-basics]
last_updated: 2026-05-17
---

# Operand Size

**Operand size** is the bit-width of data an instruction operates on. In [[X86_64|x86-64]] [[AtAndTSyntax|AT&T syntax]], the operand size is encoded as a **one-letter suffix on the instruction mnemonic** — `movb` vs `movw` vs `movl` vs `movq` are four different instructions targeting 1, 2, 4, and 8-byte operands respectively. Per [[dis-7-1-x86-64-basics|Ch 7.1]]: *"Common and arithmetic instructions have a suffix that indicates the size (associated with the type) of the data being operated on."*

## The suffix table ([[dis-7-1-x86-64-basics|Ch 7.1]])

| Suffix | C type | Size (bytes) | Size (bits) |
|---|---|---|---|
| `b` | `char` | 1 | 8 |
| `w` | `short` | 2 | 16 |
| `l` | `int` / `unsigned` | 4 | 32 |
| `s` | `float` | 4 | 32 |
| `q` | `long`, pointers | 8 | 64 |
| `d` | `double` | 8 | 64 |

The `b` / `w` / `l` / `q` integer suffixes mnemonic-encode **byte / word / long / quad** — names inherited from the original 16-bit Intel 8086, where a *word* was 16 bits and a *long* word was 32. `s` and `d` are floating-point variants (single-precision / double-precision) used by SSE / x87 instructions.

## Picks the right subregister width

The suffix and the **register name** must agree on width. A 32-bit add uses the `l` suffix and a 32-bit subregister name (`%eax`, `%r8d`); a 64-bit add uses `q` and the full 64-bit name (`%rax`, `%r8`):

```asm
addb $0x1, %al         ; 8-bit add — writes only the low byte of %rax
addw $0x1, %ax         ; 16-bit add — writes only the low 16 bits
addl $0x1, %eax        ; 32-bit add — writes %eax; on x86-64 ZEROS the high 32 bits of %rax
addq $0x1, %rax        ; 64-bit add — writes the full 64-bit %rax
```

**Subtle x86-64 rule** (not in Ch 7.1 but follows from the suffix system): a 32-bit destination implicitly zero-extends to 64 bits. The 8-bit and 16-bit variants leave the upper bits unchanged.

## Why the suffix exists

x86-64 inherited variable-width arithmetic from its [[IA32|32-bit]] and 16-bit ancestors. The same opcode "ADD register-to-register" exists in four widths; the assembler picks the right machine-code byte sequence based on the suffix. In [[AtAndTSyntax|AT&T syntax]] the size is *always* explicit on the mnemonic — there is no `add` without a suffix in compiler-generated code. In [[IntelSyntax|Intel syntax]] the size is annotated on operands instead (`dword ptr [rbp-4]`).

## The type-to-suffix mapping the compiler uses

Per [[dis-7-1-x86-64-basics|Ch 7.1]]: *"The compiler typically uses the 64-bit registers when dealing with 64-bit values (e.g., pointers or long types) and the 32-bit component registers when dealing with 32-bit types (e.g., int)."* So a C `int x; x = x + 1;` compiles to `addl $0x1, %eax` — not `addq`, because `int` is 32 bits on most x86-64 platforms (the LP64 model: `int` = 32, `long` = 64, `pointer` = 64).

## Connections

- [[dis-7-1-x86-64-basics]] — promoting source; supplies the suffix table.
- [[X86_64]] — the [[ISA]] whose instructions take size suffixes.
- [[AtAndTSyntax]] — the syntax that puts size info on the mnemonic.
- [[IntelSyntax]] — the contrasting syntax that puts size info on operands (`dword ptr`).
- [[GeneralPurposeRegister]] — the register set whose subregister widths the suffix selects.
- [[CPrimitiveType]] — the C type widths (`char` / `short` / `int` / `long` / `float` / `double`) the suffix maps from.
- [[AssemblyLanguage]] — the broader text-form of which `b`/`w`/`l`/`q` suffixes are an [[AtAndTSyntax|AT&T]]-specific convention.
- [[Operand]] — the operand taxonomy these suffixes apply to.
- [[X86AddressingMode]] — memory-operand sizes are governed by the same suffix scheme.
