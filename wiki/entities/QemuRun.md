---
title: "qemu-run"
type: entity
tags: [rust, embedded, tooling, qemu, defmt, knurling]
sources: [rust-embedded-book-start-qemu]
last_updated: 2026-05-16
---

# qemu-run

**`defmt`-aware [[QEMU]] launcher** from [[Knurling]] / [[FerrousSystems|Ferrous Systems]], living in the `defmt` repository at [`github.com/knurling-rs/defmt/tree/main/qemu-run/`](https://github.com/knurling-rs/defmt/tree/main/qemu-run/). Wraps `qemu-system-arm` with the flag set the chapter enumerates (`-cpu`, `-machine`, `-nographic`, `-semihosting-config enable=on,target=native`, `-kernel`) and consumes the binary's `.defmt` section to **decode the deferred-format log stream** [[Defmt|`defmt`]] emits — bridging the gap raised in [[rust-embedded-book-start-qemu]]: *"the host will not be able to decode the [`defmt`] output. Instead, we will need a tool by Ferrous Systems named `qemu-run`."*

Invocation in the chapter:

```bash
git clone git@github.com:knurling-rs/defmt.git
cd defmt/qemu-run/
cargo run -- --machine lm3s6965evb ../qemu-rs/target/thumbv7m-none-eabi/debug/hello
```

## Connections

- [[Defmt]] — the logging framework whose output `qemu-run` decodes.
- [[QEMU]] — the underlying emulator `qemu-run` wraps.
- [[Knurling]] — the project group that maintains it.
- [[FerrousSystems]] — parent organization.
- [[LM3S6965]] — the typical `--machine` target.
- [[TheEmbeddedRustBook]] — invoked in [[rust-embedded-book-start-qemu]] as the host-side log decoder.
