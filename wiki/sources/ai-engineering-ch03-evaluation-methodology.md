---
title: "AI Engineering Ch 3 — Evaluation Methodology"
type: source
tags: [book, evaluation, ai-engineering, oreilly, ai-engineering-book]
date: 2024-12-04
source_file: raw/papers/ai-engineering/ch03-evaluation-methodology.md
parent_source: ai-engineering-chip-huyen
---

# AI Engineering Ch 3 — Evaluation Methodology

## Summary

Chapter 3 of [[ChipHuyen|Chip Huyen]]'s *AI Engineering* ([[OReilly|O'Reilly Media]], 2024) is the **methodology half** of the book's two-chapter [[Evaluation|evaluation]] backbone (Ch 4 covers *applying* methodology to AI systems). It opens with the **structural reasons evaluation is harder for [[FoundationModel|foundation models]]** — open-endedness, model opacity, fast benchmark saturation, expanded scope — then walks four families of automatic evaluation in increasing subjectivity: (1) **language modeling metrics** ([[CrossEntropy|cross entropy]], [[Perplexity|perplexity]], [[BitsPerCharacter|BPC]], [[BitsPerByte|BPB]]); (2) **[[ExactEvaluation|exact evaluation]]** — [[FunctionalCorrectness|functional correctness]] (the `pass@k` family used by [[HumanEval]] / [[MBPP]] / [[Spider]]) and [[SimilarityMeasurement|similarity to reference data]] (exact match, [[LexicalSimilarity|lexical]] via [[bleu|BLEU]] / [[ROUGE]] / [[METEOR]] / [[TER]] / [[CIDEr]], [[SemanticSimilarity|semantic]] via embeddings / [[BERTScore]] / [[MoverScore]]); (3) **[[LLMAsAJudge|AI as a judge]]** — the rising-star subjective method, with three usage patterns (score by itself, compare to reference, pairwise compare) and three specialized variants ([[RewardModel|reward models]] like Google's [[Cappy]], [[ReferenceBasedJudge|reference-based judges]] like [[BLEURT]] / [[Prometheus2|Prometheus]], [[PreferenceModel|preference models]] like [[PandaLM]] / [[JudgeLM]]); and (4) **[[ComparativeEvaluation|comparative evaluation]]** — ranking models via pairwise matches with rating algorithms ([[EloRating|Elo]], [[BradleyTerry|Bradley-Terry]], [[TrueSkill]]), exemplified by [[ChatbotArena|LMSYS Chatbot Arena]].

The chapter's signature framing: **AI judges are not just models — they are systems (model + prompt + sampling)**. Changing any of these changes the judge. Because criteria like *faithfulness* are not standardized — [[MLflow]], [[Ragas]], and [[LlamaIndex]] all ship different faithfulness prompts with different scoring scales (1-5, 0/1, YES/NO) — scores are **not comparable across tools**. Huyen's directive is unambiguous: *"do not trust any AI judge if you can't see the model and the prompt used for the judge."*

The chapter also names five concrete **AI-judge biases**: [[SelfBiasJudge|self-bias]] (GPT-4 favors itself by 10%, Claude-v1 by 25%), [[FirstPositionBias|first-position bias]] (the AI inverse of human [[RecencyBias|recency bias]]), [[VerbosityBias|verbosity bias]] (GPT-4 and Claude-1 prefer ~100-word factually-wrong answers over ~50-word correct ones — Wu & Aji 2023), plus inconsistency and criteria ambiguity. The comparative-evaluation section opens the wiki's first systematic treatment of [[EloRating|Elo]]-style ranking applied to LLMs, including [[ChatbotArena]]'s switch from Elo to Bradley-Terry (Elo proved sensitive to evaluator/prompt ordering), the [[TransitivityAssumption|transitivity assumption]] (and arguments against it for AI preferences), and the **scalability bottleneck** (LMSYS evaluated 57 models with only 244K comparisons = 153 per pair across 1,596 pairs).

## Key Claims

- **Evaluation is the limiting factor in real-world AI deployment.** *"As teams rush to adopt AI, many quickly realize that the biggest hurdle to bringing AI applications to reality is evaluation. For some applications, figuring out evaluation can take up the majority of the development effort."* OpenAI cofounder Greg Brockman tweeted in Dec 2023 that *"evals are surprisingly often all you need."*
- **Four structural reasons FM evaluation is harder than ML evaluation**: (1) smarter models are harder to evaluate (you'd need PhD math to grade PhD math); (2) open-endedness undermines ground-truth lists; (3) most FMs are **black boxes** to evaluators; (4) **benchmarks saturate fast** — [[GLUE]] (2018) saturated in a year → [[SuperGLUE]] (2019); [[NaturalInstructions]] (2021) → Super-NaturalInstructions (2022); [[mmlu|MMLU]] (2020) → [[MMLUPro|MMLU-Pro]] (2024).
- **Evaluation R&D lags AI R&D.** DeepMind (Balduzzi et al.) noted *"developing evaluations has received little systematic attention compared to developing algorithms."* [[anthropic|Anthropic]] has called on policymakers to fund evaluation research. Of the top 1,000 GitHub AI repos (May 2024), ≈50 are dedicated to evaluation — small vs modeling/training/orchestration tooling.
- **Four language-modeling metrics are all variants of each other**: [[CrossEntropy|cross entropy]] (the loss), [[Perplexity|perplexity]] = `2^H` (or `e^H` for [[Nat|nats]]), [[BitsPerCharacter|BPC]] (bits/character), [[BitsPerByte|BPB]] (bits/byte — the standardized cross-encoding metric). If you know one, you can compute the others. Higher predictive accuracy = lower for all four.
- **Cross-entropy decomposes** as `H(P, Q) = H(P) + D_KL(P‖Q)` — the training-data entropy plus the KL divergence between the model and the true distribution. A perfect learner has KL=0.
- **Cross entropy = compression efficiency**. If a model's BPB is 3.43, it can represent each original 8-bit byte using 3.43 bits — compressing original text to less than half its size.
- **Three rules of thumb for perplexity**: (1) more structured data → lower expected perplexity (HTML < everyday text); (2) bigger vocabulary → higher perplexity (War and Peace > children's book; word-level > character-level); (3) longer context length → lower perplexity. Modern models compute PPL conditioned on 500–10,000 previous tokens. Values **as low as 3 or below** are common.
- **Perplexity can detect data contamination and deduplicate training data**: if a model's perplexity on a benchmark is unusually low, that benchmark was likely in training data. Conversely: add new data to training only if its perplexity is high.
- **Perplexity caveat for post-trained models**: *"A language model's perplexity typically increases after post-training. Some people say that post-training collapses entropy."* SFT and RLHF teach task completion at the expense of next-token-prediction calibration. [[Quantization|Quantization]] also changes perplexity in unexpected ways.
- **Exact evaluation has two branches**: [[FunctionalCorrectness|functional correctness]] (does the system perform its intended function?) and [[SimilarityMeasurement|similarity to references]] (exact match / lexical / semantic).
- **`pass@k` is the canonical code-eval metric.** For each problem, generate `k` candidate solutions; a problem is "solved" if any of the `k` passes all unit tests. Higher `k` → higher score. Used by [[HumanEval]] (OpenAI), [[MBPP]] (Google), and the text-to-SQL benchmarks [[Spider]] / [[BIRDSQL|BIRD-SQL]] / [[WikiSQL]].
- **BLEU correlates with neither functional correctness nor human judgment reliably.** OpenAI found on [[HumanEval]] that BLEU scores for incorrect and correct solutions were similar (Chen et al. 2021). Adept's [[Fuyu]] model received low scores not because outputs were wrong but because reference captions were incomplete. [[WMT2023]] organizers found *"many bad reference translations in their data."*
- **Lexical similarity = surface overlap** (BLEU n-gram precision, ROUGE n-gram recall, [[EditDistance|edit distance]] / fuzzy matching, [[METEOR]] / [[TER]] / [[CIDEr]]). **Semantic similarity = embedding-space cosine** ([[BERTScore]], [[MoverScore]]). Examples of the lexical/semantic divergence: *"What's up?"* vs *"How are you?"* (lexically distant, semantically close); *"Let's eat, grandma"* vs *"Let's eat grandma"* (lexically close, semantically opposite).
- **Embedding sizes** (Table 3-2): [[bert|BERT]]-base 768 / large 1024; [[CLIP]] text 512 / image 512; OpenAI `text-embedding-3-small` 1536 / `text-embedding-3-large` 3072; Cohere `embed-english-v3.0` 1024 / light 384. *"Typically between 100 and 10,000."*
- **Joint / multimodal embedding spaces** are the new frontier: [[CLIP]] (text + image, 2021), [[ULIP]] (text + image + 3D point clouds, 2022), [[ImageBind]] (6 modalities including audio, 2023).
- **The MTEB benchmark** ([[MTEB|Massive Text Embedding Benchmark]], Muennighoff et al. 2023) measures embedding quality across multiple downstream tasks.
- **AI-as-judge is the dominant in-production evaluation method as of 2024.** [[LangChain]]'s 2023 State of AI report: **58% of evaluations on their platform were done by AI judges**. Most AI-eval startup demos in 2023-2024 leveraged AI as a judge.
- **GPT-4 reaches 85% agreement with humans** on [[MTBench]] — *higher than human-to-human agreement (81%)* (Zheng et al. 2023). [[AlpacaEval]] has 0.98 correlation with [[ChatbotArena|LMSYS Chat Arena]] (Dubois et al. 2023).
- **Three patterns for using AI as a judge**: (1) score a response by itself, (2) compare to reference, (3) pairwise-compare two responses. The third feeds preference data for post-training and powers comparative evaluation.
- **Built-in AI-judge criteria vary by tool** (Table 3-3): [[AzureAIStudio]] has *groundedness, relevance, coherence, fluency, similarity*; [[MLflow]] has *faithfulness, relevance*; [[LangChain]] Criteria Evaluation has 11 including *conciseness, harmfulness, maliciousness, misogyny*; [[Ragas]] has *faithfulness, answer relevance*. **None are standardized.**
- **Three scoring-system choices for AI judges**: classification, discrete numerical (1-5), or continuous numerical (0-1). *"Language models are generally better with text than with numbers."* Classification > numerical; discrete > continuous; wider discrete range → worse.
- **Including evaluation examples in the prompt** raises GPT-4 judge consistency from 65% to 77.5% but **quadruples GPT-4 API spend** (Zheng et al. 2023). High consistency ≠ high accuracy — the judge may consistently make the same mistakes.
- **Three documented AI-judge biases**: [[SelfBiasJudge|self-bias]] (GPT-4 +10%, Claude-v1 +25% own-response win-rate); [[FirstPositionBias|first-position bias]] (humans have the opposite [[RecencyBias|recency bias]]); [[VerbosityBias|verbosity bias]] (GPT-4 and Claude-1 prefer longer-but-wrong answers; Saito et al. 2023 — at 2× length the judge "almost always prefers the longer one"; gets better with stronger models).
- **A judge can be stronger, weaker, or the same as the model judged.** Each scenario has trade-offs. *"Some argue that judging is an easier task than generating. Anyone can have an opinion about whether a song is good, but not everyone can write a song. Weaker models should be able to judge the outputs of stronger models."*
- **[[SelfEvaluation|Self-evaluation]] / [[SelfCritique|self-critique]]** (Press et al. 2022; Gou et al. 2023; Valmeekam et al. 2023) — a model judges its own response and may revise. Useful for sanity checks despite self-bias.
- **Three specialized judge types**: [[RewardModel|reward models]] (Google's [[Cappy]], 360M params, score in [0,1]); [[ReferenceBasedJudge|reference-based judges]] ([[BLEURT|BLEURT]] outputs similarity in ≈[-2.5, 1.0]; [[Prometheus2|Prometheus]] outputs 1-5 assuming reference = 5); [[PreferenceModel|preference models]] ([[PandaLM]], [[JudgeLM]]) — predict which of two responses humans would prefer.
- **[[ComparativeEvaluation|Comparative evaluation]] was first used in AI by [[anthropic|Anthropic]] in 2021** to rank models, and powers [[ChatbotArena|LMSYS Chatbot Arena]]. *"For responses whose quality is subjective, comparative evaluation is typically easier to do than pointwise evaluation."*
- **Win rate is the basic comparative signal**, then a [[RatingAlgorithm|rating algorithm]] (Elo, Bradley-Terry, TrueSkill) converts pairwise win rates into a model ranking. **LMSYS originally used [[EloRating|Elo]] but switched to [[BradleyTerry|Bradley-Terry]]** because *"they found Elo sensitive to the order of evaluators and prompts."* Even after switching, the Bradley-Terry scores were rescaled (×400, +1000, normalized so Llama-13b=800) to *"make them look like Elo scores."*
- **Comparative-evaluation scalability bottleneck**: number of model pairs grows quadratically. **LMSYS evaluated 57 models using 244,000 comparisons = ≈153 per pair across 1,596 pairs.** Transitivity assumption (A>B, B>C → A>C) is used but is contested for AI preferences (Boubdir et al.; Balduzzi et al.; Munos et al.).
- **Not all questions should be answered by preference.** *"Imagine asking the model 'Is there a link between cell phone radiation and brain tumors?' and the model presents two options, 'Yes' and 'No', for you to choose from. Preference-based voting can lead to wrong signals."* Preference-voting only works when voters are knowledgeable. Comparative evaluation must not be confused with [[ABTesting|A/B testing]] (A/B = one output at a time; comparative = multiple side-by-side).
- **Crowdsourced comparisons have quality issues**: 180 of 33,000 LMSYS prompts in 2023 were "hello"/"hi" (0.55%); the question *"X has 3 sisters, each has a brother. How many brothers does X have?"* was asked 44 times. Simple prompts can't differentiate models — LMSYS now filters out easy prompts and ranks only on hard prompts.
- **Comparative-to-absolute gap**: a 51% win rate over a baseline does not translate cleanly to a known performance boost. *"Comparative evaluation tells us which model is better. It doesn't tell us how good a model is or whether this model is good enough for our use case."*

## Key Quotes

> "The more AI is used, the more opportunity there is for catastrophic failure." — opening of Ch 3

> "As teams rush to adopt AI, many quickly realize that the biggest hurdle to bringing AI applications to reality is evaluation. For some applications, figuring out evaluation can take up the majority of the development effort." — Ch 3

> "Evals are surprisingly often all you need." — Greg Brockman (OpenAI), December 2023, quoted in Ch 3

> "The more intelligent AI models become, the harder it is to evaluate them. Most people can tell if a first grader's math solution is wrong. Few can do the same for a PhD-level math solution." — Ch 3

> "An AI judge is not just a model — it's a system that includes both a model and a prompt. Altering the model, the prompt, or the model's sampling parameters results in a different judge." — Ch 3

> "Do not trust any AI judge if you can't see the model and the prompt used for the judge." — Ch 3

> "A ranking is correct if, for any model pair, the higher-ranked model is more likely to win in a match against the lower-ranked model." — Ch 3, on comparative evaluation

> "Comparative evaluation tells us which model is better. It doesn't tell us how good a model is or whether this model is good enough for our use case." — Ch 3, on the comparative-to-absolute gap

## Concepts Introduced or Engaged

### New concept pages
- [[BitsPerCharacter]] — *new*, BPC unit for cross entropy normalized by character count.
- [[BitsPerByte]] — *new*, BPB — the byte-normalized variant; the cross-encoding-standardized metric.
- [[Nat]] — *new*, the natural-log unit for entropy/cross-entropy used by PyTorch/TensorFlow (vs the bit, base-2).
- [[ExactEvaluation]] — *new*, the evaluation family that produces unambiguous judgments (functional correctness + reference similarity).
- [[FunctionalCorrectness]] — *new*, evaluating whether a system performs its intended function — measurable directly for code (`pass@k`), game bots, and other tasks with measurable objectives.
- [[ExecutionAccuracy]] — *new*, the specific functional-correctness flavor for code (execute the generated code, check outputs).
- [[PassAtK]] — *new*, the canonical code-evaluation metric: solve a problem if any of `k` generated samples passes all tests.
- [[HumanEval]] — *new*, OpenAI's Python code-generation benchmark using functional correctness via test cases.
- [[Spider]] — *new*, Yu et al. 2018 — text-to-SQL benchmark using functional correctness.
- [[BIRDSQL]] — *new*, Li et al. 2023 — Big Bench for Large-scale Database Grounded Text-to-SQL Evaluation.
- [[WikiSQL]] — *new*, Zhong et al. 2017 — earlier text-to-SQL benchmark using functional correctness.
- [[SimilarityMeasurement]] — *new*, the evaluation family that scores generated outputs against reference data.
- [[ReferenceData]] — *new*, the (input, reference responses) ground-truth data that reference-based metrics depend on.
- [[ReferenceFreeMetric]] — *new*, a metric that doesn't need reference data (e.g., perplexity, AI-as-judge).
- [[ReferenceBasedMetric]] — *new*, a metric that requires reference data (e.g., BLEU, ROUGE, BERTScore, exact match).
- [[ExactMatch]] — *new*, binary similarity: does the response match a reference exactly (or contain it)?
- [[LexicalSimilarity]] — *new*, surface-overlap similarity (n-gram, edit distance, fuzzy matching).
- [[EditDistance]] — *new*, the Levenshtein-style minimum-edits distance underlying fuzzy matching.
- [[FuzzyMatching]] — *new*, approximate string matching, often expressed via edit distance.
- [[NGramSimilarity]] — *new*, lexical similarity based on overlapping n-grams instead of single tokens.
- [[METEOR]] — *new*, lexical-similarity metric (one of the BLEU alternatives).
- [[TER]] — *new*, Translation Edit Rate metric.
- [[CIDEr]] — *new*, image-captioning consensus-based metric.
- [[SemanticSimilarity]] — *new*, embedding-space similarity capturing meaning rather than surface form. Also called embedding similarity.
- [[MoverScore]] — *new*, embedding-mixture-based semantic-similarity metric.
- [[MTEB]] — *new*, Massive Text Embedding Benchmark (Muennighoff et al. 2023) — measures embedding quality across multiple downstream tasks.
- [[GLUE]] — *new*, General Language Understanding Evaluation benchmark (2018); saturated in a year.
- [[SuperGLUE]] — *new*, 2019 follow-up to GLUE.
- [[MMLUPro]] — *new*, 2024 successor to MMLU after MMLU saturated for many FMs.
- [[NaturalInstructions]] — *new*, 2021 instruction-following benchmark; replaced by Super-NaturalInstructions in 2022.
- [[BenchmarkSaturation]] — *new*, the phenomenon of benchmarks becoming uninformative once models reach perfect-score territory.
- [[DataContamination]] — *new*, the phenomenon and detection of benchmark data leaking into training data (one perplexity use case).
- [[ComparativeEvaluation]] — *new*, ranking models by pairwise match outcomes rather than by independent scoring.
- [[PointwiseEvaluation]] — *new*, the alternative — evaluate each model independently and rank by score.
- [[RatingAlgorithm]] — *new*, algorithm class that converts pairwise comparison outcomes into model rankings (Elo, Bradley-Terry, TrueSkill).
- [[EloRating]] — *new*, the chess/game rating system originally used by LMSYS Chatbot Arena.
- [[BradleyTerry]] — *new*, the rating algorithm LMSYS switched to after finding Elo sensitive to ordering.
- [[TrueSkill]] — *new*, Microsoft's Bayesian rating algorithm (developed for Xbox Live).
- [[TransitivityAssumption]] — *new*, the A>B ∧ B>C ⇒ A>C assumption rating algorithms make; contested for AI preferences.
- [[WinRate]] — *new*, fraction of matches in which one model is preferred over another — the basic comparative signal.
- [[ChatbotArena]] — *new*, [[LMSYS]]'s crowdsourced LLM-comparison platform.
- [[MTBench]] — *new*, multi-turn benchmark (Zheng et al. 2023) where GPT-4-as-judge reaches 85% agreement with humans.
- [[AlpacaEval]] — *new*, the AI-judge-based eval leaderboard with 0.98 correlation to Chatbot Arena (Dubois et al. 2023).
- [[SelfBiasJudge]] — *new*, AI judge's bias toward its own outputs (GPT-4 +10%, Claude-v1 +25%).
- [[FirstPositionBias]] — *new*, AI judges' bias toward the first option in pairwise comparisons (humans have the opposite).
- [[RecencyBias]] — *new*, the human counterpart — humans favor the option seen last.
- [[VerbosityBias]] — *new*, AI judges prefer longer answers regardless of quality (Wu & Aji 2023; Saito et al. 2023).
- [[SelfEvaluation]] — *new*, a model evaluating its own outputs (overlaps with [[SelfCritique]]).
- [[SelfCritique]] — *new*, the technique of prompting a model to critique its own response and revise. Sometimes "self-ask."
- [[ReferenceBasedJudge]] — *new*, specialized AI judge that evaluates against one or more reference responses (BLEURT, Prometheus).
- [[PreferenceModel]] — *new*, specialized model trained to predict which of two responses humans would prefer (PandaLM, JudgeLM).
- [[BLEURT]] — *new*, Sellam et al. 2020 — learned reference-based similarity score; range ≈[-2.5, 1.0].
- [[PandaLM]] — *new*, Wang et al. 2023 — open preference model (outputs the winner and rationale).
- [[JudgeLM]] — *new*, Zhu et al. 2023 — open preference / judge model.
- [[Cappy]] — *new*, Google 2023 — 360M-param specialized reward model scoring (prompt, response) in [0, 1].
- [[ImageBind]] — *new*, Girdhar et al. 2023 — joint embedding across 6 modalities including text/image/audio.
- [[ULIP]] — *new*, Xue et al. 2022 — unified embedding for text, images, and 3D point clouds.
- [[MultimodalEmbeddingSpace]] — *new*, joint embedding space across modalities enabling cross-modal retrieval (text → image, etc.).
- [[EvaluationCriteriaAmbiguity]] — *new*, the failure mode where the same metric name (e.g., "faithfulness") means different things in different tools.
- [[SpotChecking]] — *new*, evaluating only a subset of responses to reduce eval cost (same as sampling).
- [[VibeCheck]] — *new*, the colloquial name for ad-hoc eyeballing of model outputs.

### Engaged concept pages (updated)
- [[Evaluation]] — *engaged*, this chapter is the methodology backbone.
- [[Perplexity]] — *engaged*, Ch 3 gives the practitioner-grade interpretation (effective vocabulary size; post-training raises PPL; quantization shifts PPL; PPL detects contamination and deduplicates training data).
- [[CrossEntropy]] — *engaged*, the `H(P, Q) = H(P) + D_KL(P‖Q)` decomposition is the chapter's load-bearing derivation.
- [[Entropy]] — *engaged*, the two-token / four-token square-position language example is Ch 3's pedagogical hook.
- [[KullbackLeiblerDivergence]] — *engaged*, named explicitly in the cross-entropy decomposition.
- [[CrossEntropyLoss]] — *engaged*, the practitioner-facing name for the loss every LM minimizes.
- [[bleu|BLEU]] — *engaged*, called out as the dominant pre-FM MT metric; flagged as poorly-correlated with functional correctness on HumanEval (Chen et al. 2021) and with human judgment on WMT'23.
- [[ROUGE]] — *engaged*, sibling to BLEU; recall-side lexical-overlap metric.
- [[BERTScore]] — *engaged*, the canonical semantic-similarity metric (BERT-embedding-based).
- [[Embedding]] — *engaged*, Ch 3 introduces embeddings as the substrate of semantic similarity, with the embedding-size table.
- [[CosineSimilarity]] — *engaged*, the metric used to compute semantic similarity from embeddings.
- [[bert|BERT]] / [[CLIP]] / [[SentenceTransformers]] / [[Word2Vec]] / [[GloVe]] — *engaged*, the embedding-model lineage.
- [[LLMAsAJudge]] / [[llmasjudge]] — *engaged*, this is the canonical AI-as-judge primer in the wiki — three usage patterns, three scoring-system options, three specialized judge types, five biases.
- [[RewardModel]] — *engaged*, Cappy is named as a reward-model judge.
- [[Verifier]] — *engaged*, conceptually adjacent to reward models and reference-based judges.
- [[mmlu|MMLU]] — *engaged*, named as the canonical example of a benchmark that saturated and was replaced (by MMLU-Pro).
- [[MBPP]] — *engaged*, named as a canonical functional-correctness benchmark.
- [[SemanticTextualSimilarity]] — *engaged*, the *task* whose metrics this chapter discusses.
- [[posttraining]] — *engaged*, PPL increases after post-training is a chapter-specific data point.
- [[Quantization]] — *engaged*, also shifts PPL in unexpected ways.

## Entities Introduced or Engaged

### New entity pages
- [[Cohere]] — *new*, embeddings provider (`embed-english-v3.0` 1024, light 384).
- [[AzureAIStudio]] — *new*, Microsoft's AI-eval platform with the built-in *groundedness/relevance/coherence/fluency/similarity* judge criteria.
- [[Ragas]] — *new* (entity for the framework, complementing the existing concept page).
- [[Adept]] — *new*, the AI startup whose [[Fuyu]] model surfaced the lexical-eval reference-data limitation.
- [[Fuyu]] — *new*, Adept's multimodal model; Ch 3's example of a model unfairly low-scored due to missing reference captions.
- [[GregBrockman]] — *new*, OpenAI cofounder; the *"evals are surprisingly often all you need"* quote.
- [[TerrenceTao]] — *new*, Fields medalist; the *"mediocre, but not completely incompetent, graduate student"* characterization of GPT-o1.
- [[a16z]] — *new*, the VC firm whose 2023 study found 6 of 70 decision-makers evaluated models *"by word of mouth."*
- [[LianminZheng]] — *new* (placeholder; principal author of the MT-Bench / GPT-4-as-judge agreement-with-humans paper, Zheng et al. 2023).
- [[ScaleAI]] — *new*, runs the private trained-evaluator comparative leaderboard mentioned as an alternative to crowdsourced.

### Engaged entity pages (updated)
- [[ChipHuyen]] — *engaged*, author; explicitly disclosed her own 2017 NeurIPS workshop paper MEWR as a forerunner of AI-as-judge.
- [[OReilly]] — *engaged*, publisher.
- [[openai|OpenAI]] — *engaged*, HumanEval, the GPT-2 perplexity table, Brockman's evals tweet.
- [[anthropic|Anthropic]] — *engaged*, first AI use of comparative evaluation in 2021; called for policymakers to fund evaluation research.
- [[google|Google]] / [[googledeepmind|Google DeepMind]] — *engaged*, MBPP, Cappy, Balduzzi et al.'s lament about underinvestment in evaluation.
- [[LMSYS]] — *engaged*, Chatbot Arena, the Elo→Bradley-Terry switch, the 57-model/244K-comparison scalability data point.
- [[LangChain]] — *engaged*, 58% of platform evaluations done by AI judges (2023 State of AI report); LangChain Criteria Evaluation has 11 built-in criteria.
- [[LlamaIndex]] — *engaged*, built-in faithfulness criterion with a YES/NO scoring system.
- [[MLflow]] — *engaged*, `MLflow.metrics` includes built-in *faithfulness, relevance*; uses 1-5 scoring.
- [[ChatGPT]] — *engaged*, occasionally asks users to compare two outputs side-by-side as in-product comparative data.

## Connections

- **Ch 2 → Ch 3 transition.** [[ai-engineering-ch02-foundation-models|Ch 2]] introduced the probabilistic, open-ended nature of foundation models — the *cause* of evaluation difficulty. Ch 3 systematizes the *response*. The cross-entropy / perplexity discussion in Ch 3 is the natural continuation of the LM-loss thread opened in Ch 2's pre-training discussion. The AI-as-judge section reuses Ch 2's sampling-variables discussion to argue for judge consistency.
- **Ch 3 → Ch 4.** Ch 4 will *apply* this methodology: evaluation criteria for specific applications, model selection, and pipeline design. Ch 3 is the toolbox; Ch 4 is the workshop.
- **Cross-chapter callbacks.** Ch 3 explicitly forward-references Ch 4 (eval pipeline), Ch 5 (prompt engineering for AI judges), Ch 6 (RAG retrieval as a similarity-search application), Ch 7 (quantization affecting perplexity), and Ch 8 (data deduplication via perplexity).
- **Four concept clusters this chapter anchors in the wiki**:
  1. **Language-modeling-metrics cluster** — [[CrossEntropy]] / [[Perplexity]] / [[BitsPerCharacter]] / [[BitsPerByte]] / [[Nat]] / [[KullbackLeiblerDivergence]]. The wiki had Perplexity, CrossEntropy, and Entropy from D2L but no FM-engineering framing; this chapter supplies it.
  2. **Exact-evaluation cluster** — [[ExactEvaluation]] / [[FunctionalCorrectness]] / [[ExecutionAccuracy]] / [[PassAtK]] / [[HumanEval]] / [[MBPP]] / [[Spider]] / [[BIRDSQL]] / [[WikiSQL]] / [[ExactMatch]] / [[LexicalSimilarity]] / [[SemanticSimilarity]] / [[EditDistance]] / [[NGramSimilarity]]. The first systematic exact-eval taxonomy in the wiki.
  3. **AI-as-judge cluster** — [[LLMAsAJudge]] / [[SelfEvaluation]] / [[SelfCritique]] / [[ReferenceBasedJudge]] / [[PreferenceModel]] / [[BLEURT]] / [[Prometheus2]] / [[PandaLM]] / [[JudgeLM]] / [[Cappy]] / [[SelfBiasJudge]] / [[FirstPositionBias]] / [[VerbosityBias]] / [[RecencyBias]] / [[EvaluationCriteriaAmbiguity]] / [[SpotChecking]]. Ch 3 is the wiki's first methodology-grade treatment of AI-as-judge; the existing [[LLMAsAJudge]] page covered the *medical-text-validation* specialization.
  4. **Comparative-evaluation cluster** — [[ComparativeEvaluation]] / [[PointwiseEvaluation]] / [[RatingAlgorithm]] / [[EloRating]] / [[BradleyTerry]] / [[TrueSkill]] / [[TransitivityAssumption]] / [[WinRate]] / [[ChatbotArena]] / [[MTBench]] / [[AlpacaEval]]. New cluster — the wiki had no Elo/Bradley-Terry/TrueSkill anchor before.
- **Embedding-cluster extension**: [[ImageBind]], [[ULIP]], and [[MultimodalEmbeddingSpace]] join [[Embedding]] / [[CLIP]] / [[BERT]] / [[Word2Vec]] / [[GloVe]] / [[CosineSimilarity]] in the wiki's multimodal-embedding cluster.

## Contradictions

- **`pass@k` increases with k by construction — but model rankings can change.** Ch 3 notes *"in expectation, pass@1 score should be lower than pass@3, which should be lower than pass@10"* — but it does not explicitly flag that the model ranking under pass@k can swap as k grows, a known phenomenon in the code-eval literature. Worth recording on the [[PassAtK]] page for future reconciliation if a source surfaces it.
- **High judge consistency ≠ high judge accuracy** (Zheng et al. 2023, cited in Ch 3): *"high consistency may not imply high accuracy — the judge might consistently make the same mistakes."* This contradicts a naive reading of the *"GPT-4 reaches 85% agreement with humans"* result, which is consistency-with-humans, not absolute correctness. Both records belong on [[LLMAsAJudge]].
- **Comparative-evaluation transitivity is assumed but contested**: rating algorithms assume A>B ∧ B>C ⇒ A>C, but Boubdir et al. / Balduzzi et al. / Munos et al. argue *"human preference is not necessarily transitive"* — and even when individual preferences are transitive, non-transitivity can emerge because different model pairs are evaluated by different evaluators on different prompts. Recorded on [[TransitivityAssumption]] and [[ComparativeEvaluation]].
- **LMSYS Chatbot Arena's Elo→Bradley-Terry switch (with cosmetic Elo-scaled output)** is an internal contradiction in nomenclature: the displayed "Elo scores" are Bradley-Terry scores scaled to look like Elo scores. Flagged on [[EloRating]] and [[ChatbotArena]].
- **BLEU optimization ≠ functional-correctness optimization** (Chen et al. 2021 on HumanEval) — this contradicts the implicit assumption behind many MT and code-generation training pipelines that BLEU is a reasonable proxy. Flagged on [[bleu|BLEU]] and [[FunctionalCorrectness]].

## See also

- [[ai-engineering-ch02-foundation-models]] — chapter immediately preceding this one; introduces the probabilistic nature of FMs that makes evaluation hard.
- [[ai-engineering-ch01-intro]] — first names evaluation as the hardest problem in AI engineering.
- [[ai-engineering-chip-huyen]] — parent source page for the full book.
