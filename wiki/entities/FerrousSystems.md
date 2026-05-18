---
title: "Ferrous Systems"
type: entity
tags: [company, rust, embedded, consultancy]
sources: [rust-embedded-book-start-qemu]
last_updated: 2026-05-16
---

# Ferrous Systems

**Berlin-based Rust consultancy and training company** — one of the most prolific contributors to the embedded-Rust ecosystem. Steward of the [[Knurling]] project, which produces the canonical modern Embedded Rust tooling layer used in *[[TheEmbeddedRustBook]]*'s first code example: [[Defmt|`defmt`]] (deferred-format logging), [[QemuRun|`qemu-run`]] (`defmt`-aware QEMU runner), `probe-rs`, `flip-link`, the `app-template` project scaffold.

Surfaces in [[rust-embedded-book-start-qemu]] as the upstream of (1) the `app-template` consumed by `cargo generate --git https://github.com/knurling-rs/app-template` and (2) the `qemu-run` tool needed to decode `defmt` output coming out of [[QEMU]].

## Connections

- [[Knurling]] — the embedded-tooling project group inside Ferrous Systems.
- [[Defmt]] — flagship logging framework.
- [[QemuRun]] — `defmt`-aware QEMU launcher.
- [[TheEmbeddedRustBook]] — depends on Ferrous Systems / Knurling tooling for [[rust-embedded-book-start-qemu|Chapter 11]]'s hello-world flow.
