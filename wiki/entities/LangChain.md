---
title: "LangChain"
type: entity
tags: [framework, open-source, llm-orchestration, python, javascript]
sources: [ai-engineering-ch01-intro, hands-on-llm-ch01-introduction-to-llms, ai-engineering-ch05-prompt-engineering, hands-on-llm-ch07-advanced-text-generation, ai-engineering-ch10-architecture-feedback, hands-on-llm-ch08-semantic-search-and-rag, dspy-yahoo-finance-react-tutorial]
last_updated: 2026-05-24
---

# LangChain

Open-source framework for composing LLM-driven applications: prompts, chains, agents, memory, retrievers, vector stores. Available in Python (`langchain`) and JavaScript (`langchain.js`). Cited in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] as one of four open-source AI-engineering tools that within two years of launch **garnered more GitHub stars than Bitcoin** — on track to surpass React and Vue. The set: **LangChain, [[AutoGPT]], [[StableDiffusion]] Web UI, [[Ollama]]**.

LangChain is also Ch 1's evidence for the **JavaScript-ification of AI engineering**: LangChain.js (alongside Transformers.js, OpenAI's Node library, and Vercel's AI SDK) demonstrates the move beyond Python-centric ML toward full-stack-flavored AI engineering.

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
