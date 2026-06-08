---
title: "Hashtron inference (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, machine-learning, hashing, bit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hashtron_inference
---

## Summary
The task asks the programmer to implement the inference (forward-evaluation) function of a Hashtron classifier — a hash-based machine-learnable model that can in principle approximate any finite computable function given enough resources. Inference takes an input "command", a desired number of output bits, and a learned program (a list of integer parameter pairs), and produces a deterministic output by repeatedly hashing and folding the input through the program's layers. The key insight is that classification is driven entirely by hashing arithmetic rather than floating-point weights.

## Task Requirements
- Implement an inference function that accepts: an input command, a number of bits to infer, and a program configuration (a list of integer pairs).
- For the test demo: with command `42`, 64 bits, and program `[[0,2]]`, produce the exact 64-bit output `14106184687260844995`.
- For the square-root demo: given a byte `0 <= command < 256`, 4 bits, and the supplied multi-layer program, produce the integer square root of the input byte.
- Output must be deterministic and reproduce the reference values exactly.

## Language Coverage
14 languages implement this task, a relatively small set typical of a newer, specialized task. Representative implementations include ALGOL 68, C++, Go, Java, Julia, Nim, Perl, Phix, PHP, Python, Raku, and Wren.

## Connections
- [[HashFunction]] — inference is built on repeated hashing of the input
- [[BitManipulation]] — output is assembled bit-by-bit, requiring masking and shifting
- [[MachineLearning]] — the program parameters are produced by a learning process
- [[Classifier]] — the Hashtron is a classification model
- [[IntegerSquareRoot]] — the demo program computes integer square roots

## Contradictions
- None — reference task page.
