---
title: "Play recorded sounds (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, audio, multimedia]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Play_recorded_sounds
---

## Summary
This task asks the programmer to load at least two prerecorded sound files and demonstrate the playback capabilities of the chosen audio library, API, or platform. Beyond simple playback, it probes the breadth of a sound system's feature set — concurrent mixing, looping, volume control, and event timing. The key emphasis is documentation: each implementation should describe the supported audio formats and assess suitability for game sound effects versus music playback.

## Task Requirements
- Load at least two prerecorded sounds.
- Demonstrate as many of these features as possible: playing sounds individually and simultaneously; stopping before the end of a sound; glitch-free looping; per-sound volume control; stereo or 3D positional mixing; triggering actions at marked times within a sound.
- Describe the supported audio formats briefly.
- Describe suitability for game sound effects (low-latency start, resource efficiency, many simultaneous sounds).
- Describe suitability for playing music (long duration).
- Categorize examples primarily by the audio facility used (library/API/program/platform) rather than the incidental language.

## Language Coverage
34 languages implement this task, reflecting broad coverage across both high-level scripting and low-level platforms — including retro assembly targets that drive hardware sound chips directly. Representative implementations include C, C#, Java, Python, Go, Swift, Ruby, Racket, Tcl, BBC BASIC, and 68000/Z80 Assembly.

## Connections
- [[AudioPlayback]] — the core capability being exercised
- [[DigitalSignalProcessing]] — mixing, volume scaling, and positional audio
- [[ConcurrentProgramming]] — playing multiple sounds simultaneously
- [[EventDrivenProgramming]] — performing actions at marked times in the sound
- [[MultimediaProgramming]] — the broader domain of temporal media handling

## Contradictions
- None — reference task page.
