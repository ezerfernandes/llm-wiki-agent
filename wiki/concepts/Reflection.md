---
title: "Reflection (Agentic Pattern)"
type: concept
tags: [agents, agentic-design-patterns, reflection, self-correction, self-critique, generator-critic, producer-reviewer, iterative-refinement, control-flow]
sources: [agentic-design-patterns-ch04-reflection, agentic-design-patterns-ch06-planning, agentic-design-patterns-ch17-reasoning]
last_updated: 2026-06-07
---

# Reflection (Agentic Pattern)

**Reflection** is the agentic design pattern in which an agent **evaluates its own work, output, or internal state and uses that evaluation to iteratively improve or refine its response**. It is a form of **self-correction / self-improvement** that introduces a *feedback loop* on top of an agent's execution — the agent does not just produce an output, it examines that output (or the process that generated it), identifies issues, and uses those insights to generate a better version or modify future actions. It is the fourth of the 21 patterns in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] (see [[agentic-design-patterns-ch04-reflection|Ch 4]]).

> This page is the **agentic-pattern** sense of "reflection." For the failure mode of reflection loops see [[ReflectionFailure]]; for storing reflections across turns see [[ReflectionMemory]]; for the single-call self-review verb see [[SelfCritique]] and [[SelfEvaluation]].

## How it works — the reflection cycle

Reflection is distinct from a sequential chain (output passed straight to the next step, see [[PromptChaining]]) and from [[Routing|routing]] (which only chooses a path). It introduces a **feedback loop** that typically runs four steps:

1. **Execution** — the agent performs the task / generates an initial output.
2. **Evaluation / Critique** — the result is analyzed (often via *another* LLM call or a set of rules) for factual accuracy, coherence, style, completeness, or adherence to instructions.
3. **Reflection / Refinement** — based on the critique, the agent decides how to improve: regenerate the output, adjust parameters, or modify the overall plan.
4. **Iteration** (optional but common) — re-execute and repeat until a satisfactory result is achieved or a stopping condition is met.

## The Producer–Critic (Generator-Critic / Producer-Reviewer) model

The chapter's central architectural claim is that the most robust implementation **separates the process into two distinct logical roles**:

| Role | Responsibility |
|---|---|
| **Producer / Generator** | Performs the initial execution — focuses entirely on generating the content (code, prose, a plan). |
| **Critic / Reviewer** | Sole purpose is to *evaluate* the Producer's output. Given a *different* set of instructions and a distinct persona (e.g. "You are a senior software engineer," "You are a meticulous fact-checker"), it finds flaws, suggests improvements, and provides **structured feedback**. |

Using two specialized agents (or two LLM calls with distinct system prompts) "often yields more robust and unbiased results" than single-agent self-reflection. The rationale is **separation of concerns**: it prevents the *"cognitive bias"* of an agent reviewing its own work — the Critic approaches the output with a fresh perspective dedicated entirely to finding errors. This is the agentic-framework realization of the idea behind [[Reflexion]] (Shinn et al. 2023), which separates an *evaluator* from a *self-reflection* module, and mirrors the [[ActorCriticAgent|actor-critic]] decomposition from reinforcement learning. The Critic is effectively an [[LLMAsAJudge|LLM-as-judge]] for self-evaluation, and a *separate* critic persona is the book's mitigation of [[SelfBiasJudge|self-bias]].

## Why it matters in agentic systems

- **Self-awareness and adaptability.** Reflection "adds a layer of meta-cognition," moving agents beyond simply executing instructions toward a more sophisticated form of problem-solving — they learn from their own outputs and processes.
- **Synergy with goals and memory.** A goal provides the benchmark for self-evaluation while monitoring tracks progress ([[GoalSettingAndMonitoring]], Ch 11); reflection becomes the *corrective engine*. Conversational [[MemoryManagement|memory]] (Ch 8) makes reflection **cumulative** — without memory each reflection is a self-contained event; with it, each cycle builds on the last for context-aware refinement and avoids repeating past critiques.
- **Inference-time scaffolding.** Reflection is a form of [[TestTimeCompute|test-time compute]]: spend extra inference budget on critique and refinement in exchange for higher quality.

## When to use it (rule of thumb)

Use reflection when the **quality, accuracy, and detail** of the final output matter more than **speed and cost** — e.g. polished long-form content, writing/debugging code, detailed planning, accurate summarization, and complex multi-step reasoning. Employ a *separate critic* when the task needs high objectivity or specialized evaluation a generalist producer might miss.

## Trade-offs

- **Cost & latency** — every refinement loop may require a new LLM call, making it suboptimal for time-sensitive applications.
- **Memory-intensive** — conversation history expands with each iteration (initial output + critique + refinements), risking context-window overflow or API throttling. See [[ReflectionFailure]] for the degenerate-loop failure mode.
- **Orchestration** — a single reflection step can be implemented in [[LangChain]]/[[LangGraph]], [[GoogleADK|ADK]], or [[CrewAI|Crew.AI]], but *true iterative* reflection "typically involves more complex orchestration" (stateful, cyclical workflows like [[LangGraph]]).

## Framework implementations (Ch 4 examples)

- **[[LangChain]] (LCEL)** — a `run_reflection_loop()` over `ChatOpenAI(model="gpt-4o", temperature=0.1)` generates a `calculate_factorial` function, then a `reflector_prompt` casts the model as a senior code reviewer; the critic emits the single phrase `CODE_IS_PERFECT` as the **stopping condition** or a bulleted critique appended to history for the next refinement (`max_iterations = 3`).
- **[[GoogleADK|Google ADK]]** — a `SequentialAgent(sub_agents=[generator, reviewer])` wires a `DraftWriter` `LlmAgent` (writes to `output_key="draft_text"`) to a `FactChecker` `LlmAgent` (reads `draft_text`, emits a structured `{status, reasoning}` dict to `review_output`). ADK's `LoopAgent` is the alternative for true iteration.
- **[[LangGraph]]** — named as the stateful/graph-based substrate for full iterative reflection loops with conditional transitions.

## Connections

- [[agentic-design-patterns-ch04-reflection]] — primary source (Ch 4).
- [[AgenticDesignPatterns]] / [[AgenticDesignPattern]] / [[AntonioGulli]] — book hub, meta-concept, author.
- [[PromptChaining]] / [[Routing]] / [[Parallelization]] — the prior control-flow patterns (Chs 1–3) reflection layers a feedback loop onto.
- [[SelfCritique]] / [[SelfEvaluation]] — the single-call self-review mechanism reflection generalizes.
- [[Reflexion]] — evaluator + self-reflection split; the technique this pattern operationalizes.
- [[ActorCriticAgent]] — the RL actor/critic decomposition the Producer-Critic model mirrors.
- [[CritiqueAgent]] — Ch 16's resource-routing application of the Generator-Critic loop: a Critic that evaluates responses and feeds back to refine a cost-aware [[ModelRouter|router]] ([[ResourceAwareOptimization]]).
- [[LLMAsAJudge]] / [[SelfBiasJudge]] — the Critic as judge; separate-critic persona mitigates self-bias.
- [[ReflectionFailure]] / [[ReflectionMemory]] — the failure mode and the cross-turn memory of reflection.
- [[FeedbackLoop]] — the general control structure reflection instantiates.
- [[MemoryManagement]] / [[GoalSettingAndMonitoring]] — Chs 8 & 11; memory makes reflection cumulative, goals provide the benchmark it corrects against.
- [[Planning]] — Ch 6; [[agentic-design-patterns-ch06-planning|its Key Takeaway]] describes [[DeepResearch|Deep Research]] as a system that "reflects, plans, and executes" — reflection drives the knowledge-gap detection that triggers dynamic re-planning.
- [[DeepResearch]] — the Ch 6 exemplar that interleaves reflection (evaluate gathered info), planning (refine the research plan), and execution (search).
- [[TestTimeCompute]] — reflection as inference-time scaffolding.
- [[LangChain]] / [[LangGraph]] / [[GoogleADK]] / [[CrewAI]] — frameworks with reflection implementations.
- [[openai|OpenAI]] / [[gemini|Gemini]] — interchangeable model providers for the examples.
- [[ReasoningTechniques]] — Ch 17 reuses Reflection as the "Self-Correction" reasoning technique (see below).

## As "Self-Correction" in the Reasoning Techniques chapter (Gulli, Ch 17)

[[agentic-design-patterns-ch17-reasoning|Chapter 17]] re-uses this pattern under the name **self-correction (self-refinement)** as one of its [[ReasoningTechniques|Reasoning Techniques]], explicitly cross-referencing the dedicated Ch 4 treatment above. It is framed as *"a crucial aspect of an agent's reasoning process, particularly within Chain-of-Thought prompting"* — the agent's internal evaluation of its generated content and intermediate thoughts to identify ambiguities, information gaps, or inaccuracies, then adjust before delivering output. The chapter's worked example is a **"Self-Correction Agent"** with a five-step analytical/revision workflow (understand requirements → analyze content → identify weaknesses → propose specific improvements → generate revised content), demonstrated on an eco-friendly social-media post that goes from a generic draft to a polished, hashtag-and-emoji-enhanced revision. The chapter's framing: *"this technique integrates a quality control measure directly into the agent's content generation"* — i.e. self-correction is the deliberation half of the chapter's thought-then-act arc, distinct from the [[react|ReAct]] acting half. It pairs with [[TreeOfThoughts|ToT]] as the two techniques that *"give agents the crucial ability to deliberate."*
