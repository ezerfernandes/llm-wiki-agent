---
title: "Command Line Arguments (argc/argv)"
type: concept
tags: [c-language, command-line-arguments, argc, argv, main, programming]
sources: [dis-2-9-2-cmd-line-args]
last_updated: 2026-05-17
---

# Command Line Arguments (`argc` / `argv`)

**Command-line arguments** are the strings the shell passes to a program when it is invoked. In [[CLanguage|C]], the runtime exposes them to user code through two parameters on the [[MainFunction|`main`]] function: `argc` (argument **c**ount) and `argv` (argument **v**ector). Introduced in [[dis-2-9-2-cmd-line-args|DIS Ch 2.9.2]] as the **generalized `main` signature** that supersedes the introductory `int main(void)` form from [[dis-1-1-getting-started|Ch 1.1]].

## The two parameters

```c
int main(int argc, char *argv[]) {
    /* ... */
    return 0;
}
```

- **`argc`** — an `int` holding the **number of arguments** the shell passed to the program, **including the program name itself** at `argv[0]`. For `./a.out 10 11 200`, `argc == 4`.
- **`argv`** — a [[CArray|`char *` array]] of [[CString|C-string]] arguments. Its `argc + 1` elements are:
  - `argv[0]` — the program-invocation name (e.g. `"a.out"` or `"./a.out"`).
  - `argv[1]..argv[argc-1]` — the user-supplied arguments, in order.
  - `argv[argc]` — a [[NullPointer|`NULL`]] sentinel marking end-of-array.

The trailing `NULL` is what lets argument-walking loops use the terminator pattern instead of needing `argc`:

```c
for (int i = 0; argv[i] != NULL; i++) {
    printf("argv[%d] = %s\n", i, argv[i]);
}
```

## Everything arrives as a string

Even numeric arguments arrive as [[CString|C strings]]. The shell's `./a.out 10` makes `argv[1]` point to the three-byte sequence `'1' '0' '\0'`, **not** to an `int` containing 10. Programs that want a number must convert:

```c
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) { return 1; }
    int n = atoi(argv[1]);           // simple but silent on errors
    /* ... */
}
```

[[Atoi|`atoi`]] is the introductory conversion ([[dis-2-6-strings|Ch 2.6]]); [[Strtol|`strtol`]] is the production replacement that distinguishes *parse failure* from the legitimate input `"0"` and reports [[IntegerOverflow|overflow]] via [[Errno|`errno`]].

## Two equivalent declarations

Because [[CArray|array]] parameters decay to [[Pointer|pointers]] in [[CLanguage|C]] (see [[ArrayDecay]]), both forms are legal and equivalent:

```c
int main(int argc, char *argv[]);   // array-of-pointer-to-char syntax
int main(int argc, char **argv);    // pointer-to-pointer-to-char syntax
```

The `[]` form is conventional because it telegraphs the *"this is an array"* intent at the call site.

## Connections

- [[CLanguage]] — the language whose `main` entry-point this generalizes.
- [[MainFunction]] / [[MainArgcArgv]] — the entry-point function whose signature `argc`/`argv` complete.
- [[CArray]] / [[CString]] / [[Pointer]] / [[NullPointer]] / [[ArrayDecay]] — the type machinery `argv` is built from.
- [[Atoi]] / [[Strtol]] — the standard-library bridges from `char *` to `int` / `long` for numeric arguments.
- [[Errno]] — the global error-flag [[Strtol|`strtol`]] uses to report [[IntegerOverflow|overflow]].
- [[dis-2-9-2-cmd-line-args]] — the introducing source.
- [[dis-1-1-getting-started]] — where the simpler `int main(void)` form was introduced.
- [[DiveIntoSystems]] — the source textbook.
