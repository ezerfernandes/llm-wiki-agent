---
title: "Chapter 4 — Reflection (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, reflection, self-correction, self-critique, generator-critic, producer-reviewer, iterative-refinement, control-flow]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 4 of [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] presents **[[Reflection]]** as the fourth of the 21 patterns: an agent evaluating its own work, output, or internal state and using that evaluation to iteratively improve or refine its response — a form of [[Reflection|self-correction]]/self-improvement that introduces a **feedback loop** on top of the control-flow trio of [[PromptChaining|chaining]] (Ch 1), [[Routing|routing]] (Ch 2), and [[Parallelization|parallelization]] (Ch 3). The chapter's central architectural move is separating the work into a **Producer** (generator) and a **Critic** (reviewer/evaluator) — the "[[Reflection|Generator-Critic]]" / "Producer-Reviewer" model — because a dedicated critic with a fresh persona avoids the "cognitive bias" of an agent reviewing its own work. It closes with two hands-on examples — a [[LangChain]] LCEL `run_reflection_loop` driving [[openai|OpenAI]]'s GPT-4o through generate→critique→refine iterations (the critic emits `CODE_IS_PERFECT` or a bulleted critique as a stopping signal), and a [[GoogleADK|Google ADK]] `SequentialAgent` wiring a `DraftWriter` generator `LlmAgent` to a `FactChecker` reviewer `LlmAgent` via shared session state. (Agentic Design Patterns, PDF pp 65–78.)

## Key Claims
- **Reflection is a self-correction feedback loop.** Unlike a sequential chain (output passed directly to the next step) or routing (which chooses a path), reflection has the agent *examine* its own output (or the process that generated it), identify issues, and use those insights to generate a better version or modify future actions. It is the pattern you reach for when an agent's initial output or plan "might not be optimal, accurate, or complete."
- **The canonical process is a 4-step cycle**: (1) **Execution** — perform the task / generate initial output; (2) **Evaluation/Critique** — analyze the result (often via another LLM call or a set of rules) for factual accuracy, coherence, style, completeness, or adherence to instructions; (3) **Reflection/Refinement** — use the critique to decide how to improve (regenerate output, adjust parameters, or modify the plan); (4) **Iteration** (optional but common) — re-execute and repeat until satisfactory or a stopping condition is met.
- **The Producer–Critic (Generator-Critic / Producer-Reviewer) separation is the key, highly effective implementation.** A **Producer agent** focuses entirely on generating content; a **Critic agent** has a *different set of instructions and a distinct persona* (e.g. "You are a senior software engineer," "You are a meticulous fact-checker") and its sole purpose is to evaluate the Producer's output against specific criteria, find flaws, and provide structured feedback. The feedback is passed back to the Producer to generate a refined version.
- **Separation of concerns prevents the "cognitive bias" of self-review.** Two specialized agents (or two LLM calls with distinct system prompts) "often yields more robust and unbiased results" than single-agent self-reflection, because the Critic approaches the output with a fresh perspective dedicated entirely to finding errors. (This is the book's framing of [[SelfBiasJudge|self-bias]].)
- **Reflection synergizes with goal-setting/monitoring (Ch 11) and memory (Ch 8).** A goal provides the benchmark for self-evaluation while monitoring tracks progress; reflection then acts as the *corrective engine*. Effectiveness is "significantly enhanced when the LLM keeps a memory of the conversation" — without memory each reflection is a self-contained event; with memory each cycle builds on the last, enabling cumulative, context-aware refinement and learning from past critiques.
- **Practical applications**: creative writing/content generation (draft → critique for flow/tone/clarity → rewrite), code generation & debugging (write → run tests/static analysis → fix), complex multi-step problem solving (propose step → evaluate/backtrack), summarization (draft summary → compare against source → refine), planning & strategy (generate plan → simulate/evaluate feasibility → revise), and conversational agents (review history + last message to maintain coherence). Reflection "adds a layer of meta-cognition to agentic systems."
- **LangChain hands-on example**: a single-file `run_reflection_loop()` over `ChatOpenAI(model="gpt-4o", temperature=0.1)` that asks for a `calculate_factorial` Python function. It maintains a `message_history` for context, generates in iteration 0 and refines afterward, then a `reflector_prompt` (a `SystemMessage` casting the model as "a senior software engineer and an expert in Python" doing "a meticulous code review") critiques the code. The critic must respond with the single phrase `CODE_IS_PERFECT` if satisfactory — which the loop treats as the **stopping condition** — otherwise a bulleted list of critiques, appended to history for the next refinement (`max_iterations = 3`).
- **Google ADK hands-on example**: a Generator-Critic structure using `from google.adk.agents import SequentialAgent, LlmAgent`. A `generator` (`DraftWriter`) `LlmAgent` writes a draft and saves it to `output_key="draft_text"`; a `reviewer` (`FactChecker`) `LlmAgent` reads `draft_text`, verifies factual accuracy, and emits a structured dictionary (`status`: "ACCURATE"/"INACCURATE" + `reasoning`) to `output_key="review_output"`. A `SequentialAgent(name="WriteAndReview_Pipeline", sub_agents=[generator, reviewer])` enforces that the generator runs before the reviewer. (A note adds that ADK's `LoopAgent` is an alternative implementation for true iteration.)
- **Trade-offs / rule of thumb**: use reflection when output quality, accuracy, and detail matter more than speed and cost. The iterative loop raises **cost and latency** (each refinement may require a new LLM call) and is **memory-intensive** (conversation history expands with each iteration: initial output + critique + refinements), risking context-window overflow or API throttling. A single reflection step can be done in LangChain/LangGraph, ADK, or Crew.AI, but *true iterative* reflection "typically involves more complex orchestration" (stateful workflows like [[LangGraph]]).

## Key Quotes
> "The Reflection pattern involves an agent evaluating its own work, output, or internal state and using that evaluation to improve its performance or refine its response. It's a form of self-correction or self-improvement, allowing the agent to iteratively refine its output or adjust its approach based on feedback, internal critique, or comparison against desired criteria." — Reflection Pattern Overview, p 1 (PDF p 65)

> "A key and highly effective implementation of the Reflection pattern separates the process into two distinct logical roles: a Producer and a Critic. This is often called the 'Generator-Critic' or 'Producer-Reviewer' model. While a single agent can perform self-reflection, using two specialized agents (or two separate LLM calls with distinct system prompts) often yields more robust and unbiased results." — p 2 (PDF p 66)

> "This separation of concerns is powerful because it prevents the 'cognitive bias' of an agent reviewing its own work. The Critic agent approaches the output with a fresh perspective, dedicated entirely to finding errors and areas for improvement." — p 2 (PDF p 66)

> "If the code is perfect and meets all requirements, respond with the single phrase 'CODE_IS_PERFECT'. Otherwise, provide a bulleted list of your critiques." — `reflector_prompt` SystemMessage, LangChain example (PDF p 71)

> "This pattern is memory-intensive; with each iteration, the conversational history expands, including the initial output, critique, and subsequent refinements." — At Glance / Key Takeaways (PDF pp 73–74)

## Connections
- [[Reflection]] — the chapter's named pattern (primary concept; augmented/created from this chapter).
- [[AgenticDesignPatterns]] — book hub; this is Chapter 4 of the 21 patterns.
- [[AgenticDesignPattern]] — the meta-concept of reusable agent design patterns.
- [[AntonioGulli]] — author.
- [[PromptChaining]] / [[Routing]] / [[Parallelization]] — Chs 1–3's control-flow patterns; reflection adds a feedback loop on top of them.
- [[SelfCritique]] / [[SelfEvaluation]] — the single-agent self-review mechanism the chapter generalizes ("a single agent can perform self-reflection").
- [[Reflexion]] — the named technique (Shinn et al. 2023) that separates evaluation from self-reflection; the chapter's Producer-Critic separation is the agentic-framework realization of the same idea (its references cite *Training Language Models to Self-Correct via RL*, arXiv:2409.12917).
- [[ActorCriticAgent]] — the RL actor (proposer) / critic (evaluator) decomposition that the Generator-Critic model mirrors at the prompt level.
- [[LLMAsAJudge]] / [[SelfBiasJudge]] — the Critic is an LLM-as-judge for self-eval; using a *separate* critic persona is the book's mitigation of self-bias / "cognitive bias."
- [[LangChain]] / [[LangGraph]] / [[GoogleADK]] / [[CrewAI]] — frameworks; LangChain LCEL `run_reflection_loop`, ADK `SequentialAgent(generator, reviewer)` + `LoopAgent`, LangGraph for stateful iterative loops, Crew.AI named as a viable single-step option.
- [[openai|OpenAI]] — the LangChain example drives `gpt-4o` via `langchain_openai.ChatOpenAI`.
- [[gemini|Gemini]] — named (with OpenAI/Anthropic) as an interchangeable model provider for the example.
- [[FeedbackLoop]] — the general control-structure abstraction reflection instantiates.
- [[MemoryManagement]] — Ch 8; conversational memory makes reflection cumulative rather than self-contained.
- [[GoalSettingAndMonitoring]] — Ch 11; goals provide the benchmark and monitoring the signal that reflection corrects against.
- [[TestTimeCompute]] — reflection is an inference-time-scaffolding strategy (spend more compute on critique/refinement to raise quality).

## Contradictions
- None found. The chapter's agentic-pattern framing of "reflection" is consistent with the wiki's existing [[SelfCritique]] / [[SelfEvaluation]] / [[Reflexion]] / [[ActorCriticAgent]] pages — it generalizes single-agent self-critique into a Producer-Critic separation and explicitly acknowledges the [[SelfBiasJudge|self-bias]] limitation those pages document (offering the separate-critic persona as the mitigation). It complements rather than conflicts with Chs 1–3's control-flow patterns.
