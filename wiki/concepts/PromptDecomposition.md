---
title: "Prompt Decomposition"
type: concept
tags: [prompt-engineering, system-design, llm]
sources: [ai-engineering-ch05-prompt-engineering, hands-on-llm-ch06-prompt-engineering, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Prompt Decomposition

**Breaking a complex multi-step prompt into a chain of smaller subtask prompts.** Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as one of six core prompt-engineering best practices.

> "For complex tasks that require multiple steps, break those tasks into subtasks. Instead of having one giant prompt for the whole task, each subtask has its own prompt. These subtasks are then chained together." — Ch 5

## Worked example: customer support

Ch 5's example (from OpenAI's prompt-engineering guide):

```
Prompt 1: intent classification
  Input: customer message
  Output: {"primary": ..., "secondary": ...}

Prompt 2: response generation (per intent)
  Input: classified intent + customer message
  Output: model response
```

If there are 10 intents, you have **11 prompts total**: one classifier + ten per-intent responders. The classifier is cheap (call a weak model); the responders are expensive (call a strong model).

## Benefits (Ch 5)

| Benefit | Mechanism |
|---|---|
| **Better performance** | Models follow simple instructions more reliably than complex ones. |
| **Monitoring** | Each intermediate output is observable, not just the final answer. |
| **Debugging** | The failing step is isolatable; you can fix it without touching the rest. |
| **Parallelization** | Independent subtasks run concurrently (Anthropic's example: generate three reading-level versions in parallel). |
| **Lower authoring effort** | Many short prompts are easier to write than one giant prompt. |
| **Lower cost** | Cheaper models can handle simpler subtasks. |

## From [[hands-on-llm-ch07-advanced-text-generation|*Hands-On LLMs* Ch 7]]

Ch 7 operationalizes prompt decomposition in [[LangChain]] via [[LLMChain]] + [[LCEL|LCEL pipe operator]]. The chapter's worked **three-stage story-generation chain** decomposes a single creative-writing task into three sequential LLM calls (`title` → `character` → `story`), each with its own narrow prompt and its own named output:

```python
title = LLMChain(llm=llm, prompt=title_prompt, output_key="title")
character = LLMChain(llm=llm, prompt=character_prompt, output_key="character")
story = LLMChain(llm=llm, prompt=story_prompt, output_key="story")
llm_chain = title | character | story
llm_chain.invoke("a girl that lost her mother")
```

Ch 7's framing of the **multi-prompt benefit**:

> *"Another advantage of dividing the problem into smaller tasks is that we now have access to these individual components. We can easily extract the title; that might not have been the case if we were to use a single prompt."* — Ch 7

This is the [[LangChain]] operationalization of [[hands-on-llm-ch06-prompt-engineering|Ch 6's]] [[PromptChaining|chain prompting]] — the same conceptual technique, exposed as a composable framework primitive rather than as a programming pattern.

## Costs

- **Higher user-perceived latency** for tasks where users don't see intermediate outputs.
- **More API calls** — but Ch 5 notes the cost is often less than the additive sum because (a) smaller prompts use fewer total tokens, and (b) cheaper models can handle the simpler subtasks.

## The [[GoDaddy]] case study

> "[[GoDaddy]] (2024) found that the prompt for their customer support chatbot bloated to over 1,500 tokens after one iteration. After decomposing the prompt into smaller prompts targeting different subtasks, they found that their model performed better while also reducing token costs." — Ch 5

This is Ch 5's headline production-data point: decomposition is one of the few prompt-engineering practices that improves **both** performance and cost simultaneously.

## How small should subtasks be?

Ch 5 doesn't prescribe — *"How small each subtask should be depends on each use case and the performance, cost, and latency trade-off you're comfortable with. You'll need to experiment to find the optimal decomposition and chaining."* The natural ceiling is when further decomposition causes more latency than it saves on quality.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PromptEngineering]] — parent.
- [[chainofthought|Chain-of-Thought]] — a degenerate case where the "chain" lives inside one prompt.
- [[SelfCritique]] — related: multiple model passes for self-verification.
- [[GoDaddy]] — production case study.
- [[Agent]] — agentic systems are decomposition taken to its logical extreme (subtasks chosen at runtime).
- [[hands-on-llm-ch06-prompt-engineering]] — Alammar & Grootendorst Ch 6 (the equivalent technique under the name *"chain prompting"*).
- [[PromptChaining]] — Ch 6's vocabulary for the same pattern.

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 names the same technique **"chain prompting"** (see [[PromptChaining]]):

> *"Instead of breaking the problem within a prompt, we can do so between prompts. Essentially, we take the output of one prompt and use it as input for the next, thereby creating a continuous chain of interactions that solves our problem."* — Ch 6

### Worked example — name → slogan → sales pitch

Ch 6's two-call example: first generate `name + slogan` for a chatbot (*"Name: 'MindMeld Messenger' / Slogan: 'Unleashing Intelligent Conversations, One Response at a Time'"*), then consume the output as input for a sales-pitch generation call. The key insight: *"each call can use different parameters"* — short `max_new_tokens` for name/slogan, longer for the pitch.

### Three use-case families (Ch 6)

| Use case | Pattern |
|---|---|
| **Response validation** | Second LLM call double-checks the first's output. |
| **Parallel prompts** | Multiple independent prompts run in parallel; merge in a final pass. |
| **Writing stories** | Summary → characters → story beats → dialogue. |

The chapter forward-references **Ch 7** for chaining beyond LLMs (memory + tool use + other tech).
