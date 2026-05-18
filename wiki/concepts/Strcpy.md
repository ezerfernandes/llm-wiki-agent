---
title: "strcpy"
type: concept
tags: [c-language, strings, standard-library, security, buffer-overflow]
sources: [dis-1-5-arrays-strings]
last_updated: 2026-05-17
---

# `strcpy`

`strcpy` is the [[StringLibrary|`<string.h>`]] function that copies a source [[CString|C string]] (including its [[NullTerminator|`'\0'`]] byte) into a destination buffer. It is also **the canonical unsafe function in the C standard library** — per [[dis-1-5-arrays-strings|Ch 1.5]] of [[DiveIntoSystems]], it *"poses a security risk because it assumes that its destination is large enough to store the entire string, which may not always be the case (for example, if the string comes from user input)."*

## Signature

```c
#include <string.h>

char *strcpy(char *dst, const char *src);
```

Returns the destination pointer (`dst`). Copies bytes from `src` into `dst` one at a time, **including** the trailing [[NullTerminator|`'\0'`]] — and stops when it has copied that `'\0'`.

## Example — the intended use

```c
char dst[16];
char src[] = "hello";
strcpy(dst, src);           // dst now holds "hello\0"
```

## Example — the security failure

```c
char dst[5];
strcpy(dst, "hello world");  // writes 12 bytes into a 5-byte buffer
                              // — overflows into adjacent memory
```

Because [[CLanguage|C]] does **no [[BoundsChecking|bounds checking]]**, `strcpy` cannot know that `dst` is only 5 bytes long; it just writes until it has copied the source's `'\0'`. The 7 bytes past the end of `dst` clobber whatever happens to be there — typically other local variables, the saved frame pointer, or the return address of the current function. This is the classic **stack-smashing** [[BufferOverflow|buffer overflow]], the historical root of an enormous family of remote-code-execution vulnerabilities.

## Why the chapter introduces this anyway

[[dis-1-5-arrays-strings|Ch 1.5]] uses `strcpy` deliberately as the *naïve* tool: the simplest function that does what the reader expects, paired with the explicit warning that it is *unsafe*. The safer bounded variant `strncpy` and the formatted variant `snprintf` are deferred to Ch 2.6, where the chapter can devote space to the security model.

## Safer alternatives (Ch 2.6 forward)

- `strncpy(dst, src, n)` — copies at most `n` bytes, *may not* terminate (caller responsible for `dst[n-1] = '\0'`).
- `snprintf(dst, n, "%s", src)` — formatted copy that always writes at most `n` bytes including the terminator. The modern best-practice substitute for `strcpy`.

## Sources

- [[dis-1-5-arrays-strings]] — Ch 1.5 §1.5.4 introduces `strcpy` and *immediately* warns that it is unsafe; foreshadows Ch 2.6's safer alternatives.
