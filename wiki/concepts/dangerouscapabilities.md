---
title: "Dangerous Capabilities"
type: concept
tags: [safety, evaluation, frontier-model]
sources: [2312.11805-gemini]
last_updated: 2026-05-10
---

# Dangerous Capabilities

A safety-evaluation taxonomy for frontier-model capabilities that could enable large-scale harm. Adopted by [[GoogleDeepMind]] for [[Gemini]] in [[2312.11805-gemini]] (Section 7.4.1.3); aligned with Shevlane et al. (2023) and the White House Commitments / U.S. EO on Safe AI / Bletchley Declaration external-evaluation regimes.

## Canonical categories (per [[2312.11805-gemini]])

| Category | Probe |
|---|---|
| **Offensive cybersecurity** | CTF challenges with bash-shell access; vulnerability identification in source code. |
| **Persuasion & deception** | 1-on-1 dialogue studies with human participants. |
| **Self-proliferation** | Whether autonomous agents can acquire resources and self-improve (Kinniment et al., 2023). |
| **Situational awareness** | Whether the model can reason about and modify its own surroundings when incentivized. |
| **CBRN** | Chemical, Biological, Radiological, Nuclear — closed-ended QA + structured human-rated risk for chemical hazards. |

## Findings reported for Gemini Ultra (December 2023 checkpoint)

- Solves entry-level / tactical CTF challenges; struggles with longer-range exploration and planning.
- Mixed persuasion-and-deception results.
- Not close to succeeding on most self-proliferation subtasks.
- Generally cannot autonomously notice opportunities to modify its surroundings.
- Unlikely to provide CBRN information that would lead to catastrophic harm.

## Role in the wider wiki

This taxonomy is the canonical reference when later papers in the corpus invoke "frontier-safety evaluations" — particularly the recursive-self-improvement framing of [[2604.25067-frontier-coding-agents-c4]], which proposes replicating past AI breakthroughs as a more leading indicator than these capability-by-capability probes.
