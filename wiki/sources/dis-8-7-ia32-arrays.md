---
title: "Dive into Systems — Ch 8.7 Arrays in Assembly (IA32)"
type: source
tags: [dive-into-systems, ia32, assembly, arrays, scaled-index, lea, 32-bit]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C8-IA32/arrays.html
sources: []
last_updated: 2026-05-17
---

## Summary

Chapter 8.7 of *[[DiveIntoSystems]]* — **seventh leaf** of Ch 8 *32-bit IA32 Assembly* and the **32-bit structural twin** of [[dis-7-7-x86-64-arrays|Ch 7.7]]. Operationalizes [[CArray|C array]] access at the [[IA32]] [[AssemblyLanguage|assembly]] surface: the compiler converts `arr[i]` into pointer arithmetic `*(arr+i)` and emits a [[ScaledIndexAddressing|scaled-index]] [[X86AddressingMode|addressing-mode]] operand `disp(base, index, scale)` where `scale = sizeof(elemtype)` — 4 for `int`/pointer, 2 for `short`, 1 for `char`, 8 for `double`. **Headline 32-vs-64 deltas**: (1) array base address loaded into a 32-bit register (`%eax` / `%edx` / `%ecx`) — not a 64-bit register; (2) index from a 32-bit register (`%ecx` / `%edx`); (3) [[LeaInstruction|`leal`]] (the `l` suffix mnemonic) computes 32-bit effective addresses — vs `leaq` on [[X86_64|x86-64]]; (4) array passed to a function arrives as a stack-pushed pointer at `0x8(%ebp)` per [[CdeclCallingConvention|cdecl]], not in `%rdi` per [[SystemVCallingConvention|System V]]; (5) the [[ScaledIndexAddressing|scaled-index]] operand syntax `0x0(,%eax,4)` — base 0, index `%eax`, scale 4 — is **structurally identical** to Ch 7.7 (CISC-family invariant); only the register names narrow. **Headline rules carry over unchanged**: (a) `arr[i]` ↔ `*(arr+i)` ↔ `&arr[i] = arr+i` — pointer-arithmetic equivalence; (b) scale-by-`sizeof(elem)` for byte-offset computation; (c) [[LeaInstruction|`leal`]] for *address* arithmetic without dereference, [[X86MovInstruction|`movl`]] for *value* access with dereference; (d) the same scaled-index operand encoding works for both. **86th ingested DIS chapter — seventh leaf of Ch 8.** **No new concept pages** — reuses [[AsmArrayAccess]], [[ScaledIndexAddressing]], [[LeaInstruction]], [[X86AddressingMode]], [[CArray]] from [[dis-7-7-x86-64-arrays|Ch 7.7]].

## Key Claims

- **`arr[i]` compiles to pointer arithmetic `*(arr+i)`.** *"Compilers commonly convert array references into pointer arithmetic prior to translating to assembly. So `arr+i` is equivalent to `&arr[i]`, and `*(arr+i)` is equivalent to `arr[i]`."* The compile-time identity is what makes the [[ScaledIndexAddressing|scaled-index]] operand format the natural codegen target.
- **Byte-addressable memory mandates `scale = sizeof(elem)`.** *"The compiler must therefore multiply the index by the size of the data type to compute the correct offset."* The [[X86AddressingMode|`disp(base, index, scale)`]] hardware addressing-mode operand encodes this: `scale ∈ {1, 2, 4, 8}` covers `char` / `short` / `int`(or pointer at IA32) / `double` / `long long`.
- **[[ScaledIndexAddressing|Scaled-index]] operand syntax `0x0(,%eax,4)`.** Decodes as base=0, index=`%eax`, scale=4 — i.e., effective address `0 + 4·%eax`. With an explicit base it becomes `(arr_base, %eax, 4)`. Same encoding as [[dis-7-7-x86-64-arrays|Ch 7.7]] — only register widths narrow.
- **[[LeaInstruction|`leal`]] vs [[X86MovInstruction|`movl`]] for address vs value.** *"`leal` computes addresses without dereferencing, while `movl` performs actual memory lookups"* — the critical distinction the compiler uses to compile `&arr[i]` (use `leal`) vs `arr[i]` (use `movl`). Both can take the same scaled-index operand; the instruction choice determines whether memory is read.
- **[[CdeclCallingConvention|Cdecl]] array-passing.** Caller pushes the array's base pointer; callee reads it from `0x8(%ebp)` and stores it (often in `%edx`) before scaled-index loops. Function parameters at positive `%ebp` offsets, local variables at negative `%ebp` offsets — the standard IA32 frame layout from [[dis-8-1-ia32-basics|Ch 8.1]].

## Key Quotes

> "Compilers commonly convert array references into pointer arithmetic prior to translating to assembly. So, `arr+i` is equivalent to `&arr[i]`, and `*(arr+i)` is equivalent to `arr[i]`." — the compile-time identity that makes [[ScaledIndexAddressing|scaled-index]] the natural codegen target.

> "The compiler must therefore multiply the index by the size of the data type to compute the correct offset." — the byte-addressability requirement that drives `scale = sizeof(elem)`.

## Connections

- [[DiveIntoSystems]] — book; **86th ingested chapter**, seventh leaf of Ch 8 *32-bit IA32 Assembly*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-7-7-x86-64-arrays]] — **structural twin** at [[X86_64|x86-64]] width.
- [[dis-8-6-ia32-recursion]] — Ch 8.6; direct predecessor.
- [[dis-8-1-ia32-basics]] — Ch 8.1; minted the [[ScaledIndexAddressing|`disp(base, index, scale)`]] addressing-mode taxonomy at IA32 width.
- [[AsmArrayAccess]] — the concept Ch 8.7 operationalizes at IA32 width — reused from [[dis-7-7-x86-64-arrays|Ch 7.7]] unchanged.
- [[ScaledIndexAddressing]] / [[X86AddressingMode]] — the hardware addressing mode `0x0(,%eax,4)` decodes to.
- [[LeaInstruction]] — `leal` for address computation without dereference; same instruction family as Ch 7.7's `leaq`.
- [[X86MovInstruction]] — `movl` for value access with dereference; the contrast partner to `leal`.
- [[CArray]] — the [[CLanguage|C]] construct compiled.
- [[CdeclCallingConvention]] — array passed as stack-pushed pointer at `0x8(%ebp)`.
- [[IA32]] — the 32-bit ISA.

## Contradictions

None. Ch 8.7 is a **consistent 32-bit re-presentation** of [[dis-7-7-x86-64-arrays|Ch 7.7]] — the scaled-index addressing-mode operand format, the `leal`-vs-`movl` distinction, and the pointer-arithmetic equivalence are structurally identical; only register names and the `l` mnemonic suffix narrow.
