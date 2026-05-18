---
title: "Kishore Papineni"
type: entity
tags: [person, researcher, nlp, machine-translation]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Kishore Papineni

Computer scientist at IBM T. J. Watson during the IBM SMT era; later at Google. First author of the **BLEU** paper (Papineni, Roukos, Ward & Zhu, ACL 2002), the most widely-used automatic metric for machine translation ([[d2l-recurrent-modern]] §seq2seq; [[BLEU]]).

## Why he matters here

- **BLEU (2002).** Defined the *modified $n$-gram precision* + *brevity penalty* family that, with various script-defined variants, has driven a decade-plus of measurable MT progress. The metric is operational and cheap to compute, which lets it serve as both a development signal and a leaderboard metric. D2L uses BLEU as the running evaluation metric in §seq2seq.

## Connections

- [[BLEU]] — the metric.
- [[MachineTranslation]] — the task BLEU was designed for.
- [[d2l-recurrent-modern]] — D2L cites Papineni et al. 2002.
