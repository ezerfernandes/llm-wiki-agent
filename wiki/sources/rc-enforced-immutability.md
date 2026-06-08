---
title: "Enforced immutability (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-features, type-systems]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Enforced_immutability
---

## Summary
This Rosetta Code task asks the programmer to demonstrate whatever mechanisms a language provides to prevent values from being modified, or to create objects that cannot be changed after construction. The key insight is that languages enforce immutability in very different ways — from compile-time keywords (`const`, `final`, `readonly`) and pure functional defaults to runtime freezing, copy-on-write, and assembly-level read-only memory — so the task surveys the spectrum of how mutation is forbidden.

## Task Requirements
- Show any means the language has to prevent modification of values.
- Alternatively (or additionally), show how to create objects that cannot be modified after they are created.

## Language Coverage
82 languages implement this task, spanning compiled, interpreted, functional, and assembly tiers. Representative entries include Ada, C, C++, C#, Java, Rust, Haskell, Clojure, Python, JavaScript, Erlang, and Scala, illustrating approaches from `const`/`final` declarations to immutable-by-default functional data and explicit object freezing.

## Connections
- [[Immutability]] — the central property the task enforces
- [[ConstCorrectness]] — keyword-based modification prevention (`const`, `final`, `readonly`)
- [[TypeSystems]] — many languages encode immutability at the type level
- [[FunctionalProgramming]] — languages where immutable values are the default
- [[DefensiveCopying]] — a runtime alternative to true enforced immutability

## Contradictions
- None — reference task page.
