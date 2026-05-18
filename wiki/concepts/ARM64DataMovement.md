---
title: "ARM64 Data Movement Instructions"
type: concept
tags: [arm64, aarch64, assembly, data-movement, load-store, mov, ldr, str, ldp, stp]
sources: [dis-9-2-arm64-common]
last_updated: 2026-05-17
---

# ARM64 Data Movement Instructions

The **data-movement instruction family** on [[ARM64]] is the **only family that touches memory** under the [[LoadStoreArchitecture|load/store rule]]. Per [[dis-9-2-arm64-common|Ch 9.2]] it consists of **five instructions** split between **register-only `mov`** and the **memory-touching `ldr` / `str` / `ldp` / `stp`** group.

## The five instructions

| Instruction | Effect | Memory side |
|---|---|---|
| `mov D, S` | `D = S` | **None** — register-to-register or immediate-to-register only |
| `ldr D, [addr]` | `D = *(addr)` — *load* memory into register | **Source** is memory |
| `str S, [addr]` | `*(addr) = S` — *store* register to memory | **Destination** is memory |
| `ldp D1, D2, [addr]` | Load **two consecutive** 64-bit values | Source is memory; two registers loaded |
| `stp S1, S2, [addr]` | Store **two consecutive** 64-bit values | Destination is memory; two registers stored |

The pair instructions `ldp` / `stp` move **two 64-bit values** at the addressed location and the **adjacent 8-byte slot**.

## Indexing variants

The bracketed operand has **three indexing forms** that fold pointer-update into the load/store itself:

| Form | Effective address | Base register after |
|---|---|---|
| `[xN, #imm]` | `xN + imm` | **Unchanged** |
| `[xN, #imm]!` (pre-indexed) | `xN + imm` | **Updated to `xN + imm`** *before* access |
| `[xN], #imm` (post-indexed) | `xN` | **Updated to `xN + imm`** *after* access |

## Canonical prologue / epilogue idiom

The pre-indexed pair form compresses the [[StackFrame|stack-frame]] prologue into **one instruction**:

```
stp x29, x30, [sp, #-16]!      ; save fp + lr AND advance sp by -16
...
ldp x29, x30, [sp], #16        ; restore fp + lr AND advance sp by +16
```

Compare with [[X86_64]] which would express the same prologue as `sub $16, %rsp` followed by two `mov` instructions (three instructions) — the [[ARM64]] composite **trades opcode-table real estate for instruction count** on the dominant prologue / epilogue pattern.

## Distinction from [[X86MovInstruction|x86 `mov`]]

[[X86MovInstruction|x86's `mov`]] is a **single instruction** that subsumes the [[ARM64]] split between `mov`, `ldr`, and `str` — its memory operand can appear on either source or destination. [[ARM64]] splits these into **three dedicated instructions** because of the [[LoadStoreArchitecture|load/store rule]]:

| C operation | x86-64 (AT&T) | ARM64 |
|---|---|---|
| `r1 = r2` (register copy) | `movq %r2, %r1` | `mov x1, x2` |
| `r1 = *(r2)` (load) | `movq (%r2), %r1` | `ldr x1, [x2]` |
| `*(r2) = r1` (store) | `movq %r1, (%r2)` | `str x1, [x2]` |

## Worked example — `adder2`'s spill/reload

Per [[dis-9-2-arm64-common|Ch 9.2]]'s annotated `adder2`:

```
str w0, [sp, #12]      ; *(sp + 12) = w0   — store parameter a
ldr w0, [sp, #12]      ; w0 = *(sp + 12)   — reload it
add w0, w0, #0x2       ; w0 = w0 + 2
```

The unoptimized compiler's **store-then-reload reflex** is visible — the value `a` cannot stay in `w0` across statement boundaries, so it round-trips through the stack. This is the [[LoadStoreArchitecture|load/store rule]] made operational.

## Connections

- [[dis-9-2-arm64-common]] — promoting source; defines the five instructions and three indexing forms.
- [[ARM64]] — the [[ISA]].
- [[LoadStoreArchitecture]] — the policy that forces the `mov` / `ldr` / `str` three-way split.
- [[ARM64AddressingMode]] — the bracketed-operand family; pre- and post-indexed forms extend this.
- [[StackFrame]] — the canonical use case for `stp` / `ldp` plus pre-/post-indexing.
- [[StackPointer]] — `sp` is the dominant base register for stack-resident operands.
- [[X86MovInstruction]] — the [[CISC]] one-mnemonic equivalent that subsumes all three [[ARM64]] dedicated instructions.
- [[X86StackInstructions]] — the [[CISC]] `push` / `pop` stack-management family that `stp` / `ldp` plus indexing replaces on [[ARM64]].
- [[Operand]] — the operand-type taxonomy.
- [[AssemblyLanguage]] — umbrella concept.
