---
title: "Universal Lambda Machine (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, lambda-calculus, interpreters, binary-encoding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Universal_Lambda_Machine
---

## Summary
The task is to implement an interpreter for the Binary Lambda Calculus (BLC), the "universal machine" of the lambda calculus that can emulate any other machine given its description. BLC encodes lambda terms as binary tokens (`00` for lambda abstraction, `01` for application, `1^n0` for the de Bruijn variable n), and defines an I/O convention where bits and lists are themselves represented as lambda terms. The interpreter parses a binary-encoded term from the start of its input, applies it to the remaining input, and prints the result interpreted as a list of bits or bytes.

## Task Requirements
- Write a BLC interpreter that simulates the universal lambda machine.
- Support bit-mode and/or byte-mode (preferably both), with byte-mode as default and a `-b` flag selecting bit mode.
- Bit-mode: reproduce BLC solutions for Quine, Sieve of Eratosthenes, and 100 doors; a given 342-bit program must output `11010`.
- Byte-mode: reproduce BLC solutions for Hilbert curve and Execute Brainfuck.
- Run the 186-byte `symbolic.Blc` program (from IOCCC 2012) on a given input and reproduce its multi-line normal-form trace output.

## Language Coverage
12 languages implement this task, a relatively small set reflecting its specialized nature, including the source BLC itself and Bruijn. Representative entries: C, Haskell, JavaScript, Julia, Perl, Phix, Prolog, Python, Ruby, and Wren.

## Connections
- [[LambdaCalculus]] — the underlying model of computation being implemented
- [[BinaryLambdaCalculus]] — the binary term encoding and I/O convention defined here
- [[DeBruijnIndex]] — nameless variable representation used by the `1^n0` token
- [[UniversalMachine]] — the theoretical construct (universal Turing machine analogue) this realizes
- [[Interpreters]] — the task is to build a term evaluator/normalizer

## Contradictions
- None — reference task page.
