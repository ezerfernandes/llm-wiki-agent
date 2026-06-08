---
title: "Program-Aided Language Models (PALMs)"
type: concept
tags: [reasoning, code-execution, neuro-symbolic, agentic-design-patterns, tool-use]
sources: [agentic-design-patterns-ch17-reasoning]
last_updated: 2026-06-07
---

# Program-Aided Language Models (PALMs)

**Program-Aided Language Models (PALMs)** integrate LLMs with **symbolic reasoning** by letting the model **generate and execute code** (e.g. Python) as part of its problem-solving process. Documented as one of the [[ReasoningTechniques|Reasoning Techniques]] in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] ([[agentic-design-patterns-ch17-reasoning|Ch 17]]; Gao et al., "Program-Aided Language Models," 2023).

## How it works

PALMs **offload complex calculations, logical operations, and data manipulation to a deterministic programming environment**. When faced with a symbolic challenge, the model produces code, executes it, and converts the results back into natural language. This hybrid methodology combines the LLM's understanding and generation abilities with **precise computation**, addressing tasks where LLMs alone exhibit limitations in accuracy or consistency.

## Why it matters in agentic systems

It lets agents perform **more accurate and reliable actions** by leveraging precise computation alongside their reasoning. Code execution acts as a deterministic, sound critic in a way that LLM prose-reasoning is not — directly complementary to the [[2402.01817-llm-modulo|LLM-Modulo]] argument that LLM reasoning needs external verifiers, and the same principle behind the wiki's [[DSPyProgramOfThought|`dspy.ProgramOfThought`]] receipt where code execution recovers a [[ChainOfThought|CoT]] arithmetic failure.

## Code example (Ch 17)

The chapter illustrates PALMs with **Google ADK**: a root agent composes a `search_agent` (Google Search specialist) and a `coding_agent` configured with `BuiltInCodeExecutor`, exposed as tools:

```python
from google.adk.tools import agent_tool
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.code_executors import BuiltInCodeExecutor

coding_agent = Agent(model='gemini-2.0-flash', name='CodeAgent',
                     instruction="You're a specialist in Code Execution",
                     code_executor=[BuiltInCodeExecutor])
root_agent = Agent(name="RootAgent", model="gemini-2.0-flash",
                   tools=[agent_tool.AgentTool(agent=search_agent),
                          agent_tool.AgentTool(agent=coding_agent)])
```

## Connections
- [[agentic-design-patterns-ch17-reasoning]] — source (Ch 17).
- [[ReasoningTechniques]] — the chapter's parent pattern.
- [[DSPyProgramOfThought]] — the DSPy Module implementing the same Program-of-Thought pattern (Chen et al. 2022), with the canonical CoT-fails-then-PoT-succeeds receipt.
- [[ChainOfThought]] — prose-reasoning counterpart that PALMs replaces with executable code for computable tasks.
- [[CodeInterpreter]] / [[LocalSandbox]] — code-execution environments.
- [[GoogleADK]] — the framework used in the chapter's example (`BuiltInCodeExecutor`).
- [[gemini|Gemini]] — the model (`gemini-2.0-flash`) in the example.
- [[ToolUse]] / [[FunctionCalling]] — code execution as a tool the agent invokes.
- [[NeuroSymbolicAI]] — the broader LLM + symbolic-computation lineage.
- [[2402.01817-llm-modulo|LLM-Modulo]] — code execution as a sound external critic.
