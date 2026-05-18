---
title: "LD_LIBRARY_PATH"
type: concept
tags: [linker, runtime, environment-variable, dynamic-linking]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# `LD_LIBRARY_PATH`

`LD_LIBRARY_PATH` is the colon-separated environment variable the [[DynamicLinker|dynamic linker]] consults at process launch to find [[DynamicLibrary|`.so`]] shared objects outside the default search path. Per [[dis-2-9-5-libraries|DIS Ch 2.9.5]], it is the **runtime equivalent of `-L<path>`** — `-L<path>` adds to the **build-time** library search path consulted by [[Linker|`ld`]] at stage 4 ([[LinkingStage|link-edit]]); `LD_LIBRARY_PATH` adds to the **launch-time** search path consulted by [[DynamicLinker|`ld.so`]] at stage 5 ([[RuntimeLinking|runtime link]]).

## Typical use

```
gcc -L./libs -lfoo main.c -o prog        # build-time -L finds libfoo.so
./prog                                   # fails: ld.so doesn't know ./libs
LD_LIBRARY_PATH=./libs ./prog            # now ld.so finds it
```

The asymmetry is the canonical surprise — the program **builds** fine but **won't launch**.

## Search precedence

`LD_LIBRARY_PATH` is consulted **before** the system `/etc/ld.so.cache` and the default `/lib` / `/usr/lib`, so it can override system-installed libraries. This makes it a convenient debugging knob and a notorious source of "works on my machine" failures.

## Why not just bake the path in

The alternative is `-Wl,-rpath,/some/path` at link time, which embeds an `RPATH` entry directly in the executable's ELF. This produces self-locating binaries (no env var required at launch) but at the cost of build-host-dependent absolute paths. `LD_LIBRARY_PATH` is the more portable, more dangerous choice; `RPATH` is the more rigid, more reliable choice.

## Security note

Setuid binaries **ignore** `LD_LIBRARY_PATH` for obvious reasons — otherwise an attacker could substitute a malicious `libc.so` and gain root. Regular binaries honor it.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[DynamicLinker]] — the agent that reads this variable.
- [[RuntimeLinking]] — the stage where it matters.
- [[DynamicLibrary]] — what gets resolved through this path.
- [[DynamicLinking]] — the link mode requiring runtime resolution.
- [[Linker]] — the build-time counterpart consulting `-L<path>` instead.
- [[LinkingStage]] — the build-time stage.
