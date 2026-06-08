---
title: "Wavelet Matrix (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, bit-manipulation, succinct-data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Wavelet_Matrix
---

## Summary
The task asks the programmer to implement a Wavelet Matrix, a compact (succinct) data structure built over a sequence of integers drawn from an alphabet of size sigma. The structure is organized as L = ceil(log2 sigma) levels of bitvectors, one per bit position from most significant to least significant, that together support efficient rank, select, and range queries on the sequence. The key insight is that at each level the sequence is stably partitioned by the current bit, letting queries be answered by descending the levels using fast rank operations on the augmented bitvectors.

## Task Requirements
- Process an initial integer sequence S = S_0 ... S_(N-1) over an alphabet [0, sigma-1].
- Build L = ceil(log2 sigma) levels, each with a bitvector B_j recording the (L-1-j)-th bit (MSB to LSB) of every element in the current permuted order.
- At each level, stably reorder elements so all those with bit 0 come first (in original relative order), followed by all with bit 1.
- Augment each bitvector to support fast rank operations (counting 0s or 1s up to a position).
- Use the resulting structure to efficiently answer queries such as rank, select, and range queries.

## Language Coverage
17 languages implement this task, giving moderate breadth across systems, functional, and scripting languages. Representative implementations include C#, Go, Rust, Zig, Java, OCaml, Julia, Python, Raku, Swift, and Wren.

## Connections
- [[SuccinctDataStructures]] — the Wavelet Matrix is a space-efficient succinct structure
- [[RankSelectQueries]] — core operations the structure supports via augmented bitvectors
- [[BitVector]] — each level is a rank-augmented bitvector keyed on one bit position
- [[BinaryRepresentation]] — levels correspond to bit positions from MSB to LSB
- [[StableSort]] — elements are stably partitioned by bit at each level

## Contradictions
- None — reference task page.
