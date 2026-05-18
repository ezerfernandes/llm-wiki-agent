---
title: "main Function"
type: concept
tags: [c-language, entry-point, programming]
sources: [dis-1-1-getting-started, dis-1-4-functions, dis-2-9-2-cmd-line-args]
last_updated: 2026-05-17
---

# main Function

In [[CLanguage|C]], **`main`** is the program's entry point — execution starts here. [[dis-1-1-getting-started|DIS Ch 1.1]] introduces it in its minimum form:

```c
int main(void) {
    /* ... */
    return 0;
}
```

- **`int` return type** — `main` returns an integer [[ExitStatus|exit status]] to the [[OperatingSystem|OS]]. `0` signifies "ran to completion without error"; non-zero conventionally signals an error.
- **`void` parameter list** — at this introductory stage, `main` is declared to take no arguments. The full form `int main(int argc, char **argv)` (command-line arguments) appears later in the book.
- **Curly-brace body** — like every C function, the body is delimited by `{ }`, and each statement ends with a `;`.

The runtime startup code in the [[BinaryExecutable|binary]] calls `main` after process initialization; when `main` returns, the runtime passes the returned value to the OS as the process exit status.

## Generalized in [[dis-1-4-functions|Ch 1.4]]

In [[dis-1-1-getting-started|Ch 1.1]] `main` is *the only [[Function|function]]* a program has. [[dis-1-4-functions|Ch 1.4]] reframes it: `main` is just *one [[Function|function]] among many* — the **first** [[StackFrame|stack frame]] on the [[ExecutionStack|execution stack]], the entry point from which all other [[FunctionCall|calls]] are issued. Its `(void)` is now a deliberate [[FunctionParameter|parameter list]] declaration (no parameters), not a special case; its `return 0;` is a normal [[ReturnStatement|`return`]] of an `int`, whose value happens to be intercepted by the runtime as the [[ExitStatus|exit status]].

## Full form delivered in [[dis-2-9-2-cmd-line-args|Ch 2.9.2]]

[[dis-2-9-2-cmd-line-args|Ch 2.9.2]] fills in the full parameter list [[dis-1-1-getting-started|Ch 1.1]] flagged as *"appears later in the book"* — the [[CommandLineArguments|`argc`/`argv`]] form:

```c
int main(int argc, char *argv[]) { ... }
```

`argc` is the [[CommandLineArguments|argument count]] (including the program name at `argv[0]`); `argv` is a [[CArray|`char *` array]] of [[CString|C-string]] arguments with a [[NullPointer|`NULL`]] sentinel at `argv[argc]`. See [[MainArgcArgv]] for the dedicated treatment. Both forms remain legal — pick `(void)` if you ignore arguments, `(int, char *[])` if you read any.

## Connections

- [[CLanguage]] — the language whose entry point this is.
- [[dis-1-1-getting-started]] — the introducing source.
- [[dis-1-4-functions]] — generalizes `main` into one [[Function|function]] among many.
- [[dis-2-9-2-cmd-line-args]] — delivers the **full** `(int argc, char *argv[])` parameter list.
- [[MainArgcArgv]] — the dedicated page for the full form.
- [[CommandLineArguments]] — the shell-to-program mechanism `argc`/`argv` implement.
- [[Function]] / [[FunctionCall]] / [[StackFrame]] / [[ExecutionStack]] — the framing concepts; `main` is the bottom-most user frame.
- [[ReturnStatement]] / [[ReturnType]] / [[VoidType]] — the structural pieces of `main`'s header.
- [[ExitStatus]] — what the integer return value becomes at process termination.
- [[BinaryExecutable]] — the artifact this function lives inside.
- [[OperatingSystem]] — the consumer of the exit status.
- [[Printf]] / [[PreprocessorDirective]] — the other minimum-surface pieces of a hello-world program.
