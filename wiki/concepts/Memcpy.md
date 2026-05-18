---
title: "memcpy (C)"
type: concept
tags: [c-language, memory, byte-level, string-library, void-pointer]
sources: [dis-2-9-3-voidstar]
last_updated: 2026-05-17
---

# `memcpy` (C)

**`memcpy`** is the [[CStandardLibrary|`<string.h>`]] byte-level copy primitive — *"copy `n` bytes from `src` to `dest`."* Mentioned in [[dis-2-9-3-voidstar|DIS Ch 2.9.3]] as one of the canonical [[VoidPointer|`void *`]]-bearing [[CStandardLibrary|standard-library]] routines that the [[VoidPointer|generic-pointer]] mechanism enables.

Declared in `<string.h>`:

```c
void *memcpy(void *dest, const void *src, size_t n);
```

- **`dest`** — destination buffer ([[VoidPointer|`void *`]] — accepts any pointer type).
- **`src`** — source buffer ([[ConstQualifier|`const`]] [[VoidPointer|`void *`]] — read-only, accepts any pointer type).
- **`n`** — byte count (typically computed via [[SizeOf|`sizeof`]] / `strlen() + 1` / explicit).
- **Return** — `dest` (for chaining).

## Why `void *`

`memcpy` works on *bytes*, not on typed objects. It must accept any pointer type — `int *`, `char *`, `struct studentT *`, anything — without recompiling per type. [[VoidPointer|`void *`]] is the [[CLanguage|C]] mechanism that achieves this. Per [[dis-2-9-3-voidstar|Ch 2.9.3]]'s framing, `memcpy` is the prototypical *byte reinterpretation* use case: one routine, all types, zero per-type machinery.

## Canonical patterns

```c
int src[10] = {1,2,3,4,5,6,7,8,9,10};
int dest[10];
memcpy(dest, src, sizeof(int) * 10);    // copy a whole array

struct studentT s1 = {...};
struct studentT s2;
memcpy(&s2, &s1, sizeof(struct studentT));    // whole-struct copy (same as s2 = s1;)

char *heap_str = malloc(strlen(orig) + 1);
memcpy(heap_str, orig, strlen(orig) + 1);    // copy a C string including '\0'
```

The third form is a [[Strcpy|`strcpy`]] alternative that doesn't scan for the [[NullTerminator|null terminator]] — useful when the length is already known.

## Three rules

### 1. No overlap

`memcpy`'s contract is *undefined behavior* if `src` and `dest` regions overlap. For overlapping copies, use `memmove`:

```c
void *memmove(void *dest, const void *src, size_t n);   // overlap-safe
```

`memmove` handles overlap by copying in the correct direction (back-to-front when `dest > src`, front-to-back otherwise). It's slightly slower in the no-overlap case — most production code uses `memcpy` when overlap is known impossible and `memmove` when it's possible.

### 2. Caller owns destination size

Just like [[Strcpy|`strcpy`]] / [[Strncpy|`strncpy`]], the caller must ensure `dest` has at least `n` bytes of writable space. `memcpy` doesn't check — it writes `n` bytes wherever `dest` points. Buffer overrun is the same [[BufferOverflow|buffer-overflow]] footgun [[dis-2-6-strings|Ch 2.6]] highlights for [[Strcpy|`strcpy`]].

### 3. Byte-level, no type interpretation

`memcpy` doesn't care what the bytes mean — it copies them verbatim. This makes it the right tool for:

- **Serialization** — copying typed data into a byte buffer for I/O.
- **Type-punning** — viewing the same bytes through a different type (with the [[StrictAliasing|strict-aliasing]] caveats — the modern correct way is `memcpy(&dst_typed, &src_typed, sizeof(...))`, not `(double *)int_ptr` casts).
- **Generic data structures** — copying payload of unknown type into / out of a container.

## Relationship to `=` and struct assignment

For named typed variables, `=` does the same job:

```c
int b = a;                      // single int copy
struct studentT s2 = s1;        // whole-struct copy (Ch 1.6's rule)
```

The compiler emits a `memcpy`-equivalent inline. `memcpy` is needed when:

- The source / destination are reached through `void *` parameters.
- The byte count is computed dynamically.
- The types don't have a copyable `=` form (e.g. flexible array members, type-punning).

## Connections

- [[dis-2-9-3-voidstar]] — mentioning source (named as a `void *`-bearing routine).
- [[VoidPointer]] — the parameter type that lets `memcpy` accept any buffer.
- [[ConstQualifier]] — `const void *src` marks the source as read-only.
- [[SizeOf]] — typical companion for computing `n`.
- [[SizeT]] — the `n` parameter type.
- [[CStandardLibrary]] / [[StringLibrary]] — `memcpy` lives in `<string.h>` alongside the C-string family.
- [[Strcpy]] / [[Strncpy]] / [[Strlcpy]] — string-aware copy alternatives ([[dis-2-6-strings|Ch 2.6]]).
- [[StructAssignment]] — the typed counterpart for whole-struct copy.
- [[BufferOverflow]] — the failure mode `memcpy` shares with [[Strcpy|`strcpy`]].
- [[CLanguage]] / [[DiveIntoSystems]].

## Status

Named-and-deferred — [[dis-2-9-3-voidstar|Ch 2.9.3]] cites `memcpy` as a [[VoidPointer|`void *`]]-bearing routine but doesn't develop it. The full treatment appears with [[dis-2-6-strings|Ch 2.6]] (string library) and Ch 9 (concurrency) onwards.
