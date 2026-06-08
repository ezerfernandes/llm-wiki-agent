---
title: "Snake (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, game-loop, real-time-input]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Snake
---

## Summary
The task asks the programmer to implement a variant of the classic Snake arcade game in any interactive environment. A single player steers a growing line (the snake) to run its head into randomly placed food items; each item eaten lengthens the snake and spawns a new item elsewhere, and the game ends when the snake collides with itself. The core insight is managing a real-time game loop with state (the snake's body as an ordered sequence of coordinates) and non-blocking directional input.

## Task Requirements
- Implement the game in an interactive environment so a sole player can control the snake.
- The player eats items by running the snake's head into them.
- Each item eaten makes the snake longer.
- After an item is eaten, a new item is randomly generated elsewhere on the plane.
- The game ends when the snake attempts to eat itself (self-collision).

## Language Coverage
29 languages implement this task, spanning systems languages, scripting languages, functional languages, and shell. Representative implementations include Ada, C, C++, Rust, Go, Java, JavaScript, Python, Haskell, Lua, and Perl.

## Connections
- [[GameLoop]] — the central update/render cycle driving real-time play
- [[NonBlockingInput]] — reading directional keys without halting the loop
- [[QueueDataStructure]] — modeling the snake body as a head-push / tail-pop sequence
- [[CollisionDetection]] — detecting head-vs-body and head-vs-food overlaps
- [[RandomNumberGeneration]] — placing new food items at random free cells

## Contradictions
- None — reference task page.
