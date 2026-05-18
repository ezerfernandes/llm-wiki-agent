---
title: "Dangling Pointer (C)"
type: concept
tags: [c-language, pointers, dynamic-allocation, bugs, undefined-behavior]
sources: [dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# Dangling Pointer (C)

A **dangling pointer** is a [[Pointer|pointer]] that still holds a [[CMemoryAddress|memory address]] but the storage at that address is no longer valid for the pointer's purpose. The pointer hasn't been zeroed — it *looks* usable — but [[DereferenceOperator|dereferencing]] it is undefined behavior.

The two canonical sources of dangling pointers:

1. **The pointee was [[Free|`free`]]d.** A heap chunk released via `free` is no longer the program's to read or write — but the pointer that referenced it still holds the chunk's old address. Subsequent use is a [[UseAfterFree|use-after-free]]. The corpus's headline case, per [[dis-2-4-dynamic-memory|DIS Ch 2.4]].
2. **The pointee went out of scope.** A pointer to a [[LocalVariable|local]] in a [[StackFrame|stack frame]] that has since been popped — e.g., returning `&local_var` from a function — points into a region the next call will overwrite. The [[StackSection|stack]] reuses that storage immediately for the next [[FunctionCall|call]]'s locals.

## The mechanism (heap case)

```c
int *p = malloc(sizeof(int));
*p = 42;
free(p);          // chunk returned to the free list
// p is now a DANGLING POINTER
*p = 99;          // use-after-free — UB
free(p);          // double-free — UB
```

## The mechanism (stack case)

```c
int *bad(void) {
    int x = 5;
    return &x;     // returns a pointer to a soon-popped frame
}                  // x's storage may be reused on the next call

int *p = bad();    // p is a DANGLING POINTER
*p = 99;           // UB — writes into whatever the next call put there
```

## Defense

The [[dis-2-4-dynamic-memory|DIS Ch 2.4]] discipline — set the pointer to [[NullPointer|`NULL`]] after [[Free|`free`]] — converts a dangling pointer into a *known-invalid* one:

```c
free(p);
p = NULL;        // not dangling — explicitly invalid
*p;              // SEGFAULT, not UAF
```

This is strictly an improvement: an accidental [[DereferenceOperator|deref]] now reliably [[SegmentationFault|segfaults]] (Ch 2.2's failure mode) rather than silently misbehaving. It doesn't help when *multiple* pointers aliased the freed chunk — that requires explicit ownership tracking.

For the stack case the defense is structural: never return the [[AddressOfOperator|address]] of a [[LocalVariable|local]] from a function. Either pass the buffer in as an [[OutputParameter|output parameter]] (caller owns the storage) or [[Malloc|`malloc`]] heap storage and return that pointer instead.

## State vs operation

A dangling pointer is the *state*; the dangerous *operations* on it are:

- [[UseAfterFree|Use-after-free]] — [[DereferenceOperator|dereferencing]] it.
- [[DoubleFree|Double-free]] — passing it to [[Free|`free`]] again.
- *Comparison-based bugs* — `if (p == q)` may incorrectly succeed because both still hold the old address, even though neither is now valid.

## Connections

- [[dis-2-4-dynamic-memory]] — introducing source.
- [[Free]] / [[Malloc]] — the API whose mis-pairing creates dangling pointers.
- [[NullPointer]] — the discipline-anchor that *disarms* a dangling pointer.
- [[UseAfterFree]] / [[DoubleFree]] — the operations a dangling pointer enables.
- [[MemoryLeak]] — the *opposite* failure mode (still-reachable chunk, no `free`).
- [[Pointer]] / [[PointerDeclaration]] / [[DereferenceOperator]] — the [[dis-2-2-pointers|Ch 2.2]] machinery.
- [[StackSection]] / [[StackFrame]] / [[LocalVariable]] — the stack-case scope-exit substrate.
- [[HeapSection]] / [[FreeList]] — the heap-case substrate.
- [[SegmentationFault]] — the *visible* failure mode the `NULL`-discipline produces.
- [[CLanguage]] / [[DiveIntoSystems]].
