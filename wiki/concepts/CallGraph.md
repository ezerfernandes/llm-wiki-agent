---
title: "Call Graph"
type: concept
tags: [program-analysis, control-flow, static-analysis, fuzzing, graph]
sources: [fuzzingbook-06-greybox-fuzzer]
last_updated: 2026-06-06
---

# CallGraph

A **call graph** is a directed graph whose nodes are a program's functions and whose edges represent "function *A* may call function *B*." It captures the possible order of function execution and is a foundational artifact of static program analysis. Distances within the call graph (shortest paths between functions) are used to reason about how "close" one part of a program is to another — for example, how close a given execution is to reaching a target function.

## From The Fuzzing Book — Greybox Fuzzing
[[fuzzingbook-06-greybox-fuzzer|Ch 6]] uses the static call graph of generated maze code to drive [[DirectedGreyboxFuzzing|directed greybox fuzzing]]. It imports `get_callgraph`/`callgraph` (returning a [networkx] graph) from the [[ControlFlow|`ControlFlow`]] module, identifies the target function (`target_tile()`), and computes each function's **function-level distance** to the target as `nx.shortest_path_length(cg, node, target_node)` (assigning `0xFFFF` when no path exists). These pre-computed distances become the basis of the `DirectedSchedule`/`AFLGoSchedule` [[PowerSchedule|power schedules]], which give a seed [[SeedEnergy|energy]] inversely proportional to the average call-graph distance of the functions it covers. The chapter notes the related (harder) problem of basic-block-level distance over each function's control-flow graph.

## Connections
- [[DirectedGreyboxFuzzing]] — uses call-graph distance to steer the fuzzer toward a target.
- [[ControlFlow]] — the chapter's `ControlFlow` module supplies `callgraph`/`get_callgraph`.
- [[PowerSchedule]] / [[SeedEnergy]] — consume call-graph distances to weight seeds.
- [[GreyboxFuzzing]] — the fuzzing model the call-graph analysis supports.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — where the call graph is used for distance computation.

## Sources
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing."
