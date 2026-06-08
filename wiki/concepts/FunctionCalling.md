---
title: "Function Calling"
type: concept
tags: [agents, tools, api, llm, tool-calling, json-schema, agentic-design-patterns]
sources: [ai-engineering-ch06-rag-agents, agentic-design-patterns-ch05-tool-use, agentic-design-patterns-ch10-mcp, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# Function Calling

**Function calling** is the model-provider API surface for **agent tool use** — the protocol by which an LM tells the application *"call this tool, with these arguments"* and receives the tool's output as a structured observation. Per [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]:

> *"Many model providers offer tool use for their models, effectively turning their models into agents. A tool is a function. Invoking a tool is, therefore, often called function calling."*

## The canonical API shape

Three core operations:

1. **Create a tool inventory** — declare each tool by name, parameter schema, and docstring/description.
2. **Specify per-query tool availability** — different queries may surface different tools.
3. **Choose tool-use mode**:
   - `required` — model must use at least one tool.
   - `none` — model must not use any tool.
   - `auto` — model decides.

## The `lbs_to_kg(40)` example

For *"How many kilograms are 40 pounds?"*, the agent generates:

```python
ModelResponse(
   finish_reason='tool_calls',
   message=Message(
       content=None,
       role='assistant',
       tool_calls=[
           ToolCall(
               function=Function(
                   arguments='{"lbs":40}',
                   name='lbs_to_kg'),
               type='function')
       ])
)
```

The application invokes `lbs_to_kg(lbs=40)` and feeds the result back into the next reasoning step.

## What function-calling APIs guarantee — and don't

> *"Some function calling APIs will make sure that only valid functions are generated, though they won't be able to guarantee the correct parameter values."*

The valid-function guarantee comes from constrained decoding (the model's output is masked to the tool inventory). The correct-parameter guarantee can't be made because **parameter values are content** — they're as fallible as any other generated text. Huyen's practical guidance: *"Always ask the system to report what parameter values it uses for each function call. Inspect these values to make sure they are correct."*

## Failure modes (see [[PlanningFailure]])

- **Invalid tool**: model generates `bing_search` when only `google_search` exists.
- **Valid tool, invalid parameters**: calls `lbs_to_kg` with two parameters when it requires one.
- **Valid tool, incorrect parameter values**: calls `lbs_to_kg(lbs=100)` when the user said 120.

## Agentic Design Patterns (Gulli) perspective ([[agentic-design-patterns-ch05-tool-use]])

[[agentic-design-patterns-ch05-tool-use|Chapter 5]] of [[AgenticDesignPatterns|*Agentic Design Patterns*]] treats function calling as the concrete implementation of the [[ToolUse|Tool Use]] pattern, while preferring the broader term **"tool calling"**: "While 'function calling' aptly describes invoking specific, predefined code functions, it's useful to consider the more expansive concept of 'tool calling'" — a tool can also be a complex API endpoint, a database request, or an instruction directed at another agent.

Gulli's loop matches Huyen's API shape but emphasizes the **agent-vs-tool boundary**: the LLM only *generates* the structured (JSON) call naming the tool + arguments; the **agentic/orchestration layer intercepts and executes it**, then feeds the observation back. Frameworks ([[LangChain]] `@tool` + `create_tool_calling_agent`, [[CrewAI]] `@tool`, [[GoogleADK|Google ADK]] `FunctionTool`/pre-built tools) wrap this, "often leveraging the native function calling capabilities of modern LLMs like those in the [[gemini|Gemini]] or [[openai|OpenAI]] series."

The chapter also contrasts function calling with [[VertexAIExtensions|Vertex AI extensions]] on the execution axis: **"Vertex AI automatically executes extensions, whereas function calls require manual execution by the user or client."**

### MCP vs. function calling — Ch 10's five-axis contrast ([[agentic-design-patterns-ch10-mcp]])

[[agentic-design-patterns-ch10-mcp|Chapter 10]] sharpens the function-calling/[[ModelContextProtocol|MCP]] distinction into a five-axis table, treating **tool function calling** as the *direct, proprietary, one-to-one, statically-declared* mechanism and **MCP** as the *open, federated, client-server, dynamically-discoverable* framework:

| Axis | Tool Function Calling | MCP |
|---|---|---|
| Standardization | Proprietary, vendor-specific | Open, standardized |
| Scope | Direct request to one predefined function | Broad discover-and-communicate framework |
| Architecture | One-to-one (LLM ↔ app's tool logic) | Client-server (clients ↔ many servers) |
| Discovery | LLM explicitly told which tools exist | Dynamic — client queries server's catalog |
| Reusability | Tightly coupled to the app + LLM | Standalone, reusable MCP servers |

Gulli's analogy: function calling = "a specific set of custom-built tools, like a particular wrench and screwdriver" (good for a fixed workshop); MCP = "a universal, standardized power outlet system" any compliant tool can plug into. The rule of thumb: simple apps with a fixed, limited set of functions → function calling suffices; complex, interconnected, evolving systems → MCP. Note both still rest on the LLM's native function-calling capability at the lowest layer — MCP standardizes *discovery, transport, and reuse* on top of it, it does not replace the call mechanism itself.

## Connections

- [[Agent]] — the application surface.
- [[ToolUse]] — the pattern function calling implements.
- [[ToolInventory]] — what function calling exposes.
- [[react|ReAct]] — the reasoning loop function calling sits inside.
- [[StructuredOutput]] — function-calling outputs are a special case.
- [[ModelContextProtocol|MCP]] — standardizes tool definition across frameworks (function calling's per-framework wrappers are what MCP supersedes for portability).
- [[VertexAIExtensions]] — auto-executed alternative; differs from function calling on who runs the tool.
- [[PlanningFailure]] — the failure-mode taxonomy.
- [[ai-engineering-ch06-rag-agents]] / [[agentic-design-patterns-ch05-tool-use]] / [[agentic-design-patterns-ch10-mcp]] — primary sources.
- [[agentic-design-patterns-appendix-a-prompting]] — Gulli's Appendix A restates function calling at the prompt level: the model interprets tool descriptions, emits a structured JSON `tool_code`/`tool_name`/`parameters` call (the `get_current_weather`/London example), and the agentic system executes it.
