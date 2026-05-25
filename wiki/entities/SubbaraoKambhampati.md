---
title: "Subbarao Kambhampati"
type: entity
tags: [person, researcher, planning, ai]
sources: [2402.01817-llm-modulo, ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Subbarao Kambhampati

Professor at the **School of Computing and AI, [[ArizonaStateUniversity]]** (Tempe, AZ). Long-time automated-planning researcher and a prominent skeptic of claims that LLMs can plan or self-verify. Past president of AAAI.

## Position in the Field
- Argues LLMs are **pseudo-System 1** approximate knowledge sources, *not* System-2 reasoners — see [[2402.01817-llm-modulo]].
- Proposes [[LLMModuloFramework]] (Generate-Test-Critique with external sound critics) as the principled way to leverage LLMs in planning/reasoning, instead of either over-trusting them or relegating them to syntax translation.
- Coined **[[PolanyisRevenge]]** (CACM 2021): LLMs make tacit knowledge cheaply accessible without explicit articulation, avenging Polanyi's paradox for AI.
- Long line of empirical work showing LLMs do approximate plan retrieval rather than planning: [[PlanBench]] (Valmeekam et al. 2023), graph-coloring self-verification analyses (Stechly et al. 2023, 2024), ToM-illusion work (Verma et al. 2024).

## Key Co-authors (this wiki)
- Karthik Valmeekam, Lin Guan, Mudit Verma, Kaya Stechly, Siddhant Bhambri, Lucas Saldyt, Anil Murthy (all ASU)

## Sources in this wiki
- [[2402.01817-llm-modulo]] — *Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks* (ICML 2024)

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

[[ChipHuyen|Huyen]] cites Kambhampati's *Can LLMs Really Reason and Plan?* (2023) article in Ch 6's planning section:

> *"In the article 'Can LLMs Really Reason and Plan?' Kambhampati (2023) argues that LLMs are great at extracting knowledge but not planning. Kambhampati suggests that the papers claiming planning abilities of LLMs confuse general planning knowledge extracted from the LLMs with executable plans."*

The Ch 6 quote that crystallizes Kambhampati's position:

> *"The plans that come out of LLMs may look reasonable to the lay user, and yet lead to execution time interactions and errors."*

This is the **plan-knowledge-vs-executable-plan** distinction at the heart of [[2402.01817-llm-modulo|LLM-Modulo]] — the wiki's existing primary entry for Kambhampati's position. Ch 6 records this skeptic position alongside [[YannLeCun|LeCun]]'s but doesn't adjudicate; Huyen counters with [[ReasoningWithLanguageModelIsPlanningWithWorldModel|Hao et al. 2023]] and notes empirical uncertainty.
