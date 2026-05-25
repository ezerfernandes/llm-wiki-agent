---
title: "Perspective-Guided Expert Agent"
type: concept
tags: [multi-agent, llm-role, perspective-diversity]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# Perspective-Guided Expert Agent

**Perspective-guided expert** — an LM-played role in [[CoSTORM|Co-STORM]] (and originally in [[STORM]]) where each agent $p_j$ is conditioned on a **specific expertise or viewpoint** to ensure perspective diversity in the discourse.

## How experts are instantiated

Given an initial topic $t$:

1. Co-STORM retrieves background information on $t$ via the search engine.
2. The LM is prompted with the background to generate an **expert list** $\mathcal{P} = \{p_1, ..., p_N\}$ ($N = 3$ default) — e.g., for the topic *"AlphaFold 3"*, the LM suggests an *"AI Expert"*, a *"Geneticist"*, and a *"Molecular Biology Expert"*.
3. The list can be **dynamically updated** to $\mathcal{P}'$ by the [[ModeratorAgent|moderator]] when the discourse shifts direction.

## How an expert takes a turn

Each expert $p_j$ runs the following per-turn pipeline:

1. **Choose intent** $a_i$ — the LM picks an [[UtteranceIntent|intent]] (Original Question / Information Request / Potential Answer / Further Details) based on discourse history $\{u_1, ..., u_{i-1}\}$ and the expert's perspective.
2. **Branch on intent**:
   - If intent is **Potential Answer** or **Further Details**: prompt the LM to generate a search query $q$, retrieve via [[YouCom|You.com]], generate a response with **inline citations**.
   - Otherwise (question-asking intents): prompt the LM to directly generate a question grounded in discourse history.
3. **Polish** — final LM call rewrites the utterance for engagement / chattiness.

The branching is what gives the discourse alternating *question* and *answer* phases without manual scripting.

## Why perspective diversity matters

Per the Co-STORM analysis, ablating to a single expert (**w/o Multi-Expert**) drops Novelty 3.05→2.93 and Breadth 3.79→3.75 — small but consistent. The bigger effect of perspective diversity is **qualitative**: different perspectives surface different *kinds* of questions, increasing the probability that at least one perspective covers any given facet of the topic.

This is the same mechanism used by [[STORM]] for question generation; Co-STORM inherits it and adds the [[ModeratorAgent|moderator]] on top.

## Echo-chamber risk

Sharma et al. 2024 ([[ShermanEtAl2024]]) flagged that LLM-powered search systems can induce **echo chambers**. Co-STORM's perspective-guided experts are a **partial** mitigation — they introduce viewpoint diversity *within the model's distribution* but cannot escape biases shared across perspectives by the underlying LM.

## See also
- [[CoSTORM]] · [[STORM]] · [[ModeratorAgent]] · [[UtteranceIntent]]
