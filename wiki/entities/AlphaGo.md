---
title: "AlphaGo"
type: entity
tags: [system, reinforcement-learning, deepmind, mlsysbook]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# AlphaGo

DeepMind's Go-playing system (Silver et al. 2016) that achieved superhuman play by combining supervised learning from expert games, reinforcement learning via self-play, and neural-network-guided tree search — rather than hand-coded Go strategy. Cited in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Ch 1]]) as a [[BitterLesson|Bitter Lesson]] exemplar.

Its successor **AlphaGo Zero** used self-play exclusively and surpassed the original after **3 days on 4 TPUs (288 TPU-hours), winning 100–0** — making *infrastructure budget*, not hand-coded expertise, the binding constraint.

## Connections

- [[BitterLesson]] — the principle it validates.
- [[mlsysbook-ch01-introduction]] — the chapter citing it.
- [[DeepMind]] — its creator.
- [[GoogleTPU]] — the hardware behind AlphaGo Zero.
- [[AlphaFold]] — DeepMind sibling and Ch 1 case study.
