---
title: "GDB `list` (`l`)"
type: concept
tags: [debugging, gdb, c-language, debugging-primitive, source-context]
sources: [dis-3-1-gdb, dis-3-2-gdb-commands]
last_updated: 2026-05-17
---

# GDB `list` (`l`)

The [[GDB]] command that **shows source code** around the current execution point (or a user-named line / function / file). Lets you read source from inside GDB without switching to an editor.

## Forms

| Form | Effect |
|---|---|
| `list` / `l` | Show 10 lines around the current execution point (after a breakpoint hit or step). |
| `list N` | Show 10 lines centered on line `N`. |
| `list N,M` / `list 30 100` | Show lines `N` through `M`. |
| `list main` | Show 10 lines around the start of function `main`. |
| `list file.c:42` | Show 10 lines around line 42 of `file.c`. |
| `list file.c:func` | Show 10 lines around the start of `func` in `file.c`. |
| `list ,N` | Show 10 lines ending at line `N`. |
| `list N,` | Show 10 lines starting at line `N`. |

Bare `list` after a previous `list` **continues** — the next 10 lines after the last shown. Useful for paging through source.

## Default listing size

10 lines is the convention; configurable via `set listsize N`. `set listsize 0` disables `list` (used in scripts that want to avoid output noise).

## Reading the output

`list` annotates the **current execution point** with `>` if you're paused mid-stream:

```text
(gdb) break main
(gdb) run
Breakpoint 1, main () at hello.c:5
5           int x = 10;
(gdb) list
1       #include <stdio.h>
2
3       int main(void) {
4           int y = 5;
5    >      int x = 10;
6           printf("%d\n", x + y);
7           return 0;
8       }
```

After a [[GdbBacktrace|`frame N`]] switch, `list` shows source around frame `N`'s current line — same scope-aware behavior as [[GdbPrint|`print`]].

## Where it fits in the workflow

[[dis-3-1-gdb|Ch 3.1]] places `list` between *setting breakpoints* and *advancing execution*: after `break` halts the debuggee, `list` shows the **surrounding code context** so you know where you are without external reference. For deep call stacks, `list` is the GDB-native alternative to opening the source file in another window.

The pairing [[GdbBacktrace|`bt`]] + `list` is canonical:

```text
(gdb) bt
#0  process at handler.c:42
#1  main at main.c:13
(gdb) frame 1
(gdb) list           # shows source around main.c:13
```

## Connections

- [[dis-3-1-gdb]] — introducing source.
- [[dis-3-2-gdb-commands]] — adds the range and function-target forms.
- [[GDB]] / [[Debugger]] — the host tool.
- [[Breakpoint]] / [[StepDebug]] — the halt events that make `list` interesting.
- [[GdbBacktrace]] — `frame N; list` is the standard call-chain inspection recipe.
- [[GdbPrint]] / [[GdbInfo]] — sibling inspection commands.
- [[DebugSymbol]] — source-to-binary mapping; without `-g` ([[GccDashG]]) `list` has nothing to show.
