---
title: "Dive into Systems — 13.4.1 Signals"
type: source
tags: [textbook, operating-systems, ipc, signal, signal-handler, sigaction, kill, sigchld]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C13-OS/ipc_signals.html
---

## Summary

**First sub-leaf of [[dis-13-4-ipc|Ch 13.4]]** — formalizes the [[Signal|signal]] mechanism as the **most restricted** IPC family. Defines a signal as a **software interrupt** delivered by one [[Process|process]] (or the [[Kernel|kernel]]) to another through the OS — *asynchronous* unlike synchronous traps. The receiver's execution is paused, the **[[SignalHandler|signal handler]]** runs, then normal execution resumes (unless the handler terminates). Processes send signals via the [[Kill|`kill`]] [[SystemCall|system call]] — despite the name, *"`kill` isn't limited to termination signals — it delivers any signal type."* The OS itself initiates signals to notify processes of system events (e.g., `SIGCHLD` to a parent when a child exits). Lists the canonical signal set (`SIGINT` / `SIGKILL` / `SIGCHLD` / `SIGSEGV` / `SIGBUS` / `SIGALRM` / `SIGSTOP` / `SIGCONT`). **Default handler actions**: terminate, ignore, block, unblock; programmers override most via `signal()` (simpler, learning) or `sigaction()` (POSIX-compliant, production). **`SIGKILL` and `SIGSTOP` cannot be caught.** **`SIGCHLD` zombie-reaping idiom**: `waitpid(-1, &status, WNOHANG)` *"in a loop to reap multiple zombies"* — because the OS doesn't track signal *counts*, only that the signal occurred. **Headline limitation**: *"Systems define a fixed number of signals (e.g., Linux defines 32 different signals)"* — the limited namespace makes signals unsuitable for arbitrary IPC, restricting them to predefined notifications.

## Key Claims

- **[[Signal|Signals]] are software interrupts** — asynchronous, kernel-delivered, distinct from synchronous traps and from hardware interrupts (which are hardware-driven).
- **[[Kill|`kill(pid, sig)`]] is the universal send primitive** — sends any signal type, not just termination. The OS handles delivery and arranges for the [[SignalHandler|handler]] to run.
- **Receiver execution model**: signal arrives → OS pauses current execution → signal handler runs → control returns to interrupted point (unless handler terminates).
- **Canonical signal table**: `SIGINT` (Ctrl-C), `SIGKILL` (force termination, uncatchable), `SIGCHLD` (child exited), `SIGSEGV` ([[SegmentationFault|segfault]]), `SIGBUS` (bus error — see [[SIGBUS]]), `SIGALRM` (timer), `SIGSTOP`/`SIGCONT` (suspend/resume).
- **Four default handler actions**: terminate, ignore, block, unblock — programmers can override most via two registration system calls.
- **Two registration system calls**: *"Linux supports two different system calls that can be used to change the default behavior of a signal or to register a signal handler on a particular signal: `sigaction` and `signal`."* `sigaction` is POSIX-compliant and preferred; `signal` is simpler.
- **Handler signature**: `void handler_function(int signum)` — the standard prototype for all custom signal handlers.
- **`SIGCHLD` zombie-reaping pattern**: register a `SIGCHLD` handler that calls `waitpid(-1, &status, WNOHANG)` in a loop. *Because the OS does not count signal occurrences*, multiple children exiting in quick succession may coalesce into one `SIGCHLD` delivery — the loop is necessary.
- **Two uncatchable signals**: `SIGKILL` and `SIGSTOP` — the OS guarantees these always take their default action, providing the [[Kernel|kernel]]-side override path.
- **Headline structural limitation**: *"Systems define a fixed number of signals (e.g., Linux defines 32 different signals)"* — limited namespace ⇒ signals are unsuitable for arbitrary data exchange and serve only predefined event notification.

## Key Quotes

> "Linux supports two different system calls that can be used to change the default behavior of a signal or to register a signal handler on a particular signal: `sigaction` and `signal`."

> "Systems define a fixed number of signals (e.g., Linux defines 32 different signals)." — the structural reason signals cannot replace message passing or shared memory.

> "waitpid(-1, &status, WNOHANG) in a loop to reap multiple zombies" — the canonical `SIGCHLD` handler pattern, since the OS records *occurrence* not *count*.

## Connections

- [[DiveIntoSystems]] — first sub-leaf of Ch 13.4; **122nd ingested DIS chapter**.
- [[dis-13-4-ipc]] — parent hub. 13.4.1 is the first of three sibling IPC mechanism leaves.
- [[dis-13-4-2-message-passing]] — next sibling. Message passing addresses signals' fixed-namespace limitation.
- [[dis-13-4-3-shared-memory]] — third sibling.
- [[dis-13-2-processes]] — names [[Wait|`wait` / `waitpid`]] and [[Zombie|zombie processes]] that 13.4.1 operationalizes via `SIGCHLD` handlers.
- [[dis-3-4-gdb-advanced]] — Ch 3.4 introduced [[Signal]] / [[Kill]] / [[SIGBUS]] in the GDB-debugger context; 13.4.1 promotes them to the IPC context.
- [[Signal]] — pre-existing canonical concept page; **extended in place** with IPC framing.
- [[SignalHandler]] — **new concept page**; the registered callback that runs on signal delivery, with the `void handler(int signum)` prototype.
- [[Kill]] — pre-existing concept page; **extended in place** with the *send-any-signal* IPC framing.
- [[SIGBUS]] — pre-existing concept page; canonical example of a fatal signal.
- [[InterprocessCommunication]] — parent umbrella concept; signals are the first IPC family.
- [[SystemCall]] — `kill` / `signal` / `sigaction` are all syscalls.

## Contradictions

- None. The 13.4.1 treatment of [[Signal|`signal()`]] vs [[Signal|`sigaction()`]] is consistent with the [[dis-3-4-gdb-advanced|Ch 3.4]] forward reference (which deferred formal coverage to Ch 9+).
