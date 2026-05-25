---
title: "Hallucination"
type: concept
tags: [llm, safety, evaluation]
sources: [2507.03152-medval, 2408.08849-ecg-chat, ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms, ai-engineering-ch05-prompt-engineering, ai-engineering-ch06-rag-agents, ai-engineering-ch07-finetuning, ai-engineering-ch08-dataset-engineering, hands-on-llm-ch06-prompt-engineering, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Hallucination

When an LLM produces confident output that is factually wrong or unsupported by its inputs. Mitigations include [[rag]], verified tool use, [[SelfVerification]], constraint-based decoding, and **LM-as-judge validation** ([[LLMAsAJudge]] / [[MedVAL]]); closely related to [[AlignmentHallucination]] in agentic settings.

## In medical text — fine-grained taxonomy

[[2507.03152-medval|MedVAL (Aali et al. 2026)]] breaks hallucinations into five sub-types as part of its physician-defined error taxonomy:
- **Fabricated claim** — claim not present in the input. *Most common error in MedVAL-Bench at 45.7% of all errors.*
- **Misleading justification** — incorrect reasoning leading to misleading conclusions.
- **Detail misidentification** — incorrect reference to a detail in the input.
- **False comparison** — comparison not supported by the input.
- **Incorrect recommendation** — diagnosis or follow-up outside the input scope. Third most common at 12.6%.

These join **omissions** (missing claim, missing comparison, missing context) and **certainty misalignments** (overstating, understating intensity) as the full error category space. Hallucinations as a class are the dominant failure mode for LM-generated clinical text — far outweighing omissions or certainty issues in MedVAL-Bench's 840 physician-annotated outputs.

## In ECG report generation — prompt-side mitigation stack

[[2408.08849-ecg-chat|ECG-Chat (Zhao et al. 2025)]] frames hallucination in cardiac MLLMs as *"semantic deviations caused by generated text that does not align with the actual situation"* — root-caused to *"the model's lack of prior knowledge in certain specialized fields."* The paper's three-layer mitigation stack is a wiki-relevant counterpoint to [[2507.03152-medval|MedVAL's]] post-hoc validator stance: do the work **before** generation rather than after.

1. **[[GraphRAG]]** over seven cardiology textbooks (knowledge critic). Lifts [[RAGAS]] Faithfulness from 39.87 → 76.60 alone.
2. **[[DSPy]]** automated prompt tuning (orchestration critic). Lifts Context Recall from 9.03 → 27.57 alone.
3. **[[DiagnosisDrivenPrompt|DDP]]** classifier-into-prompt (deterministic critic). Doubles BLEU and triples Rhythm F1 in report generation.

Together (GraphRAG + DSPy + DDP), ECG-Chat reaches 80+ on five of seven [[RAGAS]] metrics. This is a deployed instance of the [[LLMModuloFramework|LLM-Modulo]] Generate-Test-Critique pattern applied to a clinical specialty.

## Connections

- [[2507.03152-medval]] — the paper with the most detailed taxonomy of medical hallucination types this wiki has recorded.
- [[2408.08849-ecg-chat]] — the paper with the most aggressive *pre-hoc* hallucination-mitigation stack (GraphRAG + DSPy + DDP + LaTeX template).
- [[GraphRAG]], [[DSPy]], [[DiagnosisDrivenPrompt]] — the three modules in ECG-Chat's mitigation stack.
- [[MedVAL]] / [[LLMAsAJudge]] — the validator framework + paradigm for detecting hallucinations at deployment time.
- [[MedicalTextValidation]] — the task family hallucination-detection serves in clinical contexts.
- [[RiskLevelTaxonomy]] — the orthogonal severity grading attached to each error.
- [[AlignmentHallucination]] — sister phenomenon in agentic settings.

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] flags hallucination as **the headline blocker of the [[LastMileChallenge|last-mile challenge]]** — the reason teams can reach 80% target quality in a month but need four more months to reach 95%. LinkedIn's 2024 case study (reported in Ch 1) cites *"dealing with hallucinations"* as one of the two biggest reasons the last 15% takes vastly longer than the first 80%.

The Ch 1 framing complements this page's clinical-specialty deep dive: where [[2507.03152-medval|MedVAL]] and [[2408.08849-ecg-chat|ECG-Chat]] give the wiki its taxonomy and mitigation stacks, Huyen's *AI Engineering* situates hallucination as **a planning-level project risk** that needs to be priced into milestone planning, [[UsefulnessThreshold|usefulness thresholds]], and [[AIProductDefensibility|defensibility]] analyses.

The root cause Huyen names is shared with the existing entries: hallucination follows from the **[[AutoregressiveLanguageModel|probabilistic nature]] of generative models** — *"completions are predictions, based on probabilities, and not guaranteed to be correct."* This probability-distribution framing is the structural reason hallucination cannot be eliminated, only managed.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 supplies the **two-hypothesis explanation** for *why* language models hallucinate — both complementary, both recorded in the wiki as separate concept pages:

1. **[[SelfDelusion|Self-delusion]]** (Ortega et al., [[googledeepmind|DeepMind]] 2021) — the model can't differentiate between *data it's given* and *data it generates*. Once it generates a wrong assertion, the next-token prediction treats that assertion as fact. This produces [[SnowballingHallucination|snowballing hallucination]] (Zhang et al. 2023): an initial wrong assumption causes the model to make mistakes on questions it would otherwise answer correctly. Worked example from Ch 2: LLaVA-v1.5-7B identifies a shampoo bottle as milk, then adds milk to the ingredients list it "reads" from the label.
2. **[[InternalKnowledgeMismatch|Internal-knowledge mismatch]]** ([[LeoGao]] / [[JohnSchulman]] 2023) — during [[SupervisedFinetuning|SFT]], the model is trained to mimic labeler responses requiring knowledge the model doesn't have, **effectively teaching the model to make things up**. Schulman's proposed mitigations: ask the model to retrieve sources, and train the [[RewardModel|reward model]] to punish making things up more heavily.

Per Ch 2: *"The self-delusion hypothesis focuses on how self-supervision causes hallucinations, whereas the mismatched internal knowledge hypothesis focuses on how supervision causes hallucinations."* The two are complementary.

### The contested RLHF empirical record

Ch 2 documents an internal-to-OpenAI contradiction worth flagging in the wiki:

- **John Schulman** (UC Berkeley 2023): OpenAI found RLHF *helps reduce* hallucinations.
- **InstructGPT paper** (Ouyang et al. 2022, Fig 2-26 in Ch 2): RLHF *worsened* hallucinations vs SFT alone.

Net: labelers preferred the RLHF model overall even though it hallucinated more — RLHF improved other qualities that mattered to users.

### Practical mitigations from Ch 2

- Prompt the model to be honest: *"Answer as truthfully as possible, and if you're unsure, say 'Sorry, I don't know.'"*
- Ask for **concise responses** — fewer tokens, fewer opportunities to invent.
- Prompting + memory systems (Chs 5–6).
- Detection / measurement covered in Ch 4.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 supplies the **measurement framework**. The operationalization is [[FactualConsistency|factual consistency]] — split into [[LocalFactualConsistency|local]] (against given context — RAG, summarization, customer support) and [[GlobalFactualConsistency|global]] (against open knowledge — chatbots, fact-checking). Three detection approaches:

1. **[[LLMAsAJudge|AI-as-judge prompts]]** — Liu et al. 2023, Luo et al. 2023 — GPT-3.5/4 outperform prior methods.
2. **[[SelfCheckGPT|Self-verification]]** — Manakul et al. 2023 — generate N variants, check disagreement. Expensive.
3. **[[SAFEEvaluator|Knowledge-augmented verification]]** — Wei et al. 2024 (DeepMind) — decompose, revise, search, verify.

[[TextualEntailment|NLI/textual entailment]] classifiers like [[DeBERTaV3FactConsistency|DeBERTa-v3-base-mnli-fever-anli]] (184M params) provide cheap specialized scorers — *"much smaller, faster, and cheaper than general-purpose AI judges."*

Ch 4's hallucination-pattern observations from Huyen's own work:
- **Niche knowledge** — more hallucination on VMO (Vietnamese Math Olympiad) than IMO.
- **Non-existent referents** — more hallucination on *"What did X say about Y?"* when X never said anything about Y.

Use these to design hallucination-focused [[PrivateBenchmark|private evaluation sets]]. [[TruthfulQA]] / [[GPTJudge]] are the canonical public benchmark + paired judge for global factual consistency (90-96% human agreement).

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

[[hands-on-llm-ch01-introduction-to-llms|Hands-On LLMs Ch 1]] mentions hallucination under the *"Generating harmful content"* point of its responsibility framing:

> "An LLM does not necessarily generate ground-truth content and might confidently output incorrect text. Moreover, they can be used to generate fake news, articles, and other misleading sources of information." — Ch 1

The framing here is **societal-impact-first** rather than the mechanistic / measurement / mitigation breakdown the Huyen and MedVAL / ECG-Chat treatments provide elsewhere on this page. Together they triangulate hallucination from three angles: societal risk (Alammar & Grootendorst), engineering-discipline planning risk (Huyen), and clinical-deployment mitigation engineering (MedVAL / ECG-Chat).

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Ch 5 names hallucination as the **headline failure mode that prompt engineering tries to mitigate** — and three Ch 5 levers connect directly:

1. **[[ContextConstruction|Context construction]]** — *"Context can also mitigate hallucinations. If the model isn't provided with the necessary information, it'll have to rely on its internal knowledge, which might be unreliable, causing it to hallucinate."* The [[rag|RAG]] case.
2. **[[chainofthought|CoT]]** — *"LinkedIn found that CoT also reduces models' hallucinations."* Time-to-think reduces confabulation.
3. **Reverse-prompt-engineering outputs are often hallucinated.** *"Let's say you trick a model into spitting out what looks like its system prompt. How do you verify that this is legitimate? More often than not, the extracted prompt is hallucinated by the model."* — a *defensive* use of hallucination as an inadvertent attack-mitigation property.

These three threads make hallucination both a target (mitigations 1-2) and an asset (3) in Ch 5's framing.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

Ch 6 names hallucination as the **dominant failure mode of agent planning**:

> *"Because both the action sequence and the associated parameters are generated by AI models, they can be hallucinated. Hallucinations can cause the model to call an invalid function or call a valid function but with wrong parameters."*

This is the structural reason [[PlanningFailure|planning failures]] are so common — every step in a multi-step plan is a fresh hallucination surface. Concrete failure modes:

- **Hallucinated tool names** (the *"invalid tool"* failure family).
- **Hallucinated parameter values** (the *"valid tool, incorrect parameter values"* family).
- **Hallucinated identity resolution** in [[QueryRewriting|query rewriting]] — Huyen's *"How about his wife?"* example, where the rewriter must refuse rather than invent.
- **Hallucinated success signals** — the [[ReflectionFailure|reflection-failure]] family where the agent insists a task is done when it isn't.

Mitigations Huyen names that go beyond Ch 1-5's coverage:

- **Decouple planning from execution** — validate plans before running them; reject hallucinated plans.
- **Natural-language plans + translator** — translators are less prone to hallucinate than direct function-name generation when tool APIs change.
- **External verification** of reflection outputs — don't trust the model's own *"task complete"* signal.

The Ch 6 contribution is the recognition that **hallucination at the action layer is more dangerous than at the response layer** — a hallucinated bank-transfer is structurally worse than a hallucinated fact.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

Ch 7 takes a measured position on finetuning-as-hallucination-mitigation:

> "[[FineTuning|Finetuning]], on the other hand, helps your model understand and follow syntaxes and styles. While finetuning can potentially reduce hallucinations if done with enough high-quality data, it can also worsen hallucinations if the data quality is low."

So finetuning is **not the recommended primary hallucination defense** — [[rag|RAG]] is — but it can help when the hallucination is **format-driven** (e.g., the model invents fake JSON keys because it hasn't seen the target schema) rather than **fact-driven**.

[[ChipHuyen|Huyen]] also surfaces the [[Llama31Paper|Llama 3.1]] (Dubey et al. 2024) principle quoted in Ch 7:

> "post-training should align the model to 'know what it knows' rather than add knowledge."

The implication: adding new factual knowledge via finetuning is a known anti-pattern — it tends to introduce hallucination because the model hasn't generalized over the new facts the way pre-training generalizes over web-scale data. Use RAG for new facts.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Ch 8 adds a new **causal mechanism** for hallucination from the dataset-engineering side: **[[SuperficialImitation|superficial imitation]]** from synthetic-data distillation.

Per Gudibande et al. (2023) [[FalsePromiseOfImitatingLLMs|*The False Promise of Imitating Proprietary LLMs*]]:

> "Imitation can force the student model to hallucinate. Imagine if the teacher model is capable of answering complex math questions, so its responses to those questions are solutions. Training a student model on these solutions effectively teaches it to produce answers that look like solutions, even if the student model isn't capable of solving these questions."

This is **structurally identical to Schulman's [[InternalKnowledgeMismatch|internal-knowledge mismatch]] hypothesis** (Ch 2) — the only difference is whether the misaligned-knowledge-bearer is a human labeler (Ch 2) or a teacher LLM (Ch 8). In both cases, training data that demonstrates knowledge the model doesn't have teaches the model to **fabricate**.

Ch 8 footnote makes the analogy explicit:

> "The same issue can happen with human annotations. If the human labeler uses the knowledge they have but the model doesn't to answer a question, they are effectively teaching the model to hallucinate."

### Synthesis-pipeline mitigations

The chapter's recommendation: distillation should be used for **style transfer** (the student already has the capability), not **capability transfer** (the student doesn't yet have the capability). For capability building, focus on improving the **base model** rather than imitating a stronger teacher.

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 lists hallucination as the **second of three instruction-prompting tips** (after specificity, before order):

> *"LLMs may generate incorrect information confidently, which is referred to as hallucination. To reduce its impact, we can ask the LLM to only generate an answer if it knows the answer. If it does not know the answer, it can respond with 'I don't know.'"* — Ch 6

This is the **"give the model an out"** technique — an alternative to forcing the model to always answer. Consistent with Huyen Ch 2's recommendation to *"Answer as truthfully as possible, and if you're unsure, say 'Sorry, I don't know.'"*

Ch 6 also positions hallucination as **one of the four motivations** for [[OutputVerification|output verification]] — *"the aim is to double-check whether the generated information is factually accurate, coherent, or free from hallucination."* In Ch 6's framing, [[GrammarConstrainedDecoding|grammar-constrained decoding]] does not directly reduce factual hallucination (it constrains *structure*, not *truth*); only fine-tuning (Ch 12) or post-hoc validation (e.g., [[Guardrails]]) provide that lever at the model level.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 frames hallucination as **the structural motivation for [[rag|RAG]]** — the chapter's headline historical anchor:

> *"The fast adoption of text generation models led many users to ask the models questions and expect factual answers. And while the models were able to answer fluently and confidently, their answers were not always correct or up-to-date. This problem grew to be known as model 'hallucinations,' and one of the leading ways to reduce it is to build systems that can retrieve relevant information and provide it to the LLM to aid it in generating more factual answers."* — Ch 8

The same framing repeats in the RAG section:

> *"The mass adoption of LLMs quickly led to people asking them questions and expecting factual answers. While the models can answer some questions correctly, they also confidently answer lots of questions incorrectly. The leading method the industry turned to remedy this behavior is RAG."*

**The structural mitigation Ch 8 builds**: [[GroundedGeneration|grounded generation]] anchors the LLM's claims on retrieved documents (reducing hallucination by reducing the LLM's reliance on parametric memory) + [[CitationGeneration|citation generation]] makes the grounding **mechanically verifiable** (so hallucinations can be detected, not just reduced) + [[Faithfulness|Faithfulness]] / [[CitationRecall|citation recall]] evaluation axes make hallucination **measurable at scale** via [[llmasjudge|LLM-as-a-judge]].

This is **the most comprehensive hallucination-mitigation stack** in the wiki's RAG sources — Ch 8 covers the full pipeline from cause (industry adoption + factual-answer expectation gap) → architecture (retrieve + ground + cite) → evaluation (Liu et al. 2023 four-axis + Ragas).
