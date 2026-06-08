---
title: "Implicit Information Flow"
type: concept
tags: [security, information-flow, taint-analysis, control-flow, program-analysis, fuzzing]
sources: [fuzzingbook-19-information-flow]
last_updated: 2026-06-06
---

# Implicit Information Flow

**Implicit information flow** (control-flow taint) is the dependence of an output on an input that is mediated by *control flow* rather than by direct data assignment. The output is never computed from the input value; instead the input determines *which branch executes*, and the branch reconstructs equivalent data. Because there is no explicit [[DataFlow|data dependence]], any [[DynamicTaintAnalysis|dynamic taint analysis]] that propagates labels along operations will fail to see the flow — making implicit flow a fundamental limitation of taint tracking and a classic channel for laundering tainted/secret data.

## From The Fuzzing Book — Tracking Information Flow
[[fuzzingbook-19-information-flow|Ch 19]] presents implicit flow as one of the principal ways taints get lost. Its example is a string-copy function that switches on each character:
```python
for c in s:
    if c == 'a': t += 'a'
    elif c == 'b': t += 'b'
    ...
```
Here `t` ends up identical to `s` "yet there is no explicit data flow between the characters in `s` and the characters in `t`," so neither the [[TaintedString|`tstr`]] taint nor the [[CharacterOrigin|`ostr`]] origins propagate. The chapter groups this with the other taint-loss channels (string→number conversions, internal C library calls) and concludes that the only safe default is to treat untainted strings as worst-case — *possibly untrusted* and *possibly secret*. Fully following implicit flow requires reasoning about the program's branch conditions, which is exactly what the symbolic/[[ConcolicExecution|concolic]] techniques of [[fuzzingbook-20-concolic-fuzzer|Ch 20]] provide.

## Connections
- [[DataFlow]] — the explicit counterpart; implicit flow is what data-flow taint *cannot* capture.
- [[InformationFlow]] — implicit flow is the harder, control-mediated kind of flow.
- [[DynamicTaintAnalysis]] / [[CharacterOrigin]] / [[TaintedString]] — all blind to implicit flow.
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] — symbolic/concolic execution, which can reason about the branch conditions that carry implicit flow.
- [[fuzzingbook-19-information-flow]] — the chapter that identifies this limitation.

## Sources
- [[fuzzingbook-19-information-flow]] — *The Fuzzing Book* Ch 19, "Tracking Information Flow."
