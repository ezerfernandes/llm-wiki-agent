---
title: "Ambiguity"
type: concept
tags: [parsing, grammar, ambiguity, context-free-grammar, formal-languages, fuzzing]
sources: [fuzzingbook-12-parser]
last_updated: 2026-06-06
---

# Ambiguity

A grammar is **ambiguous** if some string in its language has **more than one** [[DerivationTree|derivation tree]] (also called more than one *parse*). Ambiguity is a property of the *grammar*, not the language: the same language can often be described by both an ambiguous and an unambiguous grammar. It matters for parsing because an ambiguous grammar forces a parser to decide whether to pick *one* tree (and by what rule) or return *all* of them as a [[ParseForest|parse forest]].

## The Fuzzing Book's treatment
[[fuzzingbook-12-parser|Ch 12]] illustrates ambiguity with the arithmetic grammar `A1_GRAMMAR`: the string `1+2+3` parses two ways — grouping as `[1+2]+3` or `1+[2+3]` — each a valid derivation tree. The chapter contrasts the two strategies parsers use to cope:

- **Ordered choice (resolve to one).** [[ParsingExpressionGrammar|Parsing Expression Grammars]] specify a deterministic resolution order and commit to the first matching choice, so they are *unambiguous by construction* — the [[PackratParsing|`PEGParser`]] yields exactly one tree.
- **Return all parses.** The [[EarleyParser|`EarleyParser`]] embraces ambiguity: its enhanced `extract_trees()` *yields every* derivation tree (via `itertools.product` over alternative parse paths), so the caller sees the full forest.

The chapter's `Background` adds the theoretical edge case: some context-free *languages* are **inherently ambiguous** — no unambiguous CFG exists for them — and such languages therefore have no `LR(1)` grammar. Self-referential rules can even make the set of trees *infinite*, motivating the chapter's lazy tree extractors.

## Connections
- [[ParseForest]] — the structure holding all trees of an ambiguous parse.
- [[DerivationTree]] — the multiple trees an ambiguous string admits.
- [[ParsingExpressionGrammar]] / [[PackratParsing]] — resolve ambiguity via ordered choice (one tree).
- [[EarleyParser]] — returns all parses of an ambiguous grammar.
- [[ContextFreeGrammar]] — ambiguity is a property of CFGs and their grammars.
- [[fuzzingbook-12-parser]] — the chapter that treats ambiguity in parsing.

## Sources
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs."
