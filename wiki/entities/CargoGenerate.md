---
title: "cargo-generate"
type: entity
tags: [rust, cargo-subcommand, scaffolding, template]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# cargo-generate

A [[Cargo]] subcommand for creating new Cargo projects from project templates. Maintained at [github.com/ashleygwilliams/cargo-generate](https://github.com/ashleygwilliams/cargo-generate).

In *[[TheEmbeddedRustBook]]*, `cargo-generate` exists to solve a real friction: [[BareMetalProgramming|bare-metal]] [[NoStd|`no_std`]] programs need *extra plumbing* — linker scripts, linker flags, target-specific memory layout — that an ordinary `cargo new` cannot produce. The book ships a template the reader fills in (project name, target characteristics) instead of hand-rolling the boilerplate. As fallback if the user doesn't want `cargo-generate`, the same template can be cloned with `git` / `curl` / `wget` / a browser ([[rust-embedded-book-intro-tooling]]).

Listed by the book as **optional** — `git` is an acceptable substitute.

## Connections

- [[Cargo]] — the build system whose subcommand interface is extended.
- [[BareMetalProgramming]] / [[NoStd]] — the regime that needs the extra plumbing the template carries.
- [[TheEmbeddedRustBook]] — uses `cargo-generate` for the F3 project template.
