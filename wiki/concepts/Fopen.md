---
title: "fopen (C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# fopen

**`fopen(path, mode)`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that **opens a file** and returns a [[FilePointer|`FILE *`]] handle for subsequent stream I/O. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.3 the canonical first half of the **four-step file-I/O protocol**.

```c
FILE *infile = fopen("input.txt", "r");
if (infile == NULL) {
    printf("Error: unable to open file\n");
    exit(1);
}
```

## Defining properties

- **Two arguments**: `const char *path` and `const char *mode`. The `mode` selects [[FileMode|read / write / append]] semantics.
- **Return value**: a [[FilePointer|`FILE *`]] on success or [[NullPointer|`NULL`]] on failure. **Every call site must check for `NULL`** — the chapter's standard recipe is *print error, [[Exit|`exit(1)`]]*.
- **Failure modes**: file doesn't exist (`"r"`), insufficient permissions, OS resource exhaustion, malformed path.
- **Sets `errno`** on failure — `perror("fopen")` prints a human-readable reason.

## File modes (per [[dis-2-8-io|Ch 2.8]])

| Mode | Meaning |
|---|---|
| `"r"` | Read — file must exist; position at start. |
| `"w"` | Write — **truncates** existing file or creates new; position at start. |
| `"a"` | Append — creates if absent; position at end; writes always at end. |

Adding `"+"` (e.g. `"r+"`) opens for both read and write; adding `"b"` (`"rb"`) selects binary mode (Unix doesn't distinguish; Windows does).

## Connections

- [[Fclose]] — the destructor; every successful `fopen` needs exactly one `fclose`.
- [[FilePointer]] — the type `fopen` returns.
- [[FileMode]] — the `mode` string vocabulary.
- [[NullPointer]] — the failure sentinel.
- [[Exit]] — the canonical OOM/open-failure escape.
- [[StandardIOLibrary]] — declares `fopen`.
- [[Fgetc]] / [[Fputc]] / [[Fgets]] / [[Fputs]] / [[Fprintf]] / [[Fscanf]] — the consumers of the returned `FILE *`.
- [[dis-2-8-io]] — introducing source.
