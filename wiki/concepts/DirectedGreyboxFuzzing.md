---
title: "Directed Greybox Fuzzing"
type: concept
tags: [fuzzing, greybox, afl, aflgo, power-schedule, optimization, call-graph, security]
sources: [fuzzingbook-06-greybox-fuzzer]
last_updated: 2026-06-06
---

# DirectedGreyboxFuzzing

**Directed greybox fuzzing** steers a [[GreyboxFuzzing|greybox fuzzer]] toward a *specific target location* in the source code — e.g. a suspected buffer overflow, a recent code change, or a patched line — rather than maximizing coverage in general. It frames "reach the target" as an **optimization problem**: assign more [[SeedEnergy|energy]] to seeds whose execution is "closer" to the target, where closeness is a pre-computed distance metric over the program's structure. This is the technique behind [[AFL]]'s **AFLGo** variant by [[MarcelBohme|Marcel Böhme]] et al. (*"Directed Greybox Fuzzing"*, CCS 2017).

## From The Fuzzing Book — Greybox Fuzzing
[[fuzzingbook-06-greybox-fuzzer|Ch 6]] demonstrates directed fuzzing on a generated **maze**: the fuzzer must steer the `X` to the `#` target tile via `U/D/L/R` inputs. It computes a **function-level distance** for each function as the shortest-path length to the target function in the static [[CallGraph|call graph]] (`nx.shortest_path_length`; unreachable functions get `0xFFFF`). `DirectedSchedule` then assigns each seed `energy = (1 / seed.distance) ** exponent`, where `seed.distance` is the *average* call-graph distance of the functions the seed covers. The improved `AFLGoSchedule` *normalizes* seed distances between the population's `min_dist` and `max_dist`, sharply amplifying near-target seeds — and it generates *hundreds* of maze solutions where the plain greybox fuzzer and the un-normalized `DirectedSchedule` solve it essentially never. Distances are pre-computed and injected into the binary (like coverage instrumentation), making the runtime average-distance computation extremely cheap. The chapter notes directed fuzzing's kinship with search-based optimization ([[fuzzingbook-07-search-based-fuzzer|Ch 7]]).

## Connections
- [[GreyboxFuzzing]] — the base technique being directed.
- [[CallGraph]] — supplies the function-level distances toward the target.
- [[PowerSchedule]] / [[SeedEnergy]] — `DirectedSchedule`/`AFLGoSchedule` set distance-based energy.
- [[BoostedGreyboxFuzzing]] / [[AFLFast]] — the sibling boost toward rare paths (vs toward a target).
- [[AFL]] — the real-world fuzzer whose AFLGo variant this reconstructs.
- [[MarcelBohme]] — author of the Directed Greybox Fuzzing / AFLGo work.
- [[Mutator]] — uses a `DictMutator`/`MazeMutator` to inject directional keywords.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — search-based fuzzing as the broader optimization view.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — where directed fuzzing is built (the maze example).

## Sources
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing."
