---
title: "PythonFuzzer"
type: concept
tags: [fuzzing, compiler-testing, python, ast, grammar-based-fuzzing, constraints, program-generation]
sources: [fuzzingbook-26-python-fuzzer-testing-compilers]
last_updated: 2026-06-06
---

# PythonFuzzer

**`PythonFuzzer`** is the class/approach introduced in [[fuzzingbook-26-python-fuzzer-testing-compilers|Ch 26 of *The Fuzzing Book*]] for producing arbitrary **Python code** to test a compiler/interpreter ([[CompilerTesting|compiler testing]]). It is a thin subclass of [[ISLa|`ISLaSolver`]] that drives `PYTHON_AST_GRAMMAR` — a grammar over **[[AbstractSyntaxTree|abstract syntax tree]]** constructor expressions rather than concrete Python source — and converts each solution into runnable code.

## Definition and API
```python
class PythonFuzzer(ISLaSolver):
    def __init__(self, start_symbol=None, *, grammar=None,
                 constraint=None, **kw_params): ...
    def fuzz(self) -> str: ...   # eval(str(self.solve())) → fix_missing_locations → ast.unparse
```
- **`start_symbol`** — which AST element to generate; defaults to `<FunctionDef>`. Any of the ~90 nonterminals in `PYTHON_AST_GRAMMAR` works (`<While>`, `<Module>`, `<Call>`, `<Compare>`, …), their names mirroring the Python `ast` module.
- **`grammar`** — defaults to `PYTHON_AST_GRAMMAR` (the chapter's [[EBNF]] AST grammar); converted internally with `convert_ebnf_grammar()`.
- **`constraint`** — an optional [[ISLa]] constraint string forwarded to the solver superclass.
- **`fuzz()`** — solves the grammar to an AST-string, `eval()`s it to a real `ast` tree, calls `ast.fix_missing_locations()`, and `ast.unparse()`s it to a Python source string.

Because it inherits from `ISLaSolver`, it also exposes `solve()`, `check()`, `parse()`, and `mutate()` — the latter two enabling code mutation and [[EvolutionaryFuzzing|evolutionary fuzzing]].

## How output is steered
The chapter shows two complementary ways to shape generated code:
- **Edit the grammar** — `extend_grammar()` to override a rule (e.g. force `decorator_list=[]`), then `trim_grammar()` to drop now-orphaned rules and `is_valid_grammar()` to validate.
- **Add ISLa constraints** — e.g. `str.len(<id>) = 10`; `count(def, "<stmt>", "3")` (exactly three statements); `exists <integer> x: (inside(x, <nonempty_stmt_list>) and str.to.int(x) > 1000)` (a large literal in the body); `<FunctionDef>..<expr_list> = "[]"`. Constraints are the more elegant, less grammar-coupled option.

## Caveats
Generated programs are valid only *syntactically* — very few are semantically meaningful, and many raise `TypeError` at runtime (`set() * set()`). The chapter warns explicitly against blindly executing them, since the fuzzer could synthesize destructive calls like `os.remove("/")`. Achieving full type-correctness via ISLa constraints is possible in principle but would take hundreds-to-thousands of rules.

## Connections
- [[CompilerTesting]] — the technique `PythonFuzzer` instantiates.
- [[ISLa]] — its superclass (`ISLaSolver`) and the source of constraints, `parse()`, and `mutate()`.
- [[AbstractSyntaxTree]] — `PYTHON_AST_GRAMMAR` is a grammar of AST constructor calls; `fuzz()` round-trips through `ast.unparse`.
- [[EBNF]] / [[Grammar]] / [[GrammarBasedFuzzing]] — the grammar machinery it drives.
- [[EvolutionaryFuzzing]] — built on top of `PythonFuzzer`/`ISLaSolver.mutate()` and [[Coverage|coverage]].
- [[CSmith]] — the C-compiler analogue and prior art.
- [[CPython]] — the interpreter the produced code targets.
- [[PythonLanguage]] — the language whose `ast`/`compile`/`exec` infrastructure makes the approach feasible.

## Sources
- [[fuzzingbook-26-python-fuzzer-testing-compilers]] — *The Fuzzing Book* Ch 26, "Testing Compilers (Python Fuzzer)."
