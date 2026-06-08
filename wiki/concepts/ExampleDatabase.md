---
title: "ExampleDatabase"
type: concept
tags: [testing, python, hypothesis, property-based-testing, database]
sources: [hypothesis-howto-custom-database]
last_updated: 2026-06-05
---

# ExampleDatabase

**ExampleDatabase** is [[Hypothesis]]'s pluggable, abstract key-value **byte store** for persisting and replaying *failing examples* discovered during [[PropertyBasedTesting]]. When a test fails, Hypothesis [[Shrinking|shrinks]] the input to a minimal counterexample and writes it to the database; on the next run it **re-fetches and replays** that minimal example first, so a once-found bug is rechecked deterministically (and disappears from the replay set once fixed). By default Hypothesis uses a directory-backed store (the `.hypothesis/examples` directory), but the backend is swappable.

It lives at `hypothesis.database.ExampleDatabase` and is selected per test or globally through the [[HypothesisSettings|settings]] `database=` option (e.g. `@settings(database=...)`).

## The abstract interface
A subclass implements three required abstract methods, all operating on raw `bytes` (see [[hypothesis-howto-custom-database]]):

| Method | Signature | Role |
|---|---|---|
| `save` | `save(self, key: bytes, value: bytes) -> None` | Store `value` under `key`; should be idempotent on `(key, value)`. |
| `fetch` | `fetch(self, key: bytes) -> Iterable[bytes]` | Return/yield all values stored under `key`. |
| `delete` | `delete(self, key: bytes, value: bytes) -> None` | Remove the specific `(key, value)` pair. |

Optional:
- **`move()`** — *not required*. The default move is a `delete()` from the old key followed by a `save()` under the new key; override only when the backing store offers a more efficient move.
- **Change listening** — call `_broadcast_change()` on every save/delete/move; override `_start_listening()` / `_stop_listening()` to manage expensive monitoring. The built-in `DirectoryBasedExampleDatabase` does this by installing a filesystem monitor via the `watchdog` library.

## Built-in backends
Hypothesis ships several `ExampleDatabase` implementations, all sharing the same interface:
- `DirectoryBasedExampleDatabase` — default; stores examples as files on disk (e.g. `.hypothesis/examples`) and broadcasts changes via `watchdog`.
- `InMemoryExampleDatabase` — non-persistent, useful for tests of the database itself.
- `GitHubArtifactDatabase` — read failing examples saved as CI artifacts (e.g. share a CI-discovered bug with local runs).
- `MultiplexedDatabase` — fan out reads/writes across several databases at once.
- `ReadOnlyDatabase` — wrap another database to forbid writes.
- `BackgroundWriteDatabase` — perform writes asynchronously off the hot path.

> Note: the how-to source ([[hypothesis-howto-custom-database]]) names only `DirectoryBasedExampleDatabase` directly (in the change-listening section); the other backend names come from the Hypothesis reference docs and are listed here for orientation.

## Why write a custom one
Subclass `ExampleDatabase` when the built-ins don't fit your environment — e.g. centralizing the failure store in a shared SQL/SQLite database so a flaky example found in CI replays on every developer's machine. The canonical example is the `SQLiteExampleDatabase` in [[hypothesis-howto-custom-database]], which uses `INSERT OR IGNORE` against a table with a `UNIQUE (key, value)` constraint to make `save()` idempotent.

## Connections
- [[Hypothesis]] — owns the database mechanism and the default directory store.
- [[PropertyBasedTesting]] — the database persists/replays the failing examples this paradigm finds.
- [[Shrinking]] — what gets stored is the *minimal* counterexample produced by the shrink phase.
- [[HypothesisSettings]] — a custom database is wired in via the `database=` setting.
- [[Python]] — implementation language; the reference backend uses stdlib `sqlite3`.

## Sources
- [[hypothesis-howto-custom-database]] — how-to: implement `save`/`fetch`/`delete` (optional `move`), the `SQLiteExampleDatabase` example, and the `_broadcast_change` change-listening protocol.
