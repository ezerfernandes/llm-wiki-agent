---
title: "Core File (Core Dump)"
type: concept
tags: [debugging, operating-system, crash, post-mortem, c-language]
sources: [dis-3-1-gdb]
last_updated: 2026-05-17
---

# Core File (Core Dump)

A **core file** is a snapshot of a process's memory and CPU register state at the moment it terminated abnormally — written to disk by the OS so the developer can inspect the *post-mortem* state with a [[Debugger|debugger]] after the process is gone. [[dis-3-1-gdb|DIS Ch 3.1]] introduces it as the input for the *"the program crashed yesterday, can I still ask what went wrong?"* recovery path.

## Triggering a core dump

When a process receives a fatal signal — typically [[SegmentationFault|`SIGSEGV`]] (segfault), `SIGBUS` (bus error), `SIGABRT` (abort), `SIGFPE` (arithmetic) — the kernel can write a **core image** to disk if the resource limit `RLIMIT_CORE` permits it. The conventional filename is `core` or `core.<pid>` in the process's current directory.

Default `RLIMIT_CORE` is often `0` on modern distributions (core dumps disabled by default to avoid filling disks); enable with:

```bash
ulimit -c unlimited   # bash: enable core dumps in current shell
```

## Opening a core file in GDB

```bash
gdb ./buggy core
```

GDB loads the executable's [[DebugSymbol|debug symbols]] and overlays the core file's process state. From the GDB prompt, the same commands work as in a live debugging session — with the critical limitation that **execution cannot be resumed**:

- [[GdbBacktrace|`bt`]] — show the call stack as it was at the crash.
- `frame N` — switch into any frame.
- [[GdbPrint|`print expr`]] — read any variable's last value.
- `info registers` — see the CPU register state at the crash.
- `disassemble` — see the instructions around the crash site.

What you **cannot** do: [[GdbRun|`run`]], `cont`, [[StepDebug|`next`]] / `step`, set future [[Breakpoint|breakpoints]] — the process no longer exists. The core file is a frozen forensic record.

## What's in a core file

Typically (Linux ELF core format):
- All writable memory mappings of the process (stack, heap, `.data`, `.bss`, [[StaticLibrary|static]] / [[DynamicLibrary|dynamic]] library mappings).
- The CPU register set of every thread.
- Process metadata: PID, signal that triggered the dump, [[CommandLineArguments|argv / argc]], environment.
- File-descriptor table reference (paths only, not contents).

Read-only sections (`.text`, `.rodata`) are typically *not* dumped — they're recoverable from the executable file itself, which GDB loads alongside the core.

## When core files are essential

- **Reproducibility-resistant bugs** — crashes that happen rarely in production where you cannot run the process under a [[Debugger|debugger]] live.
- **Long-running processes** — restarting under a debugger is expensive; preserving the core after the crash is cheap.
- **Distributed / unattended systems** — embedded devices, batch jobs, server farms where interactive debugging isn't an option.

## Limitations

- Cannot inspect what happened *before* the dump-trigger signal — only the final state.
- Heap contents reflect what was on the heap at crash time, not the history of allocations.
- A core file is **architecture- and ABI-specific** — generated on x86-64 Linux, only meaningful on x86-64 Linux with matching `glibc` / kernel ABI.
- File-descriptor I/O state (kernel-side socket / pipe buffers) is *not* captured.

## Connections

- [[dis-3-1-gdb]] — introducing source.
- [[GDB]] / [[Debugger]] — the tool that consumes core files.
- [[GdbBacktrace]] — the primary command for core-file analysis.
- [[GdbPrint]] — read variable values from the frozen state.
- [[SegmentationFault]] — the most common trigger.
- [[DebugSymbol]] — required in the executable for source-level core inspection.
- [[GccDashG]] — the build flag that embeds those symbols.
- [[StackFrame]] / [[ExecutionStack]] — the call-stack structures preserved in the core.
- [[OperatingSystem]] — the entity that writes the core file when a signal kills the process.
- [[Valgrind]] — complementary tool: catches memory errors *before* they segfault, often eliminating the need for a core file post-mortem.
