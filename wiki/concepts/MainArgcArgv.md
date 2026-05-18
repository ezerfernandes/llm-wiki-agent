---
title: "main(int argc, char *argv[])"
type: concept
tags: [c-language, entry-point, main, command-line-arguments, programming]
sources: [dis-2-9-2-cmd-line-args]
last_updated: 2026-05-17
---

# `int main(int argc, char *argv[])`

The **full form** of the [[CLanguage|C]] [[MainFunction|`main`]] entry point — the variant that accepts [[CommandLineArguments|command-line arguments]] from the invoking shell. Introduced in [[dis-2-9-2-cmd-line-args|DIS Ch 2.9.2]] as the generalization of the introductory `int main(void)` form from [[dis-1-1-getting-started|Ch 1.1]].

## Signature

```c
int main(int argc, char *argv[]) {
    /* ... */
    return 0;
}
```

Equivalently `int main(int argc, char **argv)` — see [[ArrayDecay]].

- **Return type `int`** — the [[ExitStatus|exit status]] the [[OperatingSystem|OS]] receives; `0` = success.
- **`argc`** — the [[CommandLineArguments|argument count]] (program name included).
- **`argv`** — the [[CommandLineArguments|argument vector]], a [[CArray|`char *` array]] of length `argc + 1` with a [[NullPointer|`NULL`]] sentinel at `argv[argc]`.

## Both forms coexist

The [[CLanguage|C]] standard permits either entry-point signature:

```c
int main(void) { ... }                    // ignore arguments
int main(int argc, char *argv[]) { ... }  // accept arguments
```

Programs that do not need command-line input may keep the simpler form; programs that **read any argument** must declare the full form so the runtime hands `argv` to them. The runtime-startup code in the [[BinaryExecutable|binary]] inspects the prototype and arranges the right calling convention.

## Position in the *Dive into Systems* corpus

- [[dis-1-1-getting-started|Ch 1.1]] introduces the minimum `int main(void)` form — the *"full form … appears later in the book"* promise.
- [[dis-1-4-functions|Ch 1.4]] reframes [[MainFunction|`main`]] as one [[Function|function]] among many — *one [[StackFrame|stack frame]] on the [[ExecutionStack|execution stack]]*.
- [[dis-2-9-2-cmd-line-args|Ch 2.9.2]] (this page's source) **fulfills the promise**: the full `(int, char *[])` parameter list, the shell-to-`argv` data flow, the `NULL`-terminator convention, the [[CString|string-typed-arrival]] rule, and the [[Atoi|`atoi`]] / [[Strtol|`strtol`]] conversion gateway.

## Connections

- [[MainFunction]] — the parent concept; this page is the *full-form* specialization.
- [[CommandLineArguments]] — the mechanism `argc` / `argv` implement.
- [[CArray]] / [[CString]] / [[NullPointer]] / [[ArrayDecay]] — the type machinery on the `argv` parameter.
- [[Atoi]] / [[Strtol]] — the standard-library bridges from `argv[i]` strings to numeric types.
- [[ExitStatus]] / [[ReturnStatement]] — the `int` returned to the [[OperatingSystem|OS]].
- [[dis-2-9-2-cmd-line-args]] — the source.
- [[DiveIntoSystems]] — the corpus.
