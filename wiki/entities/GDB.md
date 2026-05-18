---
title: "GDB (GNU Debugger)"
type: entity
tags: [debugger, gnu, embedded, tooling, c-language, dive-into-systems]
sources: [rust-embedded-book-intro-tooling, dis-3-1-gdb]
last_updated: 2026-05-17
---

# GDB (GNU Debugger)

The **canonical Unix [[Debugger|debugger]]** — a GNU Project program that controls the execution of another program so the user can inspect, modify, and step through its state. Per [[dis-3-1-gdb|DIS Ch 3.1]]'s opening definition (citing GDB as its primary example): *"a debugger is a program that controls the execution of another program… it allows programmers to see what their programs are doing as they run."*

GDB ships on every Linux distribution, every BSD, and macOS (via Homebrew / MacPorts; Apple's bundled debugger is `lldb` instead). It supports [[CLanguage|C]], C++, Objective-C, Go, Rust, Ada, Pascal, Modula-2, and Fortran as source languages and over a dozen [[ISA|ISAs]] (x86, x86-64, ARM, AArch64, RISC-V, MIPS, PowerPC, …) as targets.

## Two corpus angles

The wiki now has **two complementary views** of GDB:

1. **Hosted-Unix usage** — [[dis-3-1-gdb|DIS Ch 3.1]] introduces GDB on a local Linux process: `gdb ./a.out`, [[Breakpoint|break]] / [[GdbRun|run]] / [[GdbPrint|print]] / [[StepDebug|next/step]] / [[GdbBacktrace|backtrace]], plus [[CoreFile|core-file]] post-mortem. The OS supplies the [[Ptrace|`ptrace`]] mechanism that lets one process inspect another.
2. **Embedded usage** — [[rust-embedded-book-intro-tooling|Embedded Rust Ch I.4]] uses GDB as the front-end of a **remote** debug stack: GDB on the host machine talks GDB's **Remote Serial Protocol** to [[OpenOCD]] or [[ProbeRs]], which forwards over [[JTAG]] / [[SWD]] to a probe ([[STLink]] / [[JLink]] / [[MCULink]] / [[RustyProbe]]) attached to an ARM Cortex-M MCU. The same GDB binary, the same commands — only the *target* differs (a flashed ELF on a microcontroller rather than a hosted process).

The same tool spans the entire systems-programming stack — desktop debugging at one end, bare-metal-firmware debugging at the other.

## Core command vocabulary ([[dis-3-1-gdb|DIS Ch 3.1]] subset)

| Command | Purpose | See also |
|---|---|---|
| `break <loc>` | Set a [[Breakpoint|breakpoint]] | [[Breakpoint]] |
| `run [args]` / `r` | Start the debuggee | [[GdbRun]] |
| `cont` / `c` | Resume after pause | [[StepDebug]] |
| `next` / `n` | Step over function calls | [[StepDebug]] |
| `step` / `s` | Step into function calls | [[StepDebug]] |
| `print <expr>` / `p` | Display variable / expression value | [[GdbPrint]] |
| `list` / `l` | Show source context | [[GdbList]] |
| `display <expr>` | Auto-print expression at each pause | [[GdbDisplay]] |
| `backtrace` / `bt` / `where` | Show call stack | [[GdbBacktrace]] |
| `frame N` / `f N` | Switch to stack frame `N` | [[GdbBacktrace]] |
| `info locals` / `info args` | List visible variables / parameters | |
| `info registers` | Show CPU register state | |
| `quit` / `q` | Exit GDB | |

## Build prerequisites

GDB at full power requires the executable to be compiled with [[GccDashG|`gcc -g`]] — embedding [[DebugSymbol|debug symbols]] (DWARF) that map machine addresses to source lines, variable names, and types. [[dis-3-1-gdb|Ch 3.1]]'s rule of thumb: **debug at `-O0 -g`**, because [[CompilerOptimization|`-O2`+ optimization]] reorders, inlines, and eliminates instructions in ways that break the binary-to-source correspondence and trigger `<optimized out>` messages.

## Front-ends and integrations

- **[[DataDisplayDebugger|DDD]]** — the GNU GUI wrapper [[dis-3-1-gdb|Ch 3.1]] mentions; classic point-and-click skin with data-structure visualization.
- **VS Code C/C++ extension** — uses GDB as the backend on Linux via the MI (Machine Interface) protocol.
- **Emacs `gud`** / `realgud` / `dap-mode` — long-standing in-editor GDB integration.
- **Vim `termdebug`** — built-in GDB pane since Vim 8.1.
- **CLion** / **CodeLite** / **Code::Blocks** — IDE-bundled GDB front-ends.

## Embedded-Rust version requirements

For the [[TheEmbeddedRustBook|Embedded Rust]] workflow, GDB must be built with ARM support; the book recommends version **7.12+**, with tested versions 7.10, 7.11, 7.12, and 8.1 ([[rust-embedded-book-intro-tooling]]). GDB pretty-prints Rust types, supports conditional breakpoints, variable inspection, register inspection, and step / continue across remote-server breaks.

## Connections

- [[Debugger]] — the operation category GDB exemplifies.
- [[dis-3-1-gdb]] — the [[DiveIntoSystems]] workflow page (Ch 3.1).
- [[rust-embedded-book-intro-tooling]] — the [[TheEmbeddedRustBook|Embedded Rust]] toolchain inventory.
- [[Breakpoint]] / [[StepDebug]] / [[GdbBacktrace]] / [[GdbPrint]] — the primitives GDB exposes.
- [[GdbRun]] / [[GdbList]] / [[GdbDisplay]] / [[GDBLoad]] — additional GDB commands (`load` is the Embedded Rust flashing primitive).
- [[CoreFile]] — the post-mortem input.
- [[GccDashG]] / [[DebugSymbol]] — the build-side prerequisite.
- [[CompilerOptimization]] — the orthogonal axis (debug-hostile when high).
- [[DataDisplayDebugger]] — DDD, the GUI front-end.
- [[OpenOCD]] / [[ProbeRs]] — the embedded-side GDB servers.
- [[STLink]] / [[JLink]] / [[MCULink]] / [[RustyProbe]] — hardware probes GDB reaches via a server.
- [[OnChipDebugging]] / [[JTAG]] / [[SWD]] — the embedded debug interface.
- [[Valgrind]] — sibling C debugging tool; complementary scope (memory errors vs. execution control).
- [[Ptrace]] — the OS tracing mechanism GDB sits on top of (named-and-deferred).
- [[DiveIntoSystems]] — the book where Ch 3 *C Debugging Tools* covers GDB as the **first** of two debugging tools.
