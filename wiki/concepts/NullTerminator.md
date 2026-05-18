---
title: "Null Terminator"
type: concept
tags: [c-language, strings, sentinel]
sources: [dis-1-5-arrays-strings]
last_updated: 2026-05-17
---

# Null Terminator

The **null terminator** (also *null character*, *NUL byte*) is the byte with value **zero** (`0x00`) that marks the logical end of a [[CString|C string]]. Written in [[CLanguage|C]] source code as `'\0'`.

## Two characters that are emphatically not the same

| Literal | Character value | Byte value |
|---|---|---|
| `'\0'` | null character | `0x00` |
| `'0'` | digit zero | `0x30` (= 48) |

Confusing them is one of the first canonical [[CLanguage|C]] beginner bugs. `'0' == 0` is **false** (`48 != 0`); `'\0' == 0` is **true**.

## Why it exists

A [[CArray|C array]] does not carry its used length as metadata — the language gives you a base address and a *capacity*, but the *actual* length of the data inside is the programmer's problem. For [[CString|strings]], [[CLanguage|C]] solves this by *sentinel termination*: the string ends at the first `'\0'` byte. Every [[StringLibrary|`<string.h>`]] function — [[Strlen|`strlen`]], [[Strcpy|`strcpy`]], `strcat`, `strcmp` — scans forward until it sees one.

## Capacity must include the terminator

A 5-character string like `"hello"` needs a `char` array of capacity **6** to fit `'h' 'e' 'l' 'l' 'o' '\0'`. Per [[dis-1-5-arrays-strings|Ch 1.5]] of [[DiveIntoSystems]]: *"failing to properly account for null characters is a common source of errors for novice C programmers."*

```c
char buf[5];
strcpy(buf, "hello");   // UNDEFINED BEHAVIOR: writes 6 bytes into a 5-byte buffer
```

The 6th byte (`'\0'`) overflows the buffer — see [[BufferOverflow]].

## String literals auto-terminate

A double-quoted [[CString|string literal]] in source code has the `'\0'` appended by the compiler:

```c
char s[] = "hi";    // capacity 3: 'h', 'i', '\0'
```

Manually built strings need the byte added explicitly:

```c
char str1[10];
str1[0] = 'h';
str1[1] = 'i';
str1[2] = '\0';     // <-- without this, str1 is not a valid C string
```

## What happens if you forget it

Every library function scans past the end of the intended string into whatever bytes happen to follow in memory. [[Strlen|`strlen`]] returns garbage; [[Strcpy|`strcpy`]] copies garbage; [[Printf|`printf`]] with `%s` prints garbage. Often the program *appears* to work because the next byte happens to be zero by accident.

## Cross-walk

- [[Python]] / Java strings carry an explicit length field — no terminator needed.
- Pascal-style strings prefix the length as a byte or short. Faster `strlen` (constant time) but capped length.
- [[CLanguage|C]]'s choice trades $O(n)$ length and an extra byte for one less header field. The choice has aged poorly on safety grounds but remains the wire format of countless protocols and file formats.

## Sources

- [[dis-1-5-arrays-strings]] — Ch 1.5 §1.5.4 introduces `'\0'` as the C string sentinel and warns that forgetting it is a beginner-classic bug.
