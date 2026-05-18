---
title: "Dive into Systems — Ch 7.8 Matrices in Assembly (x86-64)"
type: source
tags: [dive-into-systems, x86-64, assembly, matrices, multidimensional-array, addressing-mode]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/matrices.html
---

## Summary

**Eighth leaf** of Ch 7 *x86-64 Assembly* of *[[DiveIntoSystems]]* — the **matrices extension** of [[dis-7-7-x86-64-arrays|Ch 7.7]]'s 1-D array-compilation pattern to the 2-D case. Walks two distinct [[CLanguage|C]] [[MultidimensionalArray|2-D-array]] memory layouts — **contiguous statically/single-`malloc`-allocated matrices** (one block in [[RowMajorOrder|row-major order]]) and **[[ArrayOfArrays|noncontiguous array-of-arrays]]** (an [[X86_64|x86-64]] register-sized `int **` outer array plus per-row inner [[Malloc|`malloc`]] calls) — and shows how the compiler emits [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] for each via the **`sumMat` (contiguous)** and **`sumMatrix` (noncontiguous)** worked examples. Headline rule: the **layout choice is observable at the assembly surface** — contiguous form collapses element access into a single linear `i*cols + j` offset using the [[AsmArrayAccess|Ch 7.7 scaled-index pattern]]; noncontiguous form requires **two separate dereferences** (one 8-byte-scaled to fetch the row pointer, one 4-byte-scaled inside the row) — the [[PointerArithmetic|pointer-arithmetic]] cost the chapter explicitly trades off against per-row [[Free|`free`]]-ability. **73rd ingested DIS chapter — eighth leaf of Ch 7.**

## Key Claims

- **Two layouts** ([[MultidimensionalArray|Ch 2.5]] recap, now at the assembly surface): **statically declared** matrices `int M1[4][3]` are stored in **one contiguous row-major block**, *"with all the rows contiguously in memory"*; **dynamically declared via array-of-pointers** `int **M2` (N+1 `malloc` calls — outer pointer-array + N row arrays) is **noncontiguous** — *"each row is allocated contiguously in memory, but separate rows are not necessarily contiguous with one another"*; the **single-`malloc` continuous variant** `int *M3 = malloc(ROWS * COLS * sizeof(int))` recovers the contiguous layout at the cost of giving up the `M[i][j]` double-bracket syntax (must hand-write `M3[i*COLS + j]`).
- **Contiguous-matrix access (`sumMat`)** — element `M[i][j]` lives at offset `((i * cols) + j) * sizeof(T)` bytes from the base. The compiler emits four steps: (1) compute `i * cols`, (2) add `j`, (3) scale by element size with [[LeaInstruction|`lea`]] (`lea 0x0(,%rax,4),%rdx` for `int` → multiplies by 4 without a memory access), (4) [[X86MovInstruction|`mov`]] the element through the [[ScaledIndexAddressing|scaled-index addressing mode]]. **Single dereference** — the same Ch 7.7 pattern with a precomputed linear index.
- **Noncontiguous-matrix access (`sumMatrix`, `int **matrix`)** — element `matrix[i][j]` requires **two dereferences**: (1) load the row pointer `matrix[i]` at offset `i * 8` bytes from the outer base (8-byte scale because `int *` is 8 bytes on x86-64), then (2) load the element at offset `j * 4` inside the row. The chapter's assembly excerpt shows *"multiply i by 8, place in %rdx"* followed by *"multiply j by 4, place in %rdx"* — **two separate scaled-multiplies and two separate memory loads**.
- **Worked address example** for the noncontiguous case: `M2[1][2]` resolves as base + `1*8 = 8` bytes → fetches row pointer (e.g., `0x36`) → add `2*4 = 8` bytes inside that row → final element address `0x44`. The contiguous case would instead resolve `M[1][2]` as `base + (1*cols + 2) * 4` — a **single absolute-address computation**.
- **Cost comparison** at the [[X86_64|x86-64]] surface: contiguous = one memory load per element; noncontiguous = two memory loads per element (pointer chase) **plus** worse cache behavior because the row pointers may live anywhere on the heap.
- **No new instructions** are introduced — the chapter reuses [[X86MovInstruction|`mov`]], [[LeaInstruction|`lea`]], [[X86MulInstruction|`imul`]], and [[ScaledIndexAddressing|scaled-index addressing]] from earlier Ch 7 sections. The novelty is the **compilation pattern**, not the instruction surface.

## Key Quotes

> "all the rows contiguously in memory" — characterizing the statically-allocated `int M1[4][3]` layout.

> "each row is allocated contiguously in memory, but separate rows are not necessarily contiguous with one another" — the [[ArrayOfArrays|`int **`]] dynamic-allocation layout.

> "multiply (i*cols+j) by 4, put in %rdx" — the `lea 0x0(,%rax,4),%rdx` step in the `sumMat` contiguous-matrix trace, reusing the [[dis-7-3-x86-64-arithmetic|Ch 7.3]] [[LeaInstruction|`lea`]]-as-shift idiom.

> "multiply i by 8, place in %rdx" / "multiply j by 4, place in %rdx" — the **two scaled-multiplies** in the `sumMatrix` noncontiguous-matrix trace, reflecting the two-stage pointer-chase that array-of-arrays incurs.

## Connections

- [[DiveIntoSystems]] — defining book; this is the **eighth leaf** of Ch 7 *x86-64 Assembly*, the **73rd ingested chapter**.
- [[dis-7-7-x86-64-arrays]] — direct prerequisite; the 1-D [[AsmArrayAccess|array-access compilation pattern]] this page extends to 2-D.
- [[dis-7-3-x86-64-arithmetic]] — supplies the [[LeaInstruction|`lea`]]-as-shift idiom used for the `i*cols + j` linear-offset materialization.
- [[dis-7-1-x86-64-basics]] — supplies the [[ScaledIndexAddressing|`disp(base, index, scale)`]] addressing mode the contiguous-matrix path rides on.
- [[dis-2-5-arrays]] — defines the two [[CLanguage|C]] 2-D-array allocation idioms ([[MultidimensionalArray|static / single-`malloc` contiguous]] vs [[ArrayOfArrays|array-of-arrays]]) at the source level; Ch 7.8 is the **assembly-level realization** of that distinction.
- [[MultidimensionalArray]] — the [[CLanguage|C]] source-level construct compiled here.
- [[RowMajorOrder]] — the layout rule the linear-offset formula `i*cols + j` realizes.
- [[ArrayOfArrays]] — the [[CLanguage|C]] `int **` pattern that produces the two-dereference pointer-chase at the assembly surface.
- [[AsmArrayAccess]] — the 1-D compilation pattern extended here; the `sumMat` contiguous case is a direct application with a precomputed linear index.
- [[ScaledIndexAddressing]] — the `disp(base, index, scale)` form; scale = 4 inside contiguous rows, scale = 8 across the outer `int **` pointer array.
- [[LeaInstruction]] — used to materialize the `(i*cols + j) * 4` offset without a memory access.
- [[X86MulInstruction]] — backs the `i * cols` row-offset multiply when `cols` is not a power of 2.
- [[X86MovInstruction]] — the load instruction that consumes the scaled-index addressing mode at the leaf step.
- [[PointerArithmetic]] — the source-level mechanism underlying the noncontiguous two-dereference pattern.
- [[CArray]] / [[CLanguage]] / [[AssemblyLanguage]] / [[X86_64]] — the broader stack.

## Contradictions

None. Ch 7.8 **extends** Ch 7.7's 1-D-array compilation pattern to the 2-D case — it does not revise the underlying [[ScaledIndexAddressing|scaled-index addressing]] mechanism or the [[LeaInstruction|`lea`]] semantics. The layout-vs-cost trade-off it documents is the **assembly-surface realization** of the [[dis-2-5-arrays|Ch 2.5]] source-level distinction between single-`malloc`-contiguous and array-of-arrays heap-2D forms — adding mechanism rather than revising claims.
