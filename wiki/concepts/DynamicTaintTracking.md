---
title: "Dynamic Taint Tracking"
type: concept
tags: [fuzzing, dynamic-analysis, taint-analysis, information-flow, security, parsing, grammar-mining, python]
sources: [fuzzingbook-18-grammar-miner, fuzzingbook-19-information-flow]
last_updated: 2026-06-06
---

# Dynamic Taint Tracking

**Dynamic taint tracking** (dynamic taint analysis) follows individual pieces of input data as they propagate through a program at runtime: each input byte/character is marked ("tainted") with its **origin**, and the taint flows along assignments and operations so that, at any later point, a value's taint records which input positions it derived from. It is the precise way to answer "did this value come from the input, and from *where*?" — the question at the heart of mapping inputs to program behavior.

## From The Fuzzing Book — Mining Input Grammars
[[fuzzingbook-18-grammar-miner|Ch 18]] contrasts dynamic taint tracking with its own cheaper heuristic. The [[GrammarMiner|`GrammarMiner`]] decides whether a variable value "came from the input" using plain **substring inclusion** (gated by `FRAGMENT_LEN`) rather than true tainting, arguing that:
- substring checks need no binary instrumentation and apply more broadly (tools like `dtrace`/`ptrace` already expose the needed values), whereas
- dynamic taints are "often lost due to implicit transmission, or at the boundary between Python and C code."

The chapter's final exercise nonetheless shows how to *upgrade* to taints: it imports the `ostr` origin-tracking string subclass from [[fuzzingbook-19-information-flow|Ch 19]], defines `is_fragment(fragment, original)` as taint-origin subset inclusion, and wires it into `TaintedInputStack`, `TaintedScopedVars`, `TaintedScopeTreeMiner`, and `recover_grammar_with_taints()`. Tainting avoids substring false positives (e.g. an embedded comma in a CSV field, or repeated fragments belonging to different tokens) but cannot observe **implicit flows** — for those the chapter points to concolic execution ([[fuzzingbook-20-concolic-fuzzer|Ch 20]]).

The mechanism itself (the `ostr` tainted-string subclass that remembers each character's origin) is developed in detail in [[fuzzingbook-19-information-flow|Ch 19]], "Tracking Information Flow."

## From The Fuzzing Book — Tracking Information Flow
[[fuzzingbook-19-information-flow|Ch 19]] is where this mechanism is actually built, as a pure-Python *library* approach to [[DynamicTaintAnalysis|dynamic taint analysis]] (following Conti et al., 2010) rather than VM/binary instrumentation. It defines two `str` subclasses: [[TaintedString|`tstr`]], which attaches one *taint* label to a whole string and propagates it through ~25 wrapped string methods (plus `__radd__`), and [[CharacterOrigin|`ostr`]], which refines this to a per-character *origin* index (each input position is effectively its own "color"), re-implementing slicing, concatenation, `split`, `replace`, `join`, `strip`, `%`, etc. to splice origin lists. These taints power a stronger-than-crash oracle: rejecting [[CodeInjection|code injection]] at an `eval` sink, detecting a Heartbleed-style privacy leak by per-character origin, and [[TaintDirectedFuzzing|taint-directed fuzzing]]. The chapter is also explicit about the limits this wiki's Ch 18 page already flagged — taints are lost across number conversions, internal C calls, and especially [[ImplicitInformationFlow|implicit (control) flow]] — which is exactly what makes the substring heuristic attractive in Ch 18 and what concolic execution ([[fuzzingbook-20-concolic-fuzzer|Ch 20]]) is needed to recover.

## Connections
- [[GrammarMiner]] / [[GrammarInference]] — Ch 18 uses (and can substitute) taint tracking to identify input fragments.
- [[fuzzingbook-19-information-flow]] — the chapter that builds the `ostr` taint mechanism in full.
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] — concolic fuzzing, the costlier alternative that can capture implicit flows taints miss.
- [[Coverage]] — both rely on hooking dynamic execution.
- [[Parser]] / [[DerivationTree]] — taints map input characters onto the recovered parse structure.
- [[DynamicTaintAnalysis]] / [[InformationFlow]] — the security framing (sources/sinks/sanitizers) and the property tracked.
- [[TaintedString]] (`tstr`) / [[CharacterOrigin]] (`ostr`) — the two concrete implementations from Ch 19.
- [[TaintDirectedFuzzing]] / [[ImplicitInformationFlow]] — the fuzzing application and the principal limitation.

## Sources
- [[fuzzingbook-18-grammar-miner]] — *The Fuzzing Book* Ch 18, "Mining Input Grammars."
- [[fuzzingbook-19-information-flow]] — *The Fuzzing Book* Ch 19, "Tracking Information Flow."
