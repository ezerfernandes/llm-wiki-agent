---
title: "fgets (C)"
type: concept
tags: [c-language, stdlib, io, file-io, safety]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# fgets

**`fgets(s, n, fp)`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that reads a **bounded line** from a [[FilePointer|`FILE *`]] into a caller-provided buffer. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.4 the **robust line reader** that fixes the [[Scanf|`scanf("%s", buf)`]] unbounded-write footgun [[dis-1-2-input-output|Ch 1.2]] flagged.

```c
char buf[256];
if (fgets(buf, sizeof(buf), infile) != NULL) {
    /* buf is null-terminated and contains at most 255 chars + '\0' */
}
```

## Defining properties

- **Three arguments**: destination buffer `char *s`, max chars `int n`, source [[FilePointer|`FILE *`]].
- **Reads at most `n - 1` characters.** One byte reserved for the terminating [[NullTerminator|`'\0'`]] — `n` is the *full buffer size including the null*, so `fgets(buf, sizeof(buf), fp)` is the canonical safe form.
- **Stops at one of three triggers**: (a) `n - 1` chars consumed, (b) **newline read and stored** (the `\n` is **included** in the buffer), (c) end-of-file / error.
- **Always [[NullTerminator|null-terminates]]** on success — contrast [[Strncpy|`strncpy`]]'s non-termination footgun.
- **Returns `s` on success, [[NullPointer|`NULL`]] on EOF or error.**

## The robust-`scanf` recipe

[[dis-1-2-input-output|Ch 1.2]] warned that [[Scanf|`scanf`]] is fragile under malformed input. The Ch 2.8 recipe is **`fgets` + `sscanf`**:

```c
char line[256];
int x;
if (fgets(line, sizeof line, stdin) && sscanf(line, "%d", &x) == 1) {
    /* x is parsed */
} else {
    /* report error without leaving stdin half-consumed */
}
```

This composes per-line buffering (no half-consumed lines), bounded buffer writes (no overflow), and the format-string parsing strength of `scanf` (typed parsing).

## Footguns

- **The newline is in the buffer.** Code that compares the result to `"yes"` will see `"yes\n"`. The canonical fix is `line[strcspn(line, "\n")] = '\0';`.
- **Truncation is silent.** If a line is longer than `n - 1`, `fgets` returns a non-newline-terminated buffer and the rest of the line remains on the stream.

## Connections

- [[Fputs]] — the writer sibling.
- [[Scanf]] — the unbounded-string footgun this replaces; the *robust* recipe is `fgets` + `sscanf`.
- [[FilePointer]] — the source type.
- [[NullTerminator]] — always appended on success.
- [[Strncpy]] — the *non-terminating* contrast.
- [[CString]] — the result type.
- [[StandardIOLibrary]] — declares the function.
- [[dis-2-8-io]] — introducing source.
