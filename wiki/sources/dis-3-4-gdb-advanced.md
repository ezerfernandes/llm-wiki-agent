---
title: "Dive into Systems — Ch 3.4 Advanced GDB Features"
type: source
tags: [dive-into-systems, c-debugging, gdb, debugger, fork, signals, attach, ddd, tooling]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C3-C_debug/gdb_advanced.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 3.4** of *[[DiveIntoSystems]]* — the **advanced-workflows extension** to the [[dis-3-1-gdb|Ch 3.1]] / [[dis-3-2-gdb-commands|Ch 3.2]] [[GDB]] block. Where Ch 3.1 framed the canonical hosted-Unix-process debugging session and Ch 3.2 fanned out the command vocabulary, **Ch 3.4 surfaces the workflows beyond *"compile, run, set breakpoints, step, print"*** — the cross-process, signal-driven, and `fork()`-aware features that turn [[GDB]] from a single-program-at-rest debugger into a tool for **already-running**, **signal-handling**, and **multi-process** programs.

Five short sections, each a self-contained workflow: (1) **GDB ↔ [[Make]] integration** — running `make` from inside the [[GDB]] session to **rebuild without losing breakpoints**; (2) **[[GdbAttach|attaching to a running process]]** via `gdb <executable> <pid>` (with [[Ps|`ps`]] / `ps -A | grep` to find the PID) — debugging programs that are **already running**, including the **self-pause idiom** `kill(getpid(), SIGSTOP)` to create an attach window from inside the program; (3) **[[GdbFollowFork|follow-fork-mode]]** — `set follow-fork-mode child` / `parent` to choose which branch of a [[Fork|`fork()`]]ed program [[GDB]] follows (default = parent); (4) **[[GdbSignalControl|signal control]]** — `signal SIGCONT` / `signal SIGUSR1` to **send** signals to the debuggee, `handle SIGBUS stop` to **intercept** signals in [[GDB]], `info signal` / `info SIGALRM` to inspect handling rules; (5) **[[DataDisplayDebugger|DDD]] settings cleanup** — `rm -rf ~/.ddd` to fix the common *"Waiting until GDB ready"* hang.

Closes the *Dive into Systems* [[GDB]] coverage with the **systems-level features** that distinguish [[GDB]] from a simple line-stepper: it can attach to, signal, and follow forks of running [[Process|processes]] — the same OS primitives ([[Ptrace|`ptrace`]] / [[Fork|`fork`]] / [[Signal|signals]]) Ch 9 / Ch 10's [[OperatingSystem|OS chapters]] will codify, here exposed as user-facing debugger features.

## Key Claims

- **`make` from inside GDB**: typing `make` at the `(gdb)` prompt invokes the build system **without exiting the session** — the debugger preserves the breakpoint list across the recompile. *"GDB accepts the `make` command to rebuild an executable during a debugging session"*. **Caveat**: if the rebuild **shifted line numbers**, the existing breakpoint IDs may now refer to wrong lines; use [[GdbBreakpointManagement|`disable` / `delete` / `break`]] to re-align.
- **[[GdbAttach|Attaching to a running process]]** — *"GDB supports debugging a program that is already running (rather than starting a program to run from within a GDB session) by attaching GDB to a running process"*. The workflow: (a) find the [[ProcessID|PID]] via [[Ps|`ps`]] or `ps -A | grep a.out`; (b) launch `gdb <executable> <pid>` (or attach from inside [[GDB]] via `attach <pid>`); (c) the target [[Process|process]] **pauses** on attach — inspect state, then [[GdbRun|`cont`]] to resume.
- **Self-pause idiom for attach windows**: `kill(getpid(), SIGSTOP)` (or `raise(SIGSTOP)`) placed inside the program creates an **attach-friendly halt** — the program suspends itself before reaching the suspect region, giving the developer time to run `ps`, attach, set breakpoints, and `signal SIGCONT` to resume. The corpus's first **debugger-aware program design** pattern.
- **[[GdbFollowFork|`set follow-fork-mode`]]** controls [[Fork|`fork()`]] behavior — *"By default, GDB follows the parent after a call to `fork()`"*. Override with `set follow-fork-mode child` (follow the new child) or `set follow-fork-mode parent` (default). `show follow-fork-mode` displays the current setting. The headline primitive for debugging **multi-process programs** without writing two debugger sessions.
- **[[GdbSignalControl|Sending signals]] from GDB**: `signal SIGCONT` resumes a stopped program; `signal SIGUSR1` / `signal SIGALARM` deliver an arbitrary signal to the running debuggee — essentially using [[GDB]] as a `kill -<SIG>` for the program under inspection.
- **[[GdbSignalControl|Intercepting signals]]**: `handle <SIG> stop` makes [[GDB]] **halt** when the debuggee receives `<SIG>` — the breakpoint-equivalent for signal-driven control flow. Useful for debugging signal handlers, asynchronous events, or [[SIGBUS]] / [[SIGSEGV]] crashes whose source is not a single line. `info signal` lists all signal-handling rules; `info SIGALRM` queries a specific signal.
- **[[SIGBUS]] and misalignment**: *"if a program tries to access memory with a misaligned memory address for the type it is accessing, it receives a `SIGBUS` signal"* — names the canonical alignment-fault scenario that `handle SIGBUS stop` exists to debug. Distinct from [[SegmentationFault|`SIGSEGV`]] (invalid address) — [[SIGBUS]] is *valid address, wrong alignment*.
- **[[DataDisplayDebugger|DDD]] settings live in `~/.ddd`**: corrupt settings cause the *"Waiting until GDB ready"* startup hang — *"Sometimes DDD hangs on startup with a 'Waiting until GDB ready' message. This often indicates an error in its saved settings files"*. Fix: `rm -rf ~/.ddd` to reset to defaults. The corpus's first **debugger-tooling-troubleshooting** entry.
- **Cross-references the OS primitives**: every advanced feature here is a thin wrapper over a [[OperatingSystem|kernel]] primitive — `attach` over [[Ptrace|`ptrace`]], `follow-fork-mode` over [[Fork|`fork()`]] tracing, `handle` / `signal` over [[Signal|signal()]] / [[Kill|`kill()`]] — the **systems-call layer the rest of *Dive into Systems* Ch 9+ will formalize**.

## Key Quotes

> "GDB accepts the `make` command to rebuild an executable during a debugging session." — on Make integration.

> "GDB supports debugging a program that is already running (rather than starting a program to run from within a GDB session) by attaching GDB to a running process." — on attach mode.

> "By default, GDB follows the parent after a call to `fork()`." — on follow-fork-mode default.

> "If a program tries to access memory with a misaligned memory address for the type it is accessing, it receives a `SIGBUS` signal." — on the canonical [[SIGBUS]] scenario.

> "Sometimes DDD hangs on startup with a 'Waiting until GDB ready' message. This often indicates an error in its saved settings files." — on the `~/.ddd` reset workflow.

## Connections

- [[DiveIntoSystems]] — book; this is **Ch 3.4**, the advanced-workflows extension to the [[dis-3-1-gdb|Ch 3.1]] / [[dis-3-2-gdb-commands|Ch 3.2]] [[GDB]] block.
- [[dis-3-1-gdb]] — the narrative workflow introduction this section extends with cross-process / signal-driven features.
- [[dis-3-2-gdb-commands]] — the command-reference companion this section sits beside; Ch 3.2 covers in-process commands, Ch 3.4 covers cross-process ones.
- [[dis-3-3-valgrind]] — sibling section in Ch 3; orthogonal tool (memory-error detector) — Ch 3.4 extends [[GDB]]'s reach instead of switching tools.
- [[GDB]] — the host tool; this source **closes** the *Dive into Systems* [[GDB]] coverage with attach / fork / signal features.
- [[Make]] — already in wiki (build tool); now connected to [[GDB]] as the in-session rebuild target.
- [[GdbAttach]] — **new concept page**; the `gdb <prog> <pid>` / `attach <pid>` workflow for already-running processes.
- [[GdbFollowFork]] — **new concept page**; the `set follow-fork-mode child` / `parent` setting for multi-process programs.
- [[GdbSignalControl]] — **new concept page**; the `signal <SIG>` / `handle <SIG> stop` / `info signal` family.
- [[Ps]] — **new concept page**; the [[OperatingSystem|Unix]] `ps` process-listing utility (PID discovery for attach).
- [[ProcessID]] — already in wiki via [[Process]]; this source promotes its debugging use case.
- [[Process]] — already in wiki; now connected to debugger attach / fork-follow primitives.
- [[Fork]] — **new concept page** (or expanded if present); the [[OperatingSystem|POSIX]] `fork()` system call that splits a process — [[GdbFollowFork]]'s underlying primitive.
- [[Signal]] — **new concept page** (or expanded if present); [[OperatingSystem|POSIX]] signal mechanism — substrate for [[GdbSignalControl]].
- [[SIGBUS]] — **new concept page**; bus-error signal raised on misaligned access — distinct from [[SegmentationFault|`SIGSEGV`]].
- [[Kill]] — **new concept page**; `kill(pid, sig)` system call — the C-side primitive behind the `kill(getpid(), SIGSTOP)` self-pause idiom.
- [[Ptrace]] — already named-and-deferred; this source surfaces it implicitly as the kernel mechanism behind attach / handle.
- [[DataDisplayDebugger]] — already in wiki; this source adds the `~/.ddd` settings-reset troubleshooting note.
- [[Debugger]] / [[Breakpoint]] / [[StepDebug]] / [[GdbBacktrace]] / [[GdbPrint]] / [[GdbBreakpointManagement]] — already in wiki; cross-references unchanged from [[dis-3-1-gdb|Ch 3.1]] / [[dis-3-2-gdb-commands|Ch 3.2]].
- [[OperatingSystem]] — already in wiki; this source is the corpus's **first user-visible exposure** to [[Ptrace]] / [[Fork]] / [[Signal]] as debugger-facing primitives (formal coverage deferred to Ch 9+).

## Contradictions

None — purely additive. Ch 3.1 / 3.2 framed [[GDB]] as a single-process line-stepping debugger; Ch 3.4 extends the **same tool** with cross-process / fork-aware / signal-aware workflows. Nothing in earlier chapters is revised — only the picture of what [[GDB]] can target (already-running processes, [[Fork|forked]] children, signal-handling code) is expanded. The [[DataDisplayDebugger|DDD]] mention in [[dis-3-1-gdb|Ch 3.1]] (GUI wrapper) is extended here with the settings-reset troubleshooting note.
