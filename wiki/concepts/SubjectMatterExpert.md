---
name: SubjectMatterExpert
title: "Subject Matter Expert (SME)"
type: concept
tags: [team-structure, ml-organization, annotation]
sources: [dmls-ch11-human-side]
last_updated: 2026-05-23
---

# Subject Matter Expert (SME)

Domain expert (doctor, lawyer, banker, mechanical engineer, biologist) who contributes domain knowledge to an ML system. Per [[ChipHuyen|Huyen]]'s [[dmls-ch11-human-side|DMLS Ch 11]] — the common reduction "SMEs are just labelers" is wrong: SMEs need to participate **across the entire ML lifecycle**, not only at the data-annotation stage.

## Where SMEs contribute (per DMLS Ch 11)
- **Problem framing** — what does success look like in this domain?
- **Data collection** — what sources have signal, what biases lurk where.
- **Labeling** — the obvious one; quality labels require domain literacy.
- **Feature engineering** — domain-specific feature constructions.
- **Model evaluation** — what failure modes matter most in this domain?
- **Deployment review** — what regulatory or operational constraints apply?
- **Monitoring + retraining decisions** — what real-world signal corresponds to drift?

## Organizational implications
For SMEs to participate broadly, they need **tooling that doesn't require ML engineering literacy** — labeling UIs, [[NoCodeMLPlatform|no-code ML platforms]], dashboard-driven monitoring, etc. The 2010s pattern of "throw the data over the fence to data scientists" is incompatible with broad SME participation; the 2020s pattern is platforms that surface ML-relevant decisions to domain experts.

## Tension with Approach 1 vs Approach 2 team structure
Ch 11 enumerates two organizational responses:
- **Approach 1** — cross-functional team of SMEs + ML engineers + data scientists; high coordination overhead (Mythical Man-Month).
- **Approach 2** — [[EndToEndDataScientist|end-to-end data scientists]] who own the lifecycle, with SMEs consulted at key checkpoints (cf. [[EricColson|Eric Colson]]'s *Beware the Data Science Pin Factory*; [[EugeneYan|Eugene Yan]]'s *Data Scientists Should Be More End-to-End*).

## Connections
- [[ResponsibleAI]] — SME participation is a core fairness lever.
- [[EndToEndDataScientist]] / [[FullCycleDeveloper]] — Approach 2 organizational patterns.
- [[NoCodeMLPlatform]] — the tooling SMEs need.
- [[DataAnnotation]] — the most familiar (but narrowest) SME contribution surface.
