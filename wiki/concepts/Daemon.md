---
title: "Daemon (UNIX)"
type: concept
tags: [unix, operating-system, process, background-service]
sources: [dis-7-10-x86-64-buffer-overflow]
last_updated: 2026-05-17
---

# Daemon (UNIX)

A **daemon** is a [[UNIX]] / [[Linux]] **background process** that runs detached from any controlling terminal, typically launched at system boot and persistent across user sessions. Daemons handle monitoring, scheduling, and service-provision tasks: `sshd` (SSH server), `httpd` / `nginx` (web servers), `cron` (job scheduler), `systemd` (init / service manager), `cupsd` (printing), historically `fingerd` (user-info lookup). Per [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]] of [[DiveIntoSystems]]: a daemon is a *"background process performing monitoring and cleanup tasks in UNIX systems."*

## Conventions

- **Name suffix `d`** — `sshd`, `httpd`, `cupsd`, `crond`, `syslogd`. (`systemd` is named with this convention even though it functions as PID 1.)
- **PID 1's child or session leader** — daemons typically detach from any login shell, are inherited by `init` / `systemd`.
- **No controlling terminal** — `setsid` to become a new session leader, redirect stdin/stdout/stderr to `/dev/null` or a log file.
- **Long-running** — life-of-the-system rather than life-of-a-login.

## Why daemons matter for security

Daemons typically:

- **Listen on network sockets**, exposing their attack surface to remote input.
- **Run with elevated privileges** (often `root` initially, then drop to a service user via `setuid`).
- **Process untrusted input** from arbitrary network peers.

A [[BufferOverflow|buffer overflow]] in a network daemon is therefore one of the most consequential vulnerability classes — remote, often root, often exploitable without authentication.

## The Morris Worm (1988)

The canonical example, cited in [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]]: the **Morris Worm** exploited a buffer overrun in the [[UNIX]] **`fingerd`** daemon (the user-information lookup service running on port 79). The worm:

1. Sent an oversized request to `fingerd` on a target host.
2. The overrun overwrote `fingerd`'s [[StackFrame|stack frame]] with shellcode + a return address pointing into the buffer.
3. Shellcode launched a copy of the worm on the target.
4. The new copy scanned for further targets and repeated.

The worm propagated faster than its author (Robert Morris) anticipated, infecting ~6,000 systems and rendering them unusable through resource exhaustion. It led directly to the formation of [[CERT|CERT/CC]] and is regarded as the **first major internet-scale security incident**.

## Modern hardening

Modern daemons combine multiple defenses against [[StackSmashing|stack-smashing]]:

- **[[StackCanary|Stack canaries]]** in the compiled binary.
- **[[AddressSpaceLayoutRandomization|ASLR]]** + [[PositionIndependentCode|PIE]] randomizing the daemon's address space.
- **[[ExecutableSpaceProtection|NX / DEP]]** on stack and heap pages.
- **Privilege separation** — a small unprivileged worker process handles untrusted input; the privileged supervisor handles only validated requests.
- **`seccomp` / sandboxing** — kernel-level syscall filtering to limit blast radius.
- **Memory-safe rewrites** — modern daemons (`rustls`, `caddy`) are written in [[MemorySafeLanguage|memory-safe languages]] that make [[BufferOverflow|buffer overflows]] unexpressible.

## Sources

- [[dis-7-10-x86-64-buffer-overflow]] — Ch 7.10 names daemons in the Morris Worm case study and defines them as *"background processes performing monitoring and cleanup tasks in UNIX systems."*
