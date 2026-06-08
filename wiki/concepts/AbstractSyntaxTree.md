---
title: "Abstract Syntax Tree"
type: concept
tags: [compilers, program-analysis, python, ast, program-transformation, software-engineering]
sources: [fuzzingbook-08-mutation-analysis, fuzzingbook-12-parser, fuzzingbook-26-python-fuzzer-testing-compilers]
last_updated: 2026-06-06
---

# Abstract Syntax Tree

An **abstract syntax tree (AST)** is the tree-structured internal representation of a program's syntax that compilers and interpreters build after parsing source text. Each node is a syntactic construct — a function definition, an `if`, a comparison, a binary operation, a literal — and child nodes capture sub-structure. Working on the AST rather than raw text lets tools *analyze and transform* programs structurally (visiting/rewriting node types) and then **unparse** the result back to source.

## From The Fuzzing Book — Mutation Analysis
[[fuzzingbook-08-mutation-analysis|Ch 8]] uses Python's built-in `ast` module as the substrate for [[MutationAnalysis|mutation analysis]]. The pipeline is: `inspect.getsource(fn)` to recover a function's text → `ast.parse(src)` to build the tree → `ast.unparse(ast)` to normalize it (parse+unparse once so later `diff`s aren't derailed by whitespace/comments) → transform → `ast.unparse()` back to runnable source. For `triangle()`, the chapter shows the tree is a `FunctionDef` whose body holds nested `If` nodes containing `Compare`, `Name`, `Return`, and `Str` nodes, inspected via `ast.dump(tree, indent=4)` (and graphically via `showast`). [[MutationOperator|Mutation operators]] are implemented as `ast.NodeTransformer` subclasses: `StmtDeletionMutator` replaces statement nodes with `ast.Pass()`, and the `BinOpMutator` (Exercise 1) rewrites a `BinOp` node's `op` attribute (`Add`/`Sub`/`Mult`/`Div`). Exercise 3 notes that when source is unavailable one could instead mutate Python *bytecode*.

## From The Fuzzing Book — Parsing Inputs
[[fuzzingbook-12-parser|Ch 12]] contrasts two ways to turn a string into a tree. The *traditional* route runs a **lexer/tokenizer** first to emit a shallow [[DerivationTree|derivation tree]] that maps directly to an AST. The chapter deliberately takes the *other* route: it [[Parser|parses]] against a grammar with full syntactic detail and then post-processes with `prune_tree()`/`coalesce()` — collapsing token nodes into leaf strings — avoiding any artificial lexing/parsing split. So while the book's [[EarleyParser|Earley]] and [[PackratParsing|PEG]] parsers produce *derivation* (concrete-syntax) trees rather than ASTs, the AST is the natural compiler-stage refinement of that output.

## From The Fuzzing Book — Testing Compilers (Python Fuzzer)
[[fuzzingbook-26-python-fuzzer-testing-compilers|Ch 26]] turns the AST from an *analysis* substrate (Ch 8) into a *generation* substrate for [[CompilerTesting|compiler testing]]. Its key move is to write a [[Grammar|grammar]] (`PYTHON_AST_GRAMMAR`) not over concrete Python *source* — which would have to model whitespace, comments, continuation lines, and non-context-free indentation — but over **AST constructor calls** themselves (e.g. `'<BinOp>': ['BinOp(left=<expr>, op=<operator>, right=<expr>)']`). This works because an `ast.dump(tree)` string is directly `eval()`-able back into a tree, so a single grammar can both *produce* and *parse* ASTs. The [[PythonFuzzer]] then closes the loop: `eval(str(solve()))` → `ast.fix_missing_locations()` → `ast.unparse()` to recover runnable source (or `compile()`/`exec()` to run it). Generated trees are syntactically valid but rarely semantically so; the chapter also mutates parsed ASTs (via [[ISLa]] [[DerivationTree|derivation trees]]) for [[EvolutionaryFuzzing|evolutionary fuzzing]]. AST shapes are version-dependent (optional fields added in Python 3.12/3.13).

## Connections
- [[Parser]] / [[EarleyParser]] / [[PackratParsing]] — produce derivation trees; the lexer route maps to an AST.
- [[CompilerTesting]] / [[PythonFuzzer]] — Ch 26 grammars over AST constructor calls to generate and mutate programs.
- [[DerivationTree]] — the concrete-syntax tree a parser builds; an AST abstracts away from it.
- [[MutationOperator]] — implemented as `ast.NodeTransformer` visitors over AST nodes.
- [[Mutant]] / [[MutationAnalysis]] — produced by transforming and re-emitting the AST.
- [[SemanticParsing]] — parsing maps text to a structured (tree/meaning) representation.
- [[Coverage]] — AST/line info underlies which constructs a test exercises.

## Sources
- [[fuzzingbook-08-mutation-analysis]] — *The Fuzzing Book* Ch 8, "Mutation Analysis."
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs" (lexing vs. tree-pruning to build trees).
- [[fuzzingbook-26-python-fuzzer-testing-compilers]] — *The Fuzzing Book* Ch 26, "Testing Compilers" (grammar over AST constructor calls to generate/mutate Python).
