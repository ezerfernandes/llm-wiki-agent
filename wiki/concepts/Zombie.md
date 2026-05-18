---
title: "Zombie Process"
type: concept
tags: [operating-systems, processes, unix, posix]
sources: [dis-13-2-processes]
last_updated: 2026-05-17
---

# Zombie Process

A **zombie** is a [[Process|process]] that has **terminated** (called [[Exit|`exit`]] or been killed) but whose [[ProcessControlBlock|PCB]] still exists because the **parent has not yet [[Wait|`wait`ed]]** for it. The process is in the [[ProcessState|Exited state]] — *"has terminated but remains in the system pending cleanup. It will never run again."* ([[dis-13-2-processes|DIS 13.2]]).

## Why zombies exist

The OS preserves enough of a terminated child to deliver its [[ExitStatus|exit status]] and termination signal to the parent. That information lives in the PCB. Discard the PCB the instant the child exits and the parent loses the ability to learn *how* the child finished — exit code, signal cause, resource usage. The zombie state is the contract that makes [[Wait|`wait` / `waitpid`]] possible.

## Life cycle

1. Child calls [[Exit|`exit(n)`]] (or receives a fatal [[Signal|signal]]).
2. OS releases the child's memory and file descriptors but **keeps the PCB**; marks the process Exited (zombie).
3. OS delivers [[Signal|`SIGCHLD`]] to the parent.
4. Parent calls [[Wait|`wait` / `waitpid`]] — reads the [[ExitStatus|exit status]] and the OS frees the PCB.

If step 4 never happens, the zombie persists. Long-running zombies leak [[ProcessID|PID]] table entries — historically a denial-of-service vector.

## Adoption by `init` — escape valve

If a parent dies before its child, the orphaned child (still alive or already a zombie) is **re-parented to [[Init|`init`]] (PID 1)**, which periodically [[Wait|`wait`s]] for any child. So zombies whose parent crashes get reaped by `init` shortly thereafter — only zombies whose live parent fails to call `wait` linger.

## Connections

- [[dis-13-2-processes]] — primary source.
- [[ProcessState]] — Zombie corresponds to the Exited state.
- [[Wait]] — the syscall that reaps zombies.
- [[Exit]] / [[ExitStatus]] — produce the zombie.
- [[Signal]] / `SIGCHLD` — notifies the parent.
- [[Init]] — the safety net that reaps orphans.
- [[Process]] / [[ProcessID]] / [[ProcessControlBlock]].
- [[Fork]] — creates the child whose termination produces the zombie.
