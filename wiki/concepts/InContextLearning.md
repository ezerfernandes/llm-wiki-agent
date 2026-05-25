---
title: "In-Context Learning"
type: concept
tags: [prompt-engineering, llm, learning-paradigms, gpt-3]
sources: [ai-engineering-ch05-prompt-engineering, hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# In-Context Learning

**Teaching a model what to do via examples in the prompt rather than by updating weights.** The term was introduced in Brown et al. (2020), *"Language Models Are Few-shot Learners"* — the [[GPT3|GPT-3]] paper — and named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the conceptual foundation that turns runtime prompting from *trick* into *adaptation paradigm*.

> "Teaching models what to do via prompts is also known as in-context learning... GPT-3 was trained for next token prediction, but the paper showed that GPT-3 could learn from the context to do translation, reading comprehension, simple math, and even answer SAT questions." — Ch 5

## The conceptual leap

Before [[GPT3|GPT-3]], an ML model could *only* do what it had been trained to do — adapting it to a new task required updating weights via [[FineTuning|finetuning]] or retraining. GPT-3 showed that with enough scale + self-supervised pretraining, a frozen model can learn arbitrary new tasks from a handful of in-prompt examples. The model's behavior changes at runtime without a gradient step.

This is the mechanism that makes [[PromptEngineering|prompt engineering]] possible as a discipline. It is also why [[ChipHuyen|Huyen]] lists [[PromptBasedAdaptation|prompt-based adaptation]] (which subsumes in-context learning, [[rag|RAG]], and [[FewShotLearning|few-shot]] prompting) as a peer category to [[FineTuning|finetuning]] in the [[ModelAdaptation|model-adaptation]] taxonomy.

## In-context learning as continual learning

Ch 5 frames it explicitly:

> "In-context learning allows a model to incorporate new information continually to make decisions, preventing it from becoming outdated. Imagine a model that was trained on the old JavaScript documentation. To use this model to answer questions about the new JavaScript version, without in-context learning, you'd have to retrain this model. With in-context learning, you can include the new JavaScript changes in the model's context, allowing the model to respond to queries beyond its cut-off date. This makes in-context learning a form of [[continuallearning|continual learning]]."

## The Chollet metaphor

François Chollet (creator of [[Keras]]) compared a foundation model to *"a library of many different programs."* In this framing, **the prompt is a program-activator** rather than an instruction-set. Prompt engineering is the practice of finding which prompt-strings reliably activate the latent program you need (haikus, limericks, JSON extraction, code generation, ...). The model's weights encode the library; the prompt is a runtime address into it.

## Shot terminology

Each example provided in the prompt is called a **shot**.

| Term | Meaning |
|---|---|
| **0-shot** | No examples provided. |
| **1-shot** | One example. |
| **5-shot** | Five examples. |
| **Few-shot** | A small number (the GPT-3-paper convention is 1–10ish). |
| **Many-shot** | Dozens to hundreds — viable once context windows pass 100K. |

## How many shots?

> "In general, the more examples you show a model, the better it can learn. The number of examples is limited by the model's maximum context length. The more examples there are, the longer your prompt will be, increasing the inference cost." — Ch 5

Microsoft 2023: few-shot showed *significant* improvement on GPT-3 but *limited* improvement on GPT-4 — i.e., the few-shot advantage shrinks as models scale. Domain-specific tasks (Ch 5's example: the Ibis dataframe API) remain a strong few-shot use case because the model has seen relatively few examples during pretraining.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source for the wiki page.
- [[PromptEngineering]] — the discipline ICL enables.
- [[FewShotLearning]] / [[ZeroShotLearning]] — special cases by shot count.
- [[GPT3]] — the model where ICL was first demonstrated; Brown et al. 2020.
- [[ContextLength]] — bounds how many shots you can fit.
- [[continuallearning]] — the framing Ch 5 uses for ICL's adaptive role.
- [[FoundationModel]] / [[ModelAdaptation]] — parent abstractions.
- [[rag|RAG]] — the retrieval-side complement: dynamic context construction, then ICL.
- [[chainofthought|Chain-of-Thought]] — ICL form where the in-context examples include step-by-step reasoning.

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 frames ICL as the **"why describe when you can show"** move:

> *"In the previous sections, we tried to accurately describe what the LLM should do. Although accurate and specific descriptions help the LLM to understand the use case, we can go one step further. Instead of describing the task, why do we not just show the task? We can provide the LLM with examples of exactly the thing that we want to achieve. This is often referred to as in-context learning, where we provide the model with correct examples."* — Ch 6

### The Gigamuru / screeg worked example

Ch 6's [[OneShotPrompting|one-shot]] demonstration: define a made-up word *Gigamuru* with a usage sentence, then ask the model to use a *different* made-up word *screeg* in a sentence:

```python
one_shot_prompt = [
    {"role": "user", "content": "A 'Gigamuru' is a type of Japanese musical instrument. An example of a sentence that uses the word Gigamuru is:"},
    {"role": "assistant", "content": "I have a Gigamuru that my uncle gave me as a gift. I love to play it at home."},
    {"role": "user", "content": "To 'screeg' something is to swing a sword at it. An example of a sentence that uses the word screeg is:"}
]
```

The model produces *"During the intense duel, the knight skillfully screeged his opponent's shield, forcing him to defend himself."* A single example was sufficient to communicate the desired structural pattern.

### The role-alternation requirement

Ch 6 emphasizes that few-shot / one-shot prompting requires the proper **chat-template role alternation**:

> *"The prompt illustrates the need to differentiate between the user and the assistant. If we did not, it would seem as if we were talking to ourselves."* — Ch 6

The rendered [[Phi3Mini|Phi-3]] template shows the alternating `<|user|>` and `<|assistant|>` blocks ending with a blank `<|assistant|>` block for the new generation to fill.

### The randomness caveat

Ch 6 notes that few-shot / one-shot is **not foolproof**:

> *"One- or few-shot prompting is not the be all and end all of prompt engineering. We can use it as one piece of the puzzle to further enhance the descriptions that we gave it. The model can still 'choose,' through random sampling, to ignore the instructions."* — Ch 6

This is consistent with Huyen Ch 5's *"some models are better than others at following instructions"* — ICL is one lever among several, not a guaranteed control mechanism.
