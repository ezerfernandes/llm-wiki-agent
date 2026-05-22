---
title: "Dive into Systems — Appendix 2.3 SSH and SCP"
type: source
tags: [unix, networking, security, remote-access]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/ssh_scp.html
---

## Summary
Third subchapter of [[DiveIntoSystems]] Appendix 2. Introduces **remote access** through [[SSH|`ssh`]] (encrypted remote shell) and **remote file transfer** through [[SCP|`scp`]] (encrypted [[UnixCommandLine|`cp`]]-over-SSH), plus key-based authentication via `ssh-keygen`.

## Key Claims
- `ssh username@hostname` opens *"a unix shell on the remote machine through which the user can access files and run applications."*
- SSH is cross-platform — native on Unix / macOS; available on Windows via PowerShell or PuTTY.
- `scp src dest` mirrors [[UnixCommandLine|`cp`]] but accepts remote paths of the form `user@host:path` on either side.
  - To remote: `scp prog.c user@host:~/`
  - From remote: `scp user@host:./file ./`
- For bulk transfers, archive + compress with [[Tar|`tar -czvf`]] first to reduce wire bytes.
- `ssh-keygen -t rsa` mints a keypair `~/.ssh/id_rsa` (private — keep secret) + `~/.ssh/id_rsa.pub` (public — copy to the remote `~/.ssh/authorized_keys`). Underlies password-less login and Git-hosting service auth (GitHub etc.).

## Connections
- [[SSH]] — the remote shell.
- [[SCP]] — the remote copy.
- [[UnixCommandLine]] / [[Tar]] — local-side tools that compose with `scp`.
- [[DiveIntoSystems]] — 154th ingested chapter.

## Contradictions
- None.
