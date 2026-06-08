---
title: "Hunt the Wumpus (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, game, graph-theory, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hunt_the_Wumpus
---

## Summary
The task asks the programmer to build a simple textual implementation of the classic 1973 game Hunt the Wumpus. The cave is a 20-room labyrinth whose connectivity mirrors the vertices of a dodecahedron, so each room links to exactly 3 others. The player navigates this graph hunting a Wumpus while avoiding bats and pits, relying only on proximity hints rather than a visible map. The key insight is modeling the cave as a fixed cubic graph and driving gameplay through neighbor-based sensing.

## Task Requirements
- Model the cave as 20 rooms, each connected to 3 others (dodecahedron vertex graph).
- Place one Wumpus, two giant bats, and two bottomless pits in the cave.
- Give the player 5 arrows; running out before killing the Wumpus loses the game.
- Entering the Wumpus room or a pit loses the game; entering a bat room teleports the player to a random empty room.
- Each turn the player either walks into or shoots into an adjacent room.
- Emit proximity warnings for adjacent hazards: "You smell something terrible nearby." (Wumpus), "You hear a rustling." (bat), "You feel a cold wind blowing from a nearby cavern." (pit).
- Shooting into the Wumpus's room wins; shooting elsewhere gives the Wumpus a 75% chance to wake and move to an adjacent room, eating the player if it lands on them.

## Language Coverage
41 languages implement this task, spanning systems languages, scripting languages, functional languages, and a wide family of BASIC dialects. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Prolog, Perl, Ruby, and Forth.

## Connections
- [[GraphTheory]] — the cave is a fixed graph of rooms and adjacency edges.
- [[Dodecahedron]] — the 20-room topology mirrors the vertices of a dodecahedron, a 3-regular (cubic) graph.
- [[GameSimulation]] — turn-based state machine with player actions and hazard events.
- [[RandomNumberGeneration]] — random hazard placement, bat teleportation, and the 75% Wumpus-wake probability.
- [[StateMachine]] — game loop tracking player position, arrows, and win/lose conditions.

## Contradictions
- None — reference task page.
