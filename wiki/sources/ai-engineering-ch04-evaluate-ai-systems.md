---
title: "AI Engineering Ch 4 — Evaluate AI Systems"
type: source
tags: [book, evaluation, ai-engineering, model-selection, oreilly, ai-engineering-book]
date: 2024-12-04
source_file: raw/papers/ai-engineering/ch04-evaluate-ai-systems.md
parent_source: ai-engineering-chip-huyen
---

# AI Engineering Ch 4 — Evaluate AI Systems

## Summary

Chapter 4 of [[ChipHuyen|Chip Huyen]]'s *AI Engineering* ([[OReilly|O'Reilly Media]], 2024) is the **applied half** of the book's evaluation backbone — where [[ai-engineering-ch03-evaluation-methodology|Ch 3]] develops the methodology, Ch 4 puts it to work in three workflows: (1) defining the **evaluation criteria** for your application, (2) **selecting models** for it, and (3) **designing the evaluation pipeline** that guides development. The chapter opens with [[EvaluationDrivenDevelopment|evaluation-driven development]] — Huyen's TDD-for-AI framing — *"defining evaluation criteria before building."* Most production AI applications (recommenders, fraud detection, coding, classification) succeed because their evaluation criteria are well-defined; the riskiest applications are those *"deployed but no one knows whether it's working."*

The chapter groups evaluation criteria into **four buckets**: (1) [[DomainSpecificCapability|domain-specific capability]] (math, coding, science, language) typically evaluated with [[ExactEvaluation|exact evaluation]] and [[CloseEndedTask|close-ended]] [[MultipleChoiceQuestion|MCQs]] — 75% of [[lm-evaluation-harness|lm-evaluation-harness]] tasks in April 2024 were MCQ; (2) [[GenerationCapability|generation capability]] — [[FactualConsistency|factual consistency]] ([[LocalFactualConsistency|local]] vs [[GlobalFactualConsistency|global]]; [[SelfCheckGPT]] and [[SAFEEvaluator|SAFE]] as advanced detectors; [[TextualEntailment]] / NLI as the classification framing; [[TruthfulQA]] as benchmark) and [[Safety|safety]] (six harm categories; [[PerspectiveAPI]], Meta's [[LlamaGuard]], [[OpenAIModeration]]; [[RealToxicityPrompts]] and [[BOLD]] benchmarks); (3) [[InstructionFollowingCapability|instruction-following capability]] — measured by [[IFEval]] (Google, 25 automatically-verifiable instruction types) and [[INFOBench]] (broader format/content/linguistic/style criteria, yes/no decomposed); plus a deep dive on [[Roleplaying]] capability ([[RoleLLM]], [[CharacterEval]]); and (4) [[CostAndLatency|cost and latency]] — [[ParetoOptimization|Pareto optimization]] across [[TTFT]] / [[TPOT]] / [[TimePerQuery|time per query]] / [[TimeBetweenTokens|time between tokens]], plus API-vs-self-hosting cost calculus.

Then the chapter develops the **model-selection workflow**: a four-step iterative loop — filter on [[HardModelAttribute|hard attributes]] → narrow with public benchmarks/[[Leaderboard|leaderboards]] → run private experiments → monitor production. Hard attributes (licenses, training data, privacy policy) cannot be changed; [[SoftModelAttribute|soft attributes]] (accuracy, toxicity) can be improved via prompting/finetuning. The chapter goes deep on the [[ModelBuildVsBuy|build-vs-buy]] decision (seven axes: data privacy, data lineage/copyright, performance, functionality, cost, control, on-device), and on the **[[OpenWeight|open-weight]] vs [[OpenSourceModel|open model]] vs [[CommercialModel|commercial model]] taxonomy** (open weight = weights public, training data not; open model = both; commercial = neither, accessed via [[ModelAPI|model API]] only). [[ModelLicense|Model licenses]] (MIT, Apache 2.0, Llama 2/3 Community License, BigCode RAIL-M) and their constraints (commercial use, MAU caps, distillation rights) are crucial filters. The [[InferenceService|inference service]] (the system hosting the model behind the API) is named explicitly.

The chapter then attacks [[PublicBenchmark|public benchmarks]] head-on: thousands exist ([[bigbench|BIG-bench]] has 214, [[lm-evaluation-harness]] supports 400+, [[OpenAIEvals]] has ≈500); [[Leaderboard|leaderboards]] aggregate a small subset of them ([[OpenLLMLeaderboard|Open LLM Leaderboard]] uses 6, [[HELMLite|HELM Lite]] uses 10, with only [[mmlu|MMLU]] and [[GSM8K]] in common). Huyen presents the **[[BenchmarkCorrelation|benchmark correlation]] table** (Galambosi 2024) showing [[ARCC]] / [[mmlu|MMLU]] / [[WinoGrande]] all strongly correlated (≈0.85-0.90) — *"strongly correlated benchmarks can exaggerate biases."* HuggingFace's June 2024 leaderboard refresh replaced [[GSM8K]] with [[MATHLevel5|MATH lvl 5]] and [[mmlu|MMLU]] with [[MMLUPro]], adding [[GPQA|GPQA]] (graduate-level Q&A), [[MuSR]] (multistep reasoning), and [[BigBenchHard|BBH]] — *"in just a couple of years, benchmarks had to change from grade-level questions to graduate-level questions."* Two leaderboard-aggregation methods are named: simple averaging (HuggingFace) vs **[[MeanWinRate|mean win rate]]** (HELM). [[DataContamination|Data contamination]] is the deepest problem: detected via [[NGramOverlap|n-gram overlap]] (precise but expensive) and [[Perplexity]] (cheap but lossy); [[RylanSchaeffer|Rylan Schaeffer]]'s 2023 satire *"Pretraining on the Test Set Is All You Need"* trained a 1M-param model on benchmark data and outperformed much larger models on those benchmarks.

The chapter ends with the **[[EvaluationPipeline|evaluation pipeline]] design** — six steps: (1) evaluate all components (per-task, per-turn, per-intermediate-output — [[TurnBasedEvaluation|turn-based]] vs [[TaskBasedEvaluation|task-based]]); (2) write an unambiguous [[EvaluationGuideline|evaluation guideline]] (LinkedIn's *"correct response is not always a good response"* — *"You are a terrible fit"* is correct but bad); (3) define criteria and [[ScoringRubric|scoring rubrics]] with worked examples; (4) tie evaluation metrics to **[[BusinessMetric|business metrics]]** (factual consistency 80% → automate 30% of support; 98% → 90%) and stickiness/engagement metrics ([[DAUWAUMAU|DAU/WAU/MAU]]); (5) select evaluation methods (mix-and-match cheap classifiers on 100% + expensive AI judges on 1%; use [[Logprobs]] when available; fall back to human evaluation, including in production — LinkedIn manually evaluates ~500 conversations/day); (6) annotate data and **[[DataSlicing|slice]] it** to detect [[SimpsonsParadox|Simpson's paradox]] and protect against biases; size each evaluation set via [[Bootstrap|bootstrap]] resampling to confirm reliability.

## Key Claims

- **Evaluation-driven development is TDD for AI engineering.** *"In AI engineering, [[EvaluationDrivenDevelopment|evaluation-driven development]] means defining evaluation criteria before building."* The most common production AI applications (recommenders, fraud detection, coding, classification) succeed because their evaluation criteria are well-defined.
- **Evaluation is the biggest bottleneck to AI adoption.** *"I believe that evaluation is the biggest bottleneck to AI adoption. Being able to build reliable evaluation pipelines will unlock many new applications."*
- **Four buckets of evaluation criteria**: [[DomainSpecificCapability]], [[GenerationCapability]] (factual consistency + safety), [[InstructionFollowingCapability]], [[CostAndLatency]].
- **75% of lm-evaluation-harness tasks are MCQ** (April 2024) — including [[mmlu|MMLU]], [[AGIEval]], [[ARCC]]. *"MCQs test the ability to differentiate good responses from bad responses (classification), which is different from the ability to generate good responses."*
- **MCQ outputs are prompt-fragile.** Alzahrani et al. 2024: adding an extra space or appending *"Choices:"* causes models to flip answers.
- **Factual consistency splits into two settings**: [[LocalFactualConsistency|local]] (against given context — summarization, customer support) and [[GlobalFactualConsistency|global]] (against open knowledge — chatbots, fact-checking). *"Factual consistency is much easier to verify against explicit facts."*
- **Models hallucinate more on niche knowledge and on non-existent referents.** Huyen's own project: more hallucination on VMO (Vietnamese Mathematical Olympiad) than IMO; more hallucination on *"What did X say about Y?"* when X never said anything about Y.
- **Three approaches to detect factual consistency**: AI-judge prompt (Liu et al. 2023, Luo et al. 2023 — GPT-3.5/GPT-4 outperform prior methods); [[SelfCheckGPT|self-verification]] (Manakul et al. 2023 — generate N variants, check consistency; expensive); [[SAFEEvaluator|knowledge-augmented verification]] (Wei et al. 2024 DeepMind — decompose, revise, search, verify).
- **[[TextualEntailment]] = factual-consistency classification.** Three classes: entailment, contradiction, neutral. [[DeBERTaV3FactConsistency|DeBERTa-v3-base-mnli-fever-anli]] (184M params, trained on 764K labeled pairs) is the small specialized scorer for this task.
- **[[GPTJudge]] reaches 90-96% accuracy on [[TruthfulQA]]** (Lin et al. 2022).
- **Six categories of unsafe content**: inappropriate language; harmful tutorials; hate speech; violence; stereotypes; political/religious bias. *"OpenAI's GPT-4 is more left-winged and libertarian-leaning, whereas Meta's Llama is more authoritarian"* (Feng et al. 2023).
- **Specialized toxicity classifiers beat general-purpose AI judges on cost.** Examples: [[FacebookHateSpeech|Facebook hate-speech model]], [[SkolkovoToxicityClassifier|Skolkovo toxicity classifier]], [[PerspectiveAPI|Perspective API]] — *"much smaller, faster, and cheaper than general-purpose AI judges."*
- **Toxicity benchmarks**: [[RealToxicityPrompts]] (Gehman et al. 2020 — 100K prompts that elicit toxicity), [[BOLD]] (Dhamala et al. 2021).
- **Instruction-following is easily confused with domain or generation capability.** *"When a model performs poorly, it can either be because the model is bad or the instruction is bad."* Vietnamese lục bát poem example.
- **[[IFEval]]'s 25 automatically-verifiable instruction types** include keyword inclusion/frequency, forbidden words, letter frequency, response language, paragraph/word/sentence count, postscripts, placeholders, bullet count, title format, JSON format.
- **[[INFOBench]] expands instruction-following** to content constraints, linguistic guidelines, style rules — decomposed into yes/no questions answerable by humans or AI. *"GPT-4 is a reasonably reliable and cost-effective evaluator… more accurate than annotators recruited through Amazon Mechanical Turk."*
- **[[Roleplaying]] is the 8th most common LMSYS use case.** Benchmarks: [[RoleLLM]] (Wang et al. 2023 — similarity scores + AI judges); [[CharacterEval]] (Tu et al. 2024 — human annotators + reward model + 5-point scale). *"Negative knowledge"* check: a Jackie Chan NPC shouldn't speak Vietnamese if Jackie Chan doesn't.
- **Latency metrics for FMs**: [[TTFT]] (time to first token), [[TimePerToken]] / [[TPOT]], [[TimeBetweenTokens]], [[TimePerQuery]]. *"It's important to differentiate between the must-have and the nice-to-have."*
- **Why 7B and 65B models exist**: GPUs come in 16/24/48/80 GB sizes; popular models max out these configurations. *"It's not a coincidence that many models today have 7 billion or 65 billion parameters."*
- **Cost economics flip at scale.** API cost per token is roughly fixed; self-hosting cost per token shrinks with utilization. Companies must reevaluate API vs self-host at different scales.
- **[[HardModelAttribute|Hard]] vs [[SoftModelAttribute|soft]] attributes**: hard (license, training data, model size, your privacy policy) — cannot change; soft (accuracy, toxicity, factual consistency) — can improve via prompting/finetuning. Latency is hard if you use an API, soft if you self-host.
- **Four-step model-selection workflow**: filter on hard attributes → narrow with public benchmarks → run private experiments → monitor production. Iterative.
- **[[OpenWeight]] ≠ [[OpenSourceModel|open model]] ≠ [[CommercialModel|commercial model]]**. Open weight: weights public, training data private. Open model: both public. Commercial: neither, accessed only via API. *"As of this writing, the vast majority of open source models are open weight only."*
- **Seven axes of build-vs-buy**: data privacy (Samsung leak via ChatGPT, May 2023 ban; Zoom 2023 ToS backlash); data lineage and copyright (StarCoder memorizes 8% of training set; commercial contracts can shield you); performance (gap closing on MMLU but proprietary leads remain — *"the strongest open source model will lag behind the strongest proprietary models for the foreseeable future"*); functionality (scaling, function calling, structured outputs, [[Logprobs]], finetuning availability); API cost vs engineering cost; control/access/transparency (rate limits, version changes, model deprecation, Italy banning OpenAI 2023); on-device.
- **API providers are motivated to provide better APIs than model providers.** *"For commercial model providers, models are their competitive advantages. For API providers that don't have their own models, APIs are their competitive advantages."*
- **GPT-3.5-turbo-0301 → 1106 migration caused a 10% drop for Voiceflow's intent classification but improved GoDaddy's customer-support chatbot.** Cited as evidence that *"the best model overall might not be the best model for your application."*
- **Same-model-different-API performance can vary.** GPT-4 is available through both [[openai|OpenAI]] and [[microsoft|Azure]]; performance may differ slightly due to optimization techniques.
- **No leaderboard tells the full story.** Hugging Face's Open LLM Leaderboard launched with 4 benchmarks, expanded to 6, then completely replaced them in June 2024. HELM Lite uses 10. Only [[mmlu|MMLU]] and [[GSM8K]] overlap. *"Different leaderboards often end up with different benchmarks, making it hard to compare and interpret their rankings."*
- **HuggingFace averages benchmark scores; HELM uses [[MeanWinRate|mean win rate]]** — *"the fraction of times a model obtains a better score than another model, averaged across scenarios."*
- **Benchmark correlation matters.** Galambosi 2024 Pearson correlation table: [[ARCC]] / [[mmlu|MMLU]] / [[WinoGrande]] are ≈0.87-0.90 correlated (all test reasoning); [[TruthfulQA]] is only moderately correlated (~0.5) with reasoning. *"If two benchmarks are perfectly correlated, you don't want both of them. Strongly correlated benchmarks can exaggerate biases."*
- **Stanford spent $80K–$100K to run full HELM on 30 models.** Running custom benchmarks is expensive; this is the practitioner-facing data point on private-benchmark cost.
- **[[DataContamination|Data contamination]] is rampant.** *"A benchmark stops being useful as soon as it becomes public."* OpenAI's GPT-3 analysis (Brown et al. 2020): **13 benchmarks were ≥40% contaminated**. Detection: [[NGramOverlap|n-gram overlap]] (e.g., 13-token sequences) is precise but expensive; [[Perplexity]] is cheap but lossy.
- **Contamination can be deliberate and benign.** A model trained on benchmark data after benchmark-based selection produces a stronger user-facing model — but the user can't evaluate it on those benchmarks anymore.
- **Public benchmarks help filter out bad models; only custom pipelines find the best.**
- **Evaluate per-component, per-turn, AND per-task.** A PDF-to-text-then-extract-employer pipeline must be evaluated at both steps and end-to-end. *"Task-based evaluation is more important"* but harder.
- **[[EvaluationGuideline|Clear guidelines]] are the backbone of reliable evaluation.** LinkedIn's deployed AI applications surfaced *"creating an evaluation guideline"* as the **first hurdle**. *"A correct response is not always a good response"* — *"You are a terrible fit"* is correct but bad for a Job Assessment app.
- **2.3 different feedback criteria** per application (LangChain State of AI 2023). Customer-support example: relevance + factual consistency + safety.
- **[[ScoringRubric|Scoring systems]] vary**: binary (0/1); ternary (-1/0/1); 1-5; continuous 0-1. The choice depends on data and needs. **Validate the rubric with humans.**
- **Map AI evaluation metrics to business metrics**: factual consistency 80% → automate 30% of support; 90% → 50%; 98% → 90%. Plan around the gradient.
- **Common business metrics**: stickiness ([[DAUWAUMAU|DAU/WAU/MAU]]), engagement (conversations/month, duration). *"While an emphasis on stickiness and engagement metrics can lead to higher revenues, it may also cause a product to prioritize addictive features or extreme content."*
- **Mix-and-match evaluation methods**: cheap classifier on 100% + AI judge on 1%. *"Use logprobs when available."* Use logprobs for classification confidence and for measuring [[Perplexity|perplexity]] of generated text.
- **Human evaluation is the north star even in production.** LinkedIn evaluates *up to 500 daily conversations* manually.
- **[[DataSlicing]] reveals what aggregates hide.** Four reasons to slice: avoid bias, debug, find improvement areas, avoid [[SimpsonsParadox|Simpson's paradox]] (the renal-calculi example: Model A beats Model B in every subgroup but loses overall). *"If you care about something, put a test set on it."*
- **Bootstrap to size your evaluation set.** Draw N samples with replacement from your N evaluation examples, re-score, repeat. If results vary wildly, you need more data.
- **Out-of-scope evaluation sets matter.** Inputs your application isn't supposed to engage with — make sure it handles them appropriately.

## Key Quotes

> "I call this approach evaluation-driven development. The name is inspired by test-driven development in software engineering, which refers to the method of writing tests before writing code. In AI engineering, evaluation-driven development means defining evaluation criteria before building." — Ch 4

> "I believe that evaluation is the biggest bottleneck to AI adoption. Being able to build reliable evaluation pipelines will unlock many new applications." — Ch 4

> "When evaluating models based on latency, it's important to differentiate between the must-have and the nice-to-have. If you ask users if they want lower latency, nobody will ever say no. But high latency is often an annoyance, not a deal breaker." — Ch 4

> "At the end of the day, you don't really care about which model is the best. You care about which model is the best for your applications." — Ch 4

> "A benchmark stops being useful as soon as it becomes public." — quoted from a friend of Huyen's, Ch 4

> "It's both really cool and intimidating to see that in just a couple of years, benchmarks had to change from grade-level questions to graduate-level questions." — Ch 4 footnote on GPQA replacing GSM-8K

> "A correct response is not always a good response. For example, for their AI-powered Job Assessment application, the response 'You are a terrible fit' might be correct but not helpful, thus making it a bad response." — LinkedIn case, quoted in Ch 4

> "If you care about something, put a test set on it." — Ch 4, on data slicing

> "Clear guideline is the backbone of a reliable evaluation pipeline." — Ch 4

## Concepts Introduced or Engaged

### New concept pages
- [[EvaluationDrivenDevelopment]] — *new*, TDD-for-AI: define eval criteria before building.
- [[DomainSpecificCapability]] — *new*, one of four evaluation-criteria buckets.
- [[GenerationCapability]] — *new*, one of four evaluation-criteria buckets (covers factual consistency + safety).
- [[InstructionFollowingCapability]] — *new*, one of four evaluation-criteria buckets.
- [[CostAndLatency]] — *new*, the fourth evaluation-criteria bucket (cost + latency Pareto axis).
- [[FactualConsistency]] — *new*, the generation-capability metric distinguishing hallucination from grounded output.
- [[LocalFactualConsistency]] — *new*, consistency against given context (summarization, customer support).
- [[GlobalFactualConsistency]] — *new*, consistency against open knowledge (chatbots, fact-checking).
- [[SelfCheckGPT]] — *new*, Manakul et al. 2023 self-verification by N-variant disagreement.
- [[SAFEEvaluator]] — *new*, DeepMind's Search-Augmented Factuality Evaluator (Wei et al. 2024 — decompose, revise, search, verify).
- [[TextualEntailment]] — *new*, NLI-style classification (entailment / contradiction / neutral) framing for factual consistency.
- [[DeBERTaV3FactConsistency]] — *new*, the 184M-param `DeBERTa-v3-base-mnli-fever-anli` factual-consistency classifier.
- [[TruthfulQA]] — *new*, Lin et al. 2022 — 817-question factuality benchmark; ships with [[GPTJudge]].
- [[GPTJudge]] — *new*, the fine-tuned TruthfulQA judge that reaches 90-96% agreement with humans.
- [[CloseEndedTask]] — *new*, evaluation framing — outputs picked from a fixed option set (MCQ, classification).
- [[MultipleChoiceQuestion]] — *new*, 75% of lm-evaluation-harness tasks; prompt-fragile (Alzahrani et al. 2024).
- [[lm-evaluation-harness]] — *new*, EleutherAI's harness supporting 400+ benchmarks.
- [[OpenAIEvals]] — *new*, OpenAI's evaluation harness for ≈500 existing benchmarks plus user-registered ones.
- [[EvaluationHarness]] — *new*, the category — tools that let you run a model against many benchmarks.
- [[ARCC]] — *new*, AI2 Reasoning Challenge — grade-school science MCQ.
- [[HellaSwag]] — *new*, Zellers et al. 2019 — sentence-completion MCQ for commonsense.
- [[WinoGrande]] — *new*, Sakaguchi et al. 2019 — pronoun-resolution MCQ.
- [[AGIEval]] — *new*, Microsoft 2023 — human-exam-derived MCQ benchmark.
- [[bigbench]] — *new*, Google's BIG-bench with 214 sub-benchmarks.
- [[BigBenchHard]] — *new*, BBH — reasoning-focused subset of BIG-bench.
- [[GPQA]] — *new* (full page; existing one-liner stub `gpqa.md` will be expanded), graduate-level Q&A benchmark (Rein et al. 2023).
- [[MuSR]] — *new*, Sprague et al. 2023 — multistep chain-of-thought reasoning benchmark.
- [[MATHLevel5]] — *new*, hardest-difficulty subset of the MATH benchmark; replaced GSM8K on Open LLM Leaderboard in June 2024.
- [[HELMLite]] — *new*, Stanford's reduced HELM (10 benchmarks).
- [[OpenLLMLeaderboard]] — *new*, HuggingFace's flagship LLM leaderboard.
- [[Leaderboard]] — *new*, the category — aggregated multi-benchmark ranking surface.
- [[BenchmarkCorrelation]] — *new*, Pearson correlation matrix of benchmarks (Galambosi 2024).
- [[MeanWinRate]] — *new*, HELM's aggregation method — fraction of pairwise wins over scenarios.
- [[CustomLeaderboard]] — *new*, the practice of building a private leaderboard over public benchmarks for your own selection criteria.
- [[Safety]] — *engaged with full rewrite* (existing stub); six harm categories.
- [[PerspectiveAPI]] — *new*, Jigsaw's toxicity API; cited as cheap specialized classifier.
- [[OpenAIModeration]] — *new*, OpenAI's content-moderation endpoint defining harm taxonomy.
- [[FacebookHateSpeech]] — *new*, Meta's specialized hate-speech detection model.
- [[SkolkovoToxicityClassifier]] — *new*, Skolkovo Institute's toxicity classifier.
- [[RealToxicityPrompts]] — *new*, Gehman et al. 2020 — 100K prompts that elicit toxicity.
- [[BOLD]] — *new*, Dhamala et al. 2021 — bias in open-ended language generation benchmark.
- [[Roleplaying]] — *new*, 8th most common LMSYS use case; instruction-following sub-skill.
- [[RoleLLM]] — *new*, Wang et al. 2023 — roleplaying benchmark using similarity scores and AI judges.
- [[CharacterEval]] — *new*, Tu et al. 2024 — roleplaying benchmark with human annotators and reward model.
- [[INFOBench]] — *new*, Qin et al. 2024 — broader instruction-following benchmark (content/linguistic/style criteria, yes/no decomposed).
- [[ParetoOptimization]] — *new*, multi-objective optimization framing for quality / latency / cost.
- [[TimePerToken]] — *new*, alternative name for [[TPOT]].
- [[TimeBetweenTokens]] — *new*, the inter-token-arrival latency metric (different from time-per-token).
- [[TimePerQuery]] — *new*, the end-to-end latency metric per request.
- [[ModelBuildVsBuy]] — *new*, the API-vs-self-hosting decision framework.
- [[OpenWeight]] — *new*, weights public, training data private (most "open source" models today).
- [[OpenSourceModel]] — *new*, the contested term; Huyen uses it broadly for weight-public models.
- [[OpenModel]] — *new*, both weights AND training data public (vs open weight).
- [[CommercialModel]] — *new*, proprietary model accessed only via the developer's API.
- [[ModelLicense]] — *new*, the open-source license attached to a model (MIT, Apache 2.0, Llama 2/3 Community, BigCode RAIL-M, etc.).
- [[LlamaLicense]] — *new*, Meta's Llama 2/3 Community License (MAU cap + distillation restriction).
- [[InferenceService]] — *new*, the service that hosts a model and exposes the API.
- [[ModelAPI]] — *new*, the interface to an inference service.
- [[ModelAPIProvider]] — *new*, the category — model providers, cloud providers, or third-party startups that expose APIs.
- [[HardModelAttribute]] — *new*, attributes that cannot be changed (license, model size, training data).
- [[SoftModelAttribute]] — *new*, attributes you can improve (accuracy, toxicity, factual consistency).
- [[ModelSelectionWorkflow]] — *new*, the four-step iterative filter → narrow → experiment → monitor loop.
- [[PublicBenchmark]] — *new*, externally-developed benchmark from a paper/leaderboard.
- [[PrivateBenchmark]] — *new*, your own evaluation set with proprietary data.
- [[BenchmarkAggregation]] — *new*, the question of how to combine benchmark scores into a single leaderboard ranking.
- [[DataContamination]] — *engaged from Ch 3; deeper treatment here* — detection ([[NGramOverlap]], [[Perplexity]]), 40%+ contamination in 13 GPT-3 benchmarks, satirical *"Pretraining on the Test Set Is All You Need"* paper.
- [[NGramOverlap]] — *new*, the precise-but-expensive contamination-detection method (e.g., 13-token sequence match).
- [[BenchmarkDecontamination]] — *new*, the practice of removing benchmark data from training data.
- [[EvaluationPipeline]] — *new*, the six-step design framework for building a production evaluation pipeline.
- [[TurnBasedEvaluation]] — *new*, evaluation per conversation turn.
- [[TaskBasedEvaluation]] — *new*, evaluation per completed user task (multi-turn).
- [[PerComponentEvaluation]] — *new*, evaluating each sub-component of a pipeline independently.
- [[EvaluationGuideline]] — *new*, the unambiguous rubric document — the backbone of reliable evaluation.
- [[ScoringRubric]] — *new*, the per-criterion scoring schema (binary, 1-5, 0-1, etc.) with worked examples.
- [[BusinessMetric]] — *new*, the dollar-or-engagement metric the evaluation metric maps to (e.g., factual consistency 90% → automate 50%).
- [[DAUWAUMAU]] — *new*, daily/weekly/monthly active users — the canonical stickiness metric.
- [[EngagementMetric]] — *new*, conversations-per-month, time-on-app — the engagement counterpart.
- [[StickinessMetric]] — *new*, retention/return-rate metrics ([[DAUWAUMAU]]).
- [[DataSlicing]] — *new*, partitioning evaluation data to detect bias, debug, and avoid Simpson's paradox.
- [[SimpsonsParadox]] — *new*, the model-A-wins-every-subgroup-but-loses-overall phenomenon; renal-calculi example.
- [[OutOfScopeEvaluation]] — *new*, evaluation set for inputs the application isn't supposed to engage with.
- [[BootstrapEvaluation]] — *new*, sampling-with-replacement procedure to size and validate an evaluation set.
- [[TwentyQuestionsTask]] — *new*, BIG-bench's task-based-evaluation example (Alice picks concept, Bob asks yes/no questions).
- [[BIRDSQLEfficiency]] — *new*, BIRD-SQL's efficiency-aware text-to-SQL evaluation (runtime vs ground-truth runtime).
- [[CodeReadability]] — *new*, the qualitative code-eval dimension AI judges must handle (no exact metric).

### Engaged concept pages (updated)
- [[ModelSelection]] — *engaged*, this chapter is the FM-engineering counterpart to the classical-ML model-selection page.
- [[mmlu|MMLU]] — *engaged*, the only benchmark in both Open LLM Leaderboard and HELM Lite; saturated and replaced by [[MMLUPro]] in June 2024.
- [[MMLUPro]] — *engaged*, the 2024 successor introduced on Open LLM Leaderboard.
- [[GSM8K]] — *engaged*, replaced by [[MATHLevel5]] on Open LLM Leaderboard in June 2024.
- [[HumanEval]] — *engaged*, omitted from HuggingFace's Open LLM Leaderboard due to compute requirements.
- [[BIRDSQL]] — *engaged*, named as the text-to-SQL benchmark that adds efficiency (runtime) to functional correctness.
- [[gpqa|GPQA]] — *engaged*, expanding the stub with Ch 4 framing.
- [[ifeval|IFEval]] — *engaged*, expanding the stub with the 25-instruction-types description and Open LLM Leaderboard usage.
- [[mathbench|MATH-benchmark]] — *engaged*, parent benchmark of [[MATHLevel5]].
- [[Hallucination]] — *engaged*, factual consistency is the metric for detecting it.
- [[safety|Safety]] — *engaged*, full content rewrite from stub.
- [[factuality|Factuality]] — *engaged*, full content rewrite from stub (effectively same topic as factual consistency).
- [[Perplexity]] — *engaged*, used both for contamination detection and as a fluency metric.
- [[Logprobs]] — *engaged*, named as an evaluation-input (classification confidence + perplexity) and as a *commercial-model-API-restriction*.
- [[LLMAsAJudge]] — *engaged*, the dominant method for factual-consistency / safety / instruction-following evaluation.
- [[ChatbotArena]] — *engaged*, used as a model-selection signal (Elo > 1200).
- [[Guardrail]] — *engaged*, called out as a model-functionality dimension.
- [[StructuredOutputs]] — *engaged*, named as a model-functionality dimension and an instruction-following capability.
- [[LlamaGuard]] — *engaged*, named as a content-moderation taxonomy/tool.
- [[FineTuning]] — *engaged*, named as a model-functionality dimension API providers may or may not expose.
- [[FunctionCalling]] — *engaged*, named as a model-functionality dimension essential for RAG and agents.
- [[Quantization]] — *engaged*, named as a self-hosting optimization dimension.
- [[Hugging Face Open LLM Leaderboard]] / [[OpenLLMLeaderboard]] — *engaged*.
- [[TTFT]] — *engaged*, P90 TTFT (< 200ms hard, < 100ms ideal) appears in the example evaluation criteria table.
- [[TPOT]] — *engaged*, alternative name for time-per-token.
- [[UsefulnessThreshold]] — *engaged*, the threshold below which an application is unusable (factual-consistency 50% minimum in the chatbot example).
- [[Benchmarking]] — *engaged*, this chapter is the FM-engineering counterpart.
- [[DistillationKnowledge|Knowledge Distillation]] / [[knowledgedistillation]] — *engaged*, model-license-on-distillation discussion (Mistral originally banned, then permitted; Llama still doesn't).
- [[ai-engineering-ch01-intro]] / [[ai-engineering-ch02-foundation-models]] / [[ai-engineering-ch03-evaluation-methodology]] — *engaged* as cross-chapter references.

## Entities Introduced or Engaged

### New entity pages
- [[RylanSchaeffer]] — *new*, Stanford PhD student, author of the satirical *"Pretraining on the Test Set Is All You Need"* paper (2023).
- [[Voiceflow]] — *new*, the company whose GPT-3.5-turbo-0301→1106 migration dropped intent classification 10%.
- [[GoDaddy]] — *new*, the company whose customer-support chatbot *improved* on the same migration.
- [[Samsung]] — *new*, the company that banned ChatGPT in May 2023 after employees leaked proprietary information.
- [[Zoom]] — *new*, the company whose Aug 2023 ToS update for AI training caused backlash.
- [[Ello]] — *new*, the startup helping kids read better — uses constrained-vocabulary instruction-following.
- [[EleutherAI]] — *new*, the organization behind [[lm-evaluation-harness]].
- [[Jigsaw]] — *new*, Google's subsidiary behind [[PerspectiveAPI]].
- [[BalazsGalambosi]] — *new*, computed the January 2024 benchmark-correlation matrix for HuggingFace.
- [[LewisTunstall]] — *new*, HuggingFace researcher who responded on Discord regarding leaderboard benchmark choice.

### Engaged entity pages (updated)
- [[ChipHuyen]] — *engaged*, author; advisor disclosure for [[Convai]] (carried forward from Ch 1).
- [[OReilly]] — *engaged*, publisher.
- [[openai|OpenAI]] — *engaged*, [[OpenAIEvals]], [[OpenAIModeration]], the GPT-3.5/GPT-4 update controversies, Italy ban anecdote, the Brown et al. 2020 contamination analysis.
- [[anthropic|Anthropic]] — *engaged*, content-moderation Claude tutorial.
- [[google|Google]] / [[googledeepmind|Google DeepMind]] — *engaged*, [[IFEval]], [[SAFEEvaluator]] (Wei et al. 2024), BIG-bench, [[GSM8K]], Gemma open-source under Apache 2.0.
- [[microsoft|Microsoft]] — *engaged*, [[AGIEval]], Azure as a GPT-4 API surface.
- [[meta|Meta]] — *engaged*, [[LlamaGuard]] paper, Llama license, hate-speech detection model.
- [[Mistral]] — *engaged*, Mistral-7B Apache 2.0 release; original distillation ban then license change.
- [[HuggingFace]] — *engaged*, Open LLM Leaderboard, BigCode RAIL-M license, June 2024 leaderboard refresh, contamination-handling practice. The existing entity stub is significantly expanded.
- [[Cohere]] — *engaged*, named as a model-provider-and-API-provider that both open sources and serves.
- [[Databricks]] — *engaged*, named (with [[Anyscale]]) as a third-party model-API provider.
- [[Anyscale]] — *engaged*, named as a third-party model-API provider.
- [[stanforduniversity|Stanford]] — *engaged*, $80K-$100K HELM evaluation cost; Schaeffer's satirical paper.
- [[LMSYS]] — *engaged*, [[ChatbotArena]] used as a soft model-selection signal (Elo > 1200).
- [[LinkedIn]] — *engaged*, the *"correct response is not always good"* Job Assessment example, 500 daily manual evaluations, 2.3-criteria median from LangChain State of AI 2023.
- [[Convai]] — *engaged*, the company that finetuned open-source models because commercial models refused to give NPCs physical abilities (*"As an AI model, I don't have physical abilities"*).
- [[LangChain]] — *engaged*, State of AI 2023 — 2.3 different criteria per app on average.
- [[a16z]] — *engaged*, 2024 study on why enterprises care about open-source models (control + customizability).
- [[microsoftresearch|Microsoft Research]] / [[Skolkovo]] / Adept — *engaged*, the toxicity-classifier landscape.

## Connections

- **Ch 3 → Ch 4 transition.** [[ai-engineering-ch03-evaluation-methodology|Ch 3]] is the methodology toolbox (language-modeling metrics, exact eval, AI-as-judge, comparative eval). Ch 4 *applies* that toolbox to AI systems: defining criteria → selecting models → designing pipelines. Every Ch 4 evaluation method calls back to a Ch 3 primitive.
- **Ch 4 ↔ Ch 5 (prompting).** Roleplaying as a prompt-engineering technique; MCQ output sensitivity to prompt formatting (Alzahrani et al. 2024); structured-output instruction-following.
- **Ch 4 ↔ Ch 6 (RAG).** Local factual consistency *is* the RAG evaluation metric; [[FactualConsistency]] is the RAG-grounding criterion.
- **Ch 4 ↔ Ch 7 (finetuning).** Soft attributes can be improved by finetuning; license restrictions on distillation are a finetuning constraint.
- **Ch 4 ↔ Ch 8 (data synthesis).** [[Roleplaying|Roleplaying]] outputs can train other models; evaluation annotation guidelines can be reused as training-data annotation guidelines.
- **Ch 4 ↔ Ch 9 (cost/latency).** This chapter introduces cost/latency as evaluation criteria; Ch 9 develops the inference-optimization techniques.
- **Ch 4 ↔ Ch 10 (monitoring).** Production monitoring is step 4 of the model-selection workflow.
- **Concept clusters this chapter anchors**:
  1. **Evaluation-criteria taxonomy** — [[DomainSpecificCapability]] / [[GenerationCapability]] / [[InstructionFollowingCapability]] / [[CostAndLatency]] / [[EvaluationDrivenDevelopment]]. New cluster.
  2. **Factual-consistency / safety cluster** — [[FactualConsistency]] / [[LocalFactualConsistency]] / [[GlobalFactualConsistency]] / [[SelfCheckGPT]] / [[SAFEEvaluator]] / [[TextualEntailment]] / [[TruthfulQA]] / [[GPTJudge]] / [[Safety]] / [[RealToxicityPrompts]] / [[BOLD]] / [[PerspectiveAPI]] / [[OpenAIModeration]] / [[LlamaGuard]]. First systematic safety-eval cluster in the wiki.
  3. **Instruction-following cluster** — [[InstructionFollowingCapability]] / [[IFEval]] / [[INFOBench]] / [[Roleplaying]] / [[RoleLLM]] / [[CharacterEval]].
  4. **Benchmark / leaderboard cluster** — [[OpenLLMLeaderboard]] / [[HELMLite]] / [[BenchmarkCorrelation]] / [[MeanWinRate]] / [[CustomLeaderboard]] / [[lm-evaluation-harness]] / [[OpenAIEvals]] / [[EvaluationHarness]] / [[bigbench]] / [[BigBenchHard]] / [[ARCC]] / [[HellaSwag]] / [[WinoGrande]] / [[AGIEval]] / [[MATHLevel5]] / [[GPQA]] / [[MuSR]].
  5. **Model build-vs-buy cluster** — [[ModelBuildVsBuy]] / [[OpenWeight]] / [[OpenSourceModel]] / [[OpenModel]] / [[CommercialModel]] / [[ModelLicense]] / [[LlamaLicense]] / [[InferenceService]] / [[ModelAPI]] / [[ModelAPIProvider]] / [[HardModelAttribute]] / [[SoftModelAttribute]] / [[ModelSelectionWorkflow]].
  6. **Data-contamination cluster** — [[DataContamination]] / [[NGramOverlap]] / [[BenchmarkDecontamination]] (extends Ch 3 cluster).
  7. **Evaluation-pipeline-design cluster** — [[EvaluationPipeline]] / [[EvaluationGuideline]] / [[ScoringRubric]] / [[BusinessMetric]] / [[DAUWAUMAU]] / [[DataSlicing]] / [[SimpsonsParadox]] / [[OutOfScopeEvaluation]] / [[BootstrapEvaluation]] / [[TurnBasedEvaluation]] / [[TaskBasedEvaluation]] / [[PerComponentEvaluation]].

## Contradictions

- **OpenAI model versions perceived as "getting worse" (Chen et al. 2023).** Stanford/UC Berkeley found significant performance changes for GPT-3.5 and GPT-4 between March 2023 and June 2023. Voiceflow lost 10% intent-classification accuracy migrating GPT-3.5-turbo-0301 → 1106, but GoDaddy's customer-support chatbot improved on the same migration. Contradiction recorded on [[openai|OpenAI]] and the new [[Voiceflow]] / [[GoDaddy]] pages.
- **Open vs proprietary performance trajectory.** The MMLU performance gap is closing (Labonne chart), but Huyen's qualitative reasoning is that *"the strongest open source model will lag behind the strongest proprietary models for the foreseeable future"* because incentives favor keeping the strongest model behind paywalls. Recorded as an open tension on [[OpenSourceModel]] and [[CommercialModel]].
- **Data contamination is sometimes the right thing to do.** *"Data contamination can also happen intentionally for good reasons"* — training your best model on benchmark data after benchmark-based selection produces a stronger user-facing model. This contradicts the standard ML-textbook advice to always remove evaluation samples from training data. Flagged on [[DataContamination]].
- **The Llama license restriction is unusual.** *"As of this writing, the Llama licenses still don't allow [output-based training]."* Mistral originally banned distillation but later changed; Llama hasn't. This is a contradiction between the most-popular open-weight model and the typical "open source means open to remix" assumption. Flagged on [[LlamaLicense]].
- **Leaderboard transparency varies.** Public leaderboards balance coverage with cost, but *"if leaderboard developers can't explain their benchmark selection processes, it might be because it's really hard to do so."* — internal contradiction in benchmark-aggregation practice. Recorded on [[Leaderboard]] and [[BenchmarkAggregation]].
- **"Open source" terminology is contested.** Huyen uses *open source* broadly (any weight-public model), while purists reserve it for fully-open (weights + data + license). Recorded on [[OpenSourceModel]] and [[OpenWeight]].

## See also

- [[ai-engineering-ch03-evaluation-methodology]] — methodology backbone; this chapter applies it.
- [[ai-engineering-ch02-foundation-models]] — foundation-model anatomy; supplies probabilistic / open-ended structure that makes evaluation hard.
- [[ai-engineering-ch01-intro]] — first names evaluation as the hardest problem in AI engineering.
- [[ai-engineering-chip-huyen]] — parent source page for the full book.
