---
title: "Canonicalize CIDR (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, bit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Canonicalize_CIDR
---

## Summary
Given an IPv4 range in CIDR notation (dotted-decimal address plus a slash and a network-bit count), output the same range in canonical form where every host bit is zeroed. The key insight is that the address is a 32-bit integer split into a network portion and a host portion at the slash boundary; canonicalizing simply masks off (clears) all bits to the right of the network/host divide. For example, `87.70.141.1/22` becomes `87.70.140.0/22`.

## Task Requirements
- Accept an IPv4 address in CIDR notation: dotted-decimal address `/` network-bit count.
- Treat the address as a 32-bit value with a network portion (leftmost `n` bits) and a host portion (remaining bits).
- Clear all host bits (set them to zero), i.e. apply a netmask of `n` leftmost ones.
- Convert the masked value back to dotted-decimal and re-attach the `/n` suffix.
- Produce correct output across the given test cases (e.g. `67.137.119.181/4 → 64.0.0.0/4`).

## Language Coverage
46 languages implement this task, showing broad coverage across systems, scripting, and functional styles. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, Ruby, JavaScript, and APL.

## Connections
- [[IPv4Addressing]] — the 32-bit address space being parsed and formatted
- [[CIDRNotation]] — the network/host boundary specified by the slash count
- [[BitMasking]] — clearing host bits via a netmask of leftmost ones
- [[SubnetMask]] — the mask derived from the prefix length
- [[BitwiseOperations]] — shifts and AND used to zero the host portion

## Contradictions
- None — reference task page.
