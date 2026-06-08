---
title: "Generator Grammar"
type: concept
tags: [fuzzing, grammar, generators, semantic-constraints, context-free-grammar, testing, syntactic-fuzzing, python]
sources: [fuzzingbook-14-generator-grammar-fuzzer, fuzzingbook-17-fuzzing-with-constraints, fuzzingbook-24-api-fuzzer]
last_updated: 2026-06-06
---

# Generator Grammar

A **generator grammar** is a [[ContextFreeGrammar|context-free grammar]] in which individual [[ProductionRule|expansion alternatives]] carry **Python functions** that are executed during [[DerivationTree|derivation-tree]] expansion to *generate*, *check*, or *repair* the produced element. It is the mechanism *The Fuzzing Book* introduces to attach **programmatic computation** to grammar production — bringing "the best of grammar generation and programming" together — so a fuzzer can satisfy [[SemanticConstraint|semantic constraints]] (checksums, value ranges, matched tags, define/use dependencies) that a pure context-free grammar cannot express.

The functions are attached with the same `opts()` annotation slot as in [[fuzzingbook-09-grammars|Ch 9]] (and `prob` in [[ProbabilisticGrammar|Ch 13]]), so the grammar stays ordinary Python data and ordinary fuzzers simply ignore the new keys:

```python
(S, opts(pre=F))    # F runs BEFORE expansion; its result replaces the expansion
(S, opts(post=F))   # F runs AFTER expansion; checks (False → retry) or repairs (string/list → replace)
(S, opts(order=[…]))  # ranks the nonterminals in S for a controlled expansion order
```

## Pre vs. post functions
- **`pre`** runs *before* the expansion of `S` and its return value *replaces* the expansion. A *string* replaces the whole expansion; a *list* `[x_1…x_n]` replaces the i-th nonterminal child with `x_i` (a `None` element leaves that child unchanged); `None`/booleans are ignored; other types are `repr()`'d. A `pre` function may be a [[Generator|Python generator]] (using `yield`, or `range()`/a comprehension), in which case successive `fuzz()` calls draw successive values while preserving state. Example: `high_charge()` produces an in-range dollar amount; `pick_area_code()` chooses a value from a programmatic list.
- **`post`** runs *after* expansion, receiving the expanded terminal strings of the nonterminal children as arguments. It serves either as a **constraint/filter** — returning `True`/`False`, where `False` forces a new expansion — or as a **repair**, returning a string or list that replaces the expansion. Example: `valid_luhn_checksum` (filter) vs. `fix_luhn_checksum` (repair), or the XML repair `lambda id1, content, id2: [None, None, id1]` that copies the opening tag's id onto the closing tag.

## Ordering
`opts(order=[…])` matters only when functions have **side effects**: it assigns each nonterminal in the expansion a rank so expansions (and their associated function calls) fire in a controlled sequence — e.g. defining a variable (`post=define_id`, `order=[2,1]`) only *after* its defining expression has been produced.

## From The Fuzzing Book — Fuzzing with Generators
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] mints the generator grammar as a *backward-compatible* extension of the [[Grammar|`Grammar`]] data structure: the same `(string, opts(...))` expansion form now carries `pre`, `post`, and `order` keys, interpreted only by the [[GeneratorGrammarFuzzer|`GeneratorGrammarFuzzer`]] (a plain [[GrammarFuzzer|`GrammarFuzzer`]] warns and ignores them). The running grammars are `CHARGE_GRAMMAR` (a [[LuhnAlgorithm|Luhn]]-valid credit-card charge), `XML_GRAMMAR` (matched tags), `negative_expr_grammar`/`binary_expr_grammar` (`eval()`-based constraints), and `CONSTRAINED_VAR_GRAMMAR` (a symbol-table def/use grammar). The chapter positions generator grammars as the *imperative* route to [[SemanticConstraint|semantic validity]], complementary to the *declarative* constraints of [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] (ISLa).

## From The Fuzzing Book — Fuzzing with Constraints
[[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] explicitly frames the generator grammar as the **imperative** alternative to its own **declarative** [[ISLa]] constraints. Where a generator grammar attaches Python `pre`/`post` *code* to expansions, ISLa declares the same [[SemanticConstraint|semantic properties]] as a grammar-plus-constraint string and has an [[SMTSolver|SMT solver]] satisfy them. The chapter argues the declarative form wins on portability (language-independent vs. Python-bound), composition (a solver combines multiple constraints automatically, vs. hand-coding a generation strategy), and bidirectionality (one constraint both *produces* and *checks* inputs, whereas attached code does only one). The XML matched-tag and define-before-use examples appear in *both* chapters — repaired by `post` code here, declared as constraints there — making the two pages direct counterparts on [[ConstraintBasedFuzzing|constraint-based fuzzing]].

## From The Fuzzing Book — Fuzzing APIs
[[fuzzingbook-24-api-fuzzer|Ch 24]] puts generator grammars to work for [[APIFuzzing|API fuzzing]] in two ways. A `post` function **synthesizes [[TestOracle|oracles]]** by enforcing a value equality a context-free grammar cannot — `URLPARSE_ORACLE_GRAMMAR` makes the input URL and the URL inside `assert urlparse('<url>').geturl() == '<url>'` identical via `opts(post=lambda url_1, url_2: [None, url_1])`. A `pre` function **bounds argument values** — `int_grammar_with_range(start, end)` and `float_grammar_with_range(start, end)` attach `opts(pre=lambda: random.randint(start, end))` (resp. `random.random()`) with `set_opts(...)`, overriding the expansion with an in-range value. The chapter's argument grammars are produced with `ProbabilisticGeneratorGrammarFuzzer`, which honors both the `prob` and the `pre`/`post` annotations at once.

## Connections
- [[ISLa]] / [[InputSpecificationLanguage]] / [[ConstraintBasedFuzzing]] — Ch 17's declarative counterpart to generator grammars.
- [[APIFuzzing]] / [[TestOracle]] — Ch 24 uses `post` to synthesize call oracles and `pre` to bound generated arguments.
- [[GeneratorGrammarFuzzer]] — the fuzzer that interprets `pre`/`post`/`order` annotations.
- [[SemanticConstraint]] — the validity-beyond-syntax property generator grammars enforce.
- [[Grammar]] — the underlying data structure; reuses the `opts()` annotation slot.
- [[ProbabilisticGrammar]] — sibling annotation form (`prob`); both ride the same `opts()` mechanism and compose in [[PGGCFuzzer|`PGGCFuzzer`]].
- [[DerivationTree]] — `post` functions traverse and rewrite the tree.
- [[Generator]] — Python `yield`-based generators usable as `pre` functions (note: that page covers GAN generators, a different sense).
- [[ContextFreeGrammar]] — the formalism whose context-free limitation generator grammars overcome.
- [[GrammarBasedFuzzing]] — the technique this concept augments with computation.
- [[LuhnAlgorithm]] — the checksum used in the canonical `post`-repair example.
- [[fuzzingbook-09-grammars|Ch 9]] — supplies the `opts()`/`extend_grammar()` mechanism.
- [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] — the declarative-constraints alternative.
- [[fuzzingbook-14-generator-grammar-fuzzer]] — the chapter that introduces generator grammars.

## Sources
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators."
- [[fuzzingbook-17-fuzzing-with-constraints]] — *The Fuzzing Book* Ch 17, "Fuzzing with Constraints" (the declarative, ISLa-based counterpart to generator grammars).
- [[fuzzingbook-24-api-fuzzer]] — *The Fuzzing Book* Ch 24, "Fuzzing APIs" (`post` for oracle synthesis, `pre` for range-bounded arguments).
