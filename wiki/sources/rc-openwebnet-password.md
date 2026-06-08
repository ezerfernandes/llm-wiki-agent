---
title: "OpenWebNet password (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, bit-manipulation, protocol]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/OpenWebNet_password
---

## Summary
This task asks the programmer to implement the password-hashing routine used by Legrand/BTicino MyHome OpenWebNet Ethernet gateways. When a client's IP address is not on the gateway whitelist, the gateway issues a numeric nonce, and the client must reply with a digest computed from the configured "open password" plus that nonce. The key insight is that the digest is produced by a fixed, idiosyncratic sequence of 32-bit integer transformations driven by each decimal digit of the nonce, all performed modulo 2^32.

## Task Requirements
- Reproduce the challenge-response handshake: the gateway sends a nonce frame such as `*#603356072##`, and the client must compute and return a password frame like `*#25280520##`.
- Calculate the response from the gateway's configured "password open" value and the received nonce.
- Implement the OpenWebNet digit-by-digit bitwise/arithmetic algorithm, masking intermediate results to 32 bits.
- Verify against the worked example (password `12345`, nonce `603356072` yields `25280520`).

## Language Coverage
22 languages implement this task, spanning systems, scripting, and functional families. Representative entries include C++, D, Go, Rust, Java, JavaScript, Python, Perl, Raku, Julia, Kotlin, and Wren.

## Connections
- [[BitwiseOperations]] — the algorithm relies on shifts and masking
- [[ModularArithmetic]] — all intermediate values are kept modulo 2^32
- [[ChallengeResponseAuthentication]] — nonce-based password exchange
- [[HomeAutomation]] — the OpenWebNet protocol domain
- [[NetworkProtocols]] — gateway message framing

## Contradictions
- None — reference task page.
