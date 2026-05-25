---
title: "Agent (Oz)"
type: concept
tags: [programming-languages, concurrency, oz, actor-model]
sources: [vol1000-oz-programming-model, ai-engineering-ch06-rag-agents, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Agent

In the [[OPM|Oz Programming Model]]: *"a computational abstraction processing messages received through a [[Port|port]]. It maintains an internal state and may send messages to other agents."* Cited in [[vol1000-oz-programming-model|Smolka 1995]] Section 11.

## Specification

An agent's functionality is given by a **serve procedure**:

$$\text{Serve}: \text{State} \times \text{Message} \to \text{NewState}$$

The constructor:

```oz
proc {NewAgent Serve Init Port}
  local Stream Feed in
    {NewPort Stream Port}
    {Feed Stream Init}
    proc {Feed Ms State}
      if Message Mr NewState in Ms=Message|Mr then
        {Serve State Message NewState}  {Feed Mr NewState}
      else true fi
    end
  end
end
```

The recursive `Feed` procedure traverses the incoming message stream, dispatching each message to `Serve` and threading the resulting state into the next call.

## Worked example: queue agent

```oz
{NewName Enqueue}
{NewName Dequeue}
proc {QueueServe State Message NewState}
  if First Last in State=First|Last then
    if X NewLast in Message=Enqueue|X then
      Last=X|NewLast   NewState=First|NewLast
    else
      if X NewFirst in Message=Dequeue|X then
        First=X|NewFirst  NewState=NewFirst|Last
      else true fi
    fi
  else true fi
end
```

Dequeue-on-empty is handled elegantly by **logic variables** — the request waits in a queue of unserved dequeues, served as soon as items arrive. *"This synchronization idea can be expressed elegantly by means of logic variables."*

## Position under distribution

> *"Agents are stationary and objects are mobile."* When a message is sent to an agent, *"the message is served at the site where the agent was created (there is a task waiting for the next message sent)."* By contrast, an [[OPMObject|object]] applied to a message serves at the *application* site.

## In this wiki

The wiki's first **agent-model** anchor. Distinct from the modern LLM-agent vocabulary ([[AgenticAI]], [[react|`dspy.ReAct`]], [[CustomerServiceAgent]] etc.) — Smolka's agent is a concurrent-PL construct (state + message dispatch via stream), not an LLM-driven decision loop. The two concepts share a name but operate in different semantic universes; this entry establishes the **OPM-original** meaning for future synthesis.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

The LLM-agent meaning — the *other* sense of "agent" the wiki carries — gets its deep-dive in Ch 6 of *AI Engineering*. [[ChipHuyen|Huyen]] inherits the [[StuartRussell|Russell]] & [[PeterNorvig|Norvig]] *AIMA* (1995) definition:

> *"An agent is anything that can perceive its environment and act upon that environment. This means that an agent is characterized by the environment it operates in and the set of actions it can perform."*

An LLM-agent decomposes into **environment** + **[[ToolInventory|tool inventory]]** + **AI planner** — three components Huyen develops separately across the chapter. Examples that anchor the definition: ChatGPT (web + code execution + image generation), RAG systems (text retrievers + image retrievers + SQL executors), [[SWEAgent]] (computer + filesystem + text edits).

The Oz-OPM agent of this page and the LLM-agent of *AI Engineering* Ch 6 are **homophones, not synonyms** — both are *"stateful entity dispatching on messages"* at a high level, but the Oz version's state is logical-variable-threaded and the LLM version's state is parametric + retrieved memory. For the LLM-agent meaning, see [[AgenticAI]], [[ToolInventory]], [[Planning]], [[CompoundErrorAccumulation]], [[FunctionCalling]], [[react|ReAct]], [[reflexion|Reflexion]], [[KnowledgeAugmentation]] / [[CapabilityExtension]] / [[WriteAction]].

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

[[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]] gives the LLM-agent its **first runnable [[LangChain]] receipt** in the wiki. Ch 7's framing:

> *"One of the most promising concepts in LLMs is their ability to determine the actions they can take. This idea is often called agents, systems that leverage a language model to determine which actions they should take and in what order."* — Ch 7

Ch 7's structural decomposition: **agents extend chains with two vital components** —

1. **Tools** the agent can use to do things it could not do itself ([[ToolInventory|tool inventory]]).
2. **The agent type** that plans the actions to take or tools to use (here: [[react|ReAct]], operationalized via [[LangChainAgent|`create_react_agent`]]).

Concrete operationalization: a two-tool [[LangChainAgent|`AgentExecutor`]] (DuckDuckGo + llm-math) running on [[ChatGPT|GPT-3.5-turbo]] — Ch 7 explicitly notes that the local [[Phi3Mini|Phi-3-mini]] is *"not sufficient to run these examples"*, surfacing the **agent-capability cliff** Huyen Ch 6 named via [[CompoundErrorAccumulation|compound-error accumulation]]. The chapter ends with the load-bearing **safety caveat** that *"there is no [[humanintheloop|human in the loop]]"* in the autonomous agent path.
