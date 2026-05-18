---
title: "Knurling"
type: entity
tags: [rust, embedded, project, ferrous-systems]
sources: [rust-embedded-book-start-qemu]
last_updated: 2026-05-16
---

# Knurling

**Embedded-Rust tooling project from [[FerrousSystems|Ferrous Systems]]**, hosted on GitHub at [`github.com/knurling-rs`](https://github.com/knurling-rs). The umbrella for the modern embedded-Rust workflow used in *[[TheEmbeddedRustBook]]*'s [[rust-embedded-book-start-qemu|first code chapter]]:

- **`app-template`** — the project template `cargo generate --git https://github.com/knurling-rs/app-template` pulls from.
- **[[Defmt|`defmt`]]** — deferred-formatting logging framework with companion sinks `defmt-rtt` and `defmt-semihosting`.
- **[[QemuRun|`qemu-run`]]** — `defmt`-aware QEMU runner that decodes the log stream produced by `defmt-semihosting`.
- `probe-run`, `flip-link`, `defmt-test`, and others outside the chapter's scope.

The project is positioned as the modern, opinionated alternative to the older `cortex-m-quickstart` + `cortex-m-semihosting` stack — though *[[TheEmbeddedRustBook]]* presents both side-by-side ([[CortexMQuickstartTemplate]] is still the canonical scaffolding example in chapter 11).

## Connections

- [[FerrousSystems]] — parent organization.
- [[Defmt]] — flagship Knurling crate.
- [[QemuRun]] — Knurling's `defmt`-aware QEMU launcher.
- [[CortexMQuickstartTemplate]] — the [[RustEmbeddedWorkingGroup]] template Knurling's `app-template` modernizes / competes with.
- [[TheEmbeddedRustBook]] — pulls Knurling's `app-template` + `qemu-run` into [[rust-embedded-book-start-qemu|Chapter 11]].
