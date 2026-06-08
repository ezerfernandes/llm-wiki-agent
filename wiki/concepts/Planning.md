---
title: "Planning (Automated / AI)"
type: concept
tags: [planning, agents, reasoning, neuro-symbolic, agentic-design-patterns, task-decomposition, dynamic-replanning]
sources: [2402.01817-llm-modulo, ai-engineering-ch06-rag-agents, agentic-design-patterns-ch06-planning, agentic-design-patterns-ch17-reasoning]
last_updated: 2026-06-07
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
- [[Prioritization]] — Ch 20 sibling pattern; prioritization orders the sub-tasks a plan produces, and its "scheduling/selection logic" may delegate to a planning component
- [[2402.01817-llm-modulo]] — source

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

[[ChipHuyen|Huyen]] devotes the majority of Ch 6's agent section to planning. Her contribution is the **decouple-planning-from-execution** pattern:

> *"You ask the agent to first generate a plan, and only after this plan is validated is it executed."*

Validation can be heuristic (eliminate plans with invalid actions or with too many steps) or AI-judge-based. The system now has **three components**: plan-generator, plan-validator, plan-executor — which Huyen frames as a [[multiagentsystems|multi-agent system]].

**Full four-step process**:

1. **Plan generation** — come up with a plan; *"a sequence of manageable actions, so this process is also called task decomposition."*
2. **Reflection and error correction** — evaluate the generated plan; if bad, generate a new one.
3. **Execution** — take the planned actions.
4. **Reflection and error correction** — evaluate outcomes; if goal not met, generate a new plan.

**Foundation Model vs RL planners** (sidebar): RL agents *train* their planner; FM agents *are* the planner. Huyen predicts long-run convergence — *"FM agents and RL agents will merge."*

**Planning-vs-acting distinction** the existing page already records (per [[2402.01817-llm-modulo|LLM-Modulo]]) is *complementary*, not contradictory, to Huyen's framing. Huyen records both [[YannLeCun|LeCun]]'s and [[SubbaraoKambhampati|Kambhampati]]'s *"LLMs can't plan"* positions and counters them with [[ReasoningWithLanguageModelIsPlanningWithWorldModel|Hao et al. 2023]] — without adjudicating. The chapter's agnostic stance reflects the empirical state of 2024: *"it's unclear whether it's because we don't know how to use LLMs the right way or because LLMs, fundamentally, can't plan."*

**Approaches to improve planning** (a practical checklist Huyen names):

- Write better system prompts with more examples.
- Give better tool descriptions and parameter documentation.
- Refactor complex functions into simpler ones.
- Use a stronger model.
- Finetune a model for plan generation.

## Agentic Design Patterns (Gulli) perspective

[[agentic-design-patterns-ch06-planning|Chapter 6 of *Agentic Design Patterns*]] (Gulli) treats Planning as the 6th of 21 [[AgenticDesignPattern|agentic design patterns]] and frames it from a practitioner, framework-centric angle — complementary to (and more optimistic than) the LLM-Modulo and Huyen treatments above.

**Initial state → goal state.** "Planning is the ability for an agent or a system of agents to formulate a sequence of actions to move from an initial state towards a goal state." The plan "is not known in advance; it is created in response to the request." This restates the classical automated-planning definition already on this page (initial state, goal state, action sequence) in agentic, LLM-era terms.

**Delegate the *what*, discover the *how*.** A planning agent is like a specialist to whom you delegate a complex goal ("organize a team offsite"): you define the objective and its constraints (the *what*) but not the steps (the *how*). The agent infers the initial state (budget, participants, dates) and goal state (a booked offsite), then charts the optimal action sequence. This is the [[GoalOriented|goal→plan→action]] bridge — see [[TaskDecomposition]] for the decompose-into-sub-goals mechanism.

**Adaptability / dynamic re-planning.** "An initial plan is merely a starting point, not a rigid script." When an obstacle appears (venue unavailable), a capable agent "registers the new constraint, re-evaluates its options, and formulates a new plan." This **dynamic re-planning** is the chapter's answer to the soundness gap the LLM-Modulo critique raises: rather than guaranteeing a sound plan up front, the agent iterates as reality diverges from the plan.

**Flexibility-vs-predictability trade-off.** Dynamic planning is "a specific tool, not a universal solution." When the solution is well-understood and repeatable, a **predetermined, fixed workflow** is more effective — limiting agent autonomy reduces uncertainty and guarantees consistent outcomes. The decision rule: *"does the 'how' need to be discovered, or is it already known?"* (If known, prefer a fixed workflow over a planning agent.)

**LLMs as plan generators.** Gulli's optimistic claim — "LLMs are particularly well-suited for this, as they can generate plausible and effective plans based on their vast training data" — is in *framing tension* with the LLM-Modulo position above (LLMs alone can't produce *sound* plans). The tension is softened by Gulli's word choice ("plausible") and his reliance on dynamic re-planning + reflection as the recovery mechanism rather than claiming one-shot soundness. Recorded as a framing difference, not a strict contradiction.

**Two ends of the spectrum (both from Ch 6):**
- *Simple sequential* — a [[CrewAI]] `planner_writer_agent` whose `Task` explicitly asks it to first create a bullet-point plan, then write from that plan (`Process.sequential`, `crew.kickoff()`). Planning is **explicitly prompted** by the task description and `expected_output` format. This is the wiki's first ADP-coverage receipt of CrewAI used for *planning* (vs. tool use / multi-agent).
- *Complex dynamic* — [[DeepResearch|Deep Research]] agents (Google Gemini DeepResearch; OpenAI Deep Research API with `o3-deep-research`/`o4-mini-deep-research`) that build iterative research plans, present them for user review, execute an asynchronous search-analysis loop, and **adapt the plan as information accumulates**. Key Takeaway: Deep Research "reflects, plans, and executes" — uniting [[Reflection]], Planning, and [[ToolUse]].

**Visual summary (Fig. 4):** Prompt → Agent ⇄ Plan (Plan 1, Plan 2, Plan 3, …) → Output → User — the plan is an explicit artifact the agent reads back from and revises.

[[agentic-design-patterns-ch17-reasoning|Chapter 17 (Reasoning Techniques)]] revisits planning as a **practical application** of advanced reasoning ("Strategic Planning": reasoning across options, consequences, and preconditions, adjusting plans on real-time feedback via [[react|ReAct]]) and notes that extended inference-time deliberation ([[ScalingInferenceLaw|Scaling Inference Law]]) *"can lead to more effective and reliable plans."* The chapter's [[DeepResearch|Deep Research]] exemplar wraps an explicit research plan around a ReAct-style search loop with [[Reflection|reflection]]-driven re-planning.
