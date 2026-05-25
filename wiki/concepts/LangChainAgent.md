---
title: "LangChain Agent (create_react_agent + AgentExecutor)"
type: concept
tags: [langchain, agent, react, tool-use, orchestration]
sources: [hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# LangChain Agent (`create_react_agent` + `AgentExecutor`)

The [[LangChain]] **agent-construction surface** — `langchain.agents.create_react_agent` builds a [[react|ReAct]] agent from `(llm, tools, prompt)`; `langchain.agents.AgentExecutor` wraps that agent into a runnable executor that drives the Thought / Action / Observation loop until completion (or until `max_iterations` is hit). The wiki's first runnable [[LangChain]]-native ReAct receipt.

## Four-line agent construction

```python
from langchain.agents import AgentExecutor, create_react_agent

agent = create_react_agent(openai_llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
)
agent_executor.invoke({"input": "What is the current price of a MacBook Pro in USD? ..."})
```

## The canonical ReAct prompt template

`create_react_agent` expects a prompt with the standard ReAct fields (`{tools}`, `{tool_names}`, `{input}`, `{agent_scratchpad}`):

```
Answer the following questions as best you can. You have access to the following tools:
{tools}
Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
Begin!
Question: {input}
Thought:{agent_scratchpad}
```

The `{agent_scratchpad}` is where `AgentExecutor` accumulates prior `Thought/Action/Observation` triples — the LangChain-native realization of the [[react|ReAct]] trajectory.

## The MacBook Pro worked example

Ch 7's canonical benchmark for the agent:

> *"What is the current price of a MacBook Pro in USD? How much would it cost in EUR if the exchange rate is 0.85 EUR for 1 USD?"*

Tools: a [[DuckDuckGoSearchResults|DuckDuckGo search]] wrapper + [[LLMMathTool|llm-math]] calculator. The agent runs **two ReAct cycles**:

1. **Cycle 1**: Thought → call DuckDuckGo → Observation: *"$2,249.00"*
2. **Cycle 2**: Thought → call llm-math with `2249 * 0.85` → Observation: *"1911.65"*

Final answer: *"The current price of a MacBook Pro in USD is $2,249.00. It would cost approximately 1911.65 EUR with an exchange rate of 0.85 EUR for 1 USD."*

## The capability ceiling

Ch 7 switches from [[Phi3Mini|Phi-3-mini]] to [[ChatGPT|GPT-3.5-turbo]] for the agent example. Per Ch 7:

> *"These autonomous processes generally require an LLM that is powerful enough to properly follow complex instructions. The LLM that we used thus far is relatively small and not sufficient to run these examples. Instead, we will be using OpenAI's GPT-3.5 model as it follows these complex instructions more closely."*

This is the chapter's honest acknowledgment that the GPU-poor / local-Phi-3 commitment has a ceiling at agents — a structural capability cliff that mirrors [[ai-engineering-ch06-rag-agents|Huyen Ch 6's]] [[CompoundErrorAccumulation|compound-error-accumulation]] argument for why agents need stronger models than chat applications.

## The safety caveat the chapter ends on

> *"By creating this relatively autonomous behavior, we are not involved in the intermediate steps. As such, there is no [[humanintheloop|human in the loop]] to judge the quality of the output or reasoning process. This double-edged sword requires a careful system design to improve its reliability."* — Ch 7

## Position relative to other ReAct receipts in the wiki

| Receipt | Framework | Signature surface |
|---|---|---|
| `dspy.ReAct(Signature, tools=[...])` | [[DSPy]] | Signature-parameterized; `pred.trajectory` introspection |
| **`create_react_agent(llm, tools, prompt) + AgentExecutor`** | [[LangChain]] | Template-parameterized; `verbose=True` prints trajectory inline |

Same underlying [[react|ReAct]] scaffold; different ergonomics. The DSPy path types the I/O at the Signature level; the LangChain path leaves I/O as free-form text wrapped by the ReAct prompt template.

## Connections

- [[LangChain]] — the framework.
- [[react|ReAct]] — the framework's prompting backbone.
- [[Agent]] / [[AgenticAI]] — the broader concept.
- [[ToolInventory]] / [[ToolUse]] — the agent's action surface.
- [[DuckDuckGoSearchResults]] / [[LLMMathTool]] — the two tools Ch 7 uses.
- [[LangChainLlamaCpp]] / [[ChatGPT]] — the LLMs (Phi-3 insufficient → GPT-3.5).
- [[PromptTemplate]] — the ReAct prompt is itself a PromptTemplate.
- [[humanintheloop]] — what's missing from the autonomous agent loop.
- [[CompoundErrorAccumulation]] — the agent-reliability risk Ch 7's safety caveat echoes.
- [[hands-on-llm-ch07-advanced-text-generation]] — primary source.

## From Hands-On LLMs Ch 7

Ch 7's agent primitive. The chapter calls `create_react_agent` *"the driving force of many agent-based systems"* and uses `AgentExecutor(verbose=True)` to print the trajectory inline as the agent runs — making the Thought/Action/Observation cycles visible to the reader. This is the **wiki's first runnable LangChain-native ReAct agent**, complementing the existing [[DSPy]]-native `dspy.ReAct` receipts in [[dspy-modules]] / [[dspy-tools]] / [[dspy-customer-service-agent]].
