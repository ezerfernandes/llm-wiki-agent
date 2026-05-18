---
title: "Dive into Systems — Ch 1.5 Arrays and Strings"
type: source
tags: [book, dive-into-systems, c-language, arrays, strings]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C1-C_intro/arrays_strings.html
---

## Summary

Section 1.5 of [[DiveIntoSystems]] (fifth content section of Ch 1 *By the C, the Beautiful C*) introduces the first **aggregate** data types of the [[CLanguage|C]] surface area: the **[[CArray|array]]** as an ordered, fixed-capacity, contiguous run of same-type elements, and the **[[CString|C string]]** as a special case of that — a `char` array whose end is marked by a single sentinel byte, the **[[NullTerminator|null character `'\0'`]]**. The chapter strips Python's auto-resizing-`list` abstraction and Java's `String` object away and shows what's actually there at the hardware level: a base address, a programmer-tracked capacity, no [[BoundsChecking|bounds checking]] by the language, and a [[PassByReference|pass-by-reference]] calling convention that *contradicts* the [[PassByValue|pass-by-value]] rule the previous chapter ([[dis-1-4-functions|Ch 1.4]]) declared as universal — because what's actually copied at the call boundary is the array's base address, not its contents. The C string library (`<string.h>`) gets a *three-function* opening — [[Strlen|`strlen()`]], [[Strcpy|`strcpy()`]], [[Sprintf|`sprintf()`]] — together with the chapter's headline safety warning: [[Strcpy|`strcpy()`]] *"poses a security risk because it assumes that its destination is large enough to store the entire string, which may not always be the case (for example, if the string comes from user input)"*, a [[BufferOverflow|buffer overflow]] foreshadowing for Ch 2.6.

## Key Claims

- **An [[CArray|array]] in [[CLanguage|C]] is fixed-capacity and contiguous.** `int arr[10];` allocates exactly 10 consecutive `int` slots; the *capacity* is part of the type and cannot grow. Unlike a [[Python]] `list`, the programmer manually tracks how many slots are actually *used* in a separate variable.
- **Memory layout is part of the language's contract.** Per the chapter, *"C dictates the array layout in program memory"* — array elements occupy consecutive memory locations, which is what later lets the chapter graft pointer arithmetic onto array access.
- **[[ArrayIndexing|Array indexing]] is zero-based and unchecked.** Valid indices run `0` through `capacity - 1`. The compiler and the runtime perform **no [[BoundsChecking|bounds checking]]** — `array[10]` on an `int array[10]` is *undefined behavior*, not a thrown exception. Per [[dis-1-5-arrays-strings|Ch 1.5]]: *"in C, it's up to the programmer to ensure that their code uses only valid index values when indexing into arrays."*
- **[[CArray|Arrays]] pass to functions by *reference* (technically: by base address).** This is the chapter's headline pivot away from the [[PassByValue|pass-by-value]] rule [[dis-1-4-functions|Ch 1.4]] declared universal. Mutating `a[i]` inside `void test(int a[], int size)` *does* persist in the caller's array; mutating `size` does not. The mechanism — *the array name decays to a pointer to its first element, and that pointer is what is passed by value* — is the lever for Ch 1.6's pointer chapter.
- **A [[CString|C string]] is a `char` array with a sentinel.** No separate `String` type. The end of the string is marked by the [[NullTerminator|null character `'\0'`]] (byte value zero, *not* the digit `'0'`). Anything that doesn't find `'\0'` will keep reading off the end — another [[BoundsChecking|no-bounds-checking]] failure mode.
- **Capacity must include the [[NullTerminator|null terminator]].** A 5-character string like `"hello"` needs at least a `char[6]` to fit `'h' 'e' 'l' 'l' 'o' '\0'`. The chapter calls failing to do this *"a common source of errors for novice C programmers."*
- **The [[StringLibrary|`<string.h>`]] library is the standard tooling.** Ch 1.5 opens with three functions — [[Strlen|`strlen()`]] (length **excluding** the null terminator), [[Strcpy|`strcpy(dst, src)`]] (copy `src` into `dst`), and [[Sprintf|`sprintf(dst, fmt, …)`]] (formatted construction into `dst`).
- **[[Strcpy|`strcpy()`]] is unsafe by design.** Per the chapter, it *"poses a security risk because it assumes that its destination is large enough to store the entire string, which may not always be the case (for example, if the string comes from user input)."* Safer alternatives (`strncpy`, `snprintf`) are deferred to Ch 2.6.
- **Multidimensional arrays are deferred.** The chapter explicitly defers `int matrix[3][4]`-style declarations to Ch 2.5; Ch 1.5 stays one-dimensional.
- **Cross-walk to [[Python]].** Python's `list` is variable-capacity, bounds-checked, and heterogeneous; Python's `str` is an immutable object with `len()` and slicing. C's `int arr[10]` and `char s[10]` are *fixed-capacity, unchecked, homogeneous byte runs* — every property the higher-level languages hide is now the programmer's responsibility.

## Key Quotes

> "C dictates the array layout in program memory." — establishes that an [[CArray|array]] is not just a logical sequence but a specific *contiguous* memory layout, the substrate for pointer arithmetic in the next chapter.

> "In C, it's up to the programmer to ensure that their code uses only valid index values when indexing into arrays." — the headline [[BoundsChecking|no-bounds-checking]] rule that distinguishes [[CLanguage|C]] arrays from [[Python]] lists and other bounds-checked languages' array types.

> "Failing to properly account for null characters is a common source of errors for novice C programmers." — the chapter's framing of the [[NullTerminator|null-terminator]] discipline as the *first* place [[CLanguage|C]]'s low-level honesty bites beginners.

> "[[Strcpy|`strcpy()`]] poses a security risk because it assumes that its destination is large enough to store the entire string, which may not always be the case (for example, if the string comes from user input)." — the [[BufferOverflow|buffer-overflow]] foreshadowing; the entire later security-and-systems story (Ch 2.6, stack smashing, ASLR) starts here.

## Worked examples

**Array declaration and bounded use:**

```c
int arr[10];     // 10 ints, valid indices 0..9
char str[20];    // 20 chars (max 19-char string + '\0')
arr[10] = 100;   // UNDEFINED BEHAVIOR — no error thrown
```

**[[PassByReference|Pass-by-reference]] for arrays, [[PassByValue|pass-by-value]] for scalars:**

```c
void test(int a[], int size) {
    if (size > 3) {
        a[3] = 8;   // persists in caller's array
    }
    size = 2;       // changes only the local parameter copy
}
```

**Manual [[CString|C string]] construction with explicit [[NullTerminator|null terminator]]:**

```c
char str1[10];
str1[0] = 'h';
str1[1] = 'i';
str1[2] = '\0';   // required — without this str1 is not a valid C string
```

**Library use — [[Strlen|`strlen`]] + [[Strcpy|`strcpy`]]:**

```c
#include <string.h>

char dst[10];
char src[] = "hello";
strcpy(dst, src);            // copies "hello\0" (6 bytes)
size_t n = strlen(dst);      // n == 5  (null terminator NOT counted)
```

## Connections

- [[DiveIntoSystems]] — the book; this is Ch 1.5 (5th content section after [[dis-1-1-getting-started|Ch 1.1]] / [[dis-1-2-input-output|Ch 1.2]] / [[dis-1-3-conditionals-loops|Ch 1.3]] / [[dis-1-4-functions|Ch 1.4]]).
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-1-1-getting-started]] — supplied the [[CPrimitiveType|primitive types]] (`int`, `char`) that arrays are now built **of**.
- [[dis-1-2-input-output]] — supplied the [[FormatSpecifier|`%s` specifier]] for printing strings; this chapter says what a string *is*.
- [[dis-1-3-conditionals-loops]] — supplied the [[ForLoop|`for`]] loop pattern used to iterate over array indices.
- [[dis-1-4-functions]] — supplied the [[PassByValue|pass-by-value]] rule that this chapter explicitly **breaks** for [[CArray|arrays]] (and which Ch 1.6 will explain by way of pointer decay).
- [[CLanguage]] — adds the first **aggregate** types ([[CArray|array]], [[CString|C string]]) to the language's surface area.
- [[CArray]] — the chapter's headline type: ordered, fixed-capacity, contiguous, same-type elements.
- [[ArrayIndexing]] — zero-based, unchecked subscripting `arr[i]`.
- [[BoundsChecking]] — *absent* from [[CLanguage|C]] by design; this section is where that fact becomes load-bearing.
- [[CString]] — a `char` array terminated by the [[NullTerminator|null character `'\0'`]].
- [[NullTerminator]] — the sentinel byte `'\0'` marking string end; *not* the digit `'0'`.
- [[StringLibrary]] — `<string.h>`: the standard string-manipulation header.
- [[Strlen]] — returns the number of characters in a [[CString|C string]], **excluding** the null terminator.
- [[Strcpy]] — copies a source [[CString|C string]] into a destination buffer; **unsafe** if the destination is too small.
- [[Sprintf]] — formatted construction of a [[CString|C string]] into a destination buffer (the [[Printf|`printf`]] family member that writes to a buffer instead of [[StandardOutput|stdout]]).
- [[BufferOverflow]] — the security failure mode [[Strcpy|`strcpy()`]] enables; chapter explicitly flags it as the motivation for Ch 2.6.
- [[PassByReference]] — the array-parameter convention that contradicts [[dis-1-4-functions|Ch 1.4]]'s blanket [[PassByValue|pass-by-value]] rule.
- [[Python]] — contrast: `list` is variable-capacity, bounds-checked, heterogeneous, and pass-by-object-reference; `str` is an immutable Unicode object with `len()` built in.

## Contradictions

- **Apparent contradiction with [[dis-1-4-functions|Ch 1.4]]'s [[PassByValue|pass-by-value]] rule.** Ch 1.4 declared *"any change to a parameter's value in the function … is not visible to the caller"* as a universal rule. Ch 1.5 immediately exhibits a counterexample: mutating an array element inside a function *is* visible to the caller. The wiki's [[PassByValue]] page must be read alongside [[PassByReference]] / [[CArray]] to see the reconciliation — what's *actually* passed by value is the array's base address (a pointer); mutating the *pointer* is invisible to the caller, but mutating what the pointer *points at* is. The full reconciliation is in Ch 1.6's pointer chapter; for now, [[CArray]] is flagged as the exception. Not a wiki-internal inconsistency, just a chapter-level pedagogical layering that Ch 1.6 will resolve.
- No contradictions with existing concept pages.
