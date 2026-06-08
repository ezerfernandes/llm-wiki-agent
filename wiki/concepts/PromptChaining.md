---
title: "Prompt Chaining"
type: concept
tags: [prompt-engineering, system-design, llm, agentic-design-patterns, pipeline-pattern]
sources: [hands-on-llm-ch06-prompt-engineering, hands-on-llm-ch07-advanced-text-generation, agentic-design-patterns-ch01-prompt-chaining, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# Prompt Chaining

**Breaking a complex problem across a sequence of LLM calls, feeding each output into the next prompt.** Named *"chain prompting"* in [[hands-on-llm-ch06-prompt-engineering|*Hands-On LLMs* Ch 6]]; equivalent to **[[PromptDecomposition|prompt decomposition]]** in [[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]]'s vocabulary.

> *"Instead of breaking the problem within a prompt, we can do so between prompts. Essentially, we take the output of one prompt and use it as input for the next, thereby creating a continuous chain of interactions that solves our problem."* — Ch 6

## Worked example (Ch 6)

Two-call chain producing a chatbot's name, slogan, and sales pitch:

```python
# Call 1: name + slogan
product_prompt = [{"role": "user", "content": "Create a name and slogan for a chatbot that leverages LLMs."}]
product_description = pipe(product_prompt)[0]["generated_text"]
# Output: "Name: 'MindMeld Messenger' / Slogan: 'Unleashing Intelligent Conversations, One Response at a Time'"

# Call 2: sales pitch, consuming previous output
sales_prompt = [{"role": "user", "content": f"Generate a very short sales pitch for the following product: '{product_description}'"}]
sales_pitch = pipe(sales_prompt)[0]["generated_text"]
```

## Why chain (Ch 6's framing)

> *"This technique of chaining prompts allows the LLM to spend more time on each individual question instead of tackling the whole problem."*

A direct consequence: **each call can use different parameters.** Ch 6's example tunes `max_new_tokens` lower for the name/slogan (short outputs) and higher for the sales pitch (longer output).

## Three use-case families (Ch 6)

| Use case | Pattern |
|---|---|
| **Response validation** | Ask a second LLM call to double-check the first's output. |
| **Parallel prompts** | Run multiple independent prompts in parallel, merge results in a final pass. *"Ask multiple LLMs to generate multiple recipes in parallel and use the combined result to create a shopping list."* |
| **Writing stories** | First write a summary, then develop characters, then story beats, then dialogue. |

The chapter forward-references **Ch 7** for chaining beyond LLMs — chaining memory, tool use, and other technology.

## Relation to [[chainofthought|chain-of-thought]]

[[chainofthought|Chain-of-thought]] keeps the reasoning *inside one prompt* (more tokens, single call); prompt chaining spreads the reasoning *across multiple calls* (more API calls, each shorter). [[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]]'s framing: both are *"give the model time to think"* levers operating at different scopes.

## Relation to [[PromptDecomposition|prompt decomposition]]

Ch 6's *"chain prompting"* and Huyen Ch 5's *"prompt decomposition"* are the **same technique under two names**. Huyen Ch 5 adds the [[GoDaddy]] customer-support case study (1,500-token bloated prompt → decomposed → better performance + lower cost) and the **monitoring / debugging / parallelization / lower-cost / lower-authoring-effort** benefits matrix. Ch 6 adds the *"writing stories"* worked use case and the natural-step toward Ch 7's agentic chaining.

## Connections

- [[hands-on-llm-ch06-prompt-engineering]] — primary source naming "chain prompting".
- [[PromptDecomposition]] — the equivalent Huyen Ch 5 vocabulary.
- [[ai-engineering-ch05-prompt-engineering]] — Huyen's framing.
- [[PromptEngineering]] — parent discipline.
- [[chainofthought]] — single-call alternative for the "time to think" lever.
- [[selfconsistency]] — N-CoT chain pattern.
- [[Agent]] / [[AgenticAI]] — agentic systems are prompt chaining taken to the extreme where the chain structure is decided at runtime.
- [[react]] — ReAct pattern: tool-using chain.
- [[agentic-design-patterns-ch01-prompt-chaining]] — Gulli's Ch 1, the "Pipeline pattern" framing + LangChain/LangGraph LCEL example.
- [[SequentialDecomposition]] — the divide-and-conquer mechanic underlying the pattern.
- [[ContextHandoff]] — structured-output passing between chain steps.
- [[hands-on-llm-ch07-advanced-text-generation]] — Ch 7 operationalization in LangChain: the **three-stage story-generation chain** (`title | character | story`) is the runnable code listing for the *"writing stories"* use case Ch 6 named.

## Ch 7 operationalization in LangChain

[[hands-on-llm-ch07-advanced-text-generation|Ch 7]] of *Hands-On LLMs* is the wiki's first runnable LangChain implementation of prompt chaining. The chapter operationalizes Ch 6's *"writing stories"* use case as a three-stage `LLMChain` pipeline:

```python
from langchain import LLMChain, PromptTemplate

# Stage 1: title from summary
title_prompt = PromptTemplate(template="""<s><|user|>
Create a title for a story about {summary}. Only return the title.<|end|>
<|assistant|>""", input_variables=["summary"])
title = LLMChain(llm=llm, prompt=title_prompt, output_key="title")

# Stage 2: character from summary + title
character = LLMChain(llm=llm, prompt=character_prompt, output_key="character")

# Stage 3: story from summary + title + character
story = LLMChain(llm=llm, prompt=story_prompt, output_key="story")

# Compose with the LCEL pipe operator
llm_chain = title | character | story
llm_chain.invoke("a girl that lost her mother")
# Returns dict with all four named keys: summary, title, character, story
```

Each `LLMChain` is **named via `output_key`** — Ch 7's mechanism for accessing intermediate components: *"Another advantage of dividing the problem into smaller tasks is that we now have access to these individual components. We can easily extract the title; that might not have been the case if we were to use a single prompt."* This is the LangChain-native answer to the **per-stage parameter tuning** Ch 6 named — each `LLMChain` can have its own LLM, prompt, max_tokens, temperature, etc.

The Ch 7 worked output for `summary="a girl that lost her mother"`:
- **title**: *"In Loving Memory: A Journey Through Grief"*
- **character**: *"The protagonist, Emily, is a resilient young girl who struggles to cope with her overwhelming grief..."*
- **story**: A single-paragraph story integrating all three prior elements.

Ch 7 extends Ch 6's three use-case taxonomy with a fourth dimension that becomes visible in code — **per-stage parameterization** (different `max_tokens`, different LLMs, different prompts per link). This is the structural advantage of chaining in framework form that bare-prompt chaining doesn't expose.

## Agentic Design Patterns (Gulli) perspective

[[agentic-design-patterns-ch01-prompt-chaining|Chapter 1]] of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) makes prompt chaining the **first and foundational** of its 21 agentic design patterns, and gives it an explicit alias: the **Pipeline pattern**. Its framing is a **divide-and-conquer** strategy — *"Rather than expecting an LLM to solve a complex problem in a single, monolithic step, prompt chaining advocates for a divide-and-conquer strategy."* The output→input dependency between steps is what *names* the pattern: *"This passing of information establishes a dependency chain, hence the name."* See [[SequentialDecomposition]] for the mechanic.

### Why single prompts fail (Ch 1's failure-mode taxonomy)
Where the *Hands-On LLMs* framing motivates chaining by "time to think," Gulli motivates it by enumerating the failure modes of a single monolithic prompt on a multifaceted task:
- **Instruction neglect** — parts of the prompt are overlooked.
- **Contextual drift** — the model loses track of the initial context.
- **Error propagation** — early errors amplify down the response.
- **Context-window pressure** — the prompt needs more context than fits.
- **Hallucination from cognitive load** — higher load raises the chance of incorrect output.

Decomposing into focused steps reduces cognitive load at each step. Ch 1 also adds **per-step role assignment** (e.g., the same market-analysis task chained as "Market Analyst" → "Trade Analyst" → "Expert Documentation Writer").

### Structured output between steps
Ch 1 elevates inter-step data integrity to a first-class concern — the [[ContextHandoff|role of structured output]]: *"If the output of one prompt is ambiguous or poorly formatted, the subsequent prompt may fail due to faulty input."* The fix is to specify a structured format ([[StructuredOutputs|JSON or XML]]) for hand-offs, making data machine-readable and unambiguously parseable into the next prompt.

### Deterministic logic between model calls
Beyond breaking down problems, Ch 1 stresses that chaining *"allows for the insertion of deterministic logic between model calls, enabling intermediate data processing, output validation, and conditional branching within the workflow"* — managed by an underlying execution framework. This is the bridge from a linear chain toward stateful, branching agent graphs ([[LangGraph]]).

### Use-case families (Ch 1)
Ch 1 enumerates seven application families, broadening Ch 6's three: **information-processing workflows**, **complex query answering** (decompose → research sub-questions → synthesize), **data extraction & transformation** (with conditional re-prompting on missing fields), **content-generation workflows** (ideate → outline → draft → review), **conversational agents with state**, **code generation & refinement**, and **multimodal multi-step reasoning**. It notes that complex pipelines often **combine parallel processing** for independent data-gathering ([[Parallelization]]) **with prompt chaining** for the dependent synthesis/refinement steps.

### Hands-on: LangChain/LangGraph LCEL
Ch 1's runnable example is a **two-step LCEL chain** (extract specs → transform to JSON) using `ChatPromptTemplate`, `StrOutputParser`, and the `|` pipe — the same LCEL backbone as the *Hands-On LLMs* Ch 7 example above, but composed with a dict-injection step `{"specifications": extraction_chain} | prompt_transform | llm | StrOutputParser()`. Ch 1 positions [[LangChain]] for linear sequences and [[LangGraph]] for *"stateful and cyclical computations ... necessary for implementing more sophisticated agentic behaviors,"* and names [[CrewAI]] and the [[GoogleADK|Google ADK]] as alternative frameworks.

### Rule of thumb (Ch 1)
> Use this pattern when a task is too complex for a single prompt, involves multiple distinct processing stages, requires interaction with external tools between steps, or when building agentic systems that need to perform multi-step reasoning and maintain state.

The chapter closes by situating chaining inside [[ContextEngineering|Context Engineering]] — the broader discipline of constructing the model's full informational environment, of which prompt engineering is one slice.

### Appendix A: "Factored Cognition / Decomposition"
[[agentic-design-patterns-appendix-a-prompting|Appendix A]] re-surfaces the same idea under the name **Factored Cognition / Decomposition**: *"For very complex tasks, break down the overall goal into smaller, more manageable sub-tasks and prompt the model separately on each sub-task. The results … are then combined to achieve the final outcome. This is related to prompt chaining and planning but emphasizes the deliberate decomposition of the problem."* Its worked example is a research-paper pipeline — *Prompt 1:* generate an outline → *Prompt 2:* write the introduction from the outline → *Prompt N:* write each remaining section → *final:* combine sections and write a conclusion. This is the appendix's vocabulary for the pattern this page documents.
