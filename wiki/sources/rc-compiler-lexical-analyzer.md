---
title: "Compiler/lexical analyzer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, compilers, lexical-analysis, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Compiler/lexical_analyzer
---

## Summary
This task asks the programmer to build a lexical analyzer (lexer/tokenizer/scanner) for a small C-like programming language, converting a raw character stream into a sequence of typed tokens. The lexer reads from a file or stdin and emits, per token, the starting line, starting column, token name, and (for identifiers, integers, and strings) the token value. The key insight is "longest token matching" — multi-character operators like `<=` and `==` must be greedily matched before their single-character prefixes — and the lexer is deliberately the first stage of a multi-task compiler pipeline (lex | parse | gen | vm).

## Task Requirements
- Recognize operators (`*`, `/`, `%`, `+`, `-`, `<`, `<=`, `>`, `>=`, `==`, `!=`, `!`, `=`, `&&`, `||`), symbols (parens, braces, semicolon, comma), and keywords (`if`, `else`, `while`, `print`, `putc`).
- Tokenize identifiers (`[_a-zA-Z][_a-zA-Z0-9]*`), integer literals, char literals (emitting the ASCII code point), and string literals.
- Support `\n` and `\\` escape sequences only; emit `End_of_input` at stream end.
- Skip whitespace and `/* ... */` comments; require whitespace between alphanumeric-edged tokens (e.g. `ifprint` is one identifier; `42fred` is invalid).
- Treat every `-` as `Op_subtract` (negation is the parser's job).
- Detect errors: empty/multi-character char constants, unknown escapes, EOF in comment, EOF/EOL in string, unrecognized characters, and malformed numbers like `123abc`.
- Output token-per-line with line, column, name, and value; output must feed the Syntax Analyzer task.

## Language Coverage
49 languages implement this task, spanning systems languages, functional languages, scripting languages, and dedicated lexer-generator tools — including C, C++, Rust, Go, Java, Python, Haskell, OCaml, Common Lisp, Perl, and Flex (the classic lex generator).

## Connections
- [[LexicalAnalysis]] — the core process this task implements
- [[FiniteStateMachine]] — the standard model for tokenizer recognition
- [[RegularExpressions]] — token classes are specified via regex patterns
- [[CompilerPipeline]] — this lexer is stage one feeding the parser, code generator, and VM
- [[Tokenization]] — splitting a character stream into meaningful units

## Contradictions
- None — reference task page.
