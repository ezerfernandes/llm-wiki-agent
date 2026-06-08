---
title: "OpenEvolve"
type: concept
tags: [agents, evolutionary-algorithm, coding-agent, self-improvement, agentic-design-patterns]
sources: [agentic-design-patterns-ch09-learning-adaptation]
last_updated: 2026-06-07
---

# OpenEvolve

**OpenEvolve** is an **open-source evolutionary coding agent** that leverages LLMs to iteratively optimize code. It is presented in [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli, Ch 9, [[LearningAndAdaptation|Learning and Adaptation]]) as the open-source counterpart to Google's [[AlphaEvolve]] — orchestrating a pipeline of **LLM-driven code generation, evaluation, and selection** to continuously enhance programs across a wide range of tasks. (github.com/codelion/openevolve)

## Key capabilities

- **Evolves entire code files**, not just single functions.
- **Versatile:** supports multiple programming languages and is compatible with **OpenAI-compatible APIs** for any LLM.
- **Multi-objective optimization**, flexible prompt engineering, and **distributed evaluation** for complex coding challenges.

## Architecture — the evolutionary loop

A central **Controller Orchestration** component manages an asynchronous pipeline optimized for maximum throughput, coordinating four components in an **evolutionary loop**:

| Component | Role |
|---|---|
| **Program Database** | Stores programs and their metrics; supplies past programs |
| **Prompt Sampler** | Creates context-rich prompts from past programs |
| **LLM Ensemble** | Generates code modifications |
| **Evaluator Pool** | Tests programs and assigns scores (metrics fed back to the database) |

The controller requests prompts from the sampler, sends code-generation requests to the LLM ensemble, dispatches generated programs to the evaluator pool, and updates the program database with scored programs — closing the loop.

## Usage sketch

The chapter's code example initializes the system with paths to an initial program, an evaluation file, and a config (`OpenEvolve(initial_program_path=..., evaluation_file=..., config_path=...)`), then runs `evolve.run(iterations=1000)` to evolve an improved program and prints the best program's metrics.

## Connections
- [[AlphaEvolve]] — the Google system OpenEvolve mirrors as open source.
- [[LearningAndAdaptation]] — the Ch 9 pattern; evolutionary self-improvement.
- [[SelfImprovingCodingAgent]] — peer self-improving coding agent.
- [[recursiveselfimprovement]] — broader self-improvement framing.
- [[AgenticDesignPatterns]] — Chapter 9; [[AntonioGulli]].
- [[agentic-design-patterns-ch09-learning-adaptation]] — source page.
