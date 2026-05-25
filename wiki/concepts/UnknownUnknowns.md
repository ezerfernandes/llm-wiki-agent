---
title: "Unknown Unknowns"
type: concept
tags: [framing, information-seeking, epistemics]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# Unknown Unknowns

**Unknown unknowns** — information the user is *unaware they should be seeking*. The central design target of [[2408.15232-co-storm|Co-STORM]].

## Origin and framing

The term originally referred to unexpected risks in military / risk-management contexts. In information-seeking, it is linked to **serendipitous discovery** ([[Foster2003|Foster & Ford 2003]]; [[Agarwal2015|Agarwal 2015]]).

[[Kirzner1997|Kirzner (1997)]] makes the load-bearing distinction:

| Mode | Definition |
|---|---|
| **Discovery** | *"The realization that one had overlooked something in fact readily available"* |
| **Successful search** | *"The deliberate production of information which one knew one had lacked"* |

The **gap** Co-STORM targets: LMs (chatbots, generative search) are excellent at *successful search* — they answer **known unknowns**. They are weak at *discovery* — surfacing what the user did not know to ask.

## Why this gap matters

In complex information-seeking domains (academic research, market analysis, decision-making), there is **no single gold query**: queries evolve dynamically toward a goal ([[Bates1989]]). Users with limited prior knowledge may struggle to formulate questions ([[Kuhlthau1991]]; [[Belkin1982]]); RAG chatbots that only react to user queries induce **echo chambers** ([[ShermanEtAl2024|Sharma et al. 2024]]).

## Co-STORM's mechanism for surfacing unknown unknowns

[[2408.15232-co-storm|Co-STORM]] simulates a **roundtable of LM agents** + a **[[ModeratorAgent|moderator]]**: the experts ask questions on the user's behalf (different perspectives surface different known-unknowns), and the moderator reranks **uncited / unused** information to steer toward *unexplored* regions — pulling out content that is on-topic but unrelated to any question the user has asked. The user observes, can step in, and at the end requests a cited report.

Per the [[2408.15232-co-storm|human evaluation]], participants reported 80 mind-map snapshots accurately tracked the discourse 71% of the time; one participant said:

> *"Co-STORM allows for almost full automation and much better understanding as it brings up topics that the user may not even think of."*

## See also
- [[CoSTORM]] · [[CollaborativeDiscourse]] · [[InformationSeeking]] · [[ModeratorAgent]]
