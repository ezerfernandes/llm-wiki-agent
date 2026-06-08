---
title: "Appendix A — Advanced Prompting Techniques (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, prompt-engineering, prompting, reasoning, context-engineering]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Appendix A of [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] is a comprehensive survey of prompting techniques, reframing prompting as a *disciplined engineering practice* rather than a casual act of asking questions (Agentic Design Patterns, PDF pp 349–377). It progresses from core principles (clarity, conciseness, action verbs, instructions-over-constraints, iteration) through basic example-based techniques (zero/one/few/many-shot), prompt structuring (system/role prompting, delimiters, [[ContextEngineering|context engineering]], structured output with [[Pydantic]]), reasoning techniques ([[ChainOfThought|CoT]], [[SelfConsistency|self-consistency]], [[StepBackPrompting|step-back]], [[TreeOfThoughts|ToT]]), action/interaction techniques ([[ToolUse|tool use]]/[[FunctionCalling|function calling]], [[react|ReAct]]), and advanced/supplementary methods ([[AutomaticPromptEngineering|APE]]/DSPy, iterative refinement, negative examples, analogies, decomposition, [[rag|RAG]], persona pattern, Google Gems, meta-prompting, code prompting, multimodal prompting), closing with a best-practices checklist (sampling controls, output formats, versioning, automated tests). The unifying thesis: these techniques are what convert a probabilistic text generator into a deterministic, trustworthy cognitive engine for an autonomous agent.

## Key Claims
- Prompting is the primary interface to language models; well-designed prompts maximize capability while poor ones yield ambiguous or erroneous output. The objective of [[PromptEngineering|prompt engineering]] is to consistently elicit high-quality responses — a skill of communicating effectively with AI.
- Core principles: **clarity & specificity**, **conciseness**, **using action verbs** (Summarize, Classify, Extract…), **instructions over constraints** (tell the model what to do, not what to avoid), and **experimentation & iteration**.
- The example-based spectrum is **zero-shot → one-shot → few-shot (3–5 examples) → many-shot** (dozens–hundreds, enabled by long-context models like [[gemini|Gemini]]; see [[FewShotLearning]]). For classification few-shot, mix up class ordering to prevent overfitting to sequence.
- **Structuring prompts**: system prompting (overall behavior/persona/safety), role prompting (assign a character to the *model*), delimiters (triple backticks, XML tags, `---`), [[ContextEngineering|context engineering]] (dynamic informational environment: system prompts + external data + implicit data), and **structured output** (JSON/XML/CSV) — requesting JSON forces structure and limits hallucination; validate with [[Pydantic]] via `model_validate_json`.
- **Reasoning techniques**: [[ChainOfThought|CoT]] (think step by step; zero-shot and few-shot variants; place answer *after* reasoning; temperature 0 for single-answer tasks), [[SelfConsistency|self-consistency]] (sample multiple high-temperature reasoning paths, majority-vote the answer), [[StepBackPrompting|step-back prompting]] (first ask a general/abstract question, use its answer as context), [[TreeOfThoughts|Tree of Thoughts]] (explore multiple branching reasoning paths concurrently).
- **Action techniques**: [[ToolUse|tool use]]/[[FunctionCalling|function calling]] (the model emits a structured JSON tool call; the *agentic system* executes it — the model never executes the tool itself) and [[react|ReAct]] (interleaved Thought → Action → Observation loop until a Final Answer).
- **[[AutomaticPromptEngineering|Automatic Prompt Engineering (APE)]]** uses an LLM as a meta-model to generate, evaluate (BLEU/ROUGE/human), and refine candidate prompts; the [[DSPy]] framework generalizes this to *programmatic* prompt optimization over a goldset + objective function, optimizing both few-shot example selection and instructional wording (e.g. via a Bayesian optimizer).
- Supplementary techniques: iterative prompting/refinement (human-driven loop), providing negative examples (used carefully), analogies, factored cognition / decomposition (relates to [[PromptChaining|prompt chaining]]), [[rag|RAG]], the **Persona Pattern** (describe the *user/audience*, vs role prompting which describes the model), **Google Gems** (user-configurable, persistent task-specific Gemini instances), and **meta-prompting** (use an LLM like Gemini to critique and improve your own prompts).
- Best practices checklist: provide examples, design with simplicity, be specific about output, prefer instructions over constraints, control max token length, use variables in prompts, experiment with input formats/writing styles, mix classes in few-shot classification, adapt to model updates, experiment with output formats (JSON/XML), collaborate, follow CoT best practices, document attempts, store prompts in codebases, rely on automated tests/evaluation. Sampling controls ([[Temperature|temperature]], [[Topk|top-k]], [[Topp|top-p]]) are part of the experimentation surface.

## Key Quotes
> "The objective of prompt engineering is to consistently elicit high-quality responses from language models. This requires understanding the capabilities and limitations of the models and effectively communicating intended goals." — Introduction to Prompting

> "Positive instructions are generally more effective than negative constraints. Specifying the desired action is preferred to outlining what not to do." — Core Prompting Principles (Instructions Over Constraints)

> "This methodology posits that the quality of a model's output depends more on the richness of the provided context than on the model's architecture. It signifies a significant evolution from traditional prompt engineering." — Contextual Engineering

> "The model does not execute the tool directly. Instead, it generates a structured output, typically in JSON format, specifying the tool and its parameters. An agentic system then processes this output, executes the tool, and provides the tool's result back to the model." — Tool Use / Function Calling

> "It's a fascinating loop where AI helps us talk better to AI." — Using LLMs to Refine Prompts (The Meta Approach)

> "Mastering this full spectrum of prompting is therefore the definitive skill that elevates a generalist language model from a simple text generator into a truly sophisticated agent, capable of performing complex tasks with autonomy, awareness, and intelligence." — Conclusion

## Connections
- [[AgenticDesignPatterns]] — the book this appendix belongs to; [[AntonioGulli]] — author; [[google|Google]] — affiliation.
- [[PromptEngineering]] — the discipline the appendix surveys; [[Prompting]] — the base activity.
- [[ContextEngineering]] — the broader discipline framed as the evolution of prompt engineering.
- [[PromptChaining]] — the appendix's "Factored Cognition / Decomposition" maps onto this pattern.
- [[ReasoningTechniques]] — Gulli Ch 17 hub; this appendix is the prompt-level companion to it.
- [[ZeroShotLearning]] / [[OneShotPrompting]] / [[FewShotLearning]] — the example-based spectrum (few-shot covers the many-shot evolution).
- [[SystemPrompt]] / [[RolePrompting|role prompting]] / [[Persona]] / [[ContextPrompt]] — prompt-structuring techniques.
- [[StructuredOutputs]] / [[Pydantic]] — machine-readable output + validation.
- [[ChainOfThought]] / [[ZeroShotCoT]] / [[SelfConsistency]] / [[StepBackPrompting]] / [[TreeOfThoughts]] — reasoning techniques.
- [[ToolUse]] / [[FunctionCalling]] / [[react|ReAct]] — action & interaction techniques.
- [[AutomaticPromptEngineering]] / [[APE]] / [[DSPy]] / [[GoogleCloudVertexAI|Vertex AI Prompt Optimizer]] — automated prompt optimization.
- [[rag|RAG]] — external-knowledge grounding technique.
- [[Temperature]] / [[Topk]] / [[Topp]] — sampling controls in the best-practices section.
- [[MultimodalLLM]] — the target of multimodal prompting.
- [[gemini|Gemini]] / [[Kaggle]] — Gems platform; the appendix's primary reference is the Kaggle *Prompt Engineering* whitepaper.

## Contradictions
- None found. The appendix is a high-level survey; its operational presentation of [[TreeOfThoughts|ToT]] (as a useful deliberation method) is in tension with the [[2402.01817-llm-modulo|Kambhampati et al.]] critique already recorded on [[TreeOfThoughts]], but this is the same constructive-vs-critical tension the wiki already documents, not a new contradiction introduced here.
