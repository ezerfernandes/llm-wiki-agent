---
title: "Segmentation Fault"
type: concept
tags: [c-language, memory, pointers, runtime-errors, operating-system]
sources: [dis-2-2-pointers]
last_updated: 2026-05-17
---

# Segmentation Fault

A **segmentation fault** (a.k.a. *segfault*, signal `SIGSEGV` on POSIX) is the runtime error a hosted [[OperatingSystem|OS]] reports when a process tries to access memory it is not allowed to access. It is the *typical* — but not the only — visible consequence of misusing a [[Pointer|pointer]] in [[CLanguage|C]].

Per [[dis-2-2-pointers|DIS Ch 2.2]], the three canonical [[Pointer|pointer]] misuses that produce segfaults:

```c
int *ptr;

*ptr = 6;     /* uninitialized — garbage address — likely segfault */

ptr = NULL;
*ptr = 6;     /* NULL dereference — segfault */

ptr = 20;
*ptr = 6;     /* dereferencing a fabricated invalid address — segfault */
```

## What triggers it

The OS partitions a process's [[AddressSpace|address space]] into regions ([[CodeSection|code]] / [[DataSection|data]] / [[HeapSection|heap]] / [[StackSection|stack]] per [[dis-2-1-scope-memory|Ch 2.1]]), each with permissions (read / write / execute). A segfault fires when:

- Reading or writing memory **outside** any mapped region.
- **Writing** to a read-only region (e.g. the [[CodeSection|code section]], or a string literal).
- **Executing** memory in a non-executable region (NX bit).
- Accessing memory at addresses the kernel reserves (`0x00000000` neighborhood on most platforms — which is why [[NullPointer|`NULL`]] dereference reliably segfaults).

## Why `NULL`-deref is reliable

Modern OSes deliberately leave the lowest page (and often several pages) of every process's virtual address space **unmapped**, so that any access through a [[NullPointer|`NULL`]] pointer hits unmapped memory and triggers a fault — instead of silently succeeding and corrupting data. This is one of the few [[CLanguage|C]] failure modes whose behavior is *de facto reliable* across platforms, even though the language standard merely calls it *undefined behavior*.

## Why an uninitialized pointer is *worse*

A [[NullPointer|`NULL`]] dereference *always* crashes — loud and easy to debug. An **uninitialized** pointer holds whatever bytes happened to be in that stack slot — often a *plausible* address inside the mapped portion of the process's [[AddressSpace|address space]]. The dereference may then:

- **Crash** if the address lies in a read-only or unmapped region.
- **Silently succeed**, corrupting some other variable's storage — the symptom may surface arbitrarily later, far from the cause.

This is why [[dis-2-2-pointers|Ch 2.2]]'s safety rule is *"initialize every pointer at declaration"* — convert the silent-corruption footgun into the loud-crash footgun.

## What segfault is *not*

- **Not a [[CLanguage|C]] exception.** [[CLanguage|C]] has no try/catch. The OS delivers `SIGSEGV` to the process; the default handler prints `Segmentation fault` (or `Segmentation fault (core dumped)`) and terminates the program.
- **Not an [[ArrayIndexing|`IndexError`]].** Out-of-range [[CArray|array]] access is [[BoundsChecking|undefined behavior]] — sometimes a segfault, sometimes silent corruption, sometimes nothing visible. Not the same guarantee as Python / Java.
- **Not always caused by [[Pointer|pointers]].** Stack overflow (deep recursion), executing data, and writing through a dangling pointer can all produce segfaults too.

## Debugging discipline

The canonical workflow when a [[CLanguage|C]] program segfaults:

1. **Compile with `-g`** (debug symbols — see [[GCC]]).
2. **Run under a debugger** (`gdb ./a.out`, then `run`).
3. On the crash, `bt` (backtrace) shows the offending line.
4. Inspect pointer values with `print ptr` — check for `0x0` ([[NullPointer|NULL]]) or improbable addresses.
5. **AddressSanitizer** (`-fsanitize=address`) catches many sub-segfault corruptions silently in the wild.

## Connections

- [[CLanguage]] — the language whose semantics permit this failure.
- [[OperatingSystem]] — the layer that detects the invalid access and signals.
- [[Pointer]] — the most common cause of segfaults via misuse.
- [[NullPointer]] — the reliably-segfaulting pointer value.
- [[DereferenceOperator]] — the operator that triggers the access.
- [[AddressSpace]] — the partitioned virtual range whose boundaries the OS enforces.
- [[ProcessMemory]] — the four-region picture from [[dis-2-1-scope-memory|Ch 2.1]] whose permissions a segfault violates.
- [[BoundsChecking]] — its absence in [[CLanguage|C]] is what allows out-of-range access to *sometimes* segfault and *sometimes* corrupt silently.
- [[BufferOverflow]] — a particular class of unchecked write that *sometimes* surfaces as a segfault.
- [[GCC]] — `-g` for debug symbols; `-fsanitize=address` for ASan.
- [[dis-2-2-pointers]] — the source chapter that introduces segfaults via [[Pointer|pointer]] misuse examples.
