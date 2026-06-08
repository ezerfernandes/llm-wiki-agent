---
title: "RCRPG (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, game, state-machine, text-adventure]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/RCRPG
---

## Summary
RCRPG asks the programmer to build a simple interactive text-based dungeon game with room-based navigation across three integer dimensions (x, y, z) and a player inventory. The key design challenge is modeling a 3D grid of rooms plus item mechanics: a sledge is needed to break passages between rooms, a ladder must be left in a room to allow vertical (upward) movement, and the player wins by reaching a goal coordinate. The task is essentially a minimal MUD (multi-user dungeon) reduced to single-player.

## Task Requirements
- Room-based navigation in three integer dimensions (x, y, z).
- A player inventory.
- Three item types: sledge, gold, and ladder.
- A goal coordinate the player must reach to win.
- The sledge is required to create a passage between rooms.
- A ladder must be present in a room (not held) for the player to climb to the room above.
- Gold has no required function.

## Language Coverage
29 languages implement this task, showing broad coverage across functional, imperative, object-oriented, and BASIC-family languages. Representative implementations include C, C++, Java, Python, Ruby, Rust, Go, Haskell, Common Lisp, Clojure, Perl, Raku, and the interactive-fiction language Inform 7.

## Connections
- [[FiniteStateMachine]] — the game world is modeled as states (rooms/inventory) with transitions.
- [[TextAdventure]] — RCRPG is a minimal text-adventure / MUD-style game.
- [[GameLoop]] — interactive command parsing and world-update cycle.
- [[GridNavigation]] — movement over a 3D integer coordinate lattice of rooms.

## Contradictions
- None — reference task page.
