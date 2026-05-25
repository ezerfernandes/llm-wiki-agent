---
title: "Hands-On LLMs Ch 7 — Advanced Text Generation Techniques and Tools"
type: source
tags: [book, hands-on-llm, oreilly, llm, langchain, chains, memory, agents, react, tool-use, prompt-template, conversation-buffer, conversation-summary, gguf, llama-cpp, quantization]
date: 2024-01-01
source_file: raw/books/hands-on-llm/ch07-advanced-text-generation.md
book: "Hands-On Large Language Models"
book_isbn13: "9781098150969"
book_authors: ["Jay Alammar", "Maarten Grootendorst"]
book_publisher: "O'Reilly Media"
book_year: 2024
---

# Hands-On LLMs Ch 7 — Advanced Text Generation Techniques and Tools

## Summary

The seventh chapter of [[JayAlammar|Jay Alammar]] and [[MaartenGrootendorst|Maarten Grootendorst]]'s *Hands-On Large Language Models* ([[OReilly|O'Reilly Media]], 2024, ISBN 978-1-098-15096-9) and **the wiki's first end-to-end pedagogical tour of the [[LangChain]] framework** as the chapter's organizing substrate. Ch 7 picks up where [[hands-on-llm-ch06-prompt-engineering|Ch 6]] left off — *"what can we do to further enhance the experience and output that we get from the LLM without needing to fine-tune the model itself?"* — and walks four advanced techniques that **extend an LLM without fine-tuning**: **Model I/O** (loading the LLM, here a [[GGUF]]-quantized [[Phi3Mini|Phi-3]] via [[llamacpp|`llama-cpp-python`]] + [[LangChain]]'s `LlamaCpp` wrapper), **Chains** (LangChain's namesake abstraction — connecting a [[PromptTemplate|prompt template]] to an LLM, then chaining multiple LLM calls sequentially), **Memory** (helping stateless LLMs remember conversations — `ConversationBufferMemory`, `ConversationBufferWindowMemory`, `ConversationSummaryMemory`), and **Agents** (LLM-driven systems that decide which tools to call — implemented via the **[[react|ReAct]]** framework of Yao et al. 2022, with `create_react_agent` + `AgentExecutor` orchestrating a [[DuckDuckGoSearch|DuckDuckGo]] search tool + [[LLMMathTool|llm-math]] calculator over [[ChatGPT|GPT-3.5-turbo]]). The chapter is **the wiki's first LangChain-centric source** — it makes LangChain's `LlamaCpp` / `PromptTemplate` / `LLMChain` / `ConversationBufferMemory` / `ConversationBufferWindowMemory` / `ConversationSummaryMemory` / `load_tools` / `Tool` / `DuckDuckGoSearchResults` / `create_react_agent` / `AgentExecutor` import paths the canonical runnable surface for the four techniques. Retrieval-augmented generation is **explicitly deferred to Ch 8** (*"Note that retrieval will be discussed in the next chapter"*).

Ch 7 is the **third chapter of Part III** (after [[hands-on-llm-ch06-prompt-engineering|Ch 6]] on prompt engineering) and the wiki's **first source whose subject is LLM-application architecture rather than the LLM itself**. Where Ch 6 frames *"how to write a better prompt"*, Ch 7 frames *"how to compose a prompt with other components into a system"* — prompt-template-as-Lego-block (Ch 6's seven-component modular prompt) extends naturally into chain-as-Lego-block (Ch 7's `prompt | llm` operator-style composition). The chapter names **[[DSPy]] and Haystack** as the *"newer frameworks of note"* alongside LangChain — *"LangChain is one of the earlier frameworks that simplify working with LLMs through useful abstractions"* — placing LangChain in pedagogical-first position despite its acknowledged seniority.

The chapter introduces **four things the wiki did not previously cover at runnable-code granularity**: (1) **the LangChain `LlamaCpp` + `LCEL` pipe operator** — `basic_chain = prompt | llm` — as the canonical composition primitive; (2) **`LLMChain` with multiple `output_key`-named sub-chains** wired together via `title | character | story` — the story-generation worked example that decomposes a single creative task into three sequential LLM calls each consuming previous outputs; (3) **the three LangChain memory types as a pros-and-cons design surface** — `ConversationBufferMemory` (full history, hits token limit), `ConversationBufferWindowMemory(k=2)` (last-k turns only, drops early state), `ConversationSummaryMemory` (running LLM-summarized history, slower but compact) — each illustrated with the same "Maarten is 33" identity-retention probe; (4) **ReAct in LangChain** — the four-line construction `agent = create_react_agent(llm, tools, prompt)` + `AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)` — running the canonical *"What is the current price of a MacBook Pro in USD? How much would it cost in EUR if the exchange rate is 0.85 EUR for 1 USD?"* benchmark that produces *"$2,249.00 ... approximately 1911.65 EUR"* via two ReAct cycles (DuckDuckGo search → llm-math). This is the wiki's **first runnable LangChain ReAct agent** and the **first runnable demonstration of [[react|ReAct]] outside [[DSPy]]'s `dspy.ReAct`** ([[dspy-customer-service-agent]], [[dspy-modules]], [[dspy-tools]]).

The chapter ends with a load-bearing **safety caveat on autonomous agents**: *"By creating this relatively autonomous behavior, we are not involved in the intermediate steps. As such, there is no [[humanintheloop|human in the loop]] to judge the quality of the output or reasoning process. This double-edged sword requires a careful system design to improve its reliability. For instance, we could have the agent return the website's URL where it found the MacBook Pro's price or ask whether the output is correct at each step."* This is consistent with [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]'s [[CompoundErrorAccumulation|compound-error-accumulation]] warning and with [[2402.01817-llm-modulo|Kambhampati et al.]]'s LLM-Modulo external-verifier framing.

## Key Claims

- **The four advanced techniques covered without fine-tuning**: **Model I/O** (loading and working with LLMs), **Memory** (helping LLMs to remember), **Agents** (combining complex behavior with external tools), and **Chains** (connecting methods and modules). All four are integrated *"with the LangChain framework that will help us easily use these advanced techniques throughout this chapter."*
- **LangChain is the chapter's organizing framework**: *"LangChain is one of the earlier frameworks that simplify working with LLMs through useful abstractions. Newer frameworks of note are [[DSPy]] and Haystack."* The chapter does not contrast them in depth — it commits to LangChain for pedagogical continuity.
- **The chapter's true thesis is composition**: *"Each of these techniques has significant strengths by themselves but their true value does not exist in isolation. It is when you combine all of these techniques that you get an LLM-based system with incredible performance. The culmination of these techniques is truly where LLMs shine."*
- **Model I/O uses a [[GGUF]]-quantized [[Phi3Mini|Phi-3]] via LangChain's `LlamaCpp`**: *"A GGUF model represents a compressed version of its original counterpart through a method called [[Quantization|quantization]], which reduces the number of bits needed to represent the parameters of an LLM."* The chapter uses an **8-bit Phi-3 variant** (relative to the original 16-bit), *"cutting the memory requirements almost in half."* The full quantization treatment is deferred to **Ch 12**.
- **Quantization rule of thumb**: *"As a rule of thumb, look for at least 4-bit quantized models. These models have a good balance between compression and accuracy. Although it is possible to use 3-bit or even 2-bit quantized models, the performance degradation becomes noticeable and it would instead be preferable to choose a smaller model with a higher precision."*
- **The clock analogy for quantization**: *"If asked what the time is, you might say '14:16,' which is correct but not a fully precise answer. You could have said it is '14:16 and 12 seconds' instead ... mentioning seconds is seldom helpful and we often simply put that in discrete numbers, namely full minutes. Quantization is a similar process that reduces the precision of a value (e.g., removing seconds) without removing vital information (e.g., retaining hours and minutes)."*
- **The `LlamaCpp` loader signature** (LangChain wrapper around [[llamacpp|llama-cpp-python]]):
  ```python
  from langchain import LlamaCpp
  llm = LlamaCpp(
      model_path="Phi-3-mini-4k-instruct-fp16.gguf",
      n_gpu_layers=-1,
      max_tokens=500,
      n_ctx=2048,
      seed=42,
      verbose=False
  )
  llm.invoke("Hi! My name is Maarten. What is 1 + 1?")  # empty output! Phi-3 needs its prompt template.
  ```
  The empty output motivates the need for **chains** — Phi-3's chat template (`<s><|user|>...<|end|><|assistant|>`) must be applied explicitly because the raw `LlamaCpp.invoke()` call does not auto-apply it like `transformers.pipeline` would.
- **Chains are LangChain's namesake**: *"LangChain is named after one of its main methods, chains. Although we can run LLMs in isolation, their power is shown when used with additional components or even when used in conjunction with each other. Chains not only allow for extending the capabilities of LLMs but also for multiple chains to be connected together."*
- **A single chain wires a prompt template to an LLM** via the LCEL pipe operator:
  ```python
  from langchain import PromptTemplate
  template = """<s><|user|>
  {input_prompt}<|end|>
  <|assistant|>"""
  prompt = PromptTemplate(template=template, input_variables=["input_prompt"])
  basic_chain = prompt | llm
  basic_chain.invoke({"input_prompt": "Hi! My name is Maarten. What is 1 + 1?"})
  # Output: "The answer to 1 + 1 is 2. It's a basic arithmetic operation..."
  ```
- **Chains generalize over reusable templates**: the chapter's *"funny business names"* example illustrates `PromptTemplate(template="Create a funny name for a business that sells {product}.", input_variables=["product"])` as a reusable component.
- **Sequential / multi-prompt chains break complex tasks into smaller subtasks** with named outputs. The chapter's **three-stage story-generation chain**:
  - **Title chain** — `title = LLMChain(llm=llm, prompt=title_prompt, output_key="title")` with template `"Create a title for a story about {summary}. Only return the title."` Given `summary="a girl that lost her mother"` produces `title=" \"Whispers of Loss: A Journey Through Grief\""`.
  - **Character chain** — depends on both `{summary}` and `{title}`, produces `output_key="character"`.
  - **Story chain** — depends on `{summary}`, `{title}`, `{character}`, produces `output_key="story"`.
  - **Full chain**: `llm_chain = title | character | story` — running `llm_chain.invoke("a girl that lost her mother")` returns all three named outputs in a dict.
- **Multi-prompt benefits**:
  - **Smaller, more manageable prompts** per step.
  - **Different parameters per call** — *"Another advantage of dividing the problem into smaller tasks is that we now have access to these individual components. We can easily extract the title; that might not have been the case if we were to use a single prompt."*
  - This is the operationalization of [[PromptChaining|prompt chaining]] / [[PromptDecomposition|prompt decomposition]] in LangChain.
- **LLMs are stateless without memory**: *"When we are using LLMs out of the box, they will not remember what was being said in a conversation. You can share your name in one prompt but it will have forgotten it by the next prompt."* The chapter demonstrates with the basic_chain — `"Hi! My name is Maarten. What is 1 + 1?"` answered correctly; then `"What is my name?"` answered *"I'm sorry, but as a language model, I don't have the ability to know personal information about individuals."*
- **The reason is statelessness**: *"these models are stateless — they have no memory of any previous conversation!"* Memory is the application's responsibility, not the LLM's.
- **`ConversationBufferMemory` appends the full conversation history** to each prompt. Implementation:
  ```python
  template = """<s><|user|>Current conversation:{chat_history}
  
  {input_prompt}<|end|>
  <|assistant|>"""
  prompt = PromptTemplate(template=template, input_variables=["input_prompt", "chat_history"])
  from langchain.memory import ConversationBufferMemory
  memory = ConversationBufferMemory(memory_key="chat_history")
  llm_chain = LLMChain(prompt=prompt, llm=llm, memory=memory)
  ```
  With this chain, *"By extending the chain with memory, the LLM was able to use the chat history to find the name we gave it previously."* LangChain saves it internally as `"Human: ...\nAI: ..."` interaction pairs.
- **`ConversationBufferWindowMemory(k=2)` retains only the last `k` conversation turns**:
  ```python
  from langchain.memory import ConversationBufferWindowMemory
  memory = ConversationBufferWindowMemory(k=2, memory_key="chat_history")
  ```
  Demonstrated by giving the LLM both name + age in turn 1, then asking name (works) and age (forgotten — age was in turn 1, which fell out of the k=2 window after turns 2 and 3).
- **`ConversationSummaryMemory` uses an LLM to summarize the running conversation**: *"This summarization process is enabled by another LLM that is given the conversation history as input and asked to create a concise summary. A nice advantage of using an external LLM is that we are not confined to using the same LLM during conversation."*
  ```python
  summary_prompt_template = """<s><|user|>Summarize the conversations and update with the new lines.
  Current summary: {summary}
  new lines of conversation: {new_lines}
  New summary:<|end|>
  <|assistant|>"""
  summary_prompt = PromptTemplate(input_variables=["new_lines", "summary"], template=summary_prompt_template)
  from langchain.memory import ConversationSummaryMemory
  memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history", prompt=summary_prompt)
  ```
  **Per-step cost**: two LLM calls — *"The user prompt"* + *"The summarization prompt"*. *"Although we use the same LLM for both summarizing and user prompting, you could use a smaller LLM for the summarization task to speed up computation."*
- **The summary-memory trade-off**: *"This summarization helps keep the chat history relatively small without using too many tokens during inference. However, since the original question was not explicitly saved in the chat history, the model needed to infer it based on the context. This is a disadvantage if specific information needs to be stored in the chat history. Moreover, multiple calls to the same LLM are needed, one for the prompt and one for the summarization. This can slow down computing time."*
- **The three-memory pros-and-cons table** (Table 7-1):
  | Memory type | Pros | Cons |
  |---|---|---|
  | **Conversation Buffer** | Easiest implementation; ensures no information loss within context window; large-context LLMs not needed unless chat history is large | Slower generation as more tokens are needed; only suitable for large-context LLMs; larger chat histories make information retrieval difficult |
  | **Windowed Conversation Buffer** | No information loss over the last k interactions | Only captures the last k interactions; no compression of the last k |
  | **Conversation Summary** | Captures the full history; enables long conversations; reduces tokens needed to capture full history | An additional call is necessary for each interaction; quality is reliant on the LLM's summarization capabilities |
- **Trade-off summary**: *"Often, it is a trade-off between speed, memory, and accuracy. Where ConversationBufferMemory is instant but hogs tokens, ConversationSummaryMemory is slow but frees up tokens to use."*
- **Agents are LLM-driven systems that decide which actions to take**: *"One of the most promising concepts in LLMs is their ability to determine the actions they can take. This idea is often called agents, systems that leverage a language model to determine which actions they should take and in what order."*
- **Agents extend chains with two vital components**: (1) **Tools that the agent can use to do things it could not do itself**; (2) **The agent type, which plans the actions to take or tools to use**.
- **Why agents are powerful**: *"Unlike the chains we have seen thus far, agents are able to show more advanced behavior like creating and self-correcting a roadmap to achieve a goal. They can interact with the real world through the use of tools."*
- **The motivating use case is calculator-assisted math**: *"LLMs are notoriously bad at mathematical problems and often fail at solving simple math-based tasks but they could do much more if we provide access to a calculator."* And more broadly: *"imagine we extend this with dozens of other tools, like a search engine or a weather API. Suddenly, the capabilities of LLMs increase significantly."*
- **Agents are powered by ReAct** (Yao et al. 2022, *"ReAct: Synergizing reasoning and acting in language models"*, arXiv:2210.03629): *"the driving force of many agent-based systems is the use of a framework called Reasoning and Acting (ReAct)."*
- **ReAct merges reasoning and acting in a cycle**: *"ReAct merges these two concepts and allows reasoning to affect acting and actions to affect reasoning."* The cycle iterates three steps: **Thought → Action → Observation**.
- **Mechanism**: *"the LLM is asked to create a 'thought' about the input prompt. This is similar to asking the LLM what it thinks it should do next and why. Then, based on the thought, an 'action' is triggered. The action is generally an external tool, like a calculator or a search engine. Finally, after the results of the 'action' are returned to the LLM it 'observes' the output, which is often a summary of whatever result it retrieved."*
- **The MacBook Pro worked example** (illustrating two ReAct cycles): *"imagine you are on holiday in the United States and interested in buying a MacBook Pro. Not only do you want to know the price but you need it converted to EUR as you live in Europe ..."* The agent first searches the web for current prices, then uses a calculator to convert USD to EUR.
- **Phi-3 is insufficient for ReAct; the chapter switches to GPT-3.5**: *"These autonomous processes generally require an LLM that is powerful enough to properly follow complex instructions. The LLM that we used thus far is relatively small and not sufficient to run these examples. Instead, we will be using OpenAI's GPT-3.5 model as it follows these complex instructions more closely."* This is the chapter's **honest acknowledgment that the [[Phi3Mini|Phi-3-mini]] / GPU-poor commitment has a ceiling at agents**.
- **The chapter's ReAct prompt template** (the canonical form the LangChain `create_react_agent` expects):
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
- **The tool setup** uses both the `llm-math` built-in tool and a custom DuckDuckGo wrapper:
  ```python
  from langchain.agents import load_tools, Tool
  from langchain.tools import DuckDuckGoSearchResults
  search = DuckDuckGoSearchResults()
  search_tool = Tool(
      name="duckduck",
      description="A web search engine. Use this to as a search engine for general queries.",
      func=search.run,
  )
  tools = load_tools(["llm-math"], llm=openai_llm)
  tools.append(search_tool)
  ```
- **The four-line agent construction**:
  ```python
  from langchain.agents import AgentExecutor, create_react_agent
  agent = create_react_agent(openai_llm, tools, prompt)
  agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
  ```
- **The actual result**: *"The current price of a MacBook Pro in USD is $2,249.00. It would cost approximately 1911.65 EUR with an exchange rate of 0.85 EUR for 1 USD."* — the answer reached via two ReAct cycles, one per tool.
- **The safety / reliability caveat** (the chapter's parting wisdom): *"Considering the limited tools the agent has, this is quite impressive! Using just a search engine and a calculator the agent could give us an answer. Whether that answer is actually correct should be taken into account. By creating this relatively autonomous behavior, we are not involved in the intermediate steps. As such, there is no human in the loop to judge the quality of the output or reasoning process. This double-edged sword requires a careful system design to improve its reliability. For instance, we could have the agent return the website's URL where it found the MacBook Pro's price or ask whether the output is correct at each step."*
- **Forward references**: the chapter ends with *"With this foundation in place, we are now poised to explore ways in which LLMs can be used to improve existing search systems and even become the core of new, more powerful search systems, as discussed in the next chapter."* — Ch 8 on **semantic search and RAG**.

## Key Quotes

> *"These methods are all integrated with the LangChain framework that will help us easily use these advanced techniques throughout this chapter. LangChain is one of the earlier frameworks that simplify working with LLMs through useful abstractions. Newer frameworks of note are DSPy and Haystack."* — Ch 7 (pp. 199–200)

> *"Each of these techniques has significant strengths by themselves but their true value does not exist in isolation. It is when you combine all of these techniques that you get an LLM-based system with incredible performance. The culmination of these techniques is truly where LLMs shine."* — Ch 7, opening synthesis

> *"LangChain is named after one of its main methods, chains. Although we can run LLMs in isolation, their power is shown when used with additional components or even when used in conjunction with each other."* — Ch 7, on chains

> *"these models are stateless — they have no memory of any previous conversation!"* — Ch 7, on why memory matters

> *"Often, it is a trade-off between speed, memory, and accuracy. Where ConversationBufferMemory is instant but hogs tokens, ConversationSummaryMemory is slow but frees up tokens to use."* — Ch 7, on memory trade-offs

> *"One of the most promising concepts in LLMs is their ability to determine the actions they can take. This idea is often called agents, systems that leverage a language model to determine which actions they should take and in what order."* — Ch 7, defining agents

> *"ReAct merges these two concepts and allows reasoning to affect acting and actions to affect reasoning."* — Ch 7, on ReAct

> *"By creating this relatively autonomous behavior, we are not involved in the intermediate steps. As such, there is no human in the loop to judge the quality of the output or reasoning process. This double-edged sword requires a careful system design to improve its reliability."* — Ch 7, closing safety caveat

## Connections

### Authors and publisher
- [[JayAlammar]] / [[MaartenGrootendorst]] — co-authors.
- [[OReilly]] — publisher.
- [[HandsOnLLM]] — the book.

### Sibling chapters
- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1's opening backend-stack commitment ([[HuggingFace|HF Transformers]] + [[llamacpp]] + [[LangChain]]) is **fully cashed out** in Ch 7 for the first time — Chs 2–6 used Transformers and Ch 6 added llama.cpp; Ch 7 is the **first chapter that uses LangChain centrally**.
- [[hands-on-llm-ch06-prompt-engineering]] — Ch 6's [[PromptChaining|chain prompting]] is the conceptual precursor to Ch 7's `LLMChain` sequential chains; Ch 7's `prompt | llm` LCEL pipe extends Ch 6's seven-component modular prompt with a composition operator. The story-generation worked example in Ch 7 is the **direct LangChain operationalization** of Ch 6's three-use-case taxonomy of chain prompting (specifically the *"writing stories"* use case).
- Ch 8 (semantic search and RAG) — forward-referenced for retrieval; Ch 7 explicitly defers retrieval-augmented memory / retrieval-augmented agents to Ch 8.
- Ch 12 (fine-tuning generation models) — forward-referenced for the deeper quantization treatment Ch 7 sketches.

### LangChain stack (the chapter's organizing framework)
- [[LangChain]] — the chapter's central framework; Ch 7 is the wiki's first deep treatment.
- [[LangChainLlamaCpp|`langchain.LlamaCpp`]] — the GGUF-model loader.
- [[PromptTemplate|`langchain.PromptTemplate`]] — the prompt-template primitive.
- [[LLMChain|`langchain.LLMChain`]] — the named-output chain primitive (sequential composition).
- [[LCEL|LangChain Expression Language]] — the `prompt | llm` pipe-operator composition style.
- [[ConversationBufferMemory|`langchain.memory.ConversationBufferMemory`]] — full-history memory.
- [[ConversationBufferWindowMemory|`langchain.memory.ConversationBufferWindowMemory`]] — last-k-turns memory.
- [[ConversationSummaryMemory|`langchain.memory.ConversationSummaryMemory`]] — LLM-summarized memory.
- [[LangChainAgent|`langchain.agents.create_react_agent` + `AgentExecutor`]] — ReAct agent construction.
- [[DuckDuckGoSearchResults|`langchain.tools.DuckDuckGoSearchResults`]] — search tool.
- [[LLMMathTool|`load_tools(["llm-math"])`]] — calculator tool.

### Models and inference
- [[Phi3Mini]] — the chapter's local-LLM substrate (used for chains and memory).
- [[GGUF]] — the quantized model format used to load Phi-3 efficiently.
- [[llamacpp]] / [[LangChainLlamaCpp|`langchain.LlamaCpp`]] — the loader.
- [[Quantization]] — the sketched concept (deep dive deferred to Ch 12).
- [[ChatGPT]] / [[openai|OpenAI]] — `gpt-3.5-turbo` is the LLM the chapter switches to for the ReAct agent example (Phi-3 isn't capable enough).

### Concepts
- [[PromptTemplate]] — the chapter's first chain link; LangChain's operationalization of the prompt-template concept.
- [[PromptChaining]] — Ch 6's chain-prompting concept; Ch 7 is the LangChain implementation.
- [[PromptDecomposition]] — Huyen Ch 5's vocabulary for the same technique.
- [[ChatTemplate]] — Phi-3's `<s><|user|>...<|end|><|assistant|>` template that `LlamaCpp` does **not** auto-apply (unlike `transformers.pipeline`) — the motivation for explicit `PromptTemplate` use in LangChain.
- [[ConversationHistory]] — the application-state concept; LangChain's three memory types are three operationalizations.
- [[StatelessLLM|LLM statelessness]] — the underlying reason memory abstractions exist.
- [[ContextLength]] / [[ContextWindow]] — the constraint that motivates window / summary memory over buffer memory.
- [[FIFOMemory]] — Huyen Ch 6's name for the eviction policy LangChain operationalizes as `ConversationBufferWindowMemory`.
- [[SummarizationMemory]] — Huyen Ch 6's name for the summarization-memory pattern LangChain operationalizes as `ConversationSummaryMemory`.
- [[react|ReAct]] — Yao et al. 2022's framework; Ch 7 is the wiki's first LangChain-native ReAct receipt (complements existing DSPy-native `dspy.ReAct` coverage).
- [[Agent]] / [[AgenticAI]] — the broader agent concept; Ch 7 is the wiki's first runnable LangChain-agent code listing.
- [[ToolInventory]] — the agent's tool set (DuckDuckGo search + llm-math calculator).
- [[ToolUse]] — the general technique.
- [[humanintheloop]] — what is missing from the autonomous agent loop (Ch 7's parting caveat).
- [[CompoundErrorAccumulation]] — Huyen Ch 6's warning that Ch 7's parting caveat mirrors.

### Cross-source position
- [[ai-engineering-ch06-rag-agents|Huyen Ch 6]] — the wiki's other major agents-and-memory treatment. The two are complementary: Huyen Ch 6 frames the **design discipline** (agent = environment + tool inventory + AI planner; memory hierarchy as FIFO / Summarization / Reflection); Alammar & Grootendorst Ch 7 is the **runnable LangChain operationalization** (three concrete memory classes + four-line ReAct construction).
- [[dspy-modules]] / [[dspy-tools]] / [[dspy-customer-service-agent]] — the wiki's existing DSPy-native ReAct receipts. Ch 7 is the **LangChain-native counterpart**.
- [[DSPy]] / Haystack — named in Ch 7 as *"newer frameworks of note"* alongside LangChain. The wiki has substantial DSPy coverage; Haystack remains lightly covered.

### People
- [[ShunyuYao]] — first author of the ReAct paper (Yao et al. 2022, arXiv:2210.03629) — minted as new entity page.

## Contradictions

No direct contradictions. Soft consistency notes:

- **LangChain framing**: [[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]] uses LangChain as **the cautionary tale** for [[PromptEngineeringTools|prompt-engineering tools]] — Fig 5-9 shows typos in a default critique prompt, and Ch 5 cites LangChain's 2023 remote-code-execution vulnerability as the canonical [[PromptAttack|prompt-attack]] surface. Ch 7 uses LangChain as **the pedagogical default** for chains / memory / agents and acknowledges newer alternatives ([[DSPy]] / Haystack). The two positions are not contradictions but **different operating modes** — Huyen Ch 5 focuses on production-hardening; Hands-On LLMs Ch 7 focuses on getting techniques to work. Reconciliation: LangChain is a legitimate pedagogical-first framework whose production deployment requires inspection of its templates and tools, per Huyen Ch 5's *"following the keep-it-simple principle, you might want to start by writing your own prompts without any tool"* recommendation.
- **Memory taxonomy**: Ch 7's three-memory taxonomy (`ConversationBufferMemory` / `ConversationBufferWindowMemory` / `ConversationSummaryMemory`) maps cleanly onto [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]'s four-memory taxonomy ([[FIFOMemory|FIFO]] / [[SummarizationMemory|summarization]] / [[ReflectionMemory|reflection]] / retrieval-augmented). The mapping: Buffer ≈ no eviction; Buffer Window ≈ FIFO; Summary ≈ Summarization; LangChain's `ConversationKGMemory` / `VectorStoreRetrieverMemory` (not covered in Ch 7) would be the Reflection / retrieval-augmented counterparts. Ch 7's coverage is a subset of Huyen Ch 6's broader taxonomy.
- **ReAct framing**: Ch 7's three-step *Thought → Action → Observation* cycle is consistent with [[react|ReAct]]'s existing wiki coverage from [[dspy-modules]] / [[dspy-tools]] / [[ai-engineering-ch06-rag-agents]]. Where DSPy's `dspy.ReAct` exposes a `trajectory` field for introspection, LangChain's `AgentExecutor(verbose=True)` prints the trajectory inline — different ergonomics, same underlying scaffold.
- **Agent capability ceiling at Phi-3-mini**: Ch 7 explicitly switches from [[Phi3Mini|Phi-3-mini]] to [[ChatGPT|GPT-3.5-turbo]] for the agent example — *"the LLM that we used thus far is relatively small and not sufficient to run these examples."* This is consistent with Phi-3-mini's prompt-engineering and chain-of-thought capability profile from Ch 6 (where Phi-3 handled CoT successfully on simple math, but agentic tool selection is a step harder). No contradiction — Ch 7 documents the capability cliff at the agent boundary.
- **`LlamaCpp` does not auto-apply chat templates**: Ch 7 reveals (via the empty-output demonstration) that LangChain's `LlamaCpp.invoke()` does **not** wrap the input in Phi-3's `<s><|user|>...<|end|><|assistant|>` chat template, unlike `transformers.pipeline` (which does, per Ch 6's `apply_chat_template` discussion). This is a tooling detail, not a contradiction — but it's a load-bearing operational gotcha future LangChain receipts should know.

## Position in the wiki

**First LangChain-centric source** in the wiki. Existing LangChain references ([[ai-engineering-ch01-intro]], [[ai-engineering-ch05-prompt-engineering]], [[leh-ch03-data-engineering]], [[hands-on-llm-ch01-introduction-to-llms]]) name the framework or use it for a single utility; Ch 7 makes the framework the chapter's organizing structure and walks four of its core abstractions (Model I/O, Chains, Memory, Agents) at runnable-code granularity.

**First runnable LangChain-native [[react|ReAct]] agent** in the wiki. The wiki's prior ReAct receipts ([[dspy-customer-service-agent]], [[dspy-modules]], [[dspy-tools]]) are all DSPy-native; Ch 7 is the LangChain-native counterpart. The two operationalizations target the same Yao et al. 2022 framework but expose different ergonomics — DSPy's `dspy.ReAct(Signature, tools=[...])` is signature-parameterized and exposes `trajectory`; LangChain's `create_react_agent(llm, tools, prompt) + AgentExecutor(verbose=True)` is template-parameterized and prints the trajectory inline.

**First wiki coverage of the LangChain memory class hierarchy** — Buffer / Buffer-Window / Summary as a concrete pros-and-cons design surface complementing [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]'s [[FIFOMemory]] / [[SummarizationMemory]] / [[ReflectionMemory]] conceptual taxonomy.

**First wiki coverage of LangChain's LCEL pipe operator** (`prompt | llm`, `title | character | story`) as a composition primitive.

**First wiki coverage of the DuckDuckGo search tool as a LangChain `Tool`** and of the `llm-math` built-in calculator tool.

**First wiki appearance of Shunyu Yao** (first author of the ReAct paper) — minted as a new entity page.
