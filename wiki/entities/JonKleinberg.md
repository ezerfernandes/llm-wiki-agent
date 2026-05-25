---
title: "Jon Kleinberg"
type: entity
tags: [person, researcher, algorithms, link-analysis]
sources: [iir-ch21-link-analysis]
last_updated: 2026-05-23
---

Computer scientist at Cornell University; Tisch University Professor. Inventor of the **[[HITS]]** (Hyperlink-Induced Topic Search) algorithm (*"Authoritative Sources in a Hyperlinked Environment"*, SODA 1998; J. ACM 1999) — the hubs-and-authorities link-analysis algorithm proposed contemporaneously with [[LarryPage]] and [[SergeyBrin]]'s [[PageRank]] but with a different design philosophy (query-dependent, two scores per page, principal eigenvectors of $AA^T$ and $A^TA$).

Adjacent foundational work:
- **Small-world / navigability** (*"The Small-World Phenomenon: An Algorithmic Perspective"*, STOC 2000) — proved that Milgram's six-degrees-of-separation observation requires not just a small diameter but a specific power-law distribution of long-range links for greedy routing to succeed in poly-log time.
- **Algorithmic fairness** — among the early formalizers of impossibility results (no classifier can simultaneously satisfy calibration + balance-for-positive + balance-for-negative under base-rate differences).
- **Bursts and time-series of online activity** — co-author with David Easley of the textbook *Networks, Crowds, and Markets* (Cambridge UP 2010).

Awards: MacArthur Fellowship (2005), Nevanlinna Prize (2006), Harvey Prize (2013), ACM Knuth Prize (2021). The HITS algorithm was implemented as the **Clever** project at IBM Research in the late 1990s and informally influenced [[google|Google]]'s ranking approach via the broader link-analysis-as-ranking-signal idea that PageRank and HITS arrived at simultaneously.
