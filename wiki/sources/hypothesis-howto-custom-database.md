---
title: "Write a custom Hypothesis database (Hypothesis how-to)"
type: source
tags: [testing, python, hypothesis, property-based-testing, database, how-to]
date: 2026-06-05
source_file: raw/hypothesis/how-to/hypothesis-howto-custom-database.md
---

## Summary
A how-to from the [[Hypothesis]] docs showing how to implement a custom [[ExampleDatabase]] backend — the key-value byte store Hypothesis uses to persist and replay failing examples found during [[PropertyBasedTesting]]. To create one you subclass `hypothesis.database.ExampleDatabase` and implement three abstract methods: `save(key, value)`, `fetch(key)`, and `delete(key, value)`; `move()` is optional. The guide gives a complete `SQLiteExampleDatabase` example and explains the optional change-listening protocol (`_broadcast_change()`, `_start_listening()`, `_stop_listening()`).

## Key Claims
- A custom database class is defined by subclassing `ExampleDatabase` and implementing `save()`, `fetch()`, and `delete()`.
- The store is keyed by `bytes` and stores `bytes` values: `save(self, key: bytes, value: bytes) -> None`, `fetch(self, key: bytes) -> Iterable[bytes]`, `delete(self, key: bytes, value: bytes) -> None`.
- `save()` should be idempotent on `(key, value)` — the SQLite example uses `INSERT OR IGNORE` with a `UNIQUE (key, value)` constraint so re-saving the same example is a no-op.
- `fetch()` returns an iterable of all values stored under a key (the example `yield`s them, making it a generator).
- Implementing `move()` is **not required**. The default `move()` is a `delete()` of the value under the old key followed by a `save()` under the new key; override it only when the backing store has a more efficient move.
- To support change listening, call `_broadcast_change()` whenever a value is saved, deleted, or moved in the backing store.
- `_start_listening()` / `_stop_listening()` can be overridden so the database knows when to start or stop expensive monitoring operations.
- The built-in `DirectoryBasedExampleDatabase` implements change listening by installing a filesystem monitor via the `watchdog` library to broadcast change events.

## Key Quotes
> "To define your own ExampleDatabase class, implement the save(), fetch(), and delete() methods." — opening instruction

> "Database classes are not required to implement move(). The default implementation of a move is a delete() of the value in the old key, followed by a save() of the value in the new key. You can override move() to override this behavior, if for instance the backing store offers a more efficient move implementation." — on the optional `move()` method

> "To support change listening in a database class, you should call _broadcast_change() whenever a value is saved, deleted, or moved in the backing database store... For instance, in DirectoryBasedExampleDatabase, Hypothesis installs a filesystem monitor via watchdog in order to broadcast change events." — on change listening

## Code Receipt

The abstract interface to satisfy (`hypothesis.database.ExampleDatabase`):

| Method | Signature | Required? | Behavior |
|---|---|---|---|
| `save` | `save(self, key: bytes, value: bytes) -> None` | Yes | Store `value` under `key` (idempotent on `(key, value)`). |
| `fetch` | `fetch(self, key: bytes) -> Iterable[bytes]` | Yes | Yield all values stored under `key`. |
| `delete` | `delete(self, key: bytes, value: bytes) -> None` | Yes | Remove the specific `(key, value)` pair. |
| `move` | `move(self, src, dest, value)` | No (optional) | Default = `delete(src, value)` then `save(dest, value)`; override for efficiency. |
| `_broadcast_change` | — | No | Call on every save/delete/move to notify change listeners. |
| `_start_listening` / `_stop_listening` | — | No | Override to start/stop expensive monitoring (e.g. filesystem watch). |

Full SQLite-backed implementation from the guide:

```python
import sqlite3
from collections.abc import Iterable

from hypothesis.database import ExampleDatabase

class SQLiteExampleDatabase(ExampleDatabase):
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)

        self.conn.execute("""
            CREATE TABLE examples (
                key BLOB,
                value BLOB,
                UNIQUE (key, value)
            )
        """)

    def save(self, key: bytes, value: bytes) -> None:
        self.conn.execute(
            "INSERT OR IGNORE INTO examples VALUES (?, ?)",
            (key, value),
        )

    def fetch(self, key: bytes) -> Iterable[bytes]:
        cursor = self.conn.execute("SELECT value FROM examples WHERE key = ?", (key,))
        yield from [value[0] for value in cursor.fetchall()]

    def delete(self, key: bytes, value: bytes) -> None:
        self.conn.execute(
            "DELETE FROM examples WHERE key = ? AND value = ?",
            (key, value),
        )
```

A custom database is wired into a test run through the [[HypothesisSettings|settings]] `database=` option, e.g. `@settings(database=SQLiteExampleDatabase("examples.db"))`.

## Connections
- [[ExampleDatabase]] — the abstract base class this guide subclasses; the primary concept page.
- [[Hypothesis]] — the library that owns the database mechanism.
- [[PropertyBasedTesting]] — the paradigm whose failing examples the database persists and replays.
- [[Shrinking]] — the database stores the *minimal* failing example produced by the shrink phase so it replays on the next run.
- [[HypothesisSettings]] — a custom database is selected via the `database=` setting.
- [[Python]] — implementation language; the example uses the stdlib `sqlite3` module.

## Contradictions
- None. Consistent with the existing Hypothesis cluster; this fills a previously undocumented mechanism (example persistence/replay).
