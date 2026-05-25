---
title: "ChatGPT"
type: entity
tags: [product, conversational-agent, openai, foundation-model-app]
sources: [ai-engineering-ch01-intro, hands-on-llm-ch01-introduction-to-llms, ai-engineering-ch05-prompt-engineering, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# ChatGPT

[[openai|OpenAI]]'s consumer-facing conversational application built on top of the GPT family ([[GPT4|GPT-4]] and later). Launched November 2022, ChatGPT is identified throughout [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] as **the ignition event for the [[AIEngineering|AI engineering]] discipline** — the moment foundation models crossed into mainstream consciousness and triggered the [[AIInvestmentBoom|AI investment boom]].

## In Ch 1 of *AI Engineering*

- **The "ChatGPT moment"** marks the inflection point for [[SelfSupervision|self-supervised]] [[LargeLanguageModel|LLMs]] entering general use.
- **Tokenization example**: GPT-4 (the model behind ChatGPT) breaks "I can't wait to build AI applications" into nine tokens; "can't" splits into `can` and `'t`. GPT-4 vocabulary size: 100,256.
- **MMLU comparison anecdote**: in Google's December 2023 Gemini launch, [[gemini|Gemini]] Ultra scored 90.04% on [[mmlu]] using CoT@32 prompting while [[GPT4|GPT-4]] scored 86.4% with 5-shot — *but* with 5-shot only, ChatGPT outperformed Gemini, illustrating that prompt format alone can swing benchmark rank.
- **Tutor-replacement story**: when [[ChatGPT|ChatGPT]] launched, [[Chegg|Chegg's]] share price fell from $28 (Nov 2022) to $2 (Sep 2024) as students turned to AI for homework help.
- **Banned and unbanned**: NYC Public Schools and LA Unified School District banned ChatGPT for cheating fears, then reversed within months.
- **MIT writing study (Noy and Zhang, 2023)**: ChatGPT exposure cut writing time 40% and lifted output quality 18% on occupation-specific tasks for 453 college-educated professionals.

## Connections

- [[openai|OpenAI]] — developer.
- [[GPT4]] — underlying model.
- [[FoundationModel]] / [[LargeLanguageModel]] — model class.
- [[AIEngineering]] — discipline ignited by ChatGPT's success.
- [[ai-engineering-ch01-intro]] — Ch 1 source.
- [[Perplexity]] — standalone product positioned as a ChatGPT alternative for search.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1 of *Hands-On LLMs* uses ChatGPT as the anchor event for **2023 as "the Year of Generative AI"**:

> "2022 marked the release of ChatGPT, which demonstrated how profoundly this technology was poised to revolutionize how we interact with technology and information. Reaching one million active users in five days and then one hundred million active users in two months, the new breed of AI models started out as human-like chatbots but quickly evolved into a monumental shift in our approach to common tasks." — Ch 1

The chapter clarifies the **ChatGPT-the-product vs ChatGPT-the-model** distinction:

> "When we refer to ChatGPT, we are actually talking about the product and not the underlying model. When it was first released, it was powered by the GPT-3.5 LLM and has since then grown to include several more performant variants, such as GPT-4." — Ch 1

ChatGPT is also one of the principal examples of an [[InstructModel|instruct / chat model]] — the result of fine-tuning a [[CompletionModel|completion model]] on dialog data. *"By fine-tuning these models, we can create instruct or chat models that can follow directions."*

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

ChatGPT appears in Ch 5 in **four roles** as the canonical [[SystemPrompt|system-prompt]] and prompt-attack target:

1. **System-prompt extraction target.** *"Popular applications like ChatGPT are particularly attractive targets for [[ReversePromptEngineering|reverse prompt engineering]]. In February 2024, one user claimed that ChatGPT's system prompt had 1,700 tokens. Several GitHub repositories claim to contain supposedly leaked system prompts of GPT models. However, OpenAI has confirmed none of these."* The unverifiability problem is central to Ch 5's defensive framing.
2. **[[Obfuscation|Obfuscation]] resilience.** *"I was shocked that both ChatGPT and Claude were able to understand 'el qeada' in my queries."* Misspell-based jailbreaks defeated by ChatGPT's robustness.
3. **[[DivergenceAttack|Divergence attack]] target.** [[NasrEtAl2023|Nasr et al. 2023]] demonstrated that asking ChatGPT to repeat *"poem"* forever causes it to diverge and emit training data.
4. **Implicit system-prompt user.** *"Almost all generative AI applications, including ChatGPT, have system prompts."* — ChatGPT as the canonical example of consumer-facing applications with hidden system prompts.

The four-fold positioning makes ChatGPT the wiki's most-attacked-as-a-target product in the prompt-engineering corpus.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 uses **ChatGPT (`gpt-3.5-turbo-0125`)** as the **closed-source decoder-only [[GenerativeClassification|generative-classification]] demo** — the chapter's **best result across all four regimes**:

| Metric | Value |
|---|---|
| Weighted F1 on [[RottenTomatoes|Rotten Tomatoes]] | **0.91** |
| Cost (1,066-row test sweep, 2024) | ~3 cents |
| Temperature | 0 (deterministic) |
| System prompt | *"You are a helpful assistant."* |
| Mechanism | OpenAI `client.chat.completions.create(...)` |

The chapter sketches ChatGPT's **three-step training pipeline**:

1. **Base pretraining** — next-token prediction.
2. **[[InstructionTuning|Instruction tuning]]** — manually-created (prompt, output) pairs used as SFT data, producing a *"first variant of its model."*
3. **[[PreferenceFinetuning|Preference tuning]]** — generate multiple outputs per prompt; humans **rank them best-to-worst**; train on the resulting preference data. *"A major benefit of using preference data over instruction data is the nuance it represents."* Forward-references **Ch 12** for the mechanisms ([[rlhf|RLHF]] / [[DirectPreferenceOptimization|DPO]]).

The chapter flags the **[[DataContamination|benchmark-contamination caveat]]** that bounds the validity of the 0.91 F1 number: *"since we do not know what data the model was trained on, we cannot easily use these kinds of metrics for evaluating the model. For all we know, it might have actually been trained on our dataset!"* — the chapter's most rigorous epistemological move.

Other Ch 4 details: the chapter uses the `gpt-3.5-turbo-0125` snapshot (deterministic-snapshot semantics matter for reproducibility); **[[ExponentialBackoff|exponential backoff]]** is named as the standard mitigation for OpenAI rate-limit errors.

## From [[hands-on-llm-ch07-advanced-text-generation|*Hands-On LLMs* Ch 7]]

Ch 7 uses **`gpt-3.5-turbo`** (via [[LangChain]]'s `ChatOpenAI` wrapper) as the **LLM the chapter switches to when the local [[Phi3Mini|Phi-3-mini]] proves insufficient for [[react|ReAct]] agents**. The chapter's framing is candid:

> *"These autonomous processes generally require an LLM that is powerful enough to properly follow complex instructions. The LLM that we used thus far is relatively small and not sufficient to run these examples. Instead, we will be using OpenAI's GPT-3.5 model as it follows these complex instructions more closely."* — Ch 7

This is the chapter's honest acknowledgment of the **agent capability cliff**: Phi-3-mini handles single-turn generation, chains, and conversation memory; it does **not** handle multi-tool ReAct trajectories. GPT-3.5 produces the chapter's worked agent answer — *"The current price of a MacBook Pro in USD is $2,249.00. It would cost approximately 1911.65 EUR with an exchange rate of 0.85 EUR for 1 USD"* — across two ReAct cycles (DuckDuckGo search → llm-math calculator).

The structural point: ChatGPT / GPT-3.5 is Ch 7's **first place in the [[HandsOnLLM]] book where a closed-source frontier API is required for the task to work**, complementing Ch 4's role (where GPT-3.5 was the best-result classifier but Flan-T5 was also viable). [[LangChainAgent]] documents the full agent receipt.
