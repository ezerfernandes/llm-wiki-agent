---
title: "exit (C)"
type: concept
tags: [c-language, stdlib, process, termination]
sources: [dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# `exit` (C)

**`exit`** is the [[CLanguage|C]] standard-library function that terminates the process immediately, returning a status code to the operating system. Declared in `<stdlib.h>`:

```c
void exit(int status);
```

- **Parameter** — `status`: the [[ExitStatus|exit status]] handed to the parent process. By convention `0` means success; any non-zero value indicates failure (often `1` for generic error, or per-application codes).
- **Return** — none. Marked `_Noreturn` since C11.

## The Ch 2.4 use case: OOM escape hatch

Per [[dis-2-4-dynamic-memory|DIS Ch 2.4]]'s [[Malloc|`malloc`]] safety pattern — when [[Malloc|`malloc`]] returns [[NullPointer|`NULL`]] and the program has no meaningful recovery, the canonical action is to print a diagnostic and `exit(1)`:

```c
int *p = malloc(sizeof(int) * N);
if (p == NULL) {
    printf("Bad malloc\n");
    exit(1);
}
```

This converts a soft failure (the program could try to continue but would [[NullPointer|`NULL`]]-[[DereferenceOperator|deref]] on the very next line) into a hard failure with a visible diagnostic and a non-zero shell exit code that scripts can check.

## `exit` vs `return` from `main`

Both terminate the program; both deliver an exit status to the parent. The differences:

- **`exit(n)`** works from anywhere in the program, including deeply nested calls. `return n;` works only from [[MainFunction|`main`]].
- **`exit`** runs `atexit`-registered cleanup handlers and flushes [[StandardIOLibrary|`<stdio.h>`]] buffers before terminating. `_exit` / `_Exit` skip these.
- **`return n;` from `main`** is equivalent to `exit(n)` per the C standard.

## `exit` vs `abort`

- **`exit(status)`** — orderly termination with cleanup; flushes [[StandardOutput|stdout]], runs handlers.
- **`abort`** — disorderly termination (raises `SIGABRT`); often triggers a core dump for post-mortem debugging. Used by assertion failures, allocator [[DoubleFree|double-free]] detection, etc.

The [[dis-2-4-dynamic-memory|Ch 2.4]] OOM pattern uses `exit` because the failure is *expected and reportable*, not *internally-inconsistent state*.

The flushes-and-cleanups distinction matters when the OOM diagnostic itself uses [[Printf|`printf`]] — without the flush, a buffered stderr message can be lost on crash.

## Connections

- [[dis-2-4-dynamic-memory]] — the source that uses `exit` as the OOM escape.
- [[ExitStatus]] — the value `exit` hands back to the parent.
- [[MainFunction]] — the alternative termination path (`return n;` from main).
- [[Malloc]] / [[NullPointer]] — the failure case `exit` typically handles in Ch 2.4's pattern.
- [[StandardLibrary]] / [[CLanguage]] / [[DiveIntoSystems]].
