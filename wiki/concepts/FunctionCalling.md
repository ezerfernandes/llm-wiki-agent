---
title: "Function Calling"
type: concept
tags: [agents, tools, api, llm]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
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

## Connections

- [[Agent]] — the application surface.
- [[ToolInventory]] — what function calling exposes.
- [[react|ReAct]] — the reasoning loop function calling sits inside.
- [[StructuredOutput]] — function-calling outputs are a special case.
- [[PlanningFailure]] — the failure-mode taxonomy.
- [[ai-engineering-ch06-rag-agents]] — primary source.
