---
title: "AArch64 Register Set"
type: concept
tags: [arm64, aarch64, registers, gpr, isa]
sources: [dis-9-1-arm64-basics]
last_updated: 2026-05-17
---

# AArch64 Register Set

The **[[ARM64|AArch64]]** [[ISA]] exposes **31 general-purpose 64-bit registers** plus a small set of architectural special-purpose registers. Per [[dis-9-1-arm64-basics|Ch 9.1]]: *"ARMv8 provides 31 general-purpose 64-bit registers, named `x0`–`x30`, for storing data."*

## General-purpose registers

| Width | Name range | Count | Notes |
|---|---|---|---|
| 64-bit | `x0` – `x30` | 31 | the primary names |
| 32-bit | `w0` – `w30` | 31 | **component aliases** — low 32 bits of the corresponding `xN` |

**Two register widths only.** Unlike [[X86_64|x86-64]]'s four-level subregister hierarchy (`%rax` → `%eax` → `%ax` → `%al`/`%ah`), AArch64 exposes only the **64-bit `xN`** and the **32-bit `wN`** views. There are no 16-bit or 8-bit subregister names at this chapter's surface.

**Narrowing rule.** Per [[dis-9-1-arm64-basics|Ch 9.1]]: *"If 32-bit data is stored in component register `w0`, then the upper 32 bits of the register become inaccessible, and are zeroed out."* Writing to `wN` therefore **zero-extends** into `xN` — structurally analogous to [[X86_64|x86-64]]'s *write-to-32-bit-zeros-upper-32* rule.

**Compiler-chosen width.** The C-to-assembly compiler picks `xN` for `long` / pointer values and `wN` for `int` values — operand width is selected at the **register-name** layer, not via a mnemonic suffix as in [[X86_64|x86-64]] / [[IA32]].

## Special-purpose registers

Per [[dis-9-1-arm64-basics|Ch 9.1]]:

| Name | Role | Width | Notes |
|---|---|---|---|
| `sp` | [[StackPointer\|stack pointer]] | 64-bit | top of the current call's stack |
| `pc` | program counter | 64-bit | address of the next instruction; **read-only** at user-mode |
| `zr` | zero register | 64-bit | permanently 0 — reads return 0, writes are discarded |

The **`zr` zero register** is one structural reason the GPR count is 31 (not 32) — the encoding slot a 32nd GPR would occupy is consumed by `zr`. `xzr` (64-bit form) and `wzr` (32-bit form) both name the zero register.

## Worked example — `[sp, #12]` in `adder2`

Per [[dis-9-1-arm64-basics|Ch 9.1]]'s unoptimized `adder2` trace:

```
str w0, [sp, #12]      ; store parameter a to stack at sp+12
ldr w0, [sp, #12]      ; reload from sp+12 into w0
```

`sp` is used as the base of the [[ARM64AddressingMode|`[base, #offset]`]] memory form to address a local-variable stack slot — the canonical use of the stack pointer in function bodies.

## Comparison with x86-family register counts

| ISA | GPR count | Width |
|---|---|---|
| [[IA32]] | 8 | 32-bit |
| [[X86_64]] | 16 | 64-bit |
| **[[ARM64]]** | **31** | **64-bit** |
| [[RISCV]] (RV64I) | 32 (one is `x0` zero) | 64-bit |

ARM64's 31 GPRs nearly double x86-64's count — characteristic of [[RISC]] ISAs, which trade complex addressing modes and instruction-set richness for a larger register file.

## Connections

- [[dis-9-1-arm64-basics]] — promoting source.
- [[ARM64]] — the [[ISA]] this register set belongs to.
- [[LoadStoreArchitecture]] — registers are the **only** operand class for arithmetic / logic / shift; memory is reached only via `ldr` / `str` operating on these registers.
- [[ARM64AddressingMode]] — uses `xN` registers as base and index components.
- [[GeneralPurposeRegister]] — the umbrella concept; this page contributes the AArch64 row.
- [[StackPointer]] — `sp` is the AArch64 stack pointer.
- [[X86_64]] — contrast: 16 GPRs vs ARM64's 31.
- [[IA32]] — contrast: 8 GPRs vs ARM64's 31.
- [[CallingConvention]] — `xN` / `wN` register choice is governed by the AArch64 procedure-call standard (out-of-scope for Ch 9.1).
