---
title: "PDDL"
type: concept
tags: [planning, formal-language, neuro-symbolic]
sources: [2402.01817-llm-modulo]
last_updated: 2026-05-10
---

# PDDL

**Planning Domain Definition Language** (McDermott et al. 1998), the standard formal representation used by the automated-planning community: predicates, objects, action schemas with preconditions and effects, initial state, and goal.

## Role in this wiki
- The representation used by the [[Blocksworld]] / [[PlanBench]] benchmarks.
- The target of LLM-as-translator approaches (LLM+P, Pan et al. 2023 Logic-LM, Xie et al. 2023) — which [[2402.01817-llm-modulo]] critiques as inheriting solver expressivity/search-complexity limits.
- The model that LLM-Modulo's **hard critic [[PDDL|VAL]]** (Howey et al. 2004) checks plans against.

## VAL
**VAL** is the canonical PDDL **plan validator**: given a PDDL domain, problem, and candidate plan, it returns sound pass/fail (and constructive error reports). In the [[LLMModuloFramework]] Blocksworld case study, VAL provides the *backprompt* signal that lifts GPT-4 from baseline to 82% pass rate in 15 rounds.

## Domain-model acquisition
Manually authoring PDDL is the classical AI "knowledge engineering bottleneck". One [[LLMModuloFramework]] role for LLMs is **collaborative domain extraction** (Guan et al. 2023): the LLM proposes draft action schemas; a human expert signs off. This is the [[PolanyisRevenge]] payoff.

## Connections
- [[Planning]], [[PlanBench]], [[Blocksworld]] — places PDDL is used
- [[LLMModuloFramework]] — VAL = hard critic
- [[NeuroSymbolicAI]] — PDDL sits on the symbolic side
- [[2402.01817-llm-modulo]] — source
