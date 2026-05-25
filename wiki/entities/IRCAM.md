---
title: "IRCAM"
type: entity
tags: [organization, research-lab, france, computer-music]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# IRCAM

**Institut de Recherche et Coordination Acoustique/Musique** — Paris-based computer-music research institute, founded 1977. Host of [[PeterVanRoy]]'s sabbatical during which [[vanroy-programming-paradigms-for-dummies|"Programming Paradigms for Dummies"]] was written; publisher (with Delatour France) of the host volume *New Computational Paradigms for Computer Music* (G. Assayag & A. Gerzso eds., 2009).

## Research groups and tools referenced

- **RepMus group** — music representations research; led by Gérard Assayag
- **[[OpenMusic]]** (Agon, Assayag, Bresson 2008) — graphical visual-dataflow music-composition language with discrete-synchronous semantics
- **[[Antescofo]]** (Arshia Cont 2008) — score-follower; translates clock time → tempo (BPM); composer-annotated control via DSL
- **[[MaxMSP]]** — Max dataflow language + MSP DSP + Jitter; developed at IRCAM, later commercialized via Cycling74 (Puckette)
- **[[Faust]]** (Orlarey, Fober & Letz 2004 / 2009) — visual dataflow signal-processing language with [[DiscreteSynchronousProgramming|discrete synchronous]] semantics + C++ compilation

## Position in the wiki

The wiki's first **computer-music research institute** entity and first non-ML-pedigree research site producing programming-language artifacts. Important context for [[vanroy-programming-paradigms-for-dummies]]: the chapter's recurring computer-music examples ([[OpenMusic]], [[Antescofo]], [[MaxMSP]], [[Faust]]) demonstrate that **[[DiscreteSynchronousProgramming|discrete-synchronous]] + [[FunctionalReactiveProgramming|functional-reactive]] + [[ConcurrentConstraintProgramming|constraint-programming]] paradigms are the practical workhorses of an entire applied domain** — not academic curiosities, but the only viable design space for real-time deterministic music software at three abstraction levels (composition / performance / signal processing).
