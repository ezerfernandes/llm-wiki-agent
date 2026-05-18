---
title: "C String"
type: concept
tags: [c-language, strings, arrays]
sources: [dis-1-5-arrays-strings, dis-2-6-strings]
last_updated: 2026-05-17
---

# C String

A **C string** is **not** a distinct type in the [[CLanguage|C]] language — it is a *convention* on top of a [[CArray|`char` array]]: a sequence of `char` values whose end is marked by a single sentinel byte, the [[NullTerminator|null character `'\0'`]]. The string library [[StringLibrary|`<string.h>`]] and the [[FormatSpecifier|`%s` format specifier]] both expect this convention.

## The two things a C string is

1. A `char` array (a [[CArray|C array]] of `char`).
2. With a [[NullTerminator|`'\0'`]] byte somewhere inside it marking the *logical* end.

```c
char s[10];
s[0] = 'h';
s[1] = 'i';
s[2] = '\0';    // <-- this byte is what makes s a valid C string
```

The array has capacity 10; the string is 2 characters long (`strlen` returns 2); the remaining 7 bytes are *uninitialized* and irrelevant as long as nothing reads past the `'\0'`.

## String literals are pre-terminated

`"hello"` written in source code is a `char` array of length **6**: `'h' 'e' 'l' 'l' 'o' '\0'`. The compiler inserts the trailing `'\0'` automatically. This is why the receiving buffer must always have **capacity ≥ string length + 1** — the extra byte is for the terminator. Per [[dis-1-5-arrays-strings|Ch 1.5]] of [[DiveIntoSystems]]: *"failing to properly account for null characters is a common source of errors for novice C programmers."*

## What goes wrong without the terminator

Every library function in [[StringLibrary|`<string.h>`]] — [[Strlen|`strlen`]], [[Strcpy|`strcpy`]], `strcmp`, `strcat`, [[Sprintf|`sprintf`]] (sort of), etc. — *finds the end* of its input string by **scanning forward until it sees a `'\0'`**. If the terminator is missing, the function happily reads off the end of the array until it finds a stray zero byte somewhere in the next stack frame or heap block. Best case: nonsense output. Worst case: [[BufferOverflow|buffer overflow]] or memory-protection fault.

## Comparison to other languages

- [[Python]] `str` — immutable, length-prefixed, Unicode-aware, has built-in `len()`. No terminator concept.
- Java `String` — immutable object with a length field and Unicode chars.
- [[CLanguage|C]] string — mutable (you can edit individual `char`s), length-by-scan-for-`'\0'`, byte-oriented (not Unicode-aware), no built-in length field.

The C model is **the lowest-level honest representation of a string**: it is exactly what's in memory, no metadata header, no length field. The price is the [[NullTerminator|null-terminator]] discipline and the [[BoundsChecking|no-bounds-checking]] hazards.

## Dynamic allocation — Ch 2.6 deepening

Per [[dis-2-6-strings|Ch 2.6]], dynamically allocating a string requires the same `strlen(s) + 1` byte count [[dis-1-5-arrays-strings|Ch 1.5]] flagged, now plugged into [[dis-2-4-dynamic-memory|Ch 2.4]]'s [[Malloc|`malloc`]] machinery:

```c
size_t n = strlen(src);
char *dup = malloc(sizeof(char) * (n + 1));   // +1 for '\0'
if (dup == NULL) { perror("malloc"); exit(1); }
strcpy(dup, src);
/* ... */
free(dup);
dup = NULL;
```

The `+1` is the same byte-counting trap, and the [[NullPointer|`NULL`]] check + [[Exit|`exit`]] + post-`free` `NULL`-assignment discipline is the [[dis-2-4-dynamic-memory|Ch 2.4]] standard pattern.

## Parameter passing — `char []` vs `char *`

Per [[dis-2-6-strings|Ch 2.6]]: *"both statically declared and dynamically allocated arrays of characters can be passed to a `char *` parameter because the name of either type of variable evaluates to the base address of the array in memory."* This is the [[ArrayDecay|array-decay]] rule from [[dis-2-5-arrays|Ch 2.5]] restated for strings. **But the return direction is asymmetric**: a `char *` return value cannot be assigned to a `char []` variable, because *"the name of a statically declared array variable is not a valid [[LValue|lvalue]]."*

## Sources

- [[dis-1-5-arrays-strings]] — Ch 1.5 §1.5.4 *Introduction to Strings and the C String Library* introduces the `char`-array-plus-`'\0'` convention.
- [[dis-2-6-strings]] — Ch 2.6 *Strings and the String Library* adds the dynamic-allocation pattern, the safety discipline, and the [[ArrayDecay|`char []` vs `char *`]] parameter-passing rule.
