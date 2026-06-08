---
title: "Luhn Algorithm"
type: concept
tags: [checksum, algorithm, credit-card, validation, fuzzing]
sources: [fuzzingbook-14-generator-grammar-fuzzer]
last_updated: 2026-06-06
---

# Luhn Algorithm

The **Luhn algorithm** (also "mod 10" algorithm) is a simple checksum formula used to validate identification numbers — most famously **credit-card numbers**, but also IMEIs and other IDs. It computes a single **check digit** over the preceding digits: doubling every second digit (folding values over 9 by subtracting 9, equivalently summing their digits), summing the result with the remaining digits, and choosing the check digit so the grand total is a multiple of 10. It catches all single-digit errors and most adjacent transpositions, which is why ~9 of 10 *random* 16-digit numbers fail it.

In *The Fuzzing Book* the Luhn checksum is the canonical example of a [[SemanticConstraint|semantic constraint]] — a validity condition that a [[ContextFreeGrammar|context-free grammar]] *cannot* express, because the check digit is an arithmetic function of all the other digits.

## From The Fuzzing Book — Fuzzing with Generators
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] implements the Luhn checksum to motivate and demonstrate [[GeneratorGrammar|generator grammars]]:

```python
def luhn_checksum(s: str) -> int: ...        # Luhn check digit over a digit string
def valid_luhn_checksum(s: str) -> bool: ... # is the last digit the correct check digit?
def fix_luhn_checksum(s: str) -> str: ...    # return s with a corrected check digit
```

These are attached to `CHARGE_GRAMMAR`'s `<credit-card-number>` expansion as `post` functions on the [[GeneratorGrammarFuzzer|`GeneratorGrammarFuzzer`]]. Used as a *filter* (`valid_luhn_checksum`), the fuzzer re-rolls until a valid number appears — costing ~10 attempts each. Used as a *repair* (`fix_luhn_checksum`), each generated number is fixed once and accepted, which is far more efficient. The example shows why post-expansion **repair** is preferable to **filtering** when a cheap constructive fix exists.

## Connections
- [[SemanticConstraint]] — the checksum is the archetypal semantic constraint a CFG can't capture.
- [[GeneratorGrammar]] / [[GeneratorGrammarFuzzer]] — attach `valid_luhn_checksum`/`fix_luhn_checksum` as `post` functions to enforce it.
- [[ContextFreeGrammar]] — cannot express the arithmetic relationship the Luhn check digit requires.
- [[GrammarBasedFuzzing]] — the technique whose syntactic output the Luhn repair makes *acceptable*.
- [[fuzzingbook-14-generator-grammar-fuzzer]] — the chapter that uses it as the running example.

## Sources
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators."
