---
title: "Dive into Systems — Ch 9.7 Arrays in Assembly (ARM64)"
type: source
tags: [book, dive-into-systems, arm64, armv8, assembly, arrays]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/arrays.html
sources: []
last_updated: 2026-05-17
---

## Summary

**Seventh leaf** of Ch 9 *64-bit ARM Assembly* of *[[DiveIntoSystems]]* — **non-twin structural sibling** of [[dis-7-7-x86-64-arrays|Ch 7.7]] / [[dis-8-7-ia32-arrays|Ch 8.7]]. Operationalizes [[CArray|C array]] access at the [[ARM64|AArch64]] [[AssemblyLanguage|assembly]] surface: `arr[i]` compiles to pointer arithmetic `*(arr+i)`, emitted via the **fourth [[ARM64AddressingMode|addressing-mode form]]** from [[dis-9-1-arm64-basics|Ch 9.1]] — `[xN, xM, LSL, #s]` — with `LSL, #s` encoding the per-element-size scale as a **bit count** (`#2` = ×4 for `int`, `#3` = ×8 for `long` / pointer). **Headline [[ARM64]]-distinctive feature**: the scale is **explicit shift-count, not numeric scale factor** (cf. [[X86AddressingMode|`disp(base, index, scale)`]] where scale ∈ {1, 2, 4, 8} is encoded numerically) — same effective-address arithmetic, different surface encoding. **No new concept pages** — reuses the existing [[AsmArrayAccess]] / [[ScaledIndexAddressing]] / [[CArray]] / [[ArrayIndexing]] machinery + [[ARM64AddressingMode]] from [[dis-9-1-arm64-basics|Ch 9.1]].

## Key Claims

- **`arr[i]` compiles to scaled-register-offset load.** *"`ldr w0, [x1, x2, LSL, #2]"* — the canonical [[ARM64]] integer-array-access instruction: base in `x1`, index in `x2`, `LSL, #2` (left-shift by 2 = ×4 scale, matching `sizeof(int) = 4`), load 32-bit word into `w0`. Auto-computes `address = base + index × element_size` in a single instruction — the [[ARM64]] analog of [[X86_64|x86]]'s `mov (%rdx, %rcx, 4), %eax`.
- **Byte-level offset = `index × sizeof(T)`.** Array indexing requires multiplying the index by the data type size; for integers, accessing `arr[i]` computes address `arr + (i × 4)` since `sizeof(int) = 4`. For pointers / `long`, the scale becomes 8 (`LSL, #3`). The [[ARM64AddressingMode|fourth addressing-mode form]] folds this multiply into the load/store itself.
- **`lsl` for non-power-of-two or explicit index scaling.** When the index isn't already loaded into a register usable as the scaled-offset operand, the compiler emits `lsl x0, x0, #2` (left-shift by 2 = `i × 4`) explicitly — same [[ARM64ShiftInstructions|shift-as-multiply]] strength-reduction pattern from [[dis-9-3-arm64-arithmetic|Ch 9.3]].
- **Pointer width is 64-bit (`x`-registers); element value width is 32-bit (`w`-registers).** Pointers require 64-bit `xN` registers for address arithmetic; the value loaded into `wN` is the 32-bit `int`. The **`ldrsw`** instruction (load signed word, sign-extending to 64 bits) converts 32-bit indices to 64-bit before participating in pointer calculations.
- **Two-stage compilation: scale, then load.** After computing an element's effective address (via the addressing mode or an explicit `lsl` + `add` sequence), the `ldr` instruction dereferences that address to retrieve the actual value — the [[LoadStoreArchitecture|load/store discipline]] visible at the array-access surface.
- **Same source-level `arr[i]` ↔ `*(arr+i)` equivalence.** [[ArrayDecay|Array decay]] and the `arr[i]` ↔ `*(arr+i)` identity carry over from [[CLanguage|C]] — only the assembly emission differs from [[X86_64|x86-64]] / [[IA32]].

## Key Quotes

> "each data element in arr is of type Type, arr+i implies that element i is stored at address arr + sizeof(Type) * i" — the source-level pointer-arithmetic identity that drives the assembly emission.

> "left shift i by 2 (i << 2, or i*4)" — the [[ARM64ShiftInstructions|shift-as-multiply]] strength-reduction the compiler applies to integer-array indices.

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **100th ingested chapter** / **seventh leaf of Ch 9**.
- [[dis-9-6-arm64-recursion]] — immediate predecessor; closed function-call mechanics. Ch 9.7 pivots to aggregate-data access.
- [[dis-9-1-arm64-basics]] — supplied the fourth [[ARM64AddressingMode|addressing-mode form]] `[xN, xM, LSL, #s]` that Ch 9.7 now operationalizes for arrays.
- [[dis-9-3-arm64-arithmetic]] — supplied the [[ARM64ShiftInstructions|`lsl`]] instruction used for explicit index scaling.
- [[dis-7-7-x86-64-arrays]] / [[dis-8-7-ia32-arrays]] — structural siblings; **headline [[ARM64]] delta**: scale as **bit count** (`LSL, #2`) vs **numeric scale factor** (x86 `scale=4`).
- [[AsmArrayAccess]] / [[ScaledIndexAddressing]] / [[CArray]] / [[ArrayIndexing]] / [[ArrayDecay]] — reused concept pages.
- [[LoadStoreArchitecture]] — the [[ARM64]] [[ISA]]-design rule that confines the array dereference to `ldr` / `str`.

## Contradictions

None. Ch 9.7 **extends** [[CArray|C array]] compilation to the [[ARM64]] surface using the existing [[ScaledIndexAddressing]] concept — the [[ARM64AddressingMode|bit-count scale encoding]] is a surface-syntax variant, same effective-address arithmetic.
