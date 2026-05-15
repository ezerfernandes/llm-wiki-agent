---
title: "Planning (Automated / AI)"
type: concept
tags: [planning, agents, reasoning, neuro-symbolic]
sources: [2402.01817-llm-modulo]
last_updated: 2026-05-10
---

# Planning

**Automated planning** is the AI sub-field concerned with synthesizing a sequence of actions that, when executed from an initial state, achieves a goal state, given a model of action preconditions/effects (Ghallab, Nau & Traverso, *Automated Planning*, 2004).

## Distinction from "acting"
Planning is **not** the same as **acting**. Invoking an action via an API (an *act*) carries no guarantee that the sequence of acts reaches the goal — see the critique of AutoGPT/LangChain in [[2402.01817-llm-modulo]]. Soundness is the planner's defining property.

## Knowledge requirements (per [[2402.01817-llm-modulo]] §2.3)
A planning system requires:
1. **Planning domain knowledge** — actions, preconditions, effects (typically PDDL); hierarchical recipes (HTN); past plans/cases.
2. **Reasoning/planning** — assembling that knowledge into an executable plan respecting subgoal/resource interactions.

Conflating (1) and (2) is, per the paper, the source of much over-optimism about LLM "planning". Many results that look like LLM planning are actually LLM *plan-knowledge extraction* on top of safely-ignorable subgoal interactions.

## Why LLMs alone can't plan (per [[2402.01817-llm-modulo]])
- Autoregressive, constant-time-per-token generation cannot host the search/deliberation a System-2 task requires.
- [[PlanBench]] empirical evidence: ~12% executable plans on [[Blocksworld]]; ~0% on Mystery BW (obfuscated names) — proof of approximate retrieval, not planning.
- LLMs cannot reliably verify plans, so iterative self-critique doesn't recover planning competence.

## How LLMs *can* help with planning
- As **candidate generators** inside [[LLMModuloFramework]] — sound external critics filter.
- As **domain-model acquisition partners** (extracting PDDL drafts for human sign-off).
- As **reformatters** between syntactic representations critics expect.
- As **soft critics** for style/explicability where soundness isn't required.

## Related representations
- [[PDDL]] — the standard symbolic planning language (McDermott et al. 1998).
- VAL — plan validator (Howey et al. 2004), the canonical hard critic in LLM-Modulo's Blocksworld case study.
- IPC — International Planning Competition benchmarks.

## Connections
- [[LLMModuloFramework]] — proposed integration
- [[PlanBench]] — benchmark suite
- [[Blocksworld]] — canonical domain
- [[System1And2]] — planning is a System-2 task
- [[SelfVerification]] — what LLMs can't do, hence external critics needed
- [[NeuroSymbolicAI]] — broader lineage
- [[ReinforcementLearning]] — adjacent paradigm; simulator-in-the-loop RL is an LLM-Modulo instance
- [[2402.01817-llm-modulo]] — source
