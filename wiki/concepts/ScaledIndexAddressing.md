---
title: "Scaled-Index Addressing Mode (x86-64)"
type: concept
tags: [x86-64, assembly, addressing-mode, arrays]
sources: [dis-7-7-x86-64-arrays, dis-7-1-x86-64-basics]
last_updated: 2026-05-17
---

# Scaled-Index Addressing Mode (x86-64)

The full form of the [[X86_64|x86-64]] memory operand `disp(base, index, scale)` — *scaled-index* addressing — computes the effective address `base + index*scale + displacement` as part of a single instruction, per [[dis-7-7-x86-64-arrays|Ch 7.7]] of [[DiveIntoSystems]]. Introduced as one of the six [[X86AddressingMode|addressing-mode forms]] in [[dis-7-1-x86-64-basics|Ch 7.1]] and delivered as the workhorse mechanism for [[CArray|C array]] access in Ch 7.7.

## Form

```
disp(base, index, scale)   →   base + index*scale + displacement
```

| Component | Meaning | Type |
|---|---|---|
| `base` | starting address (typically array base) | 64-bit [[GeneralPurposeRegister|GPR]] |
| `index` | subscript / offset count | 64-bit [[GeneralPurposeRegister|GPR]] |
| `scale` | element size in bytes | constant ∈ `{1, 2, 4, 8}` |
| `disp` | constant offset | signed integer literal |

The `scale ∈ {1, 2, 4, 8}` restriction is hardware-level — encoded directly in the [[X86_64|x86-64]] instruction format. The set is **exactly** the size set of [[CLanguage|C]] primitive types (`char` / `short` / `int` / `long`/pointer), which is **not** a coincidence: the addressing mode was designed for array indexing.

## Why this matters

Without scaled-index addressing, accessing `arr[i]` in [[ByteAddressable|byte-addressable]] memory would require:

```asm
imul $4, %rcx, %rax       ; rax = i * sizeof(int)
add  %rdx, %rax           ; rax = arr + i*4
mov  (%rax), %eax         ; load arr[i]
```

— three instructions per access. [[ScaledIndexAddressing|Scaled-index]] collapses this to one:

```asm
mov  (%rdx, %rcx, 4), %eax    ; load arr[i] with rdx=arr, rcx=i, scale=4
```

The CPU computes `rdx + rcx*4` inside the load — no separate arithmetic instructions, no intermediate register pressure.

## Degenerate forms

When operands are missing, the mode collapses to the simpler forms listed in [[dis-7-1-x86-64-basics|Ch 7.1]]'s [[X86AddressingMode|addressing-mode table]]:

| Form | Computes | Notes |
|---|---|---|
| `disp(base, index, scale)` | `base + index*scale + disp` | full form — used for variable array index |
| `(base, index, scale)` | `base + index*scale` | full form, no displacement |
| `disp(base)` | `base + disp` | scalar offset access — used for `&arr[3]` with constant index |
| `(base)` | `base` | plain pointer dereference |

A constant-index array access like `arr[3]` (where `3` is a literal) reduces to `disp(base)` because the compiler folds `3 * sizeof(int) = 12` into the `disp` field — `index` and `scale` are no longer needed at runtime.

## Use in `lea`

[[LeaInstruction|`lea`]] (load effective address) — introduced in [[dis-7-3-x86-64-arithmetic|Ch 7.3]] — accepts the same `disp(base, index, scale)` form as a memory operand but computes the address **without dereferencing it**. This makes `lea` a one-instruction arithmetic shortcut for `base + index*scale + disp`:

```asm
lea 0x0(,%rax,4),%rdx     ; rdx = 0 + rax*4 + 0 = rax*4
lea 0xc(%rdx), %rax       ; rax = rdx + 12 = &arr[3]
```

The first form computes `i * 4` in a single instruction without touching memory; the second computes `&arr[3]` for compile-time-constant index `3`.

## Limits

- `scale` is **hardware-restricted** to `{1, 2, 4, 8}`. Element types outside this set (e.g., [[CStruct|`struct`]] elements of size 12 or 24 bytes) require manual pre-multiplication via [[X86MulInstruction|`imul`]] or a [[LeaInstruction|`lea`]] chain before entering the addressing mode.
- Both `base` and `index` must be 64-bit [[GeneralPurposeRegister|GPRs]] when computing a memory address. 32-bit indices (common when loop counters are `int`) need `cltq` widening to 64-bit first.

## Connections

- [[X86AddressingMode]] — the broader family this mode belongs to.
- [[AsmArrayAccess]] — the [[CArray|array-access]] compilation pattern that consumes this mode as its workhorse.
- [[CArray]] — the [[CLanguage|C]] source-level construct this mode was designed to support efficiently.
- [[X86MovInstruction]] — the canonical instruction that uses this addressing mode for array loads/stores.
- [[LeaInstruction]] — uses the same mode for arithmetic without memory access.
- [[GeneralPurposeRegister]] — supplies the 64-bit registers used for `base` and `index`.
- [[dis-7-1-x86-64-basics]] — first introduced this addressing-mode form as part of the [[X86AddressingMode|six-form table]].
- [[dis-7-3-x86-64-arithmetic]] — introduced [[LeaInstruction|`lea`]] which reuses this form for non-memory arithmetic.
- [[dis-7-7-x86-64-arrays]] — the source page operationalizing this mode for [[CArray|array]] access.

## Scope

This page covers what [[dis-7-1-x86-64-basics|Ch 7.1]] and [[dis-7-7-x86-64-arrays|Ch 7.7]] cover: the form, the `{1, 2, 4, 8}` scale restriction, and array-indexing use. Encoding-level details (ModR/M + SIB byte layout) and segment-register prefixes are **not** covered by either chapter and are out of scope here.
