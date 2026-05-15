---
title: "ODS Ch.5: Hash Tables"
type: source
tags: [book, data-structures, hashing, uset]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 5
pages: "101-126"
---

## Summary
Two hash-table implementations of the USet interface, plus a treatment of hash-code design. **ChainedHashTable** uses an array of linked lists (collision resolution by chaining), maintaining the load-factor invariant n ≤ length(t). **LinearHashTable** uses open addressing with linear probing. Both achieve O(1) expected time per operation provided the hash function is sufficiently random. The chapter introduces **multiplicative hashing** as the workhorse function — `hash(x) = ((z·x) mod 2^w) div 2^(w−d)` with z random odd in {1,...,2^w−1} — and proves Pr{hash(x) = hash(y)} ≤ 2/2^d for any x ≠ y. Closes with the engineering question of computing hash *codes* for compound objects, arrays, and strings.

## Key Claims
- **ChainedHashTable invariant**: n ≤ length(t) keeps expected list length ≤ 1. Resize doubles or halves the table on the same factor-3 hysteresis as [[ods-02-array-based-lists]].
- **Expected list length lemma (5.2)**: for any x, E[length of t[hash(x)]] ≤ n_x + 2 where n_x is the number of occurrences of x. So find(x), remove(x) both run in O(1) expected.
- **Multiplicative hashing** with a random odd integer z gives a 2-universal-style guarantee Pr{hash(x) = hash(y)} ≤ 2/2^d (Lemma 5.1). The proof goes through Lemma 5.3, a number-theoretic uniqueness fact about z·q mod 2^w on odd q.
- **LinearHashTable** stores values directly in the array and uses linear probing on collision; analysis (§5.2.1) bounds expected probe length given a tabulation-hashing-style function (§5.2.3).
- **Hash codes for primitives**: integers hash to themselves; floats reinterpret bits. **For strings/arrays**: treat as a polynomial in a random base z modulo a prime p — this gives an O(k)-time hash with provable collision bounds (§5.3.3).
- **Tabulation hashing** (§5.2.3) gives an alternative with strong theoretical guarantees: precompute a table of random values, XOR by byte position.

## Key Quotes
> "The performance of a hash table depends critically on the choice of the hash function."
> "Pr{hash(x) = hash(y)} ≤ 2/2^d ."

## Connections
- [[ods-01-introduction]] — defines USet; argues to prefer it over SSet when ordering is unneeded.
- [[ods-02-array-based-lists]] — same amortized doubling/halving argument is reused.
- [[ods-03-linked-lists]] — bucket containers in ChainedHashTable.
- [[ods-12-graphs]] — uses hash tables to implement adjacency-set graph operations in O(1) expected.
- [[modulo-operator]] — multiplicative hashing relies on `mod 2^w` arithmetic.
- [[binary-coefficient]] / [[probability]] — collision analysis.

## Contradictions
None.
