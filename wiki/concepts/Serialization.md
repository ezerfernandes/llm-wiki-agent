---
title: "Serialization (Pickling)"
type: concept
tags: [serialization, pickling, persistence, testing, carving, python]
sources: [fuzzingbook-25-carver]
last_updated: 2026-06-06
---

# Serialization (Pickling)

**Serialization** creates a *persistent* byte representation of an in-memory object that can be stored, transmitted, and later **reconstructed** into an equivalent object. In Python this is commonly done with the `pickle` module (`pickle.dumps` / `pickle.loads`), where the operation is also called *pickling*.

## From The Fuzzing Book — Carving Unit Tests
[[fuzzingbook-25-carver|Ch 25]] uses serialization to solve the hardest part of [[RecordReplay|replaying]] [[TestCarving|carved]] calls: reconstructing **complex object arguments**. When a carved call takes a non-primitive value (e.g. an `email.parser.Parser` object together with a `StringIO`), the value cannot be expressed as a literal. The chapter's `call_value()` helper detects such a value (its `repr` contains `<`) and emits `pickle.loads(<pickled bytes>)` in its place; `call_string()` further turns a leading `self` argument into a method call on the unpickled object. This lets a recorded call like `email.parser.Parser.parse(...)` be re-executed with its original objects faithfully restored, provided they are *picklable*. Objects tied to external resources (open files, sockets) generally are not, which is a major reason carved calls fail to replay.

## Connections
- [[TestCarving]] — serialization is what makes complex carved arguments replayable.
- [[Carver]] — records the object arguments that are then pickled.
- [[RecordReplay]] — pickling addresses the complex-object replay challenge.
- [[fuzzingbook-25-carver]] — the chapter that applies pickling to carving.

## Sources
- [[fuzzingbook-25-carver]] — *The Fuzzing Book* Ch 25, "Carving Unit Tests."
