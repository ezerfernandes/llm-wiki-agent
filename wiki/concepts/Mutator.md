---
title: "Mutator"
type: concept
tags: [fuzzing, testing, mutation-fuzzing, string-manipulation, python]
sources: [fuzzingbook-05-mutation-fuzzer, fuzzingbook-06-greybox-fuzzer, fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# Mutator

A **mutator** is the component of a [[MutationBasedFuzzing|mutation-based fuzzer]] that applies a *mutation* — a small string (or byte) manipulation — to an existing input. A single mutation typically inserts, deletes, or alters one character/byte, keeping the result close enough to the original [[SeedInput|seed]] that it tends to remain valid while still probing new behavior. Mutators are the atomic operators a fuzzer chains and stacks; the quality and mix of mutation operators is a major lever on a fuzzer's effectiveness (the [[AFL]] author's writing on which byte-level operators "work" is referenced as further reading).

## From The Fuzzing Book — Mutation-Based Fuzzing
[[fuzzingbook-05-mutation-fuzzer|Ch 5]] defines three primitive mutation operators and a dispatcher:
- `delete_random_character(s)` — removes the character at a random position (`s[:pos] + s[pos+1:]`); returns `s` unchanged if empty.
- `insert_random_character(s)` — inserts a random printable ASCII character (`chr(random.randrange(32, 127))`) at a random position.
- `flip_random_character(s)` — flips one random bit of a random character via XOR (`ord(c) ^ (1 << random.randint(0, 6))`).
- `mutate(s)` — the mutator proper: `random.choice([...])` picks one operator uniformly and applies it.

In the `MutationFuzzer` class this becomes a `mutate()` *method* (so subclasses can extend it), and `create_candidate()` stacks between `min_mutations` and `max_mutations` calls to it on a population member. Stacking many mutations increases input variety but also the chance of invalidity — motivating the coverage guidance of [[MutationCoverageFuzzer|`MutationCoverageFuzzer`]].

## From The Fuzzing Book — Greybox Fuzzing
[[fuzzingbook-06-greybox-fuzzer|Ch 6]] repackages the three primitive operators into a standalone `Mutator` class (with `mutate()` "overloadable in subclasses") and subclasses it to widen or narrow the fuzzer's search space: `DictMutator(dictionary)` adds `insert_from_dictionary` (inject a keyword from a supplied dictionary), and `MazeMutator` adds `append_from_dictionary` and `delete_last_character` to suit the maze target. The chapter's lesson — "the mutator defines the fuzzer's search space" — frames custom mutators as the way to raise the valid-input ratio, pointing toward the grammar-based mutators of [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]].

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] subclasses `Mutator` to make mutation *structure-aware*. It re-presents `DictMutator` ([[DictionaryMutation|keyword insertion]], now for HTML) and adds two tree-level mutators that take an [[EarleyParser|`EarleyParser`]]: `FragmentMutator` ([[FragmentBasedFuzzing|swap/delete parsed subtrees]] of the same grammar symbol) and its subclass `RegionMutator` ([[RegionMutation|swap/delete byte regions]] derived even from unparsable seeds). These tree mutators stack alongside a plain byte-level `Mutator` inside [[GrammarAwareGreyboxFuzzing|`GreyboxGrammarFuzzer`]] — the concrete payoff of "the mutator defines the fuzzer's search space."

## Connections
- [[MutationBasedFuzzing]] — the technique a mutator implements.
- [[DictionaryMutation]] / [[FragmentBasedFuzzing]] / [[RegionMutation]] — Ch 15's structure-aware `Mutator` subclasses.
- [[GreyboxFuzzing]] — Ch 6 subclasses `Mutator` (`DictMutator`/`MazeMutator`) to shape the search space.
- [[SeedInput]] — the input a mutator perturbs.
- [[MutationCoverageFuzzer]] — chains mutators and keeps coverage-improving results.
- [[AFL]] — real-world fuzzer whose mutation-operator design is cited as further reading.
- [[Fuzzing]] — mutators are core to the mutation family of fuzzers.
- [[fuzzingbook-05-mutation-fuzzer|Ch 5]] — where these operators are defined.

## Sources
- [[fuzzingbook-05-mutation-fuzzer]] — *The Fuzzing Book* Ch 5, "Mutation-Based Fuzzing."
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing" (`Mutator`/`DictMutator`/`MazeMutator` classes).
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars" (structure-aware `Mutator` subclasses: `DictMutator`/`FragmentMutator`/`RegionMutator`).
