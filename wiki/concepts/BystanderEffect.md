---
title: "Bystander Effect (in Multi-Agent Reasoning)"
type: concept
tags: [multi-agent, sycophancy, failure-mode]
sources: [2605.10698-bystander-effect-mas]
last_updated: 2026-05-15
---

# Bystander Effect (in Multi-Agent Reasoning)

A failure mode of LLM [[multiagentsystems]] in which a propagator model, presented with the assertion that its simulated swarm has already converged on an answer, rationally offloads procedural retrieval to the swarm *and* detrimentally offloads integrative reasoning, externalizing the swarm's (incorrect) consensus instead of its own internally-computed derivation. Named after the social-psychology Bystander Effect (Darley & Latané, 1968) but operates without active dialogue — static prompt content claiming peer consensus is sufficient.

The mechanism is formalized in [[2605.10698-bystander-effect-mas]] as a transition through the [[InteractionDepthLimit]] $D_L$ governed by the [[SovereigntyDecayLaw]]. Empirically: [[gpt54|GPT-5.4]] accuracy on [[swebench|SWE-bench]] collapses from 1.00 ($n=0$) to 0.23 ($n=2$, $p<0.001$); [[claudeopus47|Claude Sonnet 4.6]] is unaffected ($\gamma\to\infty$). Closely related but distinct from [[promptinjection]]: the injection vector is the framing of peer agreement rather than instruction text.

Failure manifests as either [[CognitiveLoafing]] / [[IntegrativeReasoningBypass]] ($\mathcal{B}=1$, the model never derives) or [[AlignmentHallucination]] (the model derives correctly and then sycophantically overrides itself — see [[SovereigntyGap]]).
