---
title: "Embassy"
type: entity
tags: [rust, embedded, framework, async, concurrency]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# Embassy

[[RustLanguage|Rust]]-ecosystem framework for **`async` / `await`-based embedded concurrency**. The second named higher-level alternative to manual `Mutex<RefCell<Option<T>>>` boilerplate in [[rust-embedded-book-concurrency-index|the Concurrency chapter]]:

> *"Embassy is an ecosystem of libraries which focus on using the `async` / `await` syntax included in Rust for concurrency. The core of embassy is its asynchronous executor which supports most common MCU architectures."*

## Components named in the chapter

- **`embassy-executor`** — the **asynchronous executor** at the core; supports most common MCU architectures. <https://docs.rs/embassy-executor/latest/embassy_executor/>
- **`embassy-time`** — time library. <https://docs.rs/embassy-time/latest/embassy_time/>
- **HAL libraries** — *"various HAL libraries which also provide the time library support"* — Embassy ships its own [[HALCrate|HAL]] implementations across vendors.
- **`embassy-sync`** — synchronization primitives. <https://docs.embassy.dev/embassy-sync/git/default/index.html>

*"Battery-included approach"* — distinguishing it from the more-focused [[RTIC]] framework, which leaves HAL choice to the user.

## Distinguishing model vs RTIC

| | [[RTIC]] | Embassy |
|---|---|---|
| Scheduling model | Priority-driven [[Interrupt|interrupts]]-as-tasks | `async`/`await` cooperative |
| HAL | User-supplied | Bundled per-vendor |
| Time | User-supplied | `embassy-time` |
| Sync primitives | Compile-time resource tracking | `embassy-sync` runtime primitives |

Both are named by [[rust-embedded-book-concurrency-index]] as the two preferred alternatives to the manual `cortex_m::interrupt::Mutex<RefCell<Option<T>>>` pattern.

## Reference

- Project: <https://embassy.dev/>
- Book: <https://embassy.dev/book/>

## Connections

- [[TheEmbeddedRustBook]] — introduces Embassy in [[rust-embedded-book-concurrency-index|the Concurrency chapter]] as a higher-level alternative.
- [[RTIC]] — sibling higher-level alternative; different scheduling model.
- [[RustLanguage]] — `async`/`await` is the language feature Embassy is built on.
- [[Mutex]] / [[CriticalSection]] / [[RefCell]] — the lower-level mechanisms Embassy abstracts above.
- [[HALCrate]] — Embassy ships its own HAL crates as part of the battery-included approach.
- [[Interrupt]] — Embassy's executor wires `async` tasks to interrupts on the target MCU.
- [[ARMCortexM]] — supported core family among "most common MCU architectures."
