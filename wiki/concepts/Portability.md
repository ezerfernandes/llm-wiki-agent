---
title: "Portability (Embedded)"
type: concept
tags: [embedded, rust, portability, embedded-hal, architecture]
sources: [rust-embedded-book-portability-index]
last_updated: 2026-05-16
---

# Portability (Embedded)

In embedded systems, **portability** is the property of being able to write peripheral-driver and application code **once** and have it compile + run against many different chips, vendors, and boards ([[rust-embedded-book-portability-index]]). The *Portability* chapter of [[TheEmbeddedRustBook]] frames it as the **"very important topic"** of the field: *"Every vendor and even each family from a single manufacturer offers different peripherals and capabilities and similarly the ways to interact with the peripherals will vary."*

## The M·N → M+N argument

The chapter's central architectural payoff. Without a portability layer, every application would have to ship its own bindings against every peripheral it talks to — with **M** [[HALCrate|HAL implementations]] and **N** [[DriverCrate|driver crates]], the ecosystem would converge on **M·N** total implementations. Routing both sides through the [[EmbeddedHalCrate|`embedded-hal`]] trait crate collapses this to **M+N**: each HAL implements the traits once, each driver depends only on the traits, and the trait crate is the single contract both sides target.

> *"If M is the number of peripheral HAL implementations and N the number of drivers then if we were to reinvent the wheel for every application then we would end up with M·N implementations while by using the API provided by the embedded-hal traits will make the implementation complexity approach M+N."* ([[rust-embedded-book-portability-index]]).

Additional benefits: less trial-and-error against well-defined APIs, fewer total implementations to maintain.

## Why embedded portability differs from desktop portability

Traditional desktop/server HALs equalize platform differences through **OS syscalls** (the Wikipedia definition: *"providing standard operating system (OS) calls to hardware"*). Embedded targets *"typically do not have operating systems and user installable software but firmware images which are compiled as a whole as well as a number of other constraints"* — so the embedded-Rust answer is a **trait-based** HAL ([[EmbeddedHalCrate|`embedded-hal`]]) rather than a syscall-based HAL.

## Three layers of porting effort

The chapter distinguishes three roles in the `embedded-hal` ecosystem, each carrying a different porting cost:

- **HAL implementations** — chip-specific; one per chip family. Port-cost: full reimplementation per chip.
- **[[DriverCrate|Drivers]]** — chip-agnostic; written once against `embedded-hal` traits. Port-cost: **zero** (the whole point of the architecture).
- **Applications** — *"the part which requires the most adaptation efforts"*. Port-cost concentrated here: pin reassignment, clock-tree reconfiguration, peripheral-conflict resolution, bus-config differences.

## Connections

- [[EmbeddedHalCrate]] — the trait crate that mechanizes embedded portability in Rust.
- [[HALCrate]] / [[DriverCrate]] — the two ecosystem layers whose product collapses from M·N to M+N.
- [[BoardCrate]] / [[PeripheralAccessCrate]] / [[MicroArchitectureCrate]] — the other three layers of the embedded-Rust crate stack.
- [[HardwareAbstractionLayer]] — the umbrella concept; `embedded-hal` is its trait-based, no-OS realization.
- [[rust-embedded-book-portability-index]] — the chapter that names this concept.
