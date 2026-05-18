---
title: "Dive into Systems — Ch 2.9.2 Command Line Arguments"
type: source
tags: [c-language, command-line-arguments, argc, argv, main, atoi, strtol, dive-into-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/advanced_cmd_line_args.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **second subsection of [[dis-2-9-advanced|Ch 2.9]]** of *[[DiveIntoSystems]]* — extends the [[MainFunction|`main`]] signature from `int main(void)` to the **full [[CommandLineArguments|`argc`/`argv`]] form** `int main(int argc, char *argv[])`, finally delivering the argument-passing-from-the-shell mechanism the prior 19 chapters elided. Codifies the **two-parameter protocol** — `argc` is the integer count of arguments (program name included), `argv` is a [[CArray|`char *` array]] of [[CString|C-string]] arguments terminated by a [[NullPointer|`NULL`]] sentinel at `argv[argc]` — and the **string-arrive-as-strings** rule that forces numeric arguments through a conversion function ([[Atoi|`atoi`]] for the simple case, [[Strtol|`strtol`]] for production code that needs error detection).

## Key Claims

- **The full `main` signature** is `int main(int argc, char *argv[])` — equivalently `int main(int argc, char **argv)` since [[CArray|array]] parameter syntax decays to a [[Pointer|pointer]]. The shorter `int main(void)` form from [[dis-1-1-getting-started|Ch 1.1]] is a special case for programs that ignore command-line input.
- **`argc` = argument count, including the program name.** For `./a.out 10 11 200`, `argc == 4` (program name + three user arguments).
- **`argv` is a [[CArray|`char *` array]] of `argc + 1` elements** — the user arguments at indices `1..argc-1`, the program-invocation name at `argv[0]`, and a [[NullPointer|`NULL`]] terminator at `argv[argc]`. The trailing `NULL` lets argument-walking loops use `while (argv[i] != NULL)` instead of needing `argc`.
- **Every argument arrives as a [[CString|C string]]** — even numeric ones. `./a.out 10` produces `argv[1] == "10"` (the four bytes `'1' '0' '\0'` plus pointer to them), not the integer `10`. Programs that want integers must convert via [[Atoi|`atoi`]] / [[Strtol|`strtol`]] (declared in `<stdlib.h>`).
- **[[Atoi|`atoi`]] is the simple-but-silent entry point** — `int x = atoi(argv[1]);` works but returns `0` on malformed input, indistinguishable from the legitimate string `"0"`. Production code uses [[Strtol|`strtol`]] which separates *value* from *parse-success* via a `char **endptr` out-parameter and reports [[IntegerOverflow|overflow]] through [[Errno|`errno = ERANGE`]].

## Key Quotes

> "`argc` stores the **argument count**. Its value represents the number of command line arguments passed to the main function (including the name of the program)." — defining `argc`.

> "`argv` stores the **argument vector**. It contains the value of each command line argument." — defining `argv`.

> "The array contains `argc + 1` elements, with the final element set to NULL to mark the end." — the [[NullPointer|`NULL`]]-sentinel convention enabling `while (argv[i] != NULL)` iteration.

## Connections

- [[DiveIntoSystems]] — the source textbook; this section is its Ch 2.9.2.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — the authors.
- [[dis-2-9-advanced]] — the hub page that forwards to this subsection.
- [[dis-2-9-1-advanced-switch]] — the **prior** subsection (constants, switch, enum, typedef).
- [[dis-1-1-getting-started]] — introduces the **minimum** `int main(void)` form that this section generalizes.
- [[dis-1-4-functions]] — introduces [[MainFunction|`main`]] as one [[Function|function]] among many; this section finally fills in its **full parameter list**.
- [[dis-1-5-arrays-strings]] / [[dis-2-5-arrays]] — [[CArray|`char *` arrays]] / [[ArrayDecay|array decay]] / [[CString|C strings]] — the prerequisite types `argv` is built from.
- [[dis-2-2-pointers]] / [[dis-2-6-strings]] — [[Pointer|pointers]] / [[NullPointer|`NULL`]] / [[Atoi|`atoi`]] — `argv`'s pointer-array structure and the conversion gateway.
- [[CommandLineArguments]] — the **new** concept page introduced here.
- [[MainArgcArgv]] — the **new** concept page for the full `main` signature.
- [[Strtol]] — the **new** concept page for the modern [[Atoi|`atoi`]] replacement.
- [[MainFunction]] / [[Atoi]] — **updated** to point at this section.

## Contradictions

- None. The `int main(int argc, char *argv[])` form **supersedes** the `int main(void)` form from [[dis-1-1-getting-started|Ch 1.1]] for programs that accept command-line input, but both forms remain legal — the [[CLanguage|C]] standard permits either signature, and [[MainFunction|`main`]] already telegraphed *"The full form `int main(int argc, char **argv)` (command-line arguments) appears later in the book."*
