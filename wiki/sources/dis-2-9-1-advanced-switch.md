---
title: "Dive into Systems — Ch 2.9.1 Constants, switch, enum, and typedef"
type: source
tags: [book, textbook, c-language, advanced-c, dive-into-systems, constants, switch, enum, typedef]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/advanced_switch.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **first subsection of [[dis-2-9-advanced|Ch 2.9]] *Advanced C Features*** in *[[DiveIntoSystems]]*. Bundles four small but load-bearing language features — **[[CConstant|`#define` constants]]**, the **[[SwitchStatement|`switch`]] statement** (deferred from [[dis-1-3-conditionals-loops|Ch 1.3]]), **[[CEnum|enumerated types]]**, and **[[Typedef|`typedef`]]** (deferred from [[dis-1-6-structs|Ch 1.6]] / [[dis-2-7-structs|Ch 2.7]]) — into one section because they share a common purpose: **giving meaningful names to values and types** for readability, maintainability, and (for [[SwitchStatement|`switch`]]) compiler-level branch optimization.

## Key Claims

- **[[CConstant|`#define`]] creates compile-time symbolic constants**, not runtime variables — `#define N (20)` declared outside any function makes `N` an alias for `20` everywhere. *"Constants are not lvalues and cannot be reassigned at runtime"*; attempting `N = 50;` is a compilation error. The wrapping parentheses around the literal are the convention to avoid operator-precedence surprises in expression substitution.
- **The headline benefit of constants is single-point-of-change maintainability** — changing one `#define` line updates every usage, mirroring why magic numbers are anti-pattern.
- **The [[SwitchStatement|`switch`]] statement is the structured multi-way branch on an integer expression** — `switch (expr) { case literal_1: ... break; case literal_2: ... break; default: ... }`. The compiler can often turn this into a jump table that is more efficient than the equivalent [[IfStatement|`if`]] / [[ElseStatement|`else if`]] chain when there are many cases over dense integer values.
- **Three load-bearing [[SwitchStatement|`switch`]] rules** (Ch 2.9.1 codifies what Ch 1.3 only sketched): (1) **case values must be literal values, not expressions** — a runtime expression in a [[CaseLabel|case label]] is a compile error; (2) without [[BreakStatement|`break`]] execution **falls through** to subsequent cases — sometimes deliberate (stacked labels share a body), more often a bug; (3) the **`default:` label is optional and conventionally appears last**, matching any value no explicit `case` handles.
- **[[CEnum|Enumerated types]] group related integer constants under a named type** — `enum days_of_week { MON, TUES, WED, THURS, FRI };` makes `MON` = 0, `TUES` = 1, etc. Variables declared as `enum days_of_week day;` then carry the enum's intent in their type, not just a raw `int`.
- **Four advantages of [[CEnum|`enum`]] over [[CConstant|`#define`]]** for grouping related constants: (a) **logical grouping** — related constants live together in one named scope; (b) **type safety** — function parameters typed as `enum days_of_week` document intent; (c) **implicit sequential values** — no manual `#define MON 0` / `#define TUES 1` ladder; (d) **easy insertion/removal** without recomputing every neighbor's value.
- **Custom value assignment** is allowed and the sequence continues from there — `enum days_of_week { SUN = 1, MON, TUES, WED };` makes `MON = 2`, `TUES = 3`, `WED = 4`. This generalizes the "sequential auto-numbering" default.
- **[[CEnum|Enum constants print as their integer values, not their names**] — `printf("%d\n", TUES);` outputs the number. The named-constant abstraction is purely a source-code convenience; at runtime an [[CEnum|`enum`]] *is* an [[CPrimitiveType|`int`]].
- **[[CEnum|`enum`]] pairs naturally with [[SwitchStatement|`switch`]]** — the chapter's worked example dispatches on `val` of type `enum days_of_week` with `case FRI: ...` `case MON: case WED: ...` etc., demonstrating both **stacked-labels-for-shared-body** and **intentional fall-through** (FRI prints *"Orchestra practice"* then falls through to MON/WED to print *"Classes today"*).
- **[[Typedef|`typedef`]] creates a type alias** — `typedef existing_type new_name;`. Three canonical uses introduced here: (1) **alias an [[CEnum|`enum`]]** — `typedef enum class_year classYr;` lets `classYr yr;` replace `enum class_year yr;`; (2) **alias a [[CStruct|`struct`]]** — `typedef struct studentT studentT;` lets `studentT s;` replace `struct studentT s;`; (3) **alias a primitive width** — `typedef unsigned long long ull;` for ergonomic large-integer declarations.
- **The combined struct-typedef syntax** `typedef struct studentT { ... } studentT;` defines the struct and its alias in **one declaration** — the idiomatic compact form that drops the two-word `struct` prefix everywhere thereafter. This is the form most production [[CLanguage|C]] codebases use.
- **Overall significance**: these four features *enhance code clarity, maintainability, and organization by creating meaningful names for values and types, while also enabling the compiler to potentially optimize branching logic.* They are pure source-level conveniences (zero runtime overhead) with one exception — [[SwitchStatement|`switch`]] enables compiler-level jump-table optimization unavailable to [[IfStatement|`if`]] / [[ElseStatement|`else if`]] chains.

## Key Quotes

> "Constants are not lvalues and cannot be reassigned at runtime." — on [[CConstant|`#define`]] semantics.

> "Without `break`, execution 'falls through' to subsequent cases." — the [[SwitchStatement|`switch`]] fall-through default.

> "Enumerated types print their integer values, not constant names." — the [[CEnum|`enum`]] runtime reality check.

> "These features collectively enhance code clarity, maintainability, and organization by creating meaningful names for values and types, while also enabling the compiler to potentially optimize branching logic." — the chapter's closing motivation.

## Connections

- [[DiveIntoSystems]] — Ch 2.9.1 — first subsection of [[dis-2-9-advanced|Ch 2.9]]; resolves Ch 1.3 / Ch 1.6 / Ch 2.7 deferrals around [[SwitchStatement|`switch`]] and [[Typedef|`typedef`]].
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-2-9-advanced]] — parent hub page (Ch 2.9 *Advanced C Features*).
- [[dis-1-3-conditionals-loops]] — where [[SwitchStatement|`switch`]] / [[CaseLabel|`case`]] / [[BreakStatement|`break`]] were first sketched (now fully codified).
- [[dis-1-6-structs]] / [[dis-2-7-structs]] — where [[Typedef|`typedef`]] was named and deferred (now formally introduced).
- [[CConstant]] — new — the `#define const_name (literal_value)` symbolic-constant mechanism with the parenthesization convention.
- [[CEnum]] — new — the enumerated-type construct grouping related integer constants under a named type.
- [[ConstQualifier]] — new — the *other* "constant" mechanism Ch 2.9.1 contrasts with (`const` type qualifier vs `#define` preprocessor substitution).
- [[TypedefExpansion]] — new — extends the prior [[Typedef]] page with the **three canonical aliasing patterns** ([[CEnum|enum]] alias, [[CStruct|struct]] alias, primitive-width alias) and the **combined struct-typedef one-liner** as the idiomatic form.
- [[SwitchStatement]] / [[CaseLabel]] / [[BreakStatement]] — updated (Ch 2.9.1 sources added; rules formalized).
- [[Typedef]] — updated (Ch 2.9.1 source added; the three-pattern taxonomy folded in).

## Contradictions

None. Ch 2.9.1 is **additive** — it formalizes the [[SwitchStatement|`switch`]] / [[CaseLabel|`case`]] / [[BreakStatement|`break`]] semantics [[dis-1-3-conditionals-loops|Ch 1.3]] sketched and the [[Typedef|`typedef`]] convention [[dis-1-6-structs|Ch 1.6]] / [[dis-2-7-structs|Ch 2.7]] named-and-deferred. The [[CEnum|`enum`]] construct is genuinely new to the corpus; the [[CConstant|`#define`]] mechanism appears here for the first time as a *language feature* (it was implicit in `NULL`, `EOF`, `SEEK_SET`, etc. from prior chapters but never named as a user-facing tool).

## Status

**Subsection page** (Ch 2.9.1) — sits under [[dis-2-9-advanced|Ch 2.9]] hub; introduces **four new concept pages** ([[CConstant]], [[CEnum]], [[ConstQualifier]], [[TypedefExpansion]]) and **updates three existing** ([[SwitchStatement]], [[CaseLabel]], [[Typedef]]) with the Ch 2.9.1 codifications.
