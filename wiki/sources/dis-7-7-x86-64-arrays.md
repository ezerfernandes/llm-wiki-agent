---
title: "Dive into Systems — Ch 7.7 Arrays in Assembly (x86-64)"
type: source
tags: [dive-into-systems, x86-64, assembly, arrays, addressing-mode]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/arrays.html
sources: []
last_updated: 2026-05-17
---

## Summary

Chapter 7.7 of *[[DiveIntoSystems]]* — **seventh leaf** of Ch 7 *x86-64 Assembly* — shows how the compiler translates [[CLanguage|C]] [[CArray|array]] access into [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] via the **[[X86AddressingMode|scaled-index addressing mode]]** `disp(base, index, scale)` introduced as a form back in [[dis-7-1-x86-64-basics|Ch 7.1]]. The headline mechanism is **[[ScaledIndexAddressing|scaled-index addressing]]**: the compiler computes `arr[i]`'s effective address as `base + index*scale + displacement` in a **single instruction**, where `scale` ∈ {1, 2, 4, 8} matches `sizeof(element type)`. Worked example: `sumArray` — an `int` array walk — compiles to `mov (%rdx, %rcx, 4), %eax` for `x = arr[i]` because `sizeof(int) == 4`.

## Key Claims

- **Array access in [[CLanguage|C]] requires address arithmetic because memory is [[ByteAddressable|byte-addressable]].** `arr[i]` is not an opaque indexing operation — at the [[AssemblyLanguage|assembly]] level it must be computed as `arr + sizeof(T) * i`. The compiler is responsible for inserting the `* sizeof(T)` scaling at every array access.
- **[[X86_64|x86-64]] folds the scaling into the addressing mode.** The general memory-operand form `disp(base, index, scale)` from [[dis-7-1-x86-64-basics|Ch 7.1]]'s [[X86AddressingMode|addressing-mode table]] evaluates to `base + index*scale + displacement` **in hardware**, with `scale` restricted to {1, 2, 4, 8} — exactly the sizes [[CLanguage|C]] primitive types use. **`int` array** → scale 4; **`long` / pointer array** → scale 8; **`short` array** → scale 2; **`char` array** → scale 1.
- **`x = arr[i]` compiles to one instruction**: `mov (%rdx, %rcx, 4), %eax` with `%rdx` = base address of `arr`, `%rcx` = index `i`, scale 4 for `int`. The CPU computes the effective address `%rdx + %rcx*4`, dereferences it, and copies the 4-byte result into `%eax` — **all in one [[X86MovInstruction|`mov`]]**.
- **`x = &arr[3]` compiles to one [[LeaInstruction|`lea`]]**: `lea 0xc(%rdx), %rax` — load the *address* `arr + 12` (= `arr + 3*4`) into `%rax` without dereferencing. Displacement `0xc = 12` is a compile-time constant because the index `3` is a literal; no `index` / `scale` operand is needed.
- **`x = *(arr+5)` is the same as `x = arr[5]`** at the [[AssemblyLanguage|assembly]] level: `mov 0x14(%rdx), %eax` — displacement `0x14 = 20 = 5*4`, dereferenced into `%eax`. The [[CLanguage|C]] pointer-arithmetic form and the array-subscript form are **identical** after compilation; the [[ArrayDecay|array decay]] of `arr` to `&arr[0]` makes the equivalence exact.
- **The `sumArray` walked example.** The chapter traces `sumArray(int *array, int len)` through its [[X86_64|x86-64]] assembly: index `i` is sign-extended from 32-bit to 64-bit via `cltq` (because [[GeneralPurposeRegister|GPRs]] addressing memory are 64-bit but loop indices are typically `int`); the offset `i*4` is materialized via `lea 0x0(,%rax,4),%rdx` (the [[LeaInstruction|`lea`]]-as-arithmetic-shortcut idiom from [[dis-7-3-x86-64-arithmetic|Ch 7.3]] — `lea` computing `0 + i*4 + 0 = i*4` without touching memory); the base address `array` is loaded into another register; the two are added to form `array + i*4`; the result is dereferenced to retrieve `array[i]`.
- **Scale-factor selection is automatic per element type.** The compiler reads the declared type of the array and emits the matching scale — programmers do not write the `*sizeof(T)` themselves at either the [[CLanguage|C]] level (subscript and pointer arithmetic both hide it) or the [[AssemblyLanguage|assembly]] level (the addressing mode bakes it in).

## Key Quotes

> "The scaled index addressing mode allows the compiler to access any array element in a single instruction, regardless of element size." — the chapter's headline efficiency claim; `disp(base, index, scale)` collapses the address-arithmetic + load into one [[X86MovInstruction|`mov`]].

> "scale ∈ {1, 2, 4, 8}" — the [[X86_64|x86-64]] [[InstructionSet|ISA]] restriction; not coincidentally the four [[CLanguage|C]] primitive-type sizes. Larger element types (e.g., [[CStruct|`struct`]] arrays) require manual index pre-multiplication via [[X86MulInstruction|`imul`]] or [[LeaInstruction|`lea`]] chains.

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **72nd ingested chapter** and the **seventh leaf** of Ch 7 *x86-64 Assembly*.
- [[dis-7-1-x86-64-basics]] — Ch 7.1 introduced the [[X86AddressingMode|addressing-mode table]] including `disp(base, index, scale)` with the `{1, 2, 4, 8}` scale set. Ch 7.7 is the **payoff page** for that table — the chapter that shows *why* `scale` was specified.
- [[dis-7-3-x86-64-arithmetic]] — Ch 7.3 introduced [[LeaInstruction|`lea`]] as an arithmetic shortcut that computes an address without dereferencing it. Ch 7.7 reuses [[LeaInstruction|`lea`]] in both `&arr[3]` and the `sumArray` `i*4` materialization.
- [[CArray]] — the [[CLanguage|C]] aggregate type Ch 7.7 compiles down. The `arr[i]` syntax at the [[CLanguage|C]] level becomes [[ScaledIndexAddressing|scaled-index addressing]] at the [[AssemblyLanguage|assembly]] level.
- [[ArrayDecay]] — the [[CLanguage|C]] rule that `arr` decays to `&arr[0]` makes `*(arr+5)` and `arr[5]` compile to identical assembly. Ch 7.7's `*(arr+5)` example is the load-bearing demonstration of this equivalence.
- [[X86AddressingMode]] — the family of [[X86_64|x86-64]] memory-operand forms. Ch 7.7's [[ScaledIndexAddressing|scaled-index]] is the **full** form `disp(base, index, scale)` — all four components active.
- [[AsmArrayAccess]] — *new concept page minted by this ingest* — the compilation pattern for [[CArray|C array]] access at the [[X86_64|x86-64]] assembly level.
- [[ScaledIndexAddressing]] — *new concept page minted by this ingest* — the specific addressing-mode form `disp(base, index, scale)` and its `scale ∈ {1, 2, 4, 8}` restriction.
- [[X86MovInstruction]] / [[LeaInstruction]] — the two instructions Ch 7.7's array examples ride on top of; both accept the [[ScaledIndexAddressing|scaled-index]] form as their memory operand.
- [[GeneralPurposeRegister]] — the 64-bit GPRs (`%rdx`, `%rcx`, `%rax`) carrying base, index, and result; the `cltq` widen-to-64-bit step accommodates the 32-bit `int` index used at the [[CLanguage|C]] level.

## Subsections (leaf coverage)

Ch 7.7 is a **single-page section** like Ch 7.5 / Ch 7.6, not a hub. The wiki ingest mints **two new concept pages**:

- **New**: [[AsmArrayAccess]] — the array-access compilation pattern at the [[X86_64|x86-64]] assembly level.
- **New**: [[ScaledIndexAddressing]] — the `disp(base, index, scale)` addressing-mode form with its `scale ∈ {1, 2, 4, 8}` constraint.

## Scope Notes

- **No multidimensional arrays.** Ch 7.7's worked examples are all 1-D. Row-major / column-major layout, strided access, and the `arr[i][j] = arr + i*ROW_BYTES + j*sizeof(T)` two-step is **not** introduced.
- **No struct arrays.** Element sizes outside `{1, 2, 4, 8}` (e.g., [[CStruct|struct]] elements) require manual scaling via [[X86MulInstruction|`imul`]] or [[LeaInstruction|`lea`]] chains; Ch 7.7 does not cover this case.
- **No [[BoundsChecking|bounds checking]] discussion.** Consistent with [[dis-1-5-arrays-strings|Ch 1.5]]'s unchecked-indexing rule — the [[X86_64|x86-64]] [[InstructionSet|ISA]] performs no bounds checking; `mov (%rdx, %rcx, 4), %eax` faithfully computes whatever `%rdx + %rcx*4` resolves to, valid or not.
- **No [[BufferOverflow|buffer-overflow]] / out-of-bounds-attack treatment.** Wiki-flagged but deferred.

## Contradictions

None. Ch 7.7 **extends** the Ch 7 instruction-set tour by showing how the [[dis-7-1-x86-64-basics|Ch 7.1]] [[X86AddressingMode|addressing-mode table]] is **used** in the array case. It adds a compilation pattern rather than revising the underlying mechanism; every claim from [[dis-7-1-x86-64-basics|Ch 7.1]] about `disp(base, index, scale)` remains intact, and the [[LeaInstruction|`lea`]] semantics from [[dis-7-3-x86-64-arithmetic|Ch 7.3]] are reused unchanged.
