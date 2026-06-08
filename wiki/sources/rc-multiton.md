---
title: "Multiton (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, design-patterns]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Multiton
---

## Summary
This Rosetta Code task asks the programmer to implement the multiton pattern, a generalization of the singleton pattern. Where a singleton permits exactly one instance of a class, a multiton manages a controlled set of named instances through a key-to-instance map, returning the existing instance for a given key or creating it lazily on first request. The key insight is that the map (keyed by some identifier) gates instance creation so each key yields one and only one shared instance.

## Task Requirements
- Implement a basic multiton class or equivalent structure and demonstrate that it works as intended.
- If the language is not object-oriented, emulate a multiton as closely as possible with available tools.
- Optionally, if the language supports multithreading, provide a thread-safe variant.

## Language Coverage
13 languages implement this task, a modest set reflecting that the pattern is primarily an object-oriented idiom. Representative implementations include C++, Java, Python, Rust, F#, Julia, Perl, Raku, Phix, and Wren.

## Connections
- [[SingletonPattern]] — the multiton generalizes the singleton to multiple keyed instances
- [[DesignPatterns]] — multiton is a creational design pattern
- [[LazyInitialization]] — instances are typically created on first access per key
- [[ThreadSafety]] — the optional variant requires synchronized access to the instance map

## Contradictions
- None — reference task page.
