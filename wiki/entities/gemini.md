---
title: "Gemini"
type: entity
tags: [model-family, multimodal, frontier, google, deepmind]
sources: [2312.11805-gemini, 2603.19247-prompt-optimization-jailbreaking, ai-engineering-ch01-intro, agentic-design-patterns-ch05-tool-use, agentic-design-patterns-ch06-planning, agentic-design-patterns-ch08-memory-management, agentic-design-patterns-ch11-goal-setting, agentic-design-patterns-ch16-resource-aware]
last_updated: 2026-06-07
---

# Gemini

Family of natively multimodal foundation models from [[GoogleDeepMind]], introduced in [[2312.11805-gemini]] (December 2023). Built on [[Transformer]] decoders with [[MultiQueryAttention]]; trained jointly across text, image, audio, and video; deployed in three sizes:

| Variant | Role | Notes |
|---|---|---|
| **Ultra** | Frontier reasoning | First model to exceed human-expert [[MMLU]] (90.04%); SOTA on 30/32 benchmarks reported in 1.0. |
| **Pro** | Cost/latency-optimized | Powers default Gemini consumer chat and base of [[AlphaCode2]]. |
| **Nano-1 / Nano-2** | On-device | 1.8B / 3.25B params; 4-bit quantized; [[KnowledgeDistillation|distilled]] from larger Geminis. |

## Product variants

- **Gemini Apps** — consumer chat. Originally branded as **[[Bard]]** (powered by [[PaLM2]]); rebranded to *Gemini* (with Pro) and *Gemini Advanced* (with Ultra).
- **Gemini APIs** — developer-facing via Google AI Studio and Cloud Vertex AI.

Both variants share pre-training but diverge in post-training: instruction following, tool-use control loop (tools rendered as code blocks), multilinguality (40+ languages), multimodal vision SFT, and safety SFT/RLHF.

## Place in the wiki

Gemini is the second **substrate-defining** entry in the LLM corpus alongside [[1706.03762-attention-is-all-you-need]]. The 2017 paper defines the *architecture*; Gemini 1.0 defines the *frontier-multimodal-deployment template* — three-size family, native multimodality, [[RLHF]] flywheel, structured responsible-deployment review, [[DangerousCapabilities]] evaluation. Most 2026 agent papers in this wiki implicitly assume a Gemini-class base model when they discuss harnesses, memory, or skill verification.

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] in *AI Engineering* Ch 1 uses Gemini as the **canonical case study for prompt-format-dependence in benchmark scores**. From the December 2023 Gemini technical report:

| Model | Prompt format | MMLU |
|---|---|---|
| Gemini Ultra | CoT@32 | **90.04%** |
| Gemini Pro | CoT@8 | 79.13% |
| GPT-4 | 5-shot | 86.4% |
| Gemini Ultra | 5-shot (matched) | 83.7% |

Huyen's takeaway: *"Different prompts can cause models to perform very differently."* Google's claim that Gemini Ultra beats GPT-4 on MMLU only holds at CoT@32; at matched 5-shot, GPT-4 wins. This becomes Ch 1's anchor anecdote for the importance of **[[PromptEngineering|prompt engineering]] in [[Evaluation|evaluation]]**.

Gemini is also Ch 1's primary example of a **natively multimodal [[FoundationModel|foundation model]]** that justifies the *"foundation model"* umbrella term over the narrower *"LLM"*.

## Native function/tool calling (Agentic Design Patterns Ch 5)
[[agentic-design-patterns-ch05-tool-use|Ch 5 (Tool Use)]] of [[AgenticDesignPatterns|*Agentic Design Patterns*]] names the Gemini series (with the [[openai|OpenAI]] series) as the modern LLMs whose **native function calling** capabilities the agent frameworks ([[LangChain]], [[LangGraph]], [[GoogleADK|ADK]]) leverage to generate structured [[ToolUse|tool-use]] requests. The chapter's runnable LangChain tool-calling agent uses `ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)`; the ADK examples drive `gemini-2.0-flash` / `gemini-2.0-flash-exp`. See [[ToolUse]] / [[FunctionCalling]].

## DeepResearch (Agentic Design Patterns Ch 6)
[[agentic-design-patterns-ch06-planning|Ch 6 (Planning)]] presents **Google Gemini DeepResearch** as the flagship real-world exemplar of the [[Planning]] pattern (see [[DeepResearch]]): a Gemini-based agentic system that deconstructs a prompt into a multi-point research plan (presented to the user for review/edit before execution), then runs an asynchronous, iterative loop that queries **Google Search** as a tool, identifies knowledge gaps, and synthesizes a structured, citation-rich multi-page report. The Key Takeaway: Google Deep Research "reflects, plans, and executes."

## Memory extraction in Vertex AI Memory Bank (Agentic Design Patterns Ch 8)
[[agentic-design-patterns-ch08-memory-management|Ch 8 (Memory Management)]] gives Gemini an infrastructural role in [[MemoryManagement|agent memory]]: [[VertexAiMemoryBank|Vertex AI Memory Bank]] *"uses Gemini models to asynchronously analyze conversation histories to extract key facts and user preferences,"* which are then stored per user and consolidated (resolving contradictions). Gemini is thus the extraction/consolidation engine behind the managed [[LongTermMemory|long-term-memory]] service — and `gemini-2.0-flash` is the model driving the chapter's [[GoogleADK|ADK]] and [[crewai|CrewAI]] memory examples. See [[VertexAiMemoryBank]].

## Crew-of-agents for goal monitoring (Agentic Design Patterns Ch 11)
[[agentic-design-patterns-ch11-goal-setting|Ch 11 (Goal Setting and Monitoring)]] notes that the more robust alternative to a single self-judging agent is *"a personal crew of AI agents using Gemini where each has a specific role"* — Peer Programmer, Code Reviewer, Documenter, Test Writer, Prompt Refiner. Separating the Code Reviewer (the judge) from the programmer *"significantly improves objective evaluation,"* connecting Gemini to the role-separated [[MultiAgentCollaboration|multi-agent]] realization of the [[GoalSettingAndMonitoring|goal-monitoring]] pattern. See [[GoalSettingAndMonitoring]].

## Flash vs Pro as a cost tier (Agentic Design Patterns Ch 16)
[[agentic-design-patterns-ch16-resource-aware|Ch 16 (Resource-Aware Optimization)]] makes the **Gemini Flash vs Gemini Pro** split the canonical example of a **cheap-vs-frontier model tier** for [[DynamicModelSelection|dynamic model selection]]: a system *"utilizes a cost-effective language model such as Gemini Flash"* for simple queries and *"a more powerful, but expensive, language model (like Gemini Pro)"* for complex inquiries, gated by budget and time. In the worked travel-planner, Gemini Pro is the high-level **planner** (deep context understanding, logical decisions) while Gemini Flash runs the simple repetitive sub-tasks (flight prices, hotel availability, restaurant reviews). The [[GoogleADK|ADK]] hands-on instantiates this directly (`gemini-2.5-pro` for the `GeminiProAgent`, `gemini-2.5-flash` for the `GeminiFlashAgent`), routed by a [[ModelRouter|Router Agent]]. See [[ResourceAwareOptimization]].

## In [[2603.19247-prompt-optimization-jailbreaking]]

Gemini 2.5 Pro plays **two distinct roles in a single paper**: (i) one of four *target* LMs in the adaptive red-teaming grid — baseline danger **0.645** (the *highest* of the four targets; Gemini is the least safe-by-default at the seed prompts) → SIMBA 0.774; (ii) the [[GEPA]] *reflection model* generating prompt mutations against the other three targets. This dual role gives the paper a within-experiment robustness check: Gemini being both a reflection model and an attack target means any reflection-side bias would have to differentially help GEPA on non-Gemini targets and hurt on Gemini, which the table does not show.
