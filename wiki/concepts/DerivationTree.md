---
title: "Derivation Tree"
type: concept
tags: [grammar, derivation-tree, parse-tree, fuzzing, parsing, data-structure, python]
sources: [fuzzingbook-10-grammar-fuzzer, fuzzingbook-12-parser, fuzzingbook-13-probabilistic-grammar-fuzzer, fuzzingbook-14-generator-grammar-fuzzer, fuzzingbook-15-greybox-grammar-fuzzer, fuzzingbook-16-reducer, fuzzingbook-17-fuzzing-with-constraints, fuzzingbook-18-grammar-miner]
last_updated: 2026-06-06
---

# Derivation Tree

A **derivation tree** (also called a *parse tree* or *concrete syntax tree*) is a tree that records the full structure — and production/derivation history — of a string generated from (or parsed against) a [[ContextFreeGrammar|context-free grammar]]. The **root** is the grammar's start symbol; each interior node is a [[Nonterminal|nonterminal]] whose children are the symbols of the [[ProductionRule|expansion]] chosen for it; **leaves** are [[Terminal|terminals]]. Reading the leaves left-to-right reconstructs the produced string, while the tree above them preserves *which rule produced what* — making the structure trivially comparable and manipulable (e.g. swapping one subtree for another).

In *The Fuzzing Book* a derivation tree is the data structure that makes grammar fuzzing **efficient and controllable**: because the tree always exposes exactly which symbols are still unexpanded, generation proceeds by cheap in-place tree growth rather than the repeated string search-and-replace of the naive `simple_grammar_fuzzer()`.

## Python representation
A node is a pair `(SYMBOL_NAME, CHILDREN)`, captured by the type alias:

```python
DerivationTree = Tuple[str, Optional[List[Any]]]
```

The `CHILDREN` slot encodes the node's status:
- `None` — a **nonterminal placeholder** still awaiting expansion.
- `[]` (empty list) — a **terminal** leaf that will never be expanded further.
- a **non-empty list** of child nodes — an already-expanded nonterminal.

(`Any` should read `DerivationTree`, but Python's static checker cannot handle the recursive type.) Helpers convert a tree back to text: `all_terminals(tree)` concatenates every leaf symbol (rendering still-unexpanded nonterminals verbatim, e.g. `<expr>`), while `tree_to_string(tree)` renders unexpanded nonterminals as the empty string. `display_tree()` visualizes a tree with [[GraphViz]]'s `dot` engine.

## From The Fuzzing Book — Efficient Grammar Fuzzing
[[fuzzingbook-10-grammar-fuzzer|Ch 10]] mints this structure as the engine of the efficient [[GrammarFuzzer|`GrammarFuzzer`]]. Generation starts from `init_tree()` (the singleton `(start_symbol, None)`) and proceeds by `expand_tree_once()`, which finds an unexpanded node and replaces it **in place** — the source of the algorithm's speed. `expansion_to_children()` turns a grammar expansion string into the child-node list (with a special epsilon-expansion case `("", [])`); `possible_expansions()`/`any_possible_expansions()` count/detect remaining `None`-children nodes. Because the tree records the entire derivation, it is the natural medium for the later chapters that *parse* inputs into trees and recombine subtrees ([[fuzzingbook-12-parser|Ch 12]]), assign coverage to expansions ([[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]]), or weight expansions probabilistically ([[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]]). The chapter's Background notes derivation/parse trees are the standard structure compilers build (the *Dragon Book*).

## From The Fuzzing Book — Parsing Inputs
[[fuzzingbook-12-parser|Ch 12]] uses the *same* `DerivationTree` structure as the output of *parsing* — confirming that a parse tree and a generation-time derivation tree are one and the same `(SYMBOL, CHILDREN)` data structure. A [[Parser|`Parser`]] takes a string and a [[ContextFreeGrammar|grammar]] and returns derivation trees; `tree_to_string()` round-trips a parsed tree back to its input (the chapter's pervasive `assert tree_to_string(tree) == mystring`). The [[EarleyParser|Earley parser]] can yield *multiple* derivation trees for an [[Ambiguity|ambiguous]] grammar (a [[ParseForest|parse forest]]), while the [[PackratParsing|PEG parser]] yields a single tree. Once parsed, a tree's subtrees can be swapped/recombined to fuzz — the motivation for the entire chapter — and `prune_tree()`/`coalesce()` post-process leaves into clean terminal strings.

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] uses derivation trees on both sides of the loop. In *generation*, the [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]] expands the tree exactly as the base [[GrammarFuzzer|`GrammarFuzzer`]] does, only weighting `choose_node_expansion()` by `prob`. In *[[GrammarMining|learning]]*, it parses corpus inputs into derivation trees (via the [[EarleyParser|`EarleyParser`]]) and walks them to **count expansions** — `ExpansionCountMiner.add_tree()` recurses over `(symbol, children)` nodes, tallying each by `expansion_key()` — so the same tree structure that *produces* inputs is also what *measures* a sample's expansion frequencies to mine probabilities.

## From The Fuzzing Book — Fuzzing with Generators
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] treats the derivation tree as the substrate that **post-expansion functions traverse and rewrite**. The [[GeneratorGrammarFuzzer|`GeneratorGrammarFuzzer`]]'s `run_post_functions()` recurses over the tree's `(symbol, children)` nodes; `find_expansion()` recovers *which* grammar expansion produced a node's children by matching `exp_string()` against the concatenated child symbols; and `eval_function()` builds a `post` function's arguments from the nonterminal children's `all_terminals()` strings. A `post` repair returns a string/list that `apply_result()` splices back into the children (e.g. copying an XML opening-tag id onto the closing tag), and the [[PGGCFuzzer|`PGGCFuzzer`]] walks the *final* tree with `add_tree_coverage()` to recompute [[GrammarCoverage|coverage]] after discarding rejected expansions — all relying on the tree's record of which rule produced what.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] treats derivation-tree subtrees as the unit of *mutation*. The [[FragmentBasedFuzzing|`FragmentMutator`]] parses each seed into a `DerivationTree`, then recursively walks `(symbol, children)` nodes (`add_fragment()`) to fill a per-symbol **fragment pool**; `swap_fragment()` substitutes a seed subtree with a pool subtree of the *same symbol* and `delete_fragment()` removes one (`recursive_swap`/`recursive_delete`/`count_nodes`), with `tree_to_string()` serializing the mutated tree back to an input. Seeds carry their tree as `SeedWithStructure.structure`. When a seed is only *partially* parsable, the [[RegionMutation|`RegionMutator`]] instead labels byte *regions* with symbols (no full tree needed) — so derivation-tree fragments and parse-table regions are the two granularities at which Ch 15 mutates structure.

## From The Fuzzing Book — Reducing Failure-Inducing Inputs
[[fuzzingbook-16-reducer|Ch 16]] treats the derivation tree as the substrate for *reduction*. Where lexical [[DeltaDebugging|delta debugging]] cuts a flat string, the [[GrammarReducer|`GrammarReducer`]] reduces the *tree* — its [[HierarchicalDeltaDebugging|hierarchical delta debugging]] either replaces a subtree with a smaller subtree of the same root [[Nonterminal|symbol]] (`subtrees_with_symbol()`) or applies an alternate grammar expansion with fewer children (`alternate_reductions()`), reusing helpers `number_of_nodes()`, `max_height()`, and rendering back via `all_terminals()`. Because every reduced candidate is a valid tree, every test is syntactically valid by construction — turning the tree's "which rule produced what" record into the key that makes structure-aware reduction far faster than character-level cuts.

## From The Fuzzing Book — Fuzzing with Constraints
[[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] makes the derivation tree the object that [[ISLa]] constraints reference and that the `ISLaSolver` returns. `solve()` yields a `DerivationTree` (rendered to a string via `str()`/`print()`, or visualized with `display_tree()`); the chapter parses example inputs with the [[EarleyParser|`EarleyParser`]] to show the tree the constraints reason over. ISLa's **element-access operators are tree paths**: `<a>.<b>` selects an *immediate* child node, `<a>..<b>` selects *any* descendant node, and `<a>[n]` selects the *n*-th immediate child of a type (1-indexed). **Quantifiers** (`forall`/`exists`) range over tree nodes in a context, and `solution.filter(lambda n: n.value == "<chars>")` walks the tree by node value — so the same `(symbol, children)` structure that *produces* inputs is what *constraints* are evaluated against.

## From The Fuzzing Book — Mining Input Grammars
[[fuzzingbook-18-grammar-miner|Ch 18]] *builds* a derivation tree from a running program rather than from a grammar. Its `TreeMiner` starts with the whole input as a single `(<start>, [(input, [])])` node, then for each variable that held an input substring it `partition()`s the matching node value into prefix / matched-part / suffix and replaces the matched part with a [[Nonterminal|nonterminal]] node named after the variable (`insert_into_tree()`). The result is exactly the same `(symbol, children)` tree the rest of the book uses — which [[GrammarMiner|`tree_to_grammar()`]] then abstracts (over many inputs) into a recovered [[Grammar|grammar]]. The scope-aware `ScopeTreeMiner` adds a per-node scope tag so fragments are only inserted where they are genuinely in scope.

## Connections
- [[GrammarMiner]] / [[GrammarInference]] — Ch 18's `TreeMiner` assembles a derivation tree from traced input fragments, then abstracts it to a grammar.
- [[ISLa]] / [[InputSpecificationLanguage]] — Ch 17's constraints navigate and quantify over derivation-tree nodes; `solve()` returns a tree.
- [[GrammarReducer]] / [[HierarchicalDeltaDebugging]] — Ch 16 reduces by replacing/shrinking tree subtrees.
- [[GrammarFuzzer]] — the fuzzer that builds and expands derivation trees.
- [[FragmentBasedFuzzing]] / [[RegionMutation]] — Ch 15 mutates by swapping/deleting tree subtrees (fragments) or byte regions.
- [[GeneratorGrammarFuzzer]] — Ch 14's fuzzer whose `post` functions traverse and rewrite the tree (`find_expansion`, `eval_function`, `apply_result`).
- [[GrammarMining]] — counts expansions over parsed derivation trees to learn probabilities.
- [[Parser]] / [[EarleyParser]] / [[PackratParsing]] — produce derivation trees by parsing strings.
- [[ParseForest]] / [[Ambiguity]] — an ambiguous parse yields multiple derivation trees.
- [[ContextFreeGrammar]] / [[Grammar]] — the grammar a tree is a derivation of.
- [[Nonterminal]] / [[Terminal]] — interior nodes vs leaves; `None` vs `[]` children.
- [[ProductionRule]] — each interior node's children are one chosen expansion.
- [[ExpansionCost]] — cost functions decide which expansion grows the tree, used to grow/close it.
- [[GraphViz]] — `display_tree()` renders trees as `dot` graphs.
- [[GrammarBasedFuzzing]] — derivation trees make this technique efficient.
- [[fuzzingbook-10-grammar-fuzzer]] — the chapter that introduces derivation trees for fuzzing.
- [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] — keys each expansion as `SYMBOL -> EXPANSION` (via `expansion_key()` over the tree's children) to track [[GrammarCoverage|grammar coverage]].
- [[fuzzingbook-12-parser|Ch 12]] — builds derivation trees by parsing, then recombines subtrees.

## Sources
- [[fuzzingbook-10-grammar-fuzzer]] — *The Fuzzing Book* Ch 10, "Efficient Grammar Fuzzing."
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs" (derivation trees as parser output).
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing" (counting expansions over parsed trees to mine probabilities).
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators" (post-expansion functions traverse and rewrite the tree).
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars" (subtree fragments as the unit of structure-aware mutation).
- [[fuzzingbook-16-reducer]] — *The Fuzzing Book* Ch 16, "Reducing Failure-Inducing Inputs" (subtree replacement / alternate expansions as the unit of structure-aware reduction).
- [[fuzzingbook-17-fuzzing-with-constraints]] — *The Fuzzing Book* Ch 17, "Fuzzing with Constraints" (ISLa constraints navigate/quantify over derivation-tree nodes; `solve()` returns a tree).
- [[fuzzingbook-18-grammar-miner]] — *The Fuzzing Book* Ch 18, "Mining Input Grammars" (`TreeMiner` assembles a tree from traced input fragments).
