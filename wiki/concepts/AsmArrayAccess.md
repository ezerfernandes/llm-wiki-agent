---
title: "Array Access Compilation Pattern (x86-64 Assembly)"
type: concept
tags: [x86-64, assembly, arrays, addressing-mode, compilation-pattern]
sources: [dis-7-7-x86-64-arrays]
last_updated: 2026-05-17
---

# Array Access Compilation Pattern (x86-64 Assembly)

The canonical [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] pattern for compiling [[CLanguage|C]] [[CArray|array]] access — `arr[i]`, `&arr[i]`, `*(arr+i)` — per [[dis-7-7-x86-64-arrays|Ch 7.7]] of [[DiveIntoSystems]]. The pattern rests on a single mechanism: the [[ScaledIndexAddressing|scaled-index addressing mode]] `disp(base, index, scale)`, which computes `base + index*scale + displacement` in hardware as part of a memory operand.

## The three canonical forms

| C expression | x86-64 assembly | Mechanism |
|---|---|---|
| `x = arr[i]` | `mov (%rdx, %rcx, 4), %eax` | [[ScaledIndexAddressing|scaled-index]] load with `scale = sizeof(int) = 4` |
| `x = &arr[3]` | `lea 0xc(%rdx), %rax` | [[LeaInstruction|`lea`]] with constant displacement `3*4 = 12` |
| `x = *(arr+5)` | `mov 0x14(%rdx), %eax` | Identical to `arr[5]` — [[ArrayDecay|array decay]] makes them equivalent |

`%rdx` = base address of `arr`, `%rcx` = index `i`, `%eax` = 32-bit destination (matching `int`'s size).

## Why one instruction is enough

[[CLanguage|C]] memory is [[ByteAddressable|byte-addressable]], so accessing `arr[i]` of element type `T` requires computing the effective address `arr + i * sizeof(T)`. Without [[ScaledIndexAddressing|scaled-index addressing]] the compiler would need a multiply + an add before every load — three instructions per array access. [[X86_64|x86-64]] folds the entire computation into the memory operand: `mov (base, index, scale), dst` does `dst ← mem[base + index*scale]` atomically, eliminating the explicit arithmetic instructions.

The `scale` operand is restricted to `{1, 2, 4, 8}` — the same set of [[CLanguage|C]] primitive type sizes (`char`/`short`/`int`/`long`):

- `char` arrays → `scale = 1`
- `short` arrays → `scale = 2`
- `int` arrays → `scale = 4`
- `long` / pointer arrays → `scale = 8`

## The `sumArray` worked example

Ch 7.7 walks `sumArray(int *array, int len)` through compilation. The array-access kernel is:

1. **Widen the index**: `cltq` sign-extends 32-bit `i` (in `%eax`) to 64-bit (`%rax`) — needed because [[GeneralPurposeRegister|GPRs]] addressing memory must be 64-bit.
2. **Materialize the offset**: `lea 0x0(,%rax,4),%rdx` computes `rdx = 0 + i*4 + 0 = i*4` using [[LeaInstruction|`lea`]] as the [[dis-7-3-x86-64-arithmetic|Ch 7.3]] arithmetic-shortcut form.
3. **Load the base**: `mov` the `array` base pointer into another register.
4. **Add base + offset**: produces the absolute address of `array[i]`.
5. **Dereference**: `mov (...)` retrieves the `int` value.

Note: the compiler chooses between fully-folded `mov (%rdx, %rcx, 4), %eax` (one instruction) and the unfolded `lea` + separate `add` + `mov` (three instructions) depending on context — both realize the same array-access pattern.

## Constant-index degenerate form

When the index is a compile-time constant (e.g., `arr[3]`), the compiler **collapses the addressing mode**: `index` and `scale` both vanish, and the displacement absorbs the full offset:

```
arr[3]   →   12(%rdx)      (= 0xc(%rdx))
arr[5]   →   20(%rdx)      (= 0x14(%rdx))
```

This is why `&arr[3]` reduces to `lea 0xc(%rdx), %rax` rather than involving an index/scale operand.

## Connections

- [[ScaledIndexAddressing]] — the underlying addressing-mode form this compilation pattern rides on.
- [[X86AddressingMode]] — the broader family of [[X86_64|x86-64]] memory operand forms.
- [[CArray]] — the [[CLanguage|C]] source-level construct compiled by this pattern.
- [[ArrayDecay]] — the [[CLanguage|C]] rule that makes `arr[i]` and `*(arr+i)` compile identically.
- [[LeaInstruction]] — used for `&arr[i]` (address-only) and for the offset materialization in `sumArray`.
- [[X86MovInstruction]] — the load/store instruction the addressing mode plugs into.
- [[GeneralPurposeRegister]] — the 64-bit registers carrying base, index, and result; `cltq` widens 32-bit indices to 64-bit before they enter the addressing mode.
- [[dis-7-1-x86-64-basics]] — first introduced `disp(base, index, scale)` as an addressing-mode form.
- [[dis-7-3-x86-64-arithmetic]] — established [[LeaInstruction|`lea`]] as an arithmetic shortcut, reused here.
- [[dis-7-7-x86-64-arrays]] — source page; the chapter delivering this pattern.

## Scope (per Ch 7.7)

- **Covered**: 1-D arrays of primitive types with size ∈ `{1, 2, 4, 8}`.
- **Not covered**: multidimensional arrays, struct arrays, [[BoundsChecking|bounds checking]], [[BufferOverflow|buffer-overflow]] mechanics. These are scope omissions of Ch 7.7 itself.
