---
title: "SHA-256 Merkle tree (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, hashing, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/SHA-256_Merkle_tree
---

## Summary
This task asks the programmer to compute a file checksum the way Amazon S3 Glacier requires: as a Merkle tree of SHA-256 hashes. Each fixed-size block of the file is hashed, then consecutive raw hashes are paired, concatenated, and re-hashed, repeating until a single root hash remains. The key insight is that the tree operates on raw binary hash bytes (not their hex strings) during the pairing rounds, and the final root is only then rendered as hexadecimal.

## Task Requirements
- Split the file into fixed-size blocks and compute the SHA-256 hash of each block.
- Pair up consecutive raw block hashes, concatenate, and hash the concatenation; repeat over successive levels until one hash remains (handling odd/leftover nodes that carry up unchanged).
- Output the final root hash as a hexadecimal digest.
- Use a 1024-byte block size (rather than Glacier's 1 MiB) for manageability.
- Demonstrate on the RosettaCode title image; the expected digest is `a4f902cf9d51fe51eda156a6792e1445dff65edf3a217a1f3334cc9cf1495c2c`.

## Language Coverage
21 languages implement this task, spanning low-level assembly, systems, and high-level scripting languages. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, and AArch64 Assembly.

## Connections
- [[MerkleTree]] — the hierarchical hash structure this task builds
- [[SHA256]] — the underlying cryptographic hash function used at every node
- [[CryptographicHashFunction]] — the broader primitive class SHA-256 belongs to
- [[DataIntegrity]] — the checksum-verification use case driving the task

## Contradictions
- None — reference task page.
