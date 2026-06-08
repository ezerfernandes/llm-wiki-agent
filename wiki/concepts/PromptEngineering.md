---
title: "Prompt Engineering"
type: concept
tags: [prompt-engineering, adaptation, llm, ai-engineering]
sources: [ai-engineering-ch01-intro, ai-engineering-ch05-prompt-engineering, hands-on-llm-ch06-prompt-engineering, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# Prompt Engineering

**Getting an AI model to express desirable behaviors purely from the input, without changing model weights.** A [[PromptBasedAdaptation|prompt-based]] [[ModelAdaptation|model adaptation]] technique and the most accessible entry point into [[AIEngineering|AI engineering]]. Defined in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]]:

> *"Prompt engineering is about getting AI models to express the desirable behaviors from the input alone, without changing the model weights."*

## What "prompt engineering" includes

Per Ch 1, prompt engineering is **more than just telling the model what to do.** It encompasses:

- **Instructions** — task description, role specification, output format.
- **Examples** — few-shot or many-shot demonstrations.
- **Context** — supplying the model with the data it needs (overlaps with [[rag|RAG]] when context is retrieved).
- **Tools** — exposing function-call interfaces.
- **Memory management** — providing a system that lets the model track conversation history over long contexts.

Chapter 5 of the book is the deep dive; Chapter 6 covers context construction (RAG + agents).

## Worked example: the Gemini–ChatGPT MMLU swap

Ch 1's canonical anecdote for prompt-engineering impact:

| Model | Prompt format | MMLU score |
|---|---|---|
| Gemini Ultra | CoT@32 | **90.04%** |
| Gemini Pro | CoT@8 | 79.13% |
| GPT-4 | 5-shot | 86.4% |
| Gemini Ultra | 5-shot | 83.7% |

*Same model, different prompt → ranking can flip.* Gemini Ultra's MMLU rose from 83.7% to 90.04% just by switching from 5-shot to CoT@32 — a +6.3 absolute point swing.

## Disambiguating "training"

Huyen explicitly cautions that **prompt engineering ≠ training**. She cites a Business Insider article in which an author claimed she "trained ChatGPT" by feeding it her childhood journal entries through the prompt — this is colloquially correct but technically incorrect. If you're teaching the model via context input, it's prompt engineering, not training (and not [[FineTuning|finetuning]]).

## Importance in the AI Engineering Stack

Ch 1's [[AIEngineeringStack|stack]] taxonomy puts prompt engineering at the **application development layer**. The comparison table:

| Category | Building with traditional ML | Building with foundation models |
|---|---|---|
| Prompt engineering | Not applicable | Important |
| Evaluation | Important | More important |
| AI interface | Less important | Important |

## Connections

- [[ModelAdaptation]] / [[PromptBasedAdaptation]] — parent categories.
- [[rag|RAG]] / [[FineTuning|Finetuning]] — the other two core adaptation techniques.
- [[AIEngineering]] / [[AIEngineeringStack]] — discipline-level home.
- [[chainofthought]] / [[selfconsistency]] / [[react]] — concrete prompt-engineering techniques in the existing wiki.
- [[MIPROv2]] / [[GEPA]] — automated prompt-optimization techniques in the existing wiki.
- [[Hallucination]] — the headline failure mode that prompt engineering tries to mitigate.
- [[ai-engineering-ch01-intro]] — primary source (Ch 1).

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Chapter 5 is the **deep dive** the Ch 1 stub promised. It develops prompt engineering as a rigorous discipline rather than the *"fiddling with words"* caricature that prompt engineering acquired in 2022–2023.

**Definitional anchor.** Prompt engineering is **human-to-AI communication**:

> "Anyone can communicate, but not everyone can communicate effectively. Similarly, it's easy to write prompts but not easy to construct effective prompts." — Ch 5

And the OpenAI research manager Huyen quotes: *"The problem is not with prompt engineering. It's a real and useful skill to have. The problem is when prompt engineering is the only thing people know."* Prompt engineering needs to be supplemented with [[ai-engineering-ch03-evaluation-methodology|evaluation]], experiment tracking, and dataset curation.

**Six best practices** (the chapter's structural backbone):

1. **Write clear and explicit instructions.** Score 1–5 vs 1–10; ban fractional scores if you don't want them.
2. **Ask the model to adopt a [[Persona|persona]].** First-grade teacher → chicken essay 4/5 instead of 2/5.
3. **Provide examples.** Few-shot [[InContextLearning|in-context learning]]; also pick token-efficient example formats.
4. **Specify the output format.** Use end-of-prompt markers for structured output.
5. **Provide sufficient [[ContextConstruction|context]].** Hallucination mitigation.
6. **Break complex tasks into simpler subtasks** — [[PromptDecomposition|prompt decomposition]]. [[GoDaddy]] case study: 1,500-token prompt → decomposition → better performance *and* lower cost.

Plus: **give the model time to think** ([[chainofthought|CoT]] / [[SelfCritique|self-critique]]), **iterate systematically** ([[PromptIteration]]), **evaluate prompt-engineering tools** ([[PromptEngineeringTools|tool category]] — [[DSPy]], [[OpenPrompt]], [[PromptBreeder]], [[TextGrad]], [[Guidance]], [[Outlines]], [[Instructor]]; warning about hidden API-call multiplication and LangChain default-prompt typos), and **organize and version prompts** ([[PromptOrganization]] → [[PromptCatalog]] / [[Dotprompt]]-style files).

**Prompt anatomy** (Ch 5's three-part [[PromptStructure|prompt structure]]):

| Part | What it contains |
|---|---|
| Task description | What you want the model to do; the role, the output format. |
| Example(s) | Demonstrations — [[FewShotLearning\|few-shot]] [[InContextLearning\|in-context learning]]. |
| The task | The concrete input — the specific question or document. |

Mapped to model-API conventions: task description → [[SystemPrompt|system prompt]]; task → [[UserPrompt|user prompt]]. But the split is *concatenated under the hood* — any system-vs-user behavior difference comes from (a) position-in-prompt effects, and (b) [[InstructionHierarchy|instruction-hierarchy]] post-training ([[WallaceEtAl2024|Wallace et al. 2024]] at OpenAI).

**[[PromptRobustness|Prompt robustness]] is correlated with model capability.** Stronger models are more robust to prompt perturbation, which is why prompt-engineering toil shrinks as models improve. Stanford dropped robustness from HELM Lite in late 2023 once it stopped differentiating frontier models.

**Defensive prompt engineering** is the chapter's second half — see [[DefensivePromptEngineering]], [[PromptAttack]], [[PromptExtraction]], [[PromptInjection]], [[IndirectPromptInjection]], [[Jailbreak]], [[InformationExtraction]]. The wiki's prior prompt-attack pages now sit inside this Ch 5 taxonomy.

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 is the wiki's **second book-chapter prompt-engineering treatment** after Huyen Ch 5. Where Huyen Ch 5 frames the *discipline* (six best practices + defensive prompt engineering + tools taxonomy with hidden-cost warnings), Alammar & Grootendorst Ch 6 frames the **modular-component design surface**.

### The seven-component modular prompt

Ch 6's signature contribution to prompt-engineering vocabulary — a finer decomposition than Huyen Ch 5's three-part [[PromptStructure|anatomy]]:

| Component | What it specifies |
|---|---|
| **[[Persona|Persona]]** | The role the LLM should take — *"You are an expert in astrophysics"*. |
| **[[InstructionPrompt|Instruction]]** | The task itself; specificity is the most important property. |
| **[[ContextPrompt|Context]]** | Why the instruction exists / additional background. |
| **[[OutputFormat|Format]]** | What format the output should take. |
| **[[AudiencePrompt|Audience]]** | Who reads the output — *"For education purposes, it is often helpful to use ELI5"*. |
| **[[TonePrompt|Tone]]** | Voice / register. |
| **Data** | The actual content to operate on. |

Plus creative cross-cutting components like **[[EmotionPrompt|emotional stimuli]]** (Li et al. 2023 — *"This is very important for my career."*).

The seven components map cleanly onto subdivisions of Huyen Ch 5's three-part anatomy: persona + instruction + context + format + audience + tone all subdivide *"task description"*; examples remain examples; data is the task. **Both framings are complementary granularities**, not contradictions.

## Agentic Design Patterns (Gulli) — Appendix A's technique survey

[[agentic-design-patterns-appendix-a-prompting|Appendix A of *Agentic Design Patterns*]] reframes prompting as **a disciplined engineering practice rather than a simple act of asking questions**, and supplies the wiki's most comprehensive *single-source catalog* of named prompting techniques. Its five **core principles** echo the wiki's existing best-practices but add the explicit *"instructions over constraints"* maxim:

1. **Clarity & specificity** — unambiguous, precise task/format/limit definitions.
2. **Conciseness** — direct phrasing and **action verbs** (Act, Analyze, Classify, Extract, Summarize, Translate…).
3. **Using verbs** — *"Summarize the following text"* beats *"Think about summarizing this"*.
4. **Instructions over constraints** — tell the model **what to do**, not what to avoid; positive instructions reduce confusion (negative examples are an exception, used carefully).
5. **Experimentation & iteration** — draft → test → analyze → refine, documenting attempts (the discipline the wiki tracks as [[PromptIteration]]).

The appendix then organizes techniques into four buckets, each mapped to existing wiki pages: **basic/example-based** ([[ZeroShotLearning|zero]]/[[OneShotPrompting|one]]/[[FewShotLearning|few/many-shot]]), **structural** ([[SystemPrompt|system]]/[[RolePrompting|role]] prompting, delimiters, [[ContextEngineering|context engineering]], [[StructuredOutputs|structured output]] + [[Pydantic]]), **reasoning** ([[ChainOfThought|CoT]], [[SelfConsistency|self-consistency]], [[StepBackPrompting|step-back]], [[TreeOfThoughts|ToT]]), and **action/interaction** ([[ToolUse|tool use]]/[[FunctionCalling|function calling]], [[react|ReAct]]). Advanced/supplementary methods include [[AutomaticPromptEngineering|APE]]/DSPy, negative examples, analogies, factored cognition ([[PromptChaining|decomposition]]), [[rag|RAG]], the **Persona Pattern** (describe the *audience*), **Google Gems**, **meta-prompting** (use an LLM to critique your prompt), code prompting, and multimodal prompting. The appendix's thesis: *"Mastering this full spectrum of prompting is the definitive skill that elevates a generalist language model … into a truly sophisticated agent."* This appendix is the prompt-level companion to the [[ReasoningTechniques|Reasoning Techniques]] chapter (Ch 17) and is framed inside the broader discipline of [[ContextEngineering|Context Engineering]].

### The Lego-block iterative workflow

Ch 6's framing — *"think of prompts as pieces of a larger puzzle"*:

> *"This complex prompt demonstrates the modular nature of prompting. We can add and remove components freely and judge their effect on the output... The changes are not limited to simply introducing or removing components. Their order, as we saw before with the recency and primacy effects, can affect the quality of the LLM's output."* — Ch 6

The iterative workflow is **constructive** (build up by adding components) rather than **subtractive** (start large, trim). Ch 6's worked example concatenates seven component strings:
```python
query = persona + instruction + context + data_format + audience + tone + data
```

### Three instruction-prompting tips

| Tip | Ch 6's framing |
|---|---|
| **Specificity** | *"Instead of asking the LLM to 'Write a description for a product' ask it to 'Write a description for a product in less than two sentences and use a formal tone.'"* The most important of the three. |
| **[[Hallucination|Hallucination]] mitigation** | *"Ask the LLM to only generate an answer if it knows the answer. If it does not know the answer, it can respond with 'I don't know.'"* |
| **Order ([[PrimacyEffect|primacy]] / recency)** | *"Either begin or end your prompt with the instruction. Especially with long prompts, information in the middle is often forgotten."* Cites [[lostinthemiddle|Liu et al. 2023]]. |

### Position-in-the-wiki

Ch 6 is the **operational pedagogical complement** to Huyen Ch 5's disciplinary framing. The two together cover prompt engineering from both axes: Huyen frames it as a **discipline with measurable practices and tooling**; Alammar & Grootendorst frame it as a **modular design surface with reusable components**. The new concept pages [[InstructionPrompt]], [[ContextPrompt]], [[OutputFormat]], [[AudiencePrompt]], [[TonePrompt]], and [[PromptChaining]] are mainly Ch-6-anchored; [[Persona]] and [[PromptDecomposition]] are Huyen Ch 5-anchored but extended by Ch 6.
