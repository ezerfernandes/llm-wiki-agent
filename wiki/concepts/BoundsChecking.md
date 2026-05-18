---
title: "Bounds Checking (and its absence in C)"
type: concept
tags: [c-language, arrays, safety, undefined-behavior]
sources: [dis-1-5-arrays-strings]
last_updated: 2026-05-17
---

# Bounds Checking (and its absence in C)

**Bounds checking** is the runtime (or compile-time) verification that an [[ArrayIndexing|array index]] falls within the valid range `[0, capacity)` of an [[CArray|array]] before the access is performed. Languages that bounds-check turn an out-of-range index into a *defined* error (a thrown exception, a panic, a `Result::Err`); languages that don't turn it into **undefined behavior**.

[[CLanguage|C]] is the canonical *unchecked* language. Per [[dis-1-5-arrays-strings|Ch 1.5]] of [[DiveIntoSystems]]: *"in C, it's up to the programmer to ensure that their code uses only valid index values when indexing into arrays."* The language performs no bounds check at compile time or at runtime; the compiler emits a direct memory access, and whatever happens at that address happens.

## What "no bounds checking" actually means

```c
int array[10];      // valid: array[0]..array[9]
array[10] = 100;    // UB: writes past the end, no error thrown
array[-1] = 0;      // UB: writes BEFORE the array, no error thrown
array[1000000] = 0; // UB: may crash, may corrupt, may appear to work
```

Each of these *compiles*. Each is *undefined behavior*. The C standard explicitly grants the compiler the freedom to assume your code does not exhibit undefined behavior — which means modern optimizers may *delete* code paths that would only matter if an out-of-bounds access occurred.

## Consequences

- **Silent memory corruption.** A write past the end of an array on the stack typically overwrites another local variable, the saved frame pointer, or the return address of the function — see [[BufferOverflow]] and the chapter's [[Strcpy|`strcpy()`]] security warning.
- **Heisenbugs.** The same buggy code can appear to work for years under one compiler version / optimization level / input distribution, then crash when something nearby in memory changes.
- **Security holes.** Buffer overflows in C code are the historical root cause of a substantial fraction of remote-code-execution vulnerabilities — stack smashing, return-oriented programming, and most of the *"never trust user input"* refrain in security culture originate here.

## Why C made this choice

Performance and trust-the-programmer. A bounds check is one or two extra instructions per array access; on tight inner loops in the 1970s — and to a lesser extent today — that overhead was unacceptable. [[CLanguage|C]] was designed by and for systems programmers who would (in theory) reason about index validity statically. The chapter introduces this as a *fact* the reader must internalize, not a design choice to debate.

## Cross-walk to bounds-checked languages

- [[Python]] `list[i]` and `str[i]` raise `IndexError`.
- Java `arr[i]` raises `ArrayIndexOutOfBoundsException`.
- Go indexed access on slices panics.
- Rust indexing with `[]` panics; the `.get()` method returns `Option<&T>` instead.

[[CLanguage|C]] is now the outlier among production-grade languages on this dimension; the cost has been measured in CVEs.

## Sources

- [[dis-1-5-arrays-strings]] — Ch 1.5 §1.5.2 *Array Access Methods* declares the rule; §1.5.4 cashes it out as the [[Strcpy|`strcpy()`]] [[BufferOverflow|buffer-overflow]] risk.
