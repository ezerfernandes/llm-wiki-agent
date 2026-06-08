---
title: "Zig Package Manager (build.zig.zon)"
type: concept
tags: [zig, package-manager, dependencies, build-system, reproducibility]
sources: [zig-build-system-guide, zig-getting-started, zig-why-zig-vs-rust-d-cpp]
last_updated: 2026-06-07
---

# Zig Package Manager (`build.zig.zon`)

The package manager is the dependency-management half of the [[ZigBuildSystem|Zig build system]], built directly into the [[ZigToolchain|toolchain]] rather than shipped as a separate tool. Its manifest is `build.zig.zon` (ZON = **Z**ig **O**bject **N**otation), and dependencies it declares are consumed inside `build.zig` and linked into artifacts.

## Manifest: `build.zig.zon`

`zig init` scaffolds both `build.zig` (the build script) and `build.zig.zon` (the package/dependency manifest) alongside `src/main.zig` and `src/root.zig` ([[zig-getting-started]]). The manifest declares the package name/version and a set of named dependencies, each pinned by a **URL + content hash**. Pinning by hash is what makes dependency resolution **content-addressed and reproducible** — a fetched dependency that does not match its declared hash is rejected. See [[Reproducibility]].

## Consuming a dependency

Within `build.zig`, a declared dependency is materialized with `b.dependency(name, .{ .target = ..., .optimize = ... })`, which fetches (if needed) and builds the dependency's own `build.zig`, exposing its modules and artifacts. Those are then wired into the consumer's modules (e.g. `module.addImport(...)` / `module.linkLibrary(dep.artifact(...))`), so the dependency's compile steps become nodes in the same [[DirectedAcyclicGraph|build DAG]].

## Fetching and overrides (CLI)

The `zig build` CLI exposes package-management controls ([[zig-build-system-guide]]):

- `--fetch[=needed|all]` — fetch the dependency tree and exit; `needed` (default) fetches lazy dependencies only as required, `all` always fetches them.
- `--fork=[path]` — override one or more projects in the dependency tree with a local checkout (for patching / local development).
- `--system [pkgdir]` — **disable** package fetching and enable all system integrations; used by distro packagers who must build against system-provided libraries instead of fetched ones.
- `--global-cache-dir` / `--cache-dir` — relocate the caches where fetched packages and build artifacts live.

## Why a built-in package manager matters

The argument ([[zig-why-zig-vs-rust-d-cpp]]) is that system package managers (apt-get, pacman, homebrew) serve **end users** but not **developers/contributors**:

- "The difficulty of getting the project to build at all is a huge hurdle for potential contributors." A language-specific package manager "can be the difference between having no contributors and having many."
- For C/C++ projects, missing dependencies "can be fatal, especially on Windows, where there is no package manager."
- The key differentiator: *"Other languages have package managers but they do not eliminate pesky system dependencies like Zig does."* Zig lets a project depend on native libraries directly, pinned by hash, "practically guaranteed to successfully build projects on the first try regardless of what system is being used and independent of what platform is being targeted" — including [[CrossCompilation|cross-compilation]].

Per [[zig-build-system-guide]], package-provided dependencies are "expected to be the generally preferred way to depend on external libraries" over linking host system libraries, because they give reproducible, consistent results, work on every OS, and grant exact control over the entire dependency tree.

## Connections

- [[ZigBuildSystem]] — the build system this package manager is built into; `build.zig` consumes the dependencies.
- [[ZigToolchain]] — the `zig` CLI that fetches, hashes, and caches packages.
- [[Zig]] — the language whose toolchain bundles the package manager.
- [[DirectedAcyclicGraph]] — fetched dependencies' compile steps join the consumer's build DAG.
- [[CrossCompilation]] — hash-pinned native deps build for any target from any host.
- [[CInterop]] — depending on and linking native C libraries is the headline use case.
- [[CLanguage]] — managing C/C++ native dependencies is what the package manager makes tractable.
- [[Reproducibility]] — content-addressed (hash-pinned) dependencies give reproducible builds.
- [[LLVM]] — the canonical "fatal" dependency the approach aims to tame.
- [[BuildRs]] — Cargo's analog hook; Cargo + crates.io is the closest ecosystem comparison.
- [[zig-build-system-guide]] — source for the fetch/fork/system CLI surface and the system-vs-package linking guidance.
- [[zig-getting-started]] — source for `zig init` scaffolding `build.zig.zon`.
- [[zig-why-zig-vs-rust-d-cpp]] — source for the "eliminate system dependencies" argument.
</content>
