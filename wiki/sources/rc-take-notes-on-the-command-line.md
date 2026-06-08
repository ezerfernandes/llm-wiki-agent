---
title: "Take notes on the command line (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-io, command-line-arguments, text-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Take_notes_on_the_command_line
---

## Summary
This task asks the programmer to build a small command-line utility named NOTES that maintains a plain-text note file (NOTES.TXT) in the current directory. With no arguments it prints the file's current contents; with arguments it appends a timestamped entry built from the joined arguments. The key insight is exercising the basic interaction of reading command-line arguments, the system clock, and append-mode file I/O.

## Task Requirements
- Invoking NOTES with no command-line arguments displays the current contents of NOTES.TXT if it exists.
- When given arguments, append the current date and time to NOTES.TXT, followed by a newline.
- Then write all the arguments joined with spaces, prefixed with a tab and suffixed with a trailing newline.
- Create NOTES.TXT in the current directory if it does not already exist.

## Language Coverage
90 languages implement this task, giving very broad coverage across systems, scripting, and functional families — including C, C++, Rust, Go, Java, Python, Perl, Ruby, Haskell, and several BASIC and assembly dialects.

## Connections
- [[CommandLineArguments]] — reading argv to decide between display and append modes
- [[FileIO]] — opening, reading, and appending to a text file
- [[AppendMode]] — non-destructive writes that preserve prior notes
- [[DateAndTime]] — formatting the system clock into each entry
- [[TextProcessing]] — joining arguments and assembling the output line

## Contradictions
- None — reference task page.
