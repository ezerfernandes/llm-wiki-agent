---
title: "Reasoning Techniques (Agentic Pattern)"
type: concept
tags: [agents, agentic-design-patterns, reasoning, test-time-compute, chain-of-thought, multi-agent, self-correction]
sources: [agentic-design-patterns-ch17-reasoning, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# Reasoning Techniques

**Reasoning Techniques** is the 17th of the 21 patterns in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] ([[agentic-design-patterns-ch17-reasoning|Ch 17]]). It is the **hub pattern** for the family of advanced reasoning methodologies that make an agent's internal "thought" process explicit, so it can perform multi-step logical inference, decompose problems, explore solution paths, and reach more robust and accurate conclusions than a single direct pass.

## The organizing principle: compute at inference time

The chapter's unifying idea is the **allocation of increased computational resources during inference** — granting the agent (or the underlying LLM) more processing time or steps to answer. Rather than a quick single pass, the agent engages in iterative refinement, explores multiple solution paths, or uses external tools. This extended processing time often significantly improves accuracy, coherence and robustness for complex problems. This is the agentic-pattern framing of [[TestTimeCompute|test-time compute]] / [[testtimescaling|test-time scaling]], and is formalized in the chapter as the [[ScalingInferenceLaw|Scaling Inference Law]].

**Rule of thumb (chapter):** use these techniques when a problem is too complex for a single-pass answer and requires decomposition, multi-step logic, interaction with external data/tools, or strategic planning — i.e. when showing the "work" matters as much as the final answer.

## The techniques surveyed

| Technique | What it does | Wiki page |
|---|---|---|
| **Chain-of-Thought (CoT)** | Generate intermediate step-by-step reasoning before the answer; the agent's internal monologue. | [[ChainOfThought]] |
| **Tree-of-Thought (ToT)** | Branch into a tree of candidate thoughts; backtrack, self-correct, explore alternatives. | [[TreeOfThoughts]] |
| **Self-Correction / Self-Refinement** | Internal critique loop: draft → review against requirements → revise. Cross-ref Ch 4. | [[Reflection]] / [[SelfCritique]] |
| **Program-Aided Language Models (PALMs)** | Generate and execute code to offload precise computation to a deterministic environment. | [[ProgramAidedLanguageModel]] |
| **Reinforcement Learning with Verifiable Rewards (RLVR)** | Training method behind "reasoning models" that spend variable thinking time. | [[rlvr]] |
| **ReAct (Reasoning and Acting)** | Interleave reasoning with tool/environment actions in a Thought→Action→Observation loop. | [[react]] |
| **Chain of Debates (CoD)** | Multiple diverse models collaborate/argue like an AI council to reduce bias, raise accuracy. | [[ChainOfDebates]] |
| **Graph of Debates (GoD)** | Debate as a non-linear graph of supports/refutes argument nodes; conclusion = most robust cluster. | [[GraphOfDebates]] |
| **MASS (Multi-Agent System Search)** | Automated three-stage optimization of multi-agent prompts + topology. | [[MultiAgentSystemSearch]] |
| **Deep Research** | Autonomous research assistant: explore → reason/refine → follow-up → synthesize. | [[DeepResearch]] |
| **Scaling Inference Law** | A smaller model with a larger "thinking budget" can beat a larger model with a simpler process. | [[ScalingInferenceLaw]] |

## The arc of the chapter

The chapter describes a progression toward true autonomy:
1. **Internal monologue** — [[ChainOfThought|CoT]] lets an agent formulate a coherent plan before acting.
2. **Deliberation** — [[TreeOfThoughts|ToT]] and [[Reflection|self-correction]] let the agent evaluate multiple strategies, backtrack from errors, and improve its own work before execution.
3. **Acting** — [[react|ReAct]] is the pivotal leap to fully agentic systems: a thought–action–observation loop lets the agent move beyond thinking and use external tools, adapting to environmental feedback.
4. **More thinking time** — the [[ScalingInferenceLaw|Scaling Inference Law]] makes deeper deliberation a tunable resource.
5. **Collaboration** — the next frontier is multi-agent reasoning: [[ChainOfDebates|CoD]] / [[GraphOfDebates|GoD]] create agent societies that reason together to reduce individual bias, and [[MultiAgentSystemSearch|MASS]] automates the design of such teams.
6. **Culmination** — [[DeepResearch|Deep Research]] demonstrates agents that execute complex, long-running, multi-step investigations autonomously on a user's behalf.

## Why it matters in agentic systems

By making reasoning explicit, agents can formulate transparent, multi-step plans — the foundational capability for autonomous action and user trust. The chapter's thesis is that combining explicit reasoning, exploration, refinement, and tool use produces agents that are not just *automated* but truly *autonomous* — able to plan, act, and solve complex problems without direct supervision.

## Appendix A: the prompt-level companion
The book's [[agentic-design-patterns-appendix-a-prompting|Appendix A (Advanced Prompting Techniques)]] is the **prompt-engineering companion** to this chapter. Where Ch 17 frames reasoning as architectural agent patterns (with multi-agent extensions like [[ChainOfDebates|CoD]]/[[GraphOfDebates|GoD]] and the [[ScalingInferenceLaw|Scaling Inference Law]]), Appendix A presents the *prompt-level* reasoning cluster: [[ChainOfThought|CoT]] (zero-shot *"Let's think step by step"* and few-shot variants), [[SelfConsistency|self-consistency]] (sample diverse high-temperature paths, majority-vote), [[StepBackPrompting|step-back prompting]] (abstract first, then specialize), and [[TreeOfThoughts|Tree of Thoughts]] (branch into multiple concurrent reasoning paths). Appendix A also adds the prompt-engineering best practices for these methods — place the answer **after** the reasoning, and use [[Temperature|temperature]] 0 (greedy decoding) for single-correct-answer tasks like math.

## Connections
- [[agentic-design-patterns-ch17-reasoning]] — source (Ch 17).
- [[agentic-design-patterns-appendix-a-prompting]] — Appendix A, the prompt-level reasoning companion ([[StepBackPrompting]], [[SelfConsistency]], [[ChainOfThought]], [[TreeOfThoughts]]).
- [[AgenticDesignPatterns]] / [[AgenticDesignPattern]] / [[AntonioGulli]] — book hub, meta-concept, author.
- [[ChainOfThought]] / [[TreeOfThoughts]] / [[react]] / [[Reflection]] / [[SelfCritique]] — the foundational reasoning techniques.
- [[ProgramAidedLanguageModel]] / [[DSPyProgramOfThought]] — code-execution offloading.
- [[rlvr]] — training behind variable-thinking-time reasoning models.
- [[ChainOfDebates]] / [[GraphOfDebates]] / [[MultiAgentSystemSearch]] — multi-agent reasoning frameworks.
- [[DeepResearch]] — the agentic-research culmination of the chapter.
- [[ScalingInferenceLaw]] — the chapter's core performance principle.
- [[TestTimeCompute]] / [[testtimescaling]] / [[parallelreasoning]] / [[selfconsistency]] — the inference-compute family.
- [[Planning]] / [[multiagentsystems]] / [[MultiAgentCollaboration]] — adjacent patterns the chapter composes with.
- [[2402.01817-llm-modulo|LLM-Modulo]] — the critical counter-stance on whether these techniques constitute genuine reasoning.
