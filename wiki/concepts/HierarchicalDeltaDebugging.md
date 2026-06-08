---
title: "Hierarchical Delta Debugging"
type: concept
tags: [debugging, testing, fuzzing, input-reduction, grammars, parsing, derivation-tree, algorithm]
sources: [fuzzingbook-16-reducer]
last_updated: 2026-06-06
---

# Hierarchical Delta Debugging

**Hierarchical Delta Debugging (HDD)** applies [[DeltaDebugging|delta debugging]] to the *tree structure* of an input rather than its flat character sequence. Introduced by Misherghi & Su (2006), it walks a [[DerivationTree|parse/derivation tree]] level by level and tries to remove or replace whole subtrees, so every candidate it tests remains syntactically well-formed. This overcomes lexical delta debugging's central weakness: on structured inputs (programs, expressions, XML), character-level cuts almost always yield invalid inputs and the reducer stalls. HDD is the algorithm behind [[fuzzingbook-16-reducer|Ch 16]]'s [[GrammarReducer|`GrammarReducer`]].

## In The Fuzzing Book — Ch 16
[[fuzzingbook-16-reducer|Ch 16]] realizes HDD as a [[Grammar|grammar]]-driven tree reduction over the [[EarleyParser|Earley]]-parsed [[DerivationTree|derivation tree]], with two refinements:
- **Subtree replacement** — swap a subtree for a smaller subtree rooted at the same [[Nonterminal|nonterminal]] (generalized tree reduction, Herfert 2017; Perses, Sun 2018).
- **Alternate expansions** — apply a [[ProductionRule|production]] with fewer children, filling holes from the tree (a contribution original to the chapter).
- **Depth-oriented search** — reduce large/shallow subtrees first (`depth` from 0 upward, reset on success), echoing delta debugging's halving intuition and minimizing the number of tests.

Because reductions are structural, the result is both *smaller* and reached in *far fewer tests* than lexical delta debugging on syntactically complex inputs. Related techniques noted in the chapter's background include C-Reduce (Regehr et al. 2012) for C programs and J-Reduce / binary dependency-graph reduction (Kalhauge & Palsberg 2019) for Java.

## Connections
- [[GrammarReducer]] — the concrete `Reducer` implementing HDD in Ch 16.
- [[DeltaDebugging]] / [[DDMin]] — the lexical algorithm HDD lifts onto trees.
- [[DerivationTree]] — the hierarchy HDD operates over.
- [[Parser]] / [[EarleyParser]] — produce the tree HDD reduces (reused from [[fuzzingbook-12-parser|Ch 12]]).
- [[Grammar]] / [[Nonterminal]] / [[ProductionRule]] — define the legal subtree/expansion replacements.
- [[InputReduction]] / [[OneMinimality]] — the problem solved and the minimality notion involved.
- [[fuzzingbook-16-reducer]] — the chapter that implements HDD.

## Sources
- [[fuzzingbook-16-reducer]] — *The Fuzzing Book* Ch 16, "Reducing Failure-Inducing Inputs."
