---
title: "ARM64 Addressing Modes"
type: concept
tags: [arm64, aarch64, assembly, memory, addressing-mode, isa]
sources: [dis-9-1-arm64-basics]
last_updated: 2026-05-17
---

# ARM64 Addressing Modes

An **addressing mode** is a syntactic form for naming a memory location inside an instruction's memory operand. On [[ARM64]] — by virtue of the [[LoadStoreArchitecture|load/store architecture]] — memory operands appear **only** on `ldr` (load) and `str` (store) instructions, and use **bracketed syntax** with a small fixed set of forms.

## The four forms in [[dis-9-1-arm64-basics|Ch 9.1]]

| ARM64 form | Effective address | Use case |
|---|---|---|
| `[xN]` | `xN` | Plain pointer dereference: `*p` |
| `[xN, #imm]` | `xN + imm` (signed) | Struct field at offset / local-variable stack slot: `s->field`, `[sp, #12]` |
| `[xN, xM]` | `xN + xM` | Array-by-pointer with byte index |
| `[xN, xM, LSL, #s]` | `xN + (xM << s)` | Scaled-index addressing — `arr[i]` with `sizeof(elem) = 2^s` |

The fourth form is [[ARM64|ARM64]]'s analog of [[ScaledIndexAddressing|x86-64 scaled-index addressing]] — but with **two structural differences**:

1. **Explicit shift mnemonic.** ARM64 names the shift kind (`LSL` = logical shift left) in the operand. [[X86_64|x86-64]] / [[IA32]] encode it as a numeric scale factor.
2. **Shift amount is a bit count, not a byte count.** `LSL, #2` on ARM64 = ×4 on x86-64. `LSL, #3` on ARM64 = ×8 on x86-64. To index an `int` array (4-byte elements), use `LSL, #2`; for `long` / pointer arrays (8-byte elements), `LSL, #3`.

## Worked example — `adder2`'s stack-slot access

Per [[dis-9-1-arm64-basics|Ch 9.1]]'s unoptimized `adder2`:

```
str w0, [sp, #12]      ; form 2 — base + immediate offset
ldr w0, [sp, #12]      ; same form, load direction
```

This is the **canonical local-variable access** — base register [[StackPointer|`sp`]], immediate offset `#12`, accessing a 4-byte `int` slot 12 bytes above the stack pointer.

## Compare with x86-64

The same four conceptual operations side by side:

| Operation | [[X86_64\|x86-64]] (AT&T) | [[ARM64]] |
|---|---|---|
| `*p` | `(%rax)` | `[x0]` |
| `s->field` (offset 8) | `0x8(%rax)` | `[x0, #8]` |
| Array element by index | `(%rax, %rcx)` | `[x0, x1]` |
| `arr[i]` (`int` array, scale = 4) | `(%rax, %rdx, 4)` | `[x0, x2, LSL, #2]` |
| `arr[i]` (`long`/pointer array, scale = 8) | `(%rax, %rdx, 8)` | `[x0, x2, LSL, #3]` |

**Same effective-address space, different surface syntax + different scale-encoding convention.**

## Compare with x86-64's unified template

[[X86AddressingMode|x86-64 addressing modes]] use a **single unified template** `displacement(base, index, scale)` that subsumes six concrete forms by zeroing fields. ARM64's four forms are presented in Ch 9.1 as **distinct forms** rather than projections of a single template — but the same effective-address surface is reachable.

## Where these forms appear

Only on **`ldr` and `str`** (and their byte / halfword / signed-extending variants — `ldrb` / `ldrh` / `ldrsw` / etc., out of scope for Ch 9.1). **No** other instruction class — `add` / `sub` / `mul` / `and` / `cmp` — accepts a bracketed memory operand. This is the [[LoadStoreArchitecture|load/store rule]] expressed at the addressing-mode-availability surface.

## Connections

- [[dis-9-1-arm64-basics]] — promoting source; lists the four forms.
- [[ARM64]] — the [[ISA]] this template belongs to.
- [[LoadStoreArchitecture]] — the policy that restricts these addressing modes to `ldr` / `str`.
- [[AArch64Registers]] — `xN` registers are the base and index components.
- [[X86AddressingMode]] — the contrasting [[CISC]] addressing-mode template (`disp(base, index, scale)`).
- [[ScaledIndexAddressing]] — the cross-ISA concept; ARM64's `LSL, #s` form is the AArch64 instance.
- [[StackPointer]] — `sp` is the canonical base register for local-variable stack slots.
- [[Operand]] — the operand-type taxonomy.
- [[AssemblyLanguage]] — the umbrella concept.
