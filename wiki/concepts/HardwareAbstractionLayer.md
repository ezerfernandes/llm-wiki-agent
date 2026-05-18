---
title: "Hardware Abstraction Layer (HAL)"
type: concept
tags: [embedded, architecture, portability, hal]
sources: [rust-embedded-book-portability-index]
last_updated: 2026-05-16
---

# Hardware Abstraction Layer (HAL)

A **Hardware Abstraction Layer (HAL)** is a software layer that **equalizes platform-specific hardware differences** so that programs above it can be written in a device-independent way ([[rust-embedded-book-portability-index]]). The umbrella concept the *Portability* chapter of [[TheEmbeddedRustBook]] names as the standard solution to the embedded fragmentation problem, quoting the Wikipedia definition:

> *"Hardware abstractions are sets of routines in software that emulate some platform-specific details, giving programs direct access to the hardware resources. They often allow programmers to write device-independent, high performance applications by providing standard operating system (OS) calls to hardware."* — Wikipedia, via [[rust-embedded-book-portability-index]].

## Traditional (OS-syscall) HAL vs. embedded-trait HAL

The Wikipedia definition assumes an **operating system**: the HAL is exposed as a syscall surface. In embedded systems this assumption fails — *"we typically do not have operating systems and user installable software but firmware images which are compiled as a whole as well as a number of other constraints"* ([[rust-embedded-book-portability-index]]). The embedded-Rust answer is therefore a **trait-based** HAL, not a syscall-based one: [[EmbeddedHalCrate|`embedded-hal`]] defines a set of traits, and per-chip [[HALCrate|HAL crates]] implement them.

| Flavor | Where the contract lives | Embedded-suitable? |
|---|---|---|
| OS-syscall HAL | OS kernel | No — most embedded firmware has no OS |
| Trait HAL ([[EmbeddedHalCrate|`embedded-hal`]]) | Compiled-in trait crate | **Yes** — compile-time-only contract, no runtime cost |
| Adapter/mock HAL | A type that wraps another type | Useful for unit testing |
| Adapter-for-hardware HAL | An I2C-multiplexer or GPIO-expander as a synthetic HAL | First-class flavor per [[rust-embedded-book-portability-index]] |

The chapter explicitly names the **four flavors** of HAL implementation: *"Via low-level hardware access, e.g. via registers; Via operating system, e.g. by using the sysfs under Linux; Via adapter, e.g. a mock of types for unit testing; Via driver for hardware adapters, e.g. I2C multiplexer or GPIO expander."*

## Three-role taxonomy of HAL users

When a HAL is realized as a trait crate ([[EmbeddedHalCrate|`embedded-hal`]]-style), there are three classes of users:

1. **[[HALCrate|HAL implementation]]** — chip-specific, implements the traits.
2. **[[DriverCrate|Driver]]** — chip-agnostic, depends on the traits.
3. **Application** — composes a HAL implementation and one-or-more drivers; the layer at which **porting work concentrates**.

## Connections

- [[EmbeddedHalCrate]] — the **trait-based HAL** of the embedded-Rust ecosystem.
- [[HALCrate]] — a per-chip implementation of [[EmbeddedHalCrate|`embedded-hal`]] traits — *the* concrete instance of the umbrella concept.
- [[Portability]] — the architectural goal HALs exist to deliver.
- [[DriverCrate]] — depends on the HAL's trait surface, not on its implementation.
- [[rust-embedded-book-portability-index]] — the chapter that frames this concept.
