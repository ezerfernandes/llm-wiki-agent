---
title: "Sleep (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, timing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sleep
---

## Summary
This task asks the programmer to pause the main thread of execution for a caller-supplied duration. The program reads a sleep amount in whatever time unit is most natural to the language (milliseconds, seconds, ticks), prints "Sleeping...", suspends the thread for that interval, prints "Awake!", and ends. The key insight is exercising the language's standard delay/sleep primitive and clearly documenting which time unit it uses.

## Task Requirements
- Input an amount of time to sleep in the language's most natural unit; note the unit in comments or a description.
- Print "Sleeping...".
- Sleep the main thread for the given amount of time.
- Print "Awake!".
- End the program.

## Language Coverage
156 languages implement this task, reflecting that nearly every language exposes a delay primitive in its standard library or runtime. Representative implementations include C, Python, Java, Go, Rust, JavaScript, Ruby, Haskell, Perl, and the UNIX Shell.

## Connections
- [[Concurrency]] — sleeping suspends a thread's execution
- [[ThreadScheduling]] — yields the CPU back to the OS scheduler for the duration
- [[Timing]] — relies on a timer/clock to measure the delay interval
- [[BlockingCall]] — sleep is a canonical blocking operation on the main thread

## Contradictions
- None — reference task page.
