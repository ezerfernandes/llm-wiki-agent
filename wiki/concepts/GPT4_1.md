---
title: "GPT-4.1"
type: concept
tags: [model, llm, openai, frontier]
sources: [2025-bionlp-archehr-qa-neural]
last_updated: 2026-05-22
---

# GPT-4.1

[[openai|OpenAI]] frontier API model released April 2025. Used in [[2025-bionlp-archehr-qa-neural|Reddy et al. (2025)]] as the fixed backbone LM for both stages of their [[MIPROv2]]-optimized clinical-QA pipeline at 10,000-token context — temperature 0.3 for prompt-optimization feedback, temperature 0.7 for $R=5$ self-consistency sampling at inference time.

Same model family is the GPT-4.1 Mini variant used as one of two evaluation LMs in [[2507.19457-gepa|GEPA (ICLR 2026)]]. The shared-backbone pattern across these two prompt-optimization papers is what makes their results inter-comparable in principle (though no shared benchmark exists yet).

## Connections
- [[openai|OpenAI]] — provider.
- [[2025-bionlp-archehr-qa-neural]] — clinical-QA application (Neural team).
- [[2507.19457-gepa|GEPA]] — GPT-4.1 Mini used as one of two evaluation LMs.
- [[MIPROv2]] — prompt optimizer applied over it.
- [[SelfConsistency|Self-Consistency]] — used at temp 0.7 in stage 1.
