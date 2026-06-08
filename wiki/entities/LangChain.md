---
title: "LangChain"
type: entity
tags: [framework, open-source, llm-orchestration, python, javascript, agentic-design-patterns]
sources: [ai-engineering-ch01-intro, hands-on-llm-ch01-introduction-to-llms, ai-engineering-ch05-prompt-engineering, hands-on-llm-ch07-advanced-text-generation, ai-engineering-ch10-architecture-feedback, hands-on-llm-ch08-semantic-search-and-rag, dspy-yahoo-finance-react-tutorial, agentic-design-patterns-ch01-prompt-chaining, agentic-design-patterns-ch02-routing, agentic-design-patterns-ch03-parallelization, agentic-design-patterns-ch04-reflection, agentic-design-patterns-ch05-tool-use, agentic-design-patterns-ch08-memory-management, agentic-design-patterns-ch11-goal-setting, agentic-design-patterns-ch14-rag, agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# LangChain

Open-source framework for composing LLM-driven applications: prompts, chains, agents, memory, retrievers, vector stores. Available in Python (`langchain`) and JavaScript (`langchain.js`). Cited in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] as one of four open-source AI-engineering tools that within two years of launch **garnered more GitHub stars than Bitcoin** — on track to surpass React and Vue. The set: **LangChain, [[AutoGPT]], [[StableDiffusion]] Web UI, [[Ollama]]**.

LangChain is also Ch 1's evidence for the **JavaScript-ification of AI engineering**: LangChain.js (alongside Transformers.js, OpenAI's Node library, and Vercel's AI SDK) demonstrates the move beyond Python-centric ML toward full-stack-flavored AI engineering.

## In Agentic Design Patterns — Appendix C (frameworks overview)
[[agentic-design-patterns-appendices-bg|Appendix C]] (Gulli) summarizes LangChain as the **foundational, lowest-level** agentic framework: its core strength is the **LangChain Expression Language (LCEL)**, which "pipes" components into a clear, linear sequence where one step's output becomes the next step's input. It is built for **DAG** (Directed Acyclic Graph) workflows — one-directional, no loops — and is **stateless per run**. Recommended uses: simple [[rag|RAG]], summarization, and structured extraction. The appendix's comparison table: LangChain = *Chain (LCEL) / Linear (DAG) / stateless / simple predictable sequences*, vs. [[langgraph|LangGraph]] = *Graph of Nodes / Cyclical / explicit persistent state / complex dynamic stateful agents*. Choose LangChain "when your application has a clear, predictable, and linear flow of steps (A→B→C)."

## DSPy interop — `dspy.Tool.from_langchain(...)`

LangChain community tools (the `langchain_community.tools.*` namespace) are consumable directly from [[DSPy]] programs via the `Tool.from_langchain(...)` classmethod on [[DSPyTools|`dspy.Tool`]]. First wiki receipt: [[dspy-yahoo-finance-react-tutorial|the DSPy Yahoo Finance ReAct tutorial]], which wraps `YahooFinanceNewsTool()` into a `dspy.Tool` and drops it into a [[react|`dspy.ReAct`]] agent's `tools=[...]` list alongside two plain-callable tools — uniformly composed, indistinguishable downstream. This bridge is the **LangChain analog** of `dspy.Tool.from_mcp_tool(...)` ([[DSPyMCP]]) — both confirm `dspy.Tool` is the **single integration point** between DSPy and the outside tool ecosystem. LangChain's community-tool catalog (search, finance, web, databases, etc.) therefore becomes the de facto extension surface for DSPy agents without rewriting individual tools.

## Connections

- [[AIEngineering]] — discipline LangChain serves.
- [[AutoGPT]] / [[Ollama]] / [[StableDiffusion]] — peer tools in the four-OSS-tool cohort.
- [[AIInterface]] — JS-flavored AI-app development.
- [[ai-engineering-ch01-intro]] — primary source.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

[[ChipHuyen|Huyen]] uses LangChain as **the cautionary tale** for [[PromptEngineeringTools|prompt-engineering tools]] in Ch 5 — Figure 5-9 shows typos in LangChain's default critique prompt. The framing:

> "A tool developer might get the wrong template for a given model, construct a prompt by concatenating tokens instead of raw texts, or have a typo in its prompt templates. Figure 5-9 shows typos in a LangChain default critique prompt." — Ch 5

Ch 5 also cites LangChain's **2023 remote-code-execution vulnerability** ([GitHub issues 814 and 1026](https://github.com/langchain-ai/langchain)) as the canonical example of the **remote code/tool execution** risk class for [[PromptAttack|prompt attacks]]. This is the wiki's first record of a concrete LangChain security incident.

Both threads make LangChain emblematic of Ch 5's *"following the keep-it-simple principle, you might want to start by writing your own prompts without any tool"* recommendation. The lesson is not anti-LangChain — Huyen doesn't suggest avoiding it — but pro-inspect-your-tools.

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

Ch 7 of *Hands-On LLMs* is the **wiki's first LangChain-centric source** — the chapter makes LangChain the organizing substrate for four advanced LLM techniques: **Model I/O, Chains, Memory, and Agents**. *"LangChain is one of the earlier frameworks that simplify working with LLMs through useful abstractions. Newer frameworks of note are [[DSPy]] and Haystack."* Ch 7 walks LangChain at runnable-code granularity for the first time in the wiki:

### Model I/O
- **`from langchain import LlamaCpp`** — LangChain's wrapper around [[llamacpp|llama-cpp-python]] for loading [[GGUF]]-quantized models like [[Phi3Mini|Phi-3]]. Signature: `LlamaCpp(model_path, n_gpu_layers, max_tokens, n_ctx, seed, verbose)`.
- **`from langchain.chat_models import ChatOpenAI`** / **`from langchain_openai import ChatOpenAI`** — the chat-model abstraction for [[ChatGPT|GPT-3.5-turbo]] / GPT-4 etc.
- **`llm.invoke(prompt)`** — the universal LLM call.
- **Caveat the chapter exposes**: `LlamaCpp.invoke()` does **not** auto-apply the model's chat template (unlike `transformers.pipeline`). The empty output from `llm.invoke("Hi! My name is Maarten. What is 1 + 1?")` motivates the need for explicit prompt templates and chains.

### Chains
- **`from langchain import PromptTemplate`** — defines a template with `{variable}` placeholders.
- **LCEL pipe operator**: `basic_chain = prompt | llm` — the chain *is* the composition.
- **`from langchain import LLMChain`** — the named-output chain primitive: `LLMChain(llm=llm, prompt=prompt, output_key="title")`.
- **Sequential composition**: `llm_chain = title | character | story` — runs the three sub-chains in order, threading the named outputs forward.
- **The chapter's worked example**: a three-stage story-generation chain (`title` → `character` → `story`) that takes a single `summary` input and emits all three named outputs.

### Memory
- **`from langchain.memory import ConversationBufferMemory`** — stores the full conversation history; appends to the prompt's `chat_history` variable. *"Easiest implementation; ensures no information loss within context window."*
- **`from langchain.memory import ConversationBufferWindowMemory`** — `k=2` retains last 2 turns only; everything before is dropped. The "last-k" operationalization of [[FIFOMemory|FIFO eviction]].
- **`from langchain.memory import ConversationSummaryMemory`** — uses an LLM to summarize the running conversation; takes two LLM calls per turn (user prompt + summarization prompt). *"You could use a smaller LLM for the summarization task to speed up computation."*
- **Trade-off the chapter codifies**: speed vs memory vs accuracy — *"Where ConversationBufferMemory is instant but hogs tokens, ConversationSummaryMemory is slow but frees up tokens to use."*

### Agents
- **`from langchain.agents import load_tools, Tool, AgentExecutor, create_react_agent`** — the agent construction surface.
- **`from langchain.tools import DuckDuckGoSearchResults`** — the web-search tool the chapter uses.
- **`load_tools(["llm-math"], llm=openai_llm)`** — loads the built-in calculator tool.
- **Custom tools**: `Tool(name="duckduck", description="...", func=search.run)` — any callable wrapped with a description that the LLM reads.
- **Four-line agent construction**:
  ```python
  agent = create_react_agent(openai_llm, tools, prompt)
  agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
  agent_executor.invoke({"input": "What is the current price of a MacBook Pro in USD? ..."})
  ```
- **The ReAct framework** ([[react|ReAct]], Yao et al. 2022) — the *Thought / Action / Observation* cycle is the agent's prompting backbone. LangChain's `create_react_agent` is the wiki's **first runnable LangChain-native ReAct receipt** (complementing existing [[DSPy]]-native `dspy.ReAct` coverage on [[react]]).
- **Agent capability ceiling**: Ch 7 explicitly switches from [[Phi3Mini|Phi-3-mini]] to [[ChatGPT|GPT-3.5-turbo]] for the agent example — *"the LLM that we used thus far is relatively small and not sufficient to run these examples."*
- **Safety caveat the chapter ends on**: *"By creating this relatively autonomous behavior, we are not involved in the intermediate steps. As such, there is no [[humanintheloop|human in the loop]] to judge the quality of the output or reasoning process. This double-edged sword requires a careful system design to improve its reliability."*

### LangChain's positioning per Ch 7
- **Pedagogical-first framework**: the chapter commits to LangChain because of its lower learning curve and abstraction richness, while acknowledging that *"newer frameworks of note are DSPy and Haystack."*
- **Frameworks named alongside as alternatives**: [[DSPy]], Haystack.
- **Backend stack Ch 7 makes concrete**: LangChain (orchestration) + [[llamacpp]] (local inference) + [[HuggingFace|HF Transformers]] (referenced) + [[openai|OpenAI]] (for GPT-3.5 when local models are insufficient).

This is the operationalization of Ch 1's *"backend packages"* tooling commitment (LangChain + llama.cpp + HF Transformers) — the **first chapter that uses LangChain centrally**, after Chs 2–6 used Transformers only and Ch 6 added llama.cpp.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 cites LangChain first in its list of [[AIPipelineOrchestration|AI pipeline orchestration]] tools:

> *"There are many AI orchestration tools, including LangChain, LlamaIndex, Flowise, Langflow, and Haystack."* — Ch 10

The chapter's broader framing places LangChain in the **AI pipeline orchestrator** category — distinct from general workflow orchestrators (Airflow, Metaflow), tuned for synchronous user-facing inference pipelines with retrieval, tool use, and conditional branching. Sibling product [[LangSmith]] (Figure 10-11) is Ch 10's named [[RequestTrace|request-tracing]] tool.

The "start simple" caveat from Ch 5 (use no tool first, then adopt one) is reinforced in Ch 10:

> *"Any external tool brings additional complexity. An orchestrator can abstract away critical details of how your system works, making it hard to understand and debug your system."* — Ch 10

Ch 10 also flags the gateway/orchestrator boundary tension *"so many tools seem to want to become end-to-end platforms that do everything"* — LangChain is one of the orchestrators that has expanded toward [[ModelGateway|gateway]]-like functionality, illustrating the trend.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 adds **a fourth LangChain integration** to Ch 7's Model I/O / Chains / Memory / Agents trio — **Retrieval** via the [[rag|RAG]] pipeline primitives:

```python
from langchain import LlamaCpp, PromptTemplate
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

llm = LlamaCpp(model_path="Phi-3-mini-4k-instruct-fp16.gguf", n_gpu_layers=-1, ...)
embedding_model = HuggingFaceEmbeddings(model_name='thenlper/gte-small')
db = FAISS.from_texts(texts, embedding_model)
rag = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=db.as_retriever(),
    chain_type_kwargs={"prompt": prompt}
)
rag.invoke('Income generated')
```

The **wiki's first runnable `RetrievalQA.from_chain_type(chain_type='stuff', ...)` receipt**. Ch 8 demonstrates the four LangChain RAG primitives:

| Primitive | Role |
|---|---|
| `langchain.LlamaCpp` | Generation model (Phi-3) |
| `langchain.embeddings.huggingface.HuggingFaceEmbeddings` | Embedding model wrapper |
| `langchain.vectorstores.FAISS` | Vector store backend |
| `langchain.chains.RetrievalQA.from_chain_type(chain_type='stuff', ...)` | RAG pipeline orchestration |

The `chain_type='stuff'` parameter is LangChain's name for *"stuff all retrieved docs into a single prompt"* — the simplest of LangChain's retrieval-QA chain types. The local-LangChain path **loses span-level citation generation** (which the [[CohereChat|Cohere `co.chat(documents=...)`]] managed path provides).

## From [[agentic-design-patterns-ch01-prompt-chaining|Agentic Design Patterns Ch 1]]

Gulli's Ch 1 picks LangChain (with [[LangGraph]]) as the demonstration framework for the [[PromptChaining|prompt chaining]] / Pipeline pattern *"as their core APIs are explicitly designed for composing chains and graphs of operations."* The division of labor it draws: **LangChain provides foundational abstractions for linear sequences; [[LangGraph]] extends these to stateful and cyclical computations** necessary for sophisticated agentic behaviors. The runnable example is a two-step LCEL chain (`pip install langchain langchain-community langchain-openai langgraph`) — `extraction_chain = prompt_extract | llm | StrOutputParser()`, then a `full_chain` that dict-injects the first chain's output (`{"specifications": extraction_chain} | prompt_transform | llm | StrOutputParser()`). It notes `langchain-openai` can be swapped for another provider's package ([[gemini|Google Gemini]], [[Anthropic]], etc.). This reinforces LangChain's wiki role as the canonical **LCEL pipe-composition** substrate, now attested across three books.

## From [[agentic-design-patterns-ch02-routing|Agentic Design Patterns Ch 2]] (Routing)
Gulli's Ch 2 uses LangChain (with [[LangGraph]] and `langchain-google-genai`) for its [[Routing|routing]] hands-on example. The wiki's **first `RunnableBranch` receipt**: a `coordinator_router_chain` (`ChatPromptTemplate | llm | StrOutputParser()`) classifies a request into `'booker' / 'info' / 'unclear'`, and a `RunnableBranch` then dispatches the *original* request to the matching handler — an [[AgentHandoff|agent-delegation]] / [[Routing|routing]] pattern. `RunnablePassthrough` threads the original `request` alongside the router's `decision`. This is LangChain's explicit-composition answer to [[GoogleADK|ADK]]'s declarative `sub_agents` Auto-Flow.

## From [[agentic-design-patterns-ch03-parallelization|Agentic Design Patterns Ch 3]] (Parallelization)
Gulli's Ch 3 uses LangChain (LCEL) for its [[Parallelization|parallelization]] hands-on example, and gives the wiki its **first `RunnableParallel` receipt**. The framing: in LCEL the `|` pipe is *sequential* composition, while bundling runnables in a dict/list construct runs them *concurrently*. The example defines three independent chains (`summarize_chain`, `questions_chain`, `terms_chain`, each `ChatPromptTemplate | llm | StrOutputParser()` over `gpt-4o-mini`) and wraps them in `map_chain = RunnableParallel({"summary": ..., "questions": ..., "key_terms": ..., "topic": RunnablePassthrough()})` — `RunnablePassthrough` threads the original topic through alongside the parallel results. The full chain `map_chain | synthesis_prompt | llm | StrOutputParser()` then fans the parallel outputs into a sequential synthesis step (a [[ScatterGather|fan-out/fan-in]]). It is invoked asynchronously via `await full_parallel_chain.ainvoke(topic)` driven by `asyncio.run(...)` — and the chapter notes [[asyncio]] gives *concurrency, not parallelism* (single-thread event loop under the GIL). Prereqs: `langchain`, `langchain-community`, `langchain-openai`.

## From [[agentic-design-patterns-ch04-reflection|Agentic Design Patterns Ch 4]] (Reflection)
Gulli's Ch 4 uses LangChain for its [[Reflection|reflection]] hands-on example — a procedural `run_reflection_loop()` over `ChatOpenAI(model="gpt-4o", temperature=0.1)` rather than a pure LCEL pipe. The chapter explicitly frames this as the limit of single-step composition: *"The implementation of a complete, iterative reflection process necessitates mechanisms for state management and cyclical execution"* handled natively by [[LangGraph]] or via custom procedural code, while *"the fundamental principle of a single reflection cycle can be demonstrated effectively using the compositional syntax of LCEL."* The loop builds a `message_history` list (`HumanMessage`/`SystemMessage` from `langchain_core.messages`), generates code in iteration 0, then runs a **`reflector_prompt`** — a `SystemMessage` casting the model as *"a senior software engineer and an expert in Python"* doing a *"meticulous code review"* — to critique it. The critic returns the single phrase `CODE_IS_PERFECT` (the loop's **stopping condition**) or a bulleted critique appended to history for the next refinement (`max_iterations = 3`). This is the [[Reflection|Producer-Critic]] pattern realized as one model alternating personas, the LangChain counterpart to [[GoogleADK|ADK]]'s `SequentialAgent(generator, reviewer)`. Prereqs: `langchain`, `langchain-community`, `langchain-openai`.

## From [[agentic-design-patterns-ch05-tool-use|Agentic Design Patterns Ch 5]] (Tool Use)
Gulli's Ch 5 uses LangChain for the canonical **tool-calling agent** ([[ToolUse]] / [[FunctionCalling]]). Tool definition is a two-stage process: (1) wrap a Python function with the **`@tool` decorator** (`from langchain_core.tools import tool`) — the function's docstring becomes the tool description the LLM reads; (2) bind the tools to a function-calling-capable LLM. The chapter's example defines `search_information(query: str) -> str`, then builds the agent with three primitives:
- **`create_tool_calling_agent(llm, tools, agent_prompt)`** (`from langchain.agents`) — combines the LLM, tools, and a `ChatPromptTemplate` (which must include an `agent_scratchpad` placeholder for the agent's intermediate steps) into an agent.
- **`AgentExecutor(agent=agent, tools=tools, verbose=True)`** — the runtime that invokes the agent and executes the chosen tools; invoked via `await agent_executor.ainvoke({"input": query})`.

The model is [[gemini|Gemini]] (`ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)` from `langchain_google_genai`), with multiple queries fanned out concurrently via `asyncio.gather`. This complements the Ch 7 `create_react_agent` receipt: `create_tool_calling_agent` is the modern native-function-calling agent constructor, whereas `create_react_agent` drives the [[react|ReAct]] text-prompting loop. Prereqs: `langchain`, `langchain-google-genai`.

## From [[agentic-design-patterns-ch08-memory-management|Agentic Design Patterns Ch 8]] (Memory Management)
Gulli's Ch 8 uses LangChain for the **conversation-history** ([[ShortTermMemory|short-term memory]]) implementations of the [[MemoryManagement|memory-management]] pattern. Two primitives: **`ChatMessageHistory`** (`langchain.memory`) for direct, manual tracking of dialogue (`add_user_message` / `add_ai_message` / `.messages`); and **`ConversationBufferMemory`** for automated integration into an `LLMChain`, customized by `memory_key` (the prompt variable holding the history, default `"history"`) and `return_messages` (False → a single formatted string for standard LLMs; **True → a list of message objects, recommended for chat models**, paired with a `MessagesPlaceholder`). This re-grounds the [[ConversationBufferMemory]] / [[ConversationSummaryMemory]] family already documented from *Hands-On LLMs* Ch 7. Long-term memory in the chapter is handled by sibling [[LangGraph]] (namespaced store). See [[MemoryManagement]].

## From [[agentic-design-patterns-ch11-goal-setting|Agentic Design Patterns Ch 11]] (Goal Setting and Monitoring)
Gulli's Ch 11 uses LangChain (`langchain_openai` / `ChatOpenAI`, `gpt-4o`, `temperature=0.3`) for the [[GoalSettingAndMonitoring|Goal Setting and Monitoring]] hands-on example: an autonomous coding agent that runs an iterative **generate → self-review-against-goals → judge → revise** loop. The agent takes a use case plus a list of goals (e.g. `["simple", "tested", "handles edge cases"]`) and, each iteration, calls `llm.invoke` to (1) generate code, (2) `get_code_feedback` (a code-reviewer prompt critiquing against the goals), and (3) `goals_met` — a separate [[LLMAsAJudge|LLM-judge]] call that returns a parsed `True`/`False`; it stops on `True` or when `max_iterations = 5` is hit, then writes the commented result to a `.py` file. This is plain procedural LangChain (no LCEL graph), echoing the Ch 4 `run_reflection_loop` structure; the chapter notes the more robust design separates writer and reviewer into distinct agents (a [[CrewAI]]-style crew built on [[gemini|Gemini]]). Prereqs: `langchain_openai`, `openai`, `python-dotenv`.

## From [[agentic-design-patterns-ch14-rag|Agentic Design Patterns Ch 14]] (Knowledge Retrieval / RAG)
Gulli's Ch 14 uses LangChain (+ [[langgraph|LangGraph]] + [[Weaviate]]) for its third and most complete [[rag|RAG]] hands-on example — a full retrieve→generate pipeline. **Data prep & indexing**: `TextLoader` loads a document, `CharacterTextSplitter(chunk_size=500, chunk_overlap=50)` does the [[Chunking|chunking]], `OpenAIEmbeddings` (`langchain_community.embeddings`) embeds, and `Weaviate.from_documents(client, documents, embedding, by_text=False)` (`langchain_community.vectorstores`) builds the store; `vectorstore.as_retriever()` exposes retrieval. **Generation**: `ChatPromptTemplate` (`langchain_core.prompts`) holds a question-answering prompt, `StrOutputParser` (`langchain_core.output_parsers`) parses, and `rag_chain = prompt | llm | StrOutputParser()` composes the answer with [[openai|OpenAI]] `ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)`. The orchestration is delegated to [[langgraph|LangGraph]] — a `StateGraph(RAGGraphState)` (a `TypedDict` of `question` / `documents` / `generation`) with two nodes, `retrieve_documents_node` and `generate_response_node`, wired `retrieve → generate → END` and run via `app.stream(inputs)`. This is the wiki's **first LangChain RAG receipt using a managed [[VectorDatabase|vector database]] (Weaviate) plus a LangGraph `StateGraph`**, complementing the Ch 8 *Hands-On LLMs* `RetrievalQA.from_chain_type` + [[FAISS]] receipt. Prereqs include `langchain`, `langchain_community`, `langchain_core`, `langchain_openai`, `langgraph`, `weaviate`, `langchain.text_splitter`, `langchain.schema.runnable`.
