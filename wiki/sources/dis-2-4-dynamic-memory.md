---
title: "Dive into Systems — Ch 2.4 Dynamic Memory Allocation"
type: source
tags: [c-language, dynamic-allocation, heap, memory, pointers, malloc, free, systems, textbook]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/dynamic_memory.html
---

# Dive into Systems — Ch 2.4 Dynamic Memory Allocation

## Summary

The fourth section of *[[DiveIntoSystems]]* Ch 2 *A Deeper Dive Into C* — **the chapter that finally delivers the [[DynamicMemoryAllocation|dynamic-memory-allocation]] mechanism** [[dis-2-1-scope-memory|Ch 2.1]] named and deferred. Builds the [[HeapSection|heap]] story out of two API calls — [[Malloc|`malloc`]] (request *n* bytes; returns a [[Pointer|pointer]] to them or [[NullPointer|`NULL`]] on failure) and [[Free|`free`]] (release a previous allocation back to the heap) — with the [[SizeOf|`sizeof`]] operator carrying the byte-count arithmetic, the [[Exit|`exit`]] function as the canonical out-of-memory escape hatch, and the *"set the pointer to [[NullPointer|`NULL`]] after [[Free|`free`]]ing"* discipline as the load-bearing defense against [[UseAfterFree|use-after-free]] / [[DanglingPointer|dangling-pointer]] bugs. Operationalizes the [[dis-2-2-pointers|Ch 2.2]] *second* [[Pointer|pointer]] use case ([[DynamicMemoryAllocation|dynamic memory allocation]] — explicitly forward-referenced at Ch 2.2) and the [[dis-2-1-scope-memory|Ch 2.1]] *third* [[ProcessMemory|program-memory]] region ([[HeapSection|heap]]). Folds [[CArray|arrays]] back in — heap-allocated arrays use the **same** `arr[i]` syntax as the [[dis-1-5-arrays-strings|Ch 1.5]] stack-allocated kind, despite the different underlying types ([[Pointer|pointer]] vs static-array). Closes by handing heap-allocated arrays to [[Function|functions]] via the now-unified [[PassByPointer|pass-by-pointer]] mechanism from [[dis-2-3-pointers-functions|Ch 2.3]] — *"functions can use the same parameter declarations to receive both statically and dynamically allocated arrays as parameters."*

## Key Claims

- **Dynamic memory allocation** is the [[CLanguage|C]] mechanism that *"allows a C program to request more memory as it's running, and a [[Pointer|pointer variable]] stores the address of the dynamically allocated space."* The three needs it covers (per [[dis-2-1-scope-memory|Ch 2.1]] and re-stated here): arrays whose size depends on input, variable-size data without fixed capacity, and storage that grows or shrinks over the program's lifetime.
- **Heap memory is anonymous** — *"a program's heap memory is one large pool of unused memory addresses … the chunk of memory it returns lacks a programmer-assigned variable name."* The only way to refer to a heap allocation is via a [[Pointer|pointer]] holding its [[CMemoryAddress|base address]].
- **The [[HeapSection|heap]] and [[StackSection|stack]] grow toward each other** — *"the stack and heap grow toward each other as the program executes,"* both starting far apart in the [[AddressSpace|address space]] so each has room to expand. Visually completes the Ch 2.1 four-region picture.
- **[[Malloc|`malloc`]] returns a [[Pointer|pointer]]** to a contiguous range of bytes on the heap — *"to call `malloc`, a program passes in the total number of bytes of contiguous heap memory to allocate."* The byte count is computed with [[SizeOf|`sizeof`]] (e.g. `malloc(sizeof(int))` for one `int`, `malloc(sizeof(int) * 20)` for a 20-element `int` array). The returned type is `void *`, assignable to any [[PointerType|pointer type]] without an explicit cast in modern [[CLanguage|C]] (older code shows `p = (int *) malloc(...)`).
- **[[Malloc|`malloc`]] may fail** — when the heap is exhausted or the requested chunk too large, `malloc` returns [[NullPointer|`NULL`]]. The chapter's headline safety rule: *"a program should always test its return value for `NULL`."* Code calling `malloc` must check before [[DereferenceOperator|dereferencing]] — *"dereferencing a `NULL` pointer will cause your program to crash!"* — and on failure typically calls [[Exit|`exit(1)`]] to terminate.
- **Every successful [[Malloc|`malloc`]] needs a matching [[Free|`free`]]** — *"when a program no longer needs the heap memory it dynamically allocated with `malloc`, it should explicitly deallocate the memory by calling the `free` function."* Failing to free leaks the bytes ([[MemoryLeak|memory leak]]); the bytes are not reclaimed until the program exits.
- **After [[Free|`free`]], set the [[Pointer|pointer]] to [[NullPointer|`NULL`]]** — *"setting the freed pointer to `NULL` after freeing it prevents unintended memory references and helps avoid undefined program behavior."* This is the chapter's discipline against [[UseAfterFree|use-after-free]] / [[DanglingPointer|dangling-pointer]] bugs: once a pointer is `NULL`, an accidental [[DereferenceOperator|deref]] reliably [[SegmentationFault|segfaults]] (Ch 2.2's failure mode) instead of silently corrupting whatever the heap manager has since reused the bytes for.
- **Dynamically allocated arrays use the same indexing syntax as static arrays** — *"after dynamically allocating an array, a programmer can use the array index syntax to access its elements (e.g., `arr[0]` accesses the first element of array `arr`)."* The [[Pointer|pointer]] returned from [[Malloc|`malloc`]] *is* the array's base address — the same way the name of a [[dis-1-5-arrays-strings|Ch 1.5]] static array decays. The two **look** identical at the call site (`arr[i]`); they **differ** in their underlying type (`int *` vs `int[N]`) and storage region ([[HeapSection|heap]] vs [[StackSection|stack]]).
- **The same parameter declaration accepts both static and dynamic arrays** — *"functions can use the same parameter declarations to receive both statically and dynamically allocated arrays as parameters."* The `void init_array(int *arr, int size)` signature accepts either — heap-allocated array as base address (since [[Malloc|`malloc`]]'s return value *is* a [[Pointer|pointer]]), stack-allocated array via the [[PassByPointer|pass-by-pointer]] mechanism [[dis-2-3-pointers-functions|Ch 2.3]] codified. The two storage classes are unified at the function-parameter boundary.
- **The heap is managed by a [[FreeList|free list]]** — the chapter's brief implementation peek: the C runtime maintains *"a list of unused chunks of heap memory available for allocation."* Each [[Malloc|`malloc`]] call walks the list for a chunk big enough; each [[Free|`free`]] returns its chunk to the list. Repeated mixed `malloc`/`free` activity produces [[HeapFragmentation|heap fragmentation]] — *"interspersed chunks of free and allocated heap space"* — which can cause `malloc` to fail even when the total free byte count exceeds the request.
- **The heap manager stores [[HeapMetadata|metadata]] alongside each allocation** — implicit in *"the implementation of `free` is able to determine how many bytes to release given just the address of the heap memory chunk."* The size lives in a header preceding the user-visible bytes, which is why [[Free|`free`]] needs only the pointer — not the size — and why [[Free|`free`]]ing a pointer that doesn't point to a `malloc`-returned address (or [[DoubleFree|free-ing a chunk twice]]) corrupts the heap.

## Key Quotes

> "Dynamic memory allocation refers to allocating memory at run time and is performed through a set of specific C functions. Dynamic memory allocation allows a C program to request more memory as it's running, and a pointer variable stores the address of the dynamically allocated space."

> "Dynamically allocated memory occupies the heap memory region of a program's address space."

> "To call `malloc`, a program passes in the total number of bytes of contiguous heap memory to allocate. To allocate space for a single variable, the most common way to invoke `malloc` is to use the `sizeof` operator."

> "Be sure to always test the return value of `malloc` for `NULL`. Dereferencing a `NULL` pointer will cause your program to crash!"

> "When a program no longer needs the heap memory it dynamically allocated with `malloc`, it should explicitly deallocate the memory by calling the `free` function."

> "After calling free, the freed memory should no longer be used by the program … it's good programming practice to set the pointer to `NULL` after freeing it. This way, if it gets accidentally used in the program, the program will crash on a `NULL`-pointer dereference rather than execute with bad memory contents (which could result in difficult-to-debug bad behavior)."

> "The stack and heap grow toward each other as the program executes."

> "Heap memory is anonymous … the chunk of memory it returns lacks a programmer-assigned variable name."

> "Functions can use the same parameter declarations to receive both statically and dynamically allocated arrays as parameters."

## Code Examples (verbatim from the chapter)

**Single-`int` allocation + safety check + use + free:**

```c
int *p;
p = malloc(sizeof(int));      // allocate 4 bytes on the heap for one int
if (p == NULL) {              // ALWAYS check for NULL
    printf("Bad malloc\n");
    exit(1);
}
*p = 6;                       // dereference: store 6 in the heap int
printf("p: %p  *p: %d\n", p, *p);
free(p);                      // release the bytes back to the heap
p = NULL;                     // defend against use-after-free
```

**Dynamically allocated array (20 ints) and string buffer (10 chars):**

```c
int *arr;
char *c_arr;
arr   = malloc(sizeof(int)  * 20);
c_arr = malloc(sizeof(char) * 10);
if ((arr == NULL) || (c_arr == NULL)) {
    printf("Bad malloc\n");
    exit(1);
}
arr[0]   = 8;                // array indexing syntax — identical to Ch 1.5
c_arr[0] = 'h';
free(arr);   arr   = NULL;
free(c_arr); c_arr = NULL;
```

**Heap-allocated array passed to a function (`init_array`) — same signature as a stack-allocated array:**

```c
void init_array(int *arr, int size) {
    int i;
    for (i = 0; i < size; i++) {
        arr[i] = i;
    }
}

int main(void) {
    int *arr1 = malloc(sizeof(int) * 10);
    if (arr1 == NULL) {
        printf("Bad malloc\n");
        exit(1);
    }
    init_array(arr1, 10);      // pass the base address — same as Ch 1.5
    free(arr1);
    arr1 = NULL;
    return 0;
}
```

## Connections

- [[DiveIntoSystems]] — the source textbook.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — the authors.
- [[dis-2-1-scope-memory|Ch 2.1]] — *named* the heap and dynamic allocation; deferred the mechanism here.
- [[dis-2-2-pointers|Ch 2.2]] — explicitly forward-referenced dynamic memory allocation as the *second* of pointers' five use cases.
- [[dis-2-3-pointers-functions|Ch 2.3]] — supplied the [[PassByPointer|pass-by-pointer]] mechanism this chapter now reuses for heap-allocated array parameters.
- [[dis-1-5-arrays-strings|Ch 1.5]] — supplied the [[CArray|array]] / [[CString|string]] syntax this chapter reuses at heap-allocated buffers.
- [[DynamicMemoryAllocation]] — the headline concept; this chapter delivers its mechanism.
- [[Malloc]] / [[Free]] — the two-call API.
- [[SizeOf]] / [[Exit]] — the supporting operators.
- [[NullPointer]] — the failure-mode return value from [[Malloc|`malloc`]] and the discipline-anchor after [[Free|`free`]].
- [[UseAfterFree]] / [[DanglingPointer]] / [[MemoryLeak]] / [[DoubleFree]] — the headline failure modes.
- [[FreeList]] / [[HeapFragmentation]] / [[HeapMetadata]] — the implementation-side concepts.
- [[Pointer]] / [[PointerType]] / [[DereferenceOperator]] / [[AddressOfOperator]] — the [[dis-2-2-pointers|Ch 2.2]] machinery this chapter applies.
- [[HeapSection]] / [[ProcessMemory]] / [[AddressSpace]] — the memory region this chapter populates.
- [[CArray]] / [[CString]] — the [[dis-1-5-arrays-strings|Ch 1.5]] aggregates this chapter delivers heap-allocated.
- [[Function]] / [[FunctionParameter]] / [[PassByPointer]] — the calling convention this chapter reuses.
- [[SegmentationFault]] — the crash mode `NULL`-after-`free` defends against / triggers.
- [[CLanguage]] / [[StandardLibrary]].

## Contradictions

- None. Ch 2.4 *re-affirms* [[dis-2-1-scope-memory|Ch 2.1]]'s heap framing, *completes* [[dis-2-2-pointers|Ch 2.2]]'s second-use-case deferral, *re-uses* [[dis-2-3-pointers-functions|Ch 2.3]]'s pass-by-pointer mechanism for heap arrays, and *unifies* [[dis-1-5-arrays-strings|Ch 1.5]]'s array-indexing syntax across stack and heap storage. No prior wiki claim is overturned.
