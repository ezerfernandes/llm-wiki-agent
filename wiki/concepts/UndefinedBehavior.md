---
title: "Undefined Behavior (C / C++)"
type: concept
tags: [c-language, semantics, compiler, optimization, safety, computer-systems]
sources: [dis-4-5-overflow]
last_updated: 2026-05-17
---

# Undefined Behavior (UB)

**Undefined behavior (UB)** in the [[CLanguage|C]] and C++ language standards designates program constructs whose effect the standard **deliberately leaves unconstrained** — *anything may happen*, from the obvious (wrap-around, crash) to the surprising (the compiler deletes the surrounding code under the assumption UB never occurs). Distinct from *implementation-defined* (compiler must document its choice) and *unspecified* (compiler picks from a finite set without documenting).

Introduced into the wiki by [[dis-4-5-overflow|Dive into Systems Ch 4.5]]'s [[IntegerOverflow|integer-overflow]] treatment — though Ch 4.5 itself stays at the hardware-mechanics level and does not name the [[CLanguage|C]]-semantics consequence. This page collects the load-bearing UB context the systems-level chapter omits.

## Why UB exists in the standard

The [[CLanguage|C]] language was designed for *portability across heterogeneous machine architectures* in the 1970s when integer widths, signed-encoding choices, endianness, alignment rules, and trap behaviour all varied between platforms. The standards committee's response was to **not specify** behaviour for operations whose result legitimately differed across hardware — moving the cost of definition off the compiler and onto the programmer, in exchange for an optimization licence.

Modern compilers ([[GCC]] / [[Clang]] / MSVC) treat the **optimization licence** aggressively: *"if a path through the program would invoke UB, the compiler may assume that path is never taken"* — and may then prune that path, propagate the assumption backward, and reshape control flow accordingly. This is the source of the *"UB makes code disappear"* phenomenon that surprises programmers.

## The canonical signed-overflow case

Per [[dis-4-5-overflow|Ch 4.5]]'s hardware-level treatment, [[IntegerOverflow|signed-integer overflow]] is detected on most hardware via the `OF` (overflow flag) bit. The [[CLanguage|C]] standard's response:

- **Unsigned overflow**: **defined** as modular wrap-around. `UINT_MAX + 1u == 0u` is guaranteed portable, useful for ring-buffer counters / hash mixers / cryptographic primitives that *intend* modular semantics.
- **Signed overflow**: **undefined behavior**. The compiler may assume `int x; x + 1 > x` is **always true** and optimize accordingly — even though on real hardware $x + 1$ can wrap to `INT_MIN` when $x = $ `INT_MAX`.

The optimization consequence: loop-induction-variable hoisting, [[StrengthReduction|strength-reduction]], and bounds-check elimination all rely on the signed-overflow-is-UB assumption. A classic [[Clang]] / [[GCC]] surprise:

```c
int check(int x) {
    return x + 1 < x;  // intended: detect overflow
}
```

Under `-O2`, both compilers compile this to `return 0;` — the signed `x + 1 < x` can only be true if signed overflow occurred, which is UB, so the compiler concludes the predicate is unreachable and the function constant-returns `0`. The programmer's overflow check has been deleted.

The portable fix uses **unsigned** intermediate types (defined wrap) or the compiler builtins `__builtin_add_overflow` / `__builtin_smul_overflow` (which produce the overflow flag directly without invoking UB).

## Other common UB categories

The C standard lists ~200 UB cases. The load-bearing ones for systems programming:

- **Signed integer overflow** — discussed above.
- **Out-of-bounds [[CArray|array]] access** — `arr[i]` for `i >= n` is UB even if the read-from address is mapped. Compilers exploit this for bounds-check elimination.
- **[[NullPointer|Null]] pointer dereference** — `*p` when `p == NULL` is UB (separate from the segfault hardware delivers; the compiler may have already deleted the surrounding code under the assumption $p \ne \text{NULL}$).
- **[[UseAfterFree|Use-after-free]]** — accessing memory after [[Free|`free()`]] is UB. Hardware doesn't always detect it (the heap allocator may reuse the slot silently) — see [[Valgrind]] / [[AddressSanitizer]].
- **[[DataRace|Data races]]** — concurrent unsynchronized access where at least one is a write is UB in C11/C++11. Compilers may reorder, tear, or duplicate the access.
- **Strict aliasing violation** — casting `int *` to `float *` and dereferencing it is UB. The compiler may assume `int` and `float` accesses don't alias and reorder them.
- **Uninitialized [[LocalVariable|local-variable]] read** — UB regardless of what the [[StackSection|stack]] slot happens to hold. See [[UninitializedReadError]].
- **Reaching the end of a non-`void`-returning function without `return`** — UB; the caller observes whatever the [[CpuRegister|return register]] happened to contain.
- **Pointer arithmetic past the *one-past-the-end* boundary** — even forming the pointer (without dereferencing) is UB. Per [[PointerArithmetic|Ch 2.9.4]]'s mechanism, *one-past-the-end* is the only legal out-of-range pointer.
- **Integer division by zero / `INT_MIN / -1`** — UB. The first traps on most hardware; the second overflows because `-INT_MIN` is unrepresentable in two's complement.

## Detection and mitigation

- **[[Valgrind]] / [[Memcheck]]** — catches a subset (uninitialized reads, heap UAF, heap buffer overflow, double-free, leaks). Does *not* catch signed-overflow UB.
- **[[AddressSanitizer|AddressSanitizer (ASan)]]** — catches heap + stack + global out-of-bounds, UAF, double-free at runtime with ~2× slowdown.
- **UndefinedBehaviorSanitizer (UBSan)** — [[Clang]] / [[GCC]] flag `-fsanitize=undefined` instruments code to trap on signed overflow, shift-overflow, null-deref, alignment violations.
- **Compiler flags** — `-Wall -Wextra -Wpedantic` catches some UB statically. `-fwrapv` makes [[GCC]] / [[Clang]] define signed overflow as wrap-around (forfeits the optimization licence — *"fewer surprises, slower loops"*).
- **Static analyzers** — `clang-tidy`, [[CppCheck]], Coverity, PVS-Studio flag many UB patterns.

## UB in safety-critical code

The [[CLanguage|C]] subset standards [[MISRA_C|MISRA-C]] and [[CERT_C|CERT-C Coding Standard]] prohibit large UB categories outright (no signed-overflow-prone arithmetic, no pointer arithmetic outside arrays, no strict-aliasing violations) — trading expressive power for analyzability. Required reading for avionics ([[DO178C]]), automotive ([[ISO26262]]), and medical-device firmware. The [[Therac25|Therac-25]] integer-overflow case [[dis-4-5-overflow|Ch 4.5]] cites is a canonical UB-with-human-consequences study in this literature.

## See also

- [[IntegerOverflow]] — the canonical UB case introduced by [[dis-4-5-overflow|Ch 4.5]].
- [[CLanguage]] — the language whose standard defines UB.
- [[CCompiler]] / [[GCC]] / [[Clang]] — the implementations that exercise the UB optimization licence.
- [[Valgrind]] / [[AddressSanitizer]] — runtime UB detectors (subset coverage).
- [[BufferOverflow]] / [[UseAfterFree]] / [[UninitializedReadError]] — common memory-safety UB categories the wiki covers.
- [[dis-4-5-overflow|Dive into Systems Ch 4.5]] — the chapter whose [[IntegerOverflow|integer-overflow]] treatment surfaces the need for this concept (without naming UB explicitly).
