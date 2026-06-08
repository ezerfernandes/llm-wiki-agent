---
title: "Zig Build Modes (Debug / ReleaseSafe / ReleaseFast / ReleaseSmall)"
type: concept
tags: [zig, build-system, optimization, safety, compiler]
sources: [zig-build-system-guide, zig-in-depth-overview, zig-why-zig-vs-rust-d-cpp]
last_updated: 2026-06-07
---

# Zig Build Modes

[[Zig]] exposes four **build (optimization) modes** that trade off among performance, runtime safety, and binary size. They are selected per [[ZigBuildSystem|build]] via `-Doptimize=<mode>` (or the convenience `--release[=fast|safe|small]`), and Zig advertises that they can be mixed down to **scope granularity** within a single program ([[zig-in-depth-overview]]).

| Mode | Priority | Runtime safety checks | Optimizations |
|---|---|---|---|
| `Debug` | Fast compile, debuggability (default) | On | Off |
| `ReleaseSafe` | Safety + performance | On | On |
| `ReleaseFast` | Maximum speed | Off | On |
| `ReleaseSmall` | Minimum binary size | Off | On (size) |

## Selecting a mode

In a build script, `const optimize = b.standardOptimizeOption(.{});` adds the conventional `-Doptimize=[Debug|ReleaseSafe|ReleaseFast|ReleaseSmall]` flag and threads the choice into a module's `.optimize` field ([[zig-build-system-guide]]). Crucially:

> "By default none of the release options are considered the preferable choice by the build script, and the user must make a decision in order to create a release build."

So `zig build` defaults to `Debug`; a release build is an explicit user choice. The shorthand `--release[=mode]` requests release mode, optionally naming the preferred optimization (`fast`, `safe`, `small`).

## What the modes mean

- **`Debug`** — the default. Fast compilation and best debugging experience; runtime safety checks are enabled and optimizations are off.
- **`ReleaseSafe`** — optimizations on **and** runtime safety checks retained. This is Zig's distinctive "performance and safety, choose two" position: rather than stripping checks for speed, it keeps illegal-behavior detection (e.g. integer overflow, out-of-bounds) while optimizing.
- **`ReleaseFast`** — prioritizes execution speed; safety checks disabled. Triggering what would be a safety-checked illegal behavior here becomes [[UndefinedBehavior]].
- **`ReleaseSmall`** — prioritizes binary size; safety checks disabled. Useful for embedded / size-constrained targets (e.g. building a Windows `hello.exe` with `-Doptimize=ReleaseSmall`).

In safe modes Zig's runtime safety **crashes rather than invoking [[UndefinedBehavior]]**, and notably Zig treats both signed *and* unsigned integer overflow as illegal behavior ([[zig-in-depth-overview]]).

## Mixable at scope granularity

A key Zig design point: the build modes are not strictly whole-program. Per [[zig-in-depth-overview]], modes are "mixable down to scope granularity" — performance-critical or safety-critical sections can opt into a different regime than the rest of the program, supporting the "performance and safety, choose two" framing without forcing it globally.

## Connections

- [[ZigBuildSystem]] — `standardOptimizeOption` / `-Doptimize` / `--release` select the mode.
- [[Zig]] — the language whose four modes embody "performance and safety, choose two."
- [[CompilerOptimization]] — the optimization dimension the release modes turn on.
- [[UndefinedBehavior]] — what disabled safety checks (ReleaseFast/ReleaseSmall) can produce; safe modes crash instead.
- [[Comptime]] — Options-step build-time flags (often gated per mode) are comptime-known.
- [[CrossCompilation]] — release builds for multiple targets typically pin `.ReleaseSafe`.
- [[zig-build-system-guide]] — source for mode selection via the build script and CLI.
- [[zig-in-depth-overview]] — source for "performance and safety, choose two" and scope-granular mixing.
- [[zig-why-zig-vs-rust-d-cpp]] — source positioning Zig's safety/perf trade-offs against C++/D/Rust.
</content>
