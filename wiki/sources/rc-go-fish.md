---
title: "Go Fish (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, card-game, game-ai]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Go_Fish
---

## Summary
Implement the card game Go Fish so a human can play against a computer opponent. Each player starts with nine cards and, on their turn, asks the opponent for a rank they already hold; matching cards are handed over (and the turn continues) while a miss forces a draw and ends the turn. Completing a *book* (all four cards of a rank) removes it from the hand, and the player with the most books once every book is complete wins. The notable wrinkle is that the AI must use at least some strategy rather than picking legal moves entirely at random.

## Task Requirements
- Deal nine cards to each player at the start.
- A player may only ask for a rank they already hold at least one card of.
- If the opponent holds cards of the asked rank, they surrender all of them and the asker goes again; otherwise the asker draws one card and the turn ends.
- Track and remove *books* (all four cards of a rank) when completed.
- If a player's hand empties, they immediately draw a new card while the deck has any.
- End the game when all books are complete; most books wins.
- The computer opponent must apply some strategy, not purely random legal moves.

## Language Coverage
35 languages implement this task, showing broad coverage across systems, functional, and scripting languages. Representative examples include C, C++, Rust, Go, Java, Haskell, OCaml, Python, Ruby, and Wren.

## Connections
- [[GoFish]] — the card game being simulated
- [[PlayingCards]] — deck/card modeling reused from the related task
- [[GameAI]] — the required opponent strategy
- [[FisherYatesShuffle]] — typical technique for shuffling the deck
- [[StateMachine]] — turn and game-state management

## Contradictions
- None — reference task page.
