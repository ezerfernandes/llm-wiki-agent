---
title: "Dive into Systems — Ch 1.3 Conditionals and Loops"
type: source
tags: [book, dive-into-systems, c-language, control-flow]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C1-C_intro/conditionals.html
---

## Summary

Section 1.3 of [[DiveIntoSystems]] (third content section of Ch 1 *By the C, the Beautiful C*) introduces [[CLanguage|C]]'s [[ControlFlow|control-flow]] machinery — [[IfStatement|`if`]] / [[ElseStatement|`else`]] / `else if` branches, the [[SwitchStatement|`switch` statement]], and the three loop forms [[WhileLoop|`while`]] / [[DoWhileLoop|`do`–`while`]] / [[ForLoop|`for`]] — with [[BreakStatement|`break`]] and [[ContinueStatement|`continue`]] as the structured-jump pair. The chapter cross-walks against [[Python]]: same semantics, different surface — parentheses around the test, `{ }` not indentation, and a [[CBooleanExpression|Boolean expression]] vocabulary that is **integer-valued** because C has no dedicated boolean type (`0` is false, **any nonzero value** is true). Operators come in two families: [[RelationalOperator|relational]] (`==` `!=` `<` `<=` `>` `>=`) and [[LogicalOperator|logical]] (`!` `&&` `||`), with [[ShortCircuitEvaluation|short-circuit evaluation]] for `&&` and `||`. The chapter's most C-specific move is the **general-form [[ForLoop|`for` loop]]** — `for (init; cond; step) { ... }` — which is *equivalent in power* to [[WhileLoop|`while`]] (unlike [[Python]]'s sequence-iteration `for`), and the resulting design rule: **[[DefiniteIteration|definite iterations]] → `for`, [[IndefiniteIteration|indefinite iterations]] → `while`**.

## Key Claims

- **C has no dedicated boolean type.** In every conditional context, **`0` evaluates to false, any nonzero value (positive or negative) evaluates to true** — `if (x)` is valid C and tests `x != 0`. [[CBooleanExpression|Boolean expressions]] are just integer-valued expressions.
- **The conditional family is three-shaped**: one-way [[IfStatement|`if`]], two-way [[IfStatement|`if`]]/[[ElseStatement|`else`]], multi-way `if`/`else if`/.../[[ElseStatement|`else`]] — the final `else` is always optional.
- **Syntax non-negotiables (vs [[Python]])**: the test sits in **parentheses** — `if (x > 0)` — and the body sits in **`{ }` blocks**, not indented blocks. Indentation is *style*, not semantics, in [[CLanguage|C]].
- **[[RelationalOperator|Relational operators]]** (`==`, `!=`, `<`, `<=`, `>`, `>=`) compare two operands and return an integer-valued result (`0` or `1`). The single-`=`-vs-double-`==` mix-up — `if (x = 0)` assigns then tests, `if (x == 0)` compares — is the chapter's headline footgun.
- **[[LogicalOperator|Logical operators]]** `!` (NOT, unary), `&&` (AND, binary), `||` (OR, binary) combine boolean expressions. **[[ShortCircuitEvaluation|Short-circuit evaluation]]** halts the moment the result is determined: in `A && B`, `B` is skipped if `A` is false; in `A || B`, `B` is skipped if `A` is true. This makes guard idioms like `if (p != NULL && *p == 0)` legal.
- **The [[SwitchStatement|`switch` statement]]** dispatches on an integer-valued expression to `case label:` arms. **[[CaseLabel|`case` labels must be compile-time integer constants]]** (no ranges, no strings, no variables). Without an explicit [[BreakStatement|`break`]], execution **falls through** to the next case — a feature, not a bug, but a frequent source of accidents. A final `default:` handles unmatched values.
- **[[WhileLoop|`while` loop]]** checks the condition **first**; the body may execute **zero times** if the test starts false. Syntax: `while (cond) { body }`.
- **[[DoWhileLoop|`do`–`while` loop]]** checks the condition **after** the body, so **the body always executes at least once**. Syntax: `do { body } while (cond);` — note the trailing semicolon, unlike [[WhileLoop|`while`]].
- **[[ForLoop|`for` loop]]** is a **general looping construct** in C, *not* sequence iteration as in [[Python]]. Three semicolon-separated clauses — `for (init; cond; step) { body }` — execute as: (1) run *init* once; (2) test *cond*, exit if false; (3) run *body*; (4) run *step*; (5) goto (2). Any clause may be empty; `for (;;) { ... }` is the idiomatic infinite loop.
- **[[ForLoop|`for`]] ≡ [[WhileLoop|`while`]] in expressive power.** Any `while` translates mechanically to a `for` and vice versa. Design rule: use **`for` for [[DefiniteIteration|definite iteration]]** (known iteration count / range), **`while` for [[IndefiniteIteration|indefinite iteration]]** (loop until a condition emerges).
- **The [[CommaOperator|comma operator]]** lets [[ForLoop|`for`]]'s *init* and *step* clauses chain multiple side effects — `for (i = 0, j = 0; i < 10; i += 1, j += 10)`. The chapter cautions against overuse for readability.
- **[[BreakStatement|`break`]]** exits the *innermost enclosing* loop or [[SwitchStatement|`switch`]] immediately. **[[ContinueStatement|`continue`]]** skips the rest of the current loop iteration and jumps to the next test-of-condition (in [[ForLoop|`for`]], it runs the *step* first, then re-tests).

## Key Quotes

> "Zero (0) evaluates to false, and nonzero (any positive or negative value) evaluates to true." — the **integer-as-boolean** rule that organizes the rest of the chapter and motivates the `0`/`1` return convention of [[RelationalOperator|relational operators]].

> "Logical operator evaluation stops evaluating a logical expression as soon as the result is known." — the formal statement of [[ShortCircuitEvaluation|short-circuit evaluation]] that makes [[LogicalOperator|`&&`]]/[[LogicalOperator|`||`]] safe-to-chain with guard expressions.

> "The `do-while` loop will always execute the loop body at least one time." — the structural distinction that picks the correct loop form when the loop must run before its termination condition can be evaluated.

> "For loops and while loops are equivalent in power." — anchors the design rule that follows: **[[ForLoop|`for`]] for [[DefiniteIteration|definite]] iteration, [[WhileLoop|`while`]] for [[IndefiniteIteration|indefinite]] iteration** — a stylistic choice, not a capability one.

## Worked examples

**Multi-way branch + relational + logical operators:**

```c
int x;
scanf("%d", &x);
if (x > 0 && x % 2 == 0) {
    printf("positive even\n");
} else if (x > 0) {
    printf("positive odd\n");
} else if (x == 0) {
    printf("zero\n");
} else {
    printf("negative\n");
}
```

**`switch` with intentional fall-through and `default`:**

```c
switch (grade) {
    case 'A':
    case 'a':
        printf("excellent\n");
        break;
    case 'B':
    case 'b':
        printf("good\n");
        break;
    default:
        printf("see me\n");
}
```

**Three loop forms doing the same job (powers of 2 ≤ `limit`):**

```c
/* while: zero-or-more iterations */
int p = 1;
while (p <= limit) {
    printf("%d\n", p);
    p *= 2;
}

/* do-while: at-least-one iteration */
int p = 1;
do {
    printf("%d\n", p);
    p *= 2;
} while (p <= limit);

/* for: same logic, condensed */
for (int p = 1; p <= limit; p *= 2) {
    printf("%d\n", p);
}
```

**`break` and `continue`:**

```c
for (int i = 0; i < 100; i++) {
    if (i == target) break;       /* leave the loop entirely */
    if (i % 2 != 0)  continue;    /* skip odd i, go to i++ then test */
    printf("%d\n", i);
}
```

## Connections

- [[DiveIntoSystems]] — the book; this is Ch 1.3.
- [[dis-1-1-getting-started]] — Ch 1.1; supplied [[CLanguage|C]] / [[MainFunction|`main`]] / [[Printf|`printf`]] / [[VariableDeclaration|declarations]] / [[CArithmeticOperators|arithmetic operators]] — this section adds the **decision** and **iteration** layer on top.
- [[dis-1-2-input-output]] — Ch 1.2; supplied [[Scanf|`scanf`]] / [[FormatSpecifier|specifiers]] — used here for the interactive examples (e.g., reading `limit` for the powers-of-2 loop).
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[CLanguage]] — the language; [[ControlFlow|control flow]] is the next layer past types and arithmetic.
- [[ControlFlow]] — the umbrella concept this section operationalizes for [[CLanguage|C]].
- [[IfStatement]] / [[ElseStatement]] — the branching primitive and its companion clause.
- [[SwitchStatement]] / [[CaseLabel]] — integer-dispatched multi-way branch with fall-through semantics.
- [[WhileLoop]] / [[DoWhileLoop]] / [[ForLoop]] — the three loop forms; [[ForLoop|`for`]] and [[WhileLoop|`while`]] are equivalent in power.
- [[BreakStatement]] / [[ContinueStatement]] — structured early-exit and skip-to-next-iter inside loops; [[BreakStatement|`break`]] also terminates [[SwitchStatement|`switch`]] cases.
- [[RelationalOperator]] / [[LogicalOperator]] — the two operator families that build [[CBooleanExpression|boolean expressions]].
- [[CBooleanExpression]] — boolean values in [[CLanguage|C]] are integer-valued (`0` false, any nonzero true).
- [[ShortCircuitEvaluation]] — the early-exit semantics of [[LogicalOperator|`&&`]] / [[LogicalOperator|`||`]].
- [[CommaOperator]] — the operator that lets [[ForLoop|`for`]]'s *init*/*step* clauses chain multiple side effects.
- [[DefiniteIteration]] / [[IndefiniteIteration]] — the design-rule pair that distinguishes [[ForLoop|`for`]] from [[WhileLoop|`while`]] *usage*, given equivalent *power*.
- [[Python]] — contrast: Python uses indentation (no `{ }`), no parens around the test, and `for` iterates a sequence rather than acting as a general loop.

## Contradictions

- None with existing wiki content. This section **extends** [[CLanguage]] / [[CArithmeticOperators]] from [[dis-1-1-getting-started|Ch 1.1]] with a control-flow layer; it **complements** [[booleanalgebra]] (abstract two-valued algebra) with the C-specific *integer-as-boolean* implementation, and **complements** [[propositionallogic]] (the symbolic logic side) with the C-operator-syntax side. The [[ShortCircuitEvaluation|short-circuit]] semantics here are the same as those informally assumed throughout the rest of the [[DiveIntoSystems]] corpus.
