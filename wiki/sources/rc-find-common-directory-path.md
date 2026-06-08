---
title: "Find common directory path (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Find_common_directory_path
---

## Summary
The task asks for a routine that takes a set of directory-path strings plus a single separator character and returns the longest path prefix common to all of them. The key insight is that the answer must be a whole-component common prefix, not merely the longest common character substring: for `/home/user1/tmp/coverage/test`, `/home/user1/tmp/covert/operator`, and `/home/user1/tmp/coven/members` the correct result is `/home/user1/tmp`, not `/home/user1/tmp/cove`.

## Task Requirements
- Accept a set of strings representing directory paths and a single-character directory separator.
- Return the part of the directory tree common to all input paths.
- Compare path components delimited by the separator, not raw characters.
- Test with `/` as separator against the three given `/home/user1/tmp/...` paths, yielding `/home/user1/tmp`.
- If the language provides a built-in for this function, mention it as part of the solution.

## Language Coverage
95 languages implement this task, showing very broad coverage across scripting, functional, systems, and BASIC-family languages. Representative implementations include Python, Perl, Raku, Haskell, Go, Rust, C, C++, Java, JavaScript, Ruby, and Clojure.

## Connections
- [[StringProcessing]] — the core operation splits and compares delimited path strings.
- [[LongestCommonPrefix]] — the underlying algorithm, applied at component granularity rather than character granularity.
- [[FileSystemPaths]] — directory-tree semantics distinguish this from a plain substring match.
- [[Tokenization]] — paths are tokenized on the separator before comparison.

## Contradictions
- None — reference task page.
