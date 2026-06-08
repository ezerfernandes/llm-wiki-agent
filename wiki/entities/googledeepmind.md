---
title: "Google DeepMind"
type: entity
tags: [company, lab, google]
sources: [2312.11805-gemini, 2605.06651v2-ai-co-mathematician, 2603.19247-prompt-optimization-jailbreaking, ai-engineering-ch02-foundation-models, ai-engineering-ch04-evaluate-ai-systems, ai-engineering-ch05-prompt-engineering, ai-engineering-ch09-inference-optimization, agentic-design-patterns-ch21-exploration]
last_updated: 2026-06-07
---

# Google DeepMind

The 2023 merger of **Google Brain**, **Google Research**'s ML arm, and **DeepMind** into a single AI organization. Authoring entity for the [[Gemini]] technical report ([[2312.11805-gemini]]) and the [[AICoMathematician|AI co-mathematician]] paper ([[2605.06651v2-ai-co-mathematician]]).

Within this wiki, Google DeepMind sits beside (and is the modern successor to) [[Google]], which is credited as the home org for the foundational sequence-modeling papers — [[1409.3215-seq2seq]], [[1706.03762-attention-is-all-you-need]], [[1810.04805-bert]]. From PaLM / PaLM-2 / Gemini onward, the work is published under the Google DeepMind banner.

## Notable artifacts in this wiki

- [[Gemini]] family ([[2312.11805-gemini]]) — frontier multimodal foundation models, including [[GeminiDeepThink|Gemini 3.1 Deep Think]].
- [[AlphaCode2]] — Gemini-Pro-tuned competitive-programming agent.
- [[AlphaProof]] — IMO-level formal theorem proving with RL.
- [[AlphaEvolve]] — evolutionary coding agent for scientific/algorithmic discovery.
- [[GoogleCoScientist|AI Co-Scientist]] — [[Gemini]]-powered multi-agent scientific collaborator (Google Research); flagship of the [[ExplorationAndDiscovery|Exploration and Discovery]] pattern in [[AgenticDesignPatterns|Gulli Ch 21]], with wet-lab-validated discoveries (AML drug repurposing, liver-fibrosis targets, antimicrobial resistance).
- [[Aletheia]] — autonomous mathematics research system.
- [[AICoMathematician]] — interactive agentic workbench for mathematicians ([[2605.06651v2-ai-co-mathematician]]); reaches 48% on [[FrontierMath]] Tier 4.
- The DeepMind Responsibility & Safety Council reviews all Gemini model and product launches; the Gemini paper documents the responsible-deployment lifecycle (Assessment → Policy → Evaluation → Mitigation → Deployment).
- **Gemini 2.5 Pro** — used as a *target* (and, separately, as the [[GEPA]] reflection model) in [[2603.19247-prompt-optimization-jailbreaking|Shamsi et al. (2026)]] adaptive red-teaming. Baseline danger 0.645 (highest baseline of the four targets — Gemini was already the least safe-by-default at the seed prompts) → 0.774 under SIMBA. Smallest *multiplier* among the four (~1.2×) but highest absolute danger.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 adds five DeepMind-specific data points:

1. **[[AlphaFold|AlphaFold]]** — the canonical [[DomainSpecificModel|domain-specific foundation model]] (≈100K protein structures). Ch 2's marquee example of *"data unlikely to be on the public internet."*
2. **[[ChinchillaScalingLaw|Chinchilla scaling law]] (2022)** — *"Training Compute-Optimal Large Language Models"* — the rule that compute-optimal training requires ≈20 training tokens per parameter. The flagship 70B/1.4T Chinchilla model outperformed much larger contemporaries trained on fewer tokens.
3. **Gopher data filtering** — used heuristics for `[A]: [paragraph] [B]: [paragraph]` patterns to filter conversations from web data — Ch 2's example of cheap heuristic-based [[DemonstrationData|demonstration-data]] generation.
4. **[[SelfDelusion|Self-delusion]] hypothesis** (Ortega et al. 2021) — *"a language model hallucinates because it can't differentiate between the data it's given and the data it generates."* One of two leading hypotheses for [[Hallucination|hallucination]] in Ch 2.
5. **Test-time compute scaling argument** (Snell et al. 2024) — *"scaling test time compute (e.g., allocating more compute to generate more outputs during inference) can be more efficient than scaling model parameters."* The headline argument behind the [[TestTimeCompute|test-time compute]] thread.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 adds three DeepMind data points:

1. **[[SAFEEvaluator|SAFE — Search-Augmented Factuality Evaluator]]** (Wei et al. 2024, *"Long-Form Factuality in Large Language Models"*) — DeepMind's four-step pipeline for [[GlobalFactualConsistency|global factual consistency]] verification: decompose → revise → search → verify. One of three advanced [[FactualConsistency|factual-consistency]] detection methods discussed (alongside AI-judge prompts and [[SelfCheckGPT|self-verification]]).
2. **[[bigbench|BIG-bench]]** (Srivastava et al. 2022) — Google's 214-sub-benchmark collection; [[BigBenchHard]] is its reasoning subset.
3. **[[IFEval]]** (Zhou et al. 2023) — Google's instruction-following benchmark with 25 automatically-verifiable instruction types; used on HuggingFace's [[OpenLLMLeaderboard|Open LLM Leaderboard]] (June 2024 refresh).

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Google DeepMind appears in Ch 5 as the **origin lab of [[PromptBreeder|Promptbreeder]]** ([[FernandoEtAl2023|Fernando et al. 2023]]) — the evolutionary-strategy prompt optimizer that *"selectively 'breeds' prompts"* via mutation prompts that themselves evolve. Ch 5's Figure 5-8 shows the high-level mutate-then-select loop. Promptbreeder is one of two AI-powered prompt-optimization tools Ch 5 names by paper citation (the other being Stanford's [[TextGrad]]).

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

DeepMind's main appearance in Ch 9 is **the canonical [[SpeculativeDecoding|speculative-decoding]] result**:

### Chinchilla-70B speculative decoding

Chen et al. (2023) used a **4B-parameter draft model** of the same architecture to accelerate Chinchilla-70B inference:

- Draft generates tokens **8× faster than target** (1.8 ms/token vs 14.1 ms/token).
- **Overall response latency cut by > 50%** with no quality loss.

This is one of Ch 9's two flagship "speculative decoding actually works" data points (the other being Laviathan et al. 2022's T5-XXL result). The combination makes speculative decoding standard practice in production LLM serving.
