---
title: "`init` Process (PID 1)"
type: concept
tags: [operating-systems, unix, posix, processes, boot]
sources: [dis-13-2-processes]
last_updated: 2026-05-17
---

# `init` Process (PID 1)

**`init`** is *"the first user-level process created at boot, ancestor of all processes"* ([[dis-13-2-processes|DIS Ch 13.2]]). It is the **root of the [[Process|process]] hierarchy** — every other process in the system descends from `init` via repeated [[Fork|`fork`]].

## Key properties

- **[[ProcessID|PID]] 1** — fixed by convention; the first process the [[Kernel|kernel]] spawns after [[Bootloader|boot]] completes.
- **Ancestor of every user process** — by transitive [[Fork|`fork`]] from PID 1.
- **Adopter of orphans** — if a parent dies before its child, the orphan is re-parented to `init`, which periodically [[Wait|`wait`s]] so the orphan does not linger as a [[Zombie|zombie]].
- **Cannot exit while the system runs** — `init` exiting would mean kernel panic (no parent to adopt the remaining orphans).

## Modern implementations

The original Unix `init` was a small program reading `/etc/inittab` and spawning daemons. Modern Linux distributions ship one of:

- **systemd** — the dominant modern PID 1 (parallel service startup, socket-activation, journald integration).
- **OpenRC**, **runit**, **sysvinit** — minimalist alternatives.
- **launchd** — macOS's PID 1 (Apple's analog of systemd).

DIS 13.2's scope is the abstract role (*PID 1 = root of the hierarchy*) not the specific implementation.

## Why DIS 13.2 names it

`init` is the topological **base case** of the process hierarchy claim — *every process has a parent* would be a non-terminating recursion without a designated root. Naming `init` also explains where zombie children of dead parents go (re-parented to PID 1) — the implicit safety valve that keeps the [[ProcessControlBlock|PCB table]] from leaking.

## Connections

- [[dis-13-2-processes]] — primary source.
- [[Process]] — the entity `init` is the root of.
- [[ProcessID]] — `init` has PID 1.
- [[Fork]] — the call that descends from `init`.
- [[Zombie]] — what `init` adopts and reaps from dead parents.
- [[Wait]] — the call `init` periodically issues to reap orphans.
- [[Bootloader]] / [[Kernel]] — what spawns `init`.
- [[OperatingSystem]].
