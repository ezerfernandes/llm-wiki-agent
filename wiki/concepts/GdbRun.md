---
title: "GDB `run` (`r`)"
type: concept
tags: [debugging, gdb, c-language, debugging-primitive, execution-control]
sources: [dis-3-1-gdb, dis-3-2-gdb-commands]
last_updated: 2026-05-17
---

# GDB `run` (`r`)

The [[GDB]] command that **starts the debuggee from the beginning**, optionally with command-line arguments. After `gdb ./a.out` loads the executable, `run` is what actually launches the program under GDB's control — the analog of typing `./a.out` at the shell.

[[dis-3-1-gdb|DIS Ch 3.1]] introduces `run` as step 4 of the canonical workflow (after compile-with-`-g`, launch, set breakpoint, **run**, inspect, advance). [[dis-3-2-gdb-commands|Ch 3.2]] details the argument-passing surface.

## Syntax

```text
run                        # no arguments
run 2 40 100               # passes argc=4, argv = {"./a.out", "2", "40", "100"}
run < input.txt            # redirect stdin
run > output.txt           # redirect stdout
run 2 40 < in.txt > out    # args + redirection combined
```

The arguments after `run` populate [[CommandLineArguments|`argc` / `argv`]] as if typed at the shell — finally connecting [[dis-2-9-2-cmd-line-args|Ch 2.9.2]]'s argument-passing protocol to the debugging workflow. Shell-redirection syntax (`<` / `>` / `2>`) works inside `run` too.

## What `run` does at startup

1. **Loads** the executable's [[CodeSection|code]] / [[DataSection|data]] segments into a fresh process address space.
2. **Pushes** the [[StackSection|initial stack frame]] with `argc` / `argv` / `envp`.
3. **Installs** all active [[Breakpoint|breakpoints]] as trap instructions in the loaded `.text`.
4. **Begins execution** at the program entry point (`_start` → `__libc_start_main` → [[MainFunction|`main`]] on glibc).
5. **Halts** at the first breakpoint hit, signal received, or program exit — returning the prompt to the user.

If no breakpoints are set and the program doesn't crash, `run` simply executes the program to completion and reports `[Inferior 1 (process N) exited normally]`.

## Re-running

Bare `run` in a session that already executed once **terminates the current debuggee and restarts**. GDB prompts: *"The program being debugged has been started already. Start it from the beginning?"* — answer `y`. Breakpoints / [[GdbDisplay|display]] entries / [[ConditionalBreakpoint|conditions]] persist across re-runs — they live in GDB's state, not the debuggee's.

`start` is a near-synonym that automatically sets a temporary breakpoint at `main` and runs to it — useful when you forgot to set the first breakpoint.

## Reading args on restart

[[dis-3-2-gdb-commands|Ch 3.2]] notes that `run` re-uses the **last argument list** if invoked bare. `show args` displays them; `set args 2 40 100` updates them without launching. The combination lets you tweak args between runs:

```text
(gdb) set args 100
(gdb) run
... behavior with argv[1]=100 ...
(gdb) set args 200
(gdb) run
... behavior with argv[1]=200 ...
```

## Connections

- [[dis-3-1-gdb]] — first introduction (step 4 of canonical workflow).
- [[dis-3-2-gdb-commands]] — argument-passing surface detailed.
- [[GDB]] / [[Debugger]] — the host tool.
- [[Breakpoint]] / [[StepDebug]] — the halt mechanisms `run` triggers.
- [[CommandLineArguments]] / [[MainArgcArgv]] — what arguments populate.
- [[MainFunction]] — the entry point execution begins at.
- [[ProcessMemory]] — the fresh address space `run` creates.
