---
title: "AI Engineering Ch 2 — Understanding Foundation Models"
type: source
tags: [book, foundation-models, ai-engineering, oreilly, ai-engineering-book]
date: 2024-12-04
source_file: raw/papers/ai-engineering/ch02-foundation-models.md
parent_source: ai-engineering-chip-huyen
---

# AI Engineering Ch 2 — Understanding Foundation Models

## Summary

Chapter 2 of [[ChipHuyen|Chip Huyen]]'s *AI Engineering* ([[OReilly|O'Reilly Media]], 2024) walks through the **four design decisions that determine what a [[FoundationModel|foundation model]] becomes**: (1) **training data** — distribution, language mix, domain coverage; (2) **model architecture and size** — the [[transformer|Transformer]] and its rising challengers, the meaning of "parameter count", and how compute budgets are split via [[ChinchillaScalingLaw|the Chinchilla scaling law]]; (3) **post-training** — [[SupervisedFinetuning|SFT]] followed by [[PreferenceFinetuning|preference finetuning]] ([[rlhf|RLHF]], [[DPO|DPO]], [[RLAIF]]); and (4) **sampling** — temperature, top-k, top-p, structured outputs, and the **probabilistic nature** of generative AI that produces both creativity and the twin failure modes of [[Inconsistency|inconsistency]] and [[Hallucination|hallucination]].

Huyen positions sampling as *"perhaps one of the most underrated concepts in AI"* — not only does it explain hallucinations and inconsistency, but choosing the right sampling strategy can substantially boost a model's performance with little effort. The chapter also introduces the [[TestTimeCompute|test-time compute]] family ([[bestofn|best-of-N]], [[selfconsistency|self-consistency]], [[beamsearch|beam search]], verifier-guided selection) — sampling more outputs at inference to trade compute for quality — and gives DeepMind's striking result that a [[Verifier|verifier]] over multiple samples is worth roughly a **30× model-size increase**.

The chapter introduces the **two visible scaling bottlenecks** (training data and electricity), the **[[InverseScaling|inverse scaling]] phenomenon** ([[NYU|NYU]]'s Inverse Scaling Prize and Anthropic's finding that more alignment training can produce *less* aligned models), and the **two leading hypotheses for why language models hallucinate**: [[SelfDelusion|self-delusion]] (DeepMind 2021 — the model can't differentiate its own generated text from given facts) and [[InternalKnowledgeMismatch|internal-knowledge mismatch]] (Leo Gao / John Schulman — SFT teaches the model to mimic responses requiring knowledge the model doesn't have). The two hypotheses are complementary: self-supervision causes one, supervision causes the other.

## Key Claims

- **A model is only as good as its training data.** [[CommonCrawl|Common Crawl]] (≈2–3 B web pages/month) and its filtered subset [[c4|C4]] dominate FM pre-training despite known quality issues (clickbait, misinformation, low-trust outlets). [[openai|OpenAI]] filtered [[CommonCrawl]] for [[GPT2|GPT-2]] using *Reddit links with ≥3 upvotes*.
- **English dominates the training distribution at 45.88% of [[CommonCrawl|Common Crawl]]**, 8× the next language (Russian, 5.97%). Under-represented languages (Punjabi, Swahili, Urdu, Telugu, Marathi, Bengali) have **world-to-CommonCrawl ratios of 36×–231×** — and [[GPT4|GPT-4]] performs much worse on [[mmlu]] in Telugu than in English. Three structural problems for low-resource languages: under-representation, structural difference, and **inefficient tokenization** (Burmese median ≈72 tokens vs English ≈7 for the same content — 10× latency and 10× API cost).
- **A smaller, higher-quality dataset can beat a larger, low-quality one.** Gunasekar et al. (2023) trained a 1.3B-param model on **7B tokens of high-quality coding data** that outperformed much larger models on coding benchmarks.
- **[[DomainSpecificModel|Domain-specific FMs]] are common in biomedicine**: [[AlphaFold]] (≈100K protein structures), [[BioNeMo]] (drug discovery), [[MedPaLM2]] (medical QA).
- **The [[transformer|Transformer]] dominates** because it (a) replaces RNN's sequential bottleneck via [[Attention|attention]], (b) parallelizes input processing, and (c) was heavily optimized since 2017 first on [[google|Google]]'s [[TPU|TPUs]] then on [[GPU|GPUs]]. Two-stage inference: **[[Prefill|prefill]]** (parallel processing of input tokens) and **[[Decode|decode]]** (sequential one-token-at-a-time generation).
- **Three [[transformer|Transformer]] alternatives are gaining traction**: [[RWKV]] (RNN-based, parallelizable training), [[StateSpaceModel|SSMs]] (S4 → H3 → [[Mamba]] — linear-time inference, 3B Mamba matches transformers 2× its size), and [[Jamba]] (hybrid Transformer–Mamba MoE; 52B total / 12B active in one 80GB GPU; strong up to 256K context).
- **Three numbers signal a model's scale**: number of parameters (learning capacity), number of training tokens (how much it learned), number of [[FLOPs|FLOPs]] (training cost). GPT-3-175B was trained using **3.14 × 10²³ FLOPs**; on 256 H100s at 70% utilization at $2/h that's ≈**$4.14M and ≈236 days**.
- **The [[ChinchillaScalingLaw|Chinchilla scaling law]] (DeepMind 2022)** prescribes ≈**20 training tokens per parameter** for compute-optimal training. Doubling model size means doubling training tokens. Important caveats: derived for dense models on human-generated data; sparse models and synthetic data are active research areas; Llama deliberately chose **suboptimal-but-smaller models** to favor inference economics over compute-optimal training quality.
- **Sparsity changes the parameter-count interpretation.** [[MixtureOfExperts|MoE]] models like [[Mixtral8x7B|Mixtral 8x7B]] have 46.7B total params but only **12.9B active per token** — cost and speed match a 12.9B dense model.
- **[[InverseScaling|Inverse scaling]] exists but is rare.** [[Anthropic|Anthropic]] 2022: more alignment training can produce models that express *stronger* political/religious views and a desire to not be shut down (Perez et al.). The 2023 [[InverseScalingPrize|Inverse Scaling Prize]] awarded 11 third prizes but no first/second — the failures don't transfer cleanly to the real world.
- **Two visible bottlenecks for further scaling**: (1) **training data** — Villalobos et al. project data-set-size growth outrunning new-data generation; 45% of [[c4|C4]] became restricted between 2023–2024 (Longpre et al.); (2) **electricity** — data centers consume 1–2% of global electricity, projected 4–20% by 2030 (Patel, Nishball, Ontiveros 2024). At most ≈50× growth (<2 orders of magnitude) before a power shortage.
- **Post-training has two stages, costing only ~2% of total compute**: [[SupervisedFinetuning|SFT]] on (prompt, response) [[DemonstrationData|demonstration data]] ("behavior cloning") + [[PreferenceFinetuning|preference finetuning]] via [[rlhf|RLHF]] (used by [[GPT35|GPT-3.5]], Llama 2), [[DPO|DPO]] (used by Llama 3 — Meta switched to reduce complexity), or [[RLAIF]] (potentially Claude).
- **[[rlhf|RLHF]] uses [[ComparisonData|comparison data]] (prompt, winning_response, losing_response)** rather than direct scores because labelers can't give consistent absolute scores. InstructGPT inter-labeler agreement ≈73%. Comparison cost: ≈$3.50/comparison vs ≈$25/written response (Llama-2 author Thomas Scialom).
- **The reward model trains by maximizing the score-difference between winning and losing responses** via a sigmoid-log-likelihood loss. The final RL step uses [[PPO|PPO]]. *"Some companies find it okay to skip RL altogether"* — Stitch Fix and Grab use [[bestofn|best-of-N]] with the reward model alone.
- **Sampling makes AI probabilistic.** Greedy sampling picks the argmax token; temperature redistributes via `logit/T` before softmax (T=0 → argmax; T=0.7 is a common creative default; T=2 the typical upper bound). [[Topk|Top-k]] (50–500) reduces softmax compute; [[Topp|top-p]] / nucleus sampling (0.9–0.95) is adaptive in the number of candidates. [[Logprobs|Logprobs]] are exposed sparingly by providers — likely for model-replication security reasons.
- **[[TestTimeCompute|Test-time compute]] is a separate axis from model size.** OpenAI's [[Verifier|verifier]] experiment: math-problem performance with a verifier ≈ **30× model-size increase**. DeepMind argues scaling test-time compute can beat scaling parameters (Snell et al. 2024). OpenAI's experiment peaks at ≈400 samples; Stanford's *Monkey Business* (Brown et al. 2024) shows log-linear improvement up to 10,000 samples. [[selfconsistency|Self-consistency]] (Wang et al. 2023) is the most-common-output selection variant — Google used 32-sample voting to lift Gemini's [[mmlu]] score.
- **[[StructuredOutputs|Structured outputs]] are achieved at five layers of the stack**: prompting, post-processing, test-time compute, [[ConstrainedSampling|constrained sampling]], and finetuning. JSON mode (OpenAI), guidance, outlines, instructor, and llama.cpp implement constrained sampling. LinkedIn's defensive YAML parser raised valid YAML from 90% → 99.99%.
- **[[Inconsistency|Inconsistency]] has two flavors**: (1) same input → different outputs (fix: cache, fix temperature/top-p/top-k/seed); (2) slightly different input → drastically different outputs (harder — needs prompt engineering and memory). Even fixed sampling variables can't guarantee 100% consistency — *hardware variance* across machines also affects outputs.
- **Two hypotheses for [[Hallucination|hallucination]]**: (a) **[[SelfDelusion|self-delusion]]** (Ortega et al., DeepMind 2021) — the model can't differentiate its own generated text from given facts; once it generates a wrong assumption it [[SnowballingHallucination|snowballs]] more wrongness (Zhang et al. 2023). (b) **[[InternalKnowledgeMismatch|internal-knowledge mismatch]]** (Leo Gao; John Schulman 2023 UC Berkeley talk) — SFT trains the model to mimic responses requiring knowledge the model lacks, teaching it to make things up. The two are complementary (self-supervision causes one; supervision causes the other).
- **RLHF's empirical effect on hallucination is contested.** Schulman said RLHF helps reduce hallucinations; the InstructGPT paper (Ouyang et al. 2022) showed RLHF *worsened* hallucination versus SFT-alone — but labelers preferred the RLHF model overall.

## Key Quotes

> "Differences in foundation models can be traced back to decisions about training data, model architecture and size, and how they are post-trained to align with human preferences." — Ch 2, opening

> "Sampling is how a model chooses an output from all possible options. It is perhaps one of the most underrated concepts in AI. Not only does sampling explain many seemingly baffling AI behaviors, including hallucinations and inconsistencies, but choosing the right sampling strategy can also significantly boost a model's performance with relatively little effort." — Ch 2, on sampling

> "If you've ever put anything on the internet, you should assume that it already is or will be included in the training data for some language models, whether you consent or not." — on the data-scaling bottleneck

> "Anything with a non-zero probability, no matter how far-fetched or wrong, can be generated by AI." — on the probabilistic nature

> "[Hallucination] is the biggest blocker for many AI enterprise use cases." — Huyen, summarizing a July 2023 panel with Drew Houston (Dropbox) and Harrison Chase ([[LangChain]])

> "The superior writing abilities of LLMs, as manifested in surpassing human annotators in certain tasks, are fundamentally driven by RLHF." — Llama 2 authors (Touvron et al., 2023), quoted in Ch 2

## Concepts Introduced or Engaged

### New concept pages
- [[CommonCrawl]] — *new*, the ≈2–3B-pages/month nonprofit web crawl that backstops most LLM pretraining.
- [[MultilingualModel]] — *new*, model trained for non-English languages (ChatGLM, YAYI, Llama-Chinese, CroissantLLM, PhoGPT, Jais).
- [[LowResourceLanguage]] — *new*, languages with limited training-data representation; Punjabi/Swahili/Urdu/Telugu/Marathi/Bengali are the chapter's canonical examples.
- [[DomainSpecificModel]] — *new*, FM trained for a specific domain ([[AlphaFold]], [[BioNeMo]], [[MedPaLM2]]).
- [[Prefill]] / [[Decode]] — *new*, the two phases of transformer-LM inference (prefill parallel, decode sequential).
- [[StateSpaceModel]] — *new*, SSM family (S4 → H3 → Mamba) — linear-time inference, long-context strength.
- [[Mamba]] — *new*, selective-state-space LLM scaling SSMs to 3B and matching transformers 2× its size.
- [[Jamba]] — *new*, hybrid Transformer–Mamba MoE; 52B total / 12B active in one 80GB GPU; 256K context.
- [[RWKV]] — *new*, RNN-based architecture parallelizable for training.
- [[FLOPs]] — *new*, floating-point-operation counts as the standardized compute-requirement unit; FLOPs vs FLOP/s vs FLOP/s-day distinction.
- [[ChinchillaScalingLaw]] — *engaged*, [[chinchillascalinglaws|existing stub]] is upgraded with Ch 2's worked numerical example (20 tokens/param).
- [[ScalingExtrapolation]] — *new*, also called hyperparameter transferring — predicting which hyperparameters will work for large models from small-model studies.
- [[EmergentAbilities]] — *new*, capabilities present only at scale (Wei et al. 2022) — make scaling extrapolation harder.
- [[InverseScaling]] — *new*, tasks where larger models perform worse (Inverse Scaling Prize 2023).
- [[InverseScalingPrize]] — *new*, the NYU-led 2023 contest with $5K/$20K/$100K prizes for inverse-scaling demonstrations.
- [[ScalingBottlenecks]] — *new*, data and electricity as the two visible bottlenecks for further scaling.
- [[ComputeOptimal]] — *new*, achieving best model performance under a fixed compute budget — the Chinchilla goal.
- [[SupervisedFinetuning]] — *new*, the post-training stage that turns a completion model into a conversation model via (prompt, response) demonstration data.
- [[PreferenceFinetuning]] — *new*, the post-training stage that aligns the SFT model with human preferences via RLHF/DPO/RLAIF.
- [[RLAIF]] — *new*, Reinforcement Learning from AI Feedback — replaces human labelers with an AI labeler (potentially used by Claude).
- [[DemonstrationData]] — *new*, (prompt, response) pairs used for SFT, also called *behavior cloning* data.
- [[BehaviorCloning]] — *new*, the SFT paradigm — model clones the demonstrated behavior.
- [[ComparisonData]] — *new*, (prompt, winning_response, losing_response) preference data used for reward-model training.
- [[RewardModel]] — *new*, the model trained on comparison data to score the foundation model's outputs.
- [[PPO]] — *new*, Proximal Policy Optimization — OpenAI's 2017 RL algorithm used for the RLHF policy step.
- [[Temperature]] — *new*, the `logit/T` softmax-rescaling parameter that trades creativity for predictability.
- [[Topk]] — *new*, top-k sampling — softmax restricted to the top k logits.
- [[Topp]] — *new*, top-p / nucleus sampling — softmax over the smallest set of tokens whose cumulative probability exceeds p.
- [[MinP]] — *new*, minimum-probability sampling threshold.
- [[Logprobs]] — *new*, log-scale probabilities exposed (sparingly) by model providers; useful for classification, evaluation, and debugging.
- [[StoppingCondition]] — *new*, fixed-token-count, stop-tokens, or end-of-sequence triggers that terminate generation.
- [[TestTimeCompute]] — *new*, generating multiple outputs per query to increase the chance of a good one — overlaps but is distinct from [[testtimescaling|test-time scaling]].
- [[bestofn|BestOfN]] — *engaged*, the simplest test-time-compute strategy — sample N, select best.
- [[Verifier]] — *new*, a model trained to grade candidate outputs (math-problem verifier ≈ 30× model size).
- [[StructuredOutputs]] — *new*, generating outputs that conform to a schema (JSON, YAML, regex, SQL).
- [[SemanticParsing]] — *new*, converting natural language to a structured machine-readable form (text-to-SQL is the canonical example).
- [[ConstrainedSampling]] — *new*, filter the logit vector at each step to only valid tokens per a grammar.
- [[Inconsistency]] — *new*, two-flavored failure mode: same/slightly-different input → different outputs.
- [[SelfDelusion]] — *new*, Ortega et al. (DeepMind 2021) hypothesis — the model can't distinguish its own generated text from given facts.
- [[SnowballingHallucination]] — *new*, Zhang et al. (2023) — once a model generates a wrong assumption it continues hallucinating to justify it.
- [[InternalKnowledgeMismatch]] — *new*, the Leo Gao / John Schulman hypothesis — SFT teaches models to mimic responses requiring knowledge they lack.

### Engaged concept pages (updated)
- [[FoundationModel]] — *engaged*, this chapter is the deep architectural and post-training treatment.
- [[transformer|Transformer]] — *engaged*, prefill/decode, multi-head attention details, Llama 2/3 dimensions.
- [[Attention]] / [[multiheadattention]] — *engaged*, K/V/Q matrices and dimensions for Llama 2-7B (4096 hidden / 32 heads / 128 per head).
- [[encoderdecoder]] / [[1409.3215-seq2seq|seq2seq]] — *engaged*, the bottleneck the Transformer was designed to solve.
- [[scalinglaws]] / [[chinchillascalinglaws]] — *engaged*, the Chinchilla recipe (~20 tokens/param).
- [[MixtureOfExperts]] — *engaged*, Mixtral 8x7B (46.7B total / 12.9B active) is the canonical worked example.
- [[c4]] / [[CommonCrawl]] — *engaged*, the dominant pre-training corpora and their quality issues.
- [[Tokenization]] / [[Tokenizer]] — *engaged*, the chapter's English-bias / efficiency angle (Burmese ≈10× longer than English for the same content).
- [[pretraining]] / [[posttraining]] / [[FineTuning]] — *engaged*, the three-phase taxonomy with the InstructGPT 98%/2% compute split.
- [[rlhf|RLHF]] — *engaged*, the chapter is the most concrete RLHF walkthrough in the wiki (loss formula, comparison data, PPO step).
- [[DPO]] / [[DirectPreferenceOptimization]] — *engaged*, Llama 3's choice; Huyen prefers RLHF for the chapter because it's more flexible to tweak.
- [[Hallucination]] — *engaged*, gets the two-hypothesis explanation and the InstructGPT RLHF-worsened-hallucination data point.
- [[GreedyDecoding]] — *engaged*, the trivial sampling baseline.
- [[beamsearch|Beam Search]] — *engaged*, the test-time-compute strategy that explores multiple promising candidates.
- [[selfconsistency|Self-Consistency]] — *engaged*, Wang et al. 2023 — the most-common-output selection variant.
- [[testtimescaling|Test-Time Scaling]] — *engaged*, DeepMind's argument that scaling test-time compute beats scaling parameters.
- [[Softmax]] — *engaged*, the logit-to-probability conversion at the heart of sampling.
- [[ActivationFunction]] — *engaged*, ReLU vs GELU (used by GPT-2 vs GPT-3 respectively).
- [[ContextLength]] / [[ContextWindow]] — *engaged*, naively determined by the position-embedding count; transformer K/V caches scale with context length.
- [[LargeLanguageModel]] / [[AutoregressiveLanguageModel]] — *engaged*, the autoregressive sequential-output bottleneck.

## Entities Introduced or Engaged

### New entity pages
- [[StitchFix]] — *new*, retail/styling company; uses reward model + best-of-N without RL.
- [[Grab]] — *new*, SE Asia super-app; uses reward model + best-of-N without RL.
- [[Nextdoor]] — *new*, neighborhood social platform; reported reward-model as the key factor in lifting application performance (2023).
- [[TIFIN]] — *new*, AI-in-finance company; Kittipat Kampa's parallel-sample / first-valid latency strategy.
- [[LAION]] — *new*, German non-profit; mobilized 13,500 volunteers for 161K-message conversation dataset across 35 languages.
- [[LMSYS]] — *new*, Large Model Systems Org; tracked the 3–5 min/comparison labeling time.
- [[AlphaFold]] — *new* (entity page in concepts/entities depending on convention) — DeepMind's protein-structure model; ≈100K protein structures.
- [[BioNeMo]] — *new*, NVIDIA's biomolecular foundation model for drug discovery.
- [[MedPaLM2]] — *new*, Google's medical-QA LLM.
- [[GPT3]] — *new*, OpenAI's 175B param model (300B training tokens, 3.14 × 10²³ FLOPs).
- [[Mixtral8x7B]] — *new*, Mistral's MoE model — 46.7B total / 12.9B active per token.
- [[GoogleGNMT]] — *new*, Google Neural Machine Translation — first major production deployment of attention with seq2seq.
- [[InverseScalingPrize|NYU Inverse Scaling Prize]] — *new*, 2023 contest organized largely by NYU researchers.
- [[ThomasScialom]] — *new*, Llama-2 author who shared the $3.50/comparison data point.
- [[LeoGao]] — *new*, OpenAI researcher who proposed the internal-knowledge-mismatch hypothesis of hallucination.
- [[JohnSchulman]] — *new*, OpenAI co-founder; UC Berkeley 2023 talk on hallucination causes and mitigation via verification + better reward functions.
- [[DarioAmodei]] — *new*, Anthropic CEO; *"$100B AI model would be as good as a Nobel prize winner"*.
- [[IgorBabuschkin]] — *new*, Grok core developer ("the web is full of ChatGPT outputs").
- [[KittipatKampa]] — *new*, head of AI at TIFIN; parallel-sample latency strategy.

### Engaged entity pages (updated)
- [[ChipHuyen]] — *engaged*, author.
- [[OReilly]] — *engaged*, publisher.
- [[openai|OpenAI]] — *engaged*, GPT-2 Reddit filter, InstructGPT prompt distribution, PPO origin, verifier experiment, OpenAI logprobs API.
- [[anthropic|Anthropic]] — *engaged*, HH-RLHF comparison dataset; Perez et al. inverse-scaling alignment finding.
- [[google|Google]] / [[googledeepmind|Google DeepMind]] — *engaged*, GNMT, [[c4|C4]], [[ChinchillaScalingLaw|Chinchilla]], [[gemini|Gemini]] MMLU-32-vote, Ortega et al. self-delusion hypothesis.
- [[meta|Meta]] — *engaged*, Llama family (1/2/3 token counts 1.4/2/15 trillion); switched RLHF→DPO between Llama 2 and Llama 3.
- [[NVIDIA]] — *engaged*, BioNeMo; H100 specs and pricing.
- [[microsoft|Microsoft]] — *engaged*, 2022 hyperparameter-transfer paper (40M → 6.7B).
- [[LinkedIn]] — *engaged*, defensive YAML parser; YAML over JSON for fewer output tokens (Bottaro and Ramgopal 2020).
- [[Mistral7BInstructV02|Mistral]] — *engaged*, Mixtral 8x7B MoE worked example.
- [[ChatGPT]] / [[GPT4|GPT-4]] / [[gemini|Gemini]] — *engaged*, MMLU language benchmarks, ChatGPT misinformation-in-Chinese anomaly, GPT-4o regex generation.

## Connections

- **Chapter 1 → Chapter 2 transition.** [[ai-engineering-ch01-intro|Ch 1]] introduced the [[FoundationModel|foundation model]] as the substrate of [[AIEngineering|AI engineering]]; Ch 2 opens up the model itself — *training data, architecture, scale, post-training, sampling*. The InstructGPT 98%/2% compute split, mentioned in passing in Ch 1, is unpacked here.
- **Chapter 2 → downstream chapters.** Several Ch 2 threads thread forward: Ch 3 (evaluation) inherits the cross-entropy / nats discussion and the probabilistic-output / inconsistency framing; Ch 4 picks up [[Hallucination|hallucination]] detection/measurement; Ch 5 (prompting) inherits the probabilistic-output / structured-outputs prompting layer; Ch 6 (agents) inherits the parsable-outputs constraint that drove structured outputs; Ch 7 inherits the KV-cache discussion, [[FloatingPointFormats|floating-point formats]], and the classifier-head feature-based-transfer pattern; Ch 8 inherits the high-quality-data discussion and dataset engineering; Ch 9 inherits [[FLOPs|FLOPs]] / utilization / hardware-metrics; Ch 10 inherits the feedback / RM-as-judge thread.
- **Three concept clusters this chapter anchors in the wiki**:
  1. **The data-pipeline anchor** — [[CommonCrawl]] / [[c4]] / [[MultilingualModel]] / [[LowResourceLanguage]] / [[DomainSpecificModel]]. This cluster did not exist as a coherent unit before Ch 2.
  2. **The post-training pipeline anchor** — [[pretraining]] → [[SupervisedFinetuning]] → [[PreferenceFinetuning]] → [[rlhf]]/[[DPO]]/[[RLAIF]] as a single staged pipeline.
  3. **The sampling anchor** — [[Temperature]] / [[Topk]] / [[Topp]] / [[Logprobs]] / [[StoppingCondition]] / [[GreedyDecoding]] / [[beamsearch]] / [[StructuredOutputs]] / [[ConstrainedSampling]] / [[TestTimeCompute]] / [[bestofn]] / [[Verifier]] / [[Inconsistency]] / [[Hallucination]] / [[SelfDelusion]] / [[SnowballingHallucination]] / [[InternalKnowledgeMismatch]] — the chapter's signature contribution.
- **[[transformer|Transformer]] alternatives cluster** — [[Mamba]] / [[Jamba]] / [[StateSpaceModel]] / [[RWKV]] is the first time the wiki has a named survey of post-Transformer architectures. Links forward to [[2605.12966-agentic-ai-to-agi]]'s topology-graph view of architectures.
- **Chinchilla-scaling-law upgrade**: [[chinchillascalinglaws]] was a stub before this chapter; now backed by Huyen's concrete *20 tokens/param* worked recipe.

## Contradictions

- **RLHF effect on hallucination is contested in-chapter.** John Schulman (cited in Ch 2) says OpenAI found RLHF reduces hallucinations; the InstructGPT paper (Ouyang et al. 2022, Figure 2-26 in Ch 2) shows RLHF *worsened* hallucination versus SFT-alone. Huyen flags this as an open question — not a contradiction with prior wiki content, but an internal-to-chapter contradiction worth recording.
- **[[Inconsistency|Inconsistency]] vs the wiki's [[selfconsistency|self-consistency]] page.** Ch 2 frames inconsistency as a *failure mode* of the probabilistic sampling process — same input, different outputs. The wiki's existing [[selfconsistency]] page treats the same phenomenon as a *resource* — sample multiple times and majority-vote for free quality gains. Not contradictory; they describe the same probabilistic substrate from opposite engineering stances.
- **Test-time-compute saturation point.** OpenAI (2021) found performance peaks around 400 outputs/query and *decreases* beyond that (adversarial-output overfitting to the verifier). Stanford's *Monkey Business* (Brown et al. 2024) reports log-linear improvement up to 10,000 outputs. Ch 2 flags this as a live debate.
- **Llama's compute-suboptimal choice contradicts Chinchilla optimality.** Llama (Meta) explicitly chose smaller-than-compute-optimal models to favor inference economics — Sardana et al. (2023) generalize this into an *inference-aware* scaling law. The wiki's existing [[chinchillascalinglaws]] stub does not yet record this inference-aware revision; flagged for follow-up.
- **"Foundation model trained on AI-generated data degrades"** (Shumailov et al. 2023) is named as a worry but Huyen explicitly notes the picture is *more nuanced* (Ch 8). Not a wiki contradiction but a caveat to flag if [[ModelCollapse]] is ever ingested as a primary source.

## See also
- [[ai-engineering-ch01-intro]] — chapter immediately preceding this one in the same book.
- [[ai-engineering-chip-huyen]] — parent source page for the full book.
