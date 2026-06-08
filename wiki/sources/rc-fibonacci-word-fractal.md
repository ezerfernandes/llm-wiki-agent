---
title: "Fibonacci word/fractal (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, turtle-graphics, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fibonacci_word/fractal
---

## Summary
This task asks the programmer to render the Fibonacci word as a fractal curve. The infinite Fibonacci word is a binary string built by concatenating successive terms (each term is the previous two joined), and the curve is drawn by walking its characters: move forward for every character, and at each 0 turn left or right depending on whether the position index is even or odd. The key insight is that a simple drawing rule applied to a self-similar symbol sequence produces a self-similar geometric fractal.

## Task Requirements
- Generate the Fibonacci word (binary sequence) to a chosen order.
- For each character, draw a forward segment.
- When the current character is 0: turn left if the index n is even, turn right if n is odd.
- Advance the index and iterate to the end of the word.
- Display the resulting fractal, similar to Fig. 1 of the referenced paper.

## Language Coverage
44 languages implement this task, spanning systems languages, scripting languages, and math/graphics environments. Representative entries include C, C++, Rust, Go, Java, Python, Haskell, Lua, Perl, Raku, and Mathematica/Wolfram Language.

## Connections
- [[FibonacciSequence]] — the recurrence structure underlying the word's construction
- [[FibonacciWord]] — the binary string this fractal visualizes
- [[Fractal]] — the self-similar geometry being produced
- [[TurtleGraphics]] — the forward/turn drawing model used to render the curve
- [[LSystem]] — related rewriting-system approach to generating such curves

## Contradictions
- None — reference task page.
