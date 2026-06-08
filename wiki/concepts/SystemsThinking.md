---
title: "Systems Thinking"
type: concept
tags: [ml-systems, mlsysbook, systems-engineering, foundations]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Systems Thinking

Analyzing **how a system's parts interrelate** rather than optimizing each in isolation (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]). The [[DAMTaxonomy|AI Triad]]'s deepest lesson is that Data, Algorithm, and Machine *interact*: collected data constrains feasible algorithms; the chosen algorithm dictates feasible hardware; target hardware reshapes processable data. "Pull on any single thread and the entire system shifts." Optimizing each piece in isolation is how teams build "accurate models that cannot be deployed and efficient pipelines that feed the wrong data."

Ch 3 formalizes three structural patterns that recur across the [[MLSystemLifecycle|lifecycle]]:

1. **[[ConstraintPropagationPrinciple|Constraint propagation]]** — decisions cascade (bidirectionally) and late-discovered constraints cost exponentially more.
2. **[[MultiScaleFeedback|Multi-scale feedback]]** — feedback loops operate from minutes to quarters (~five orders of magnitude).
3. **[[EmergentBehavior|Emergent complexity]] and resource trade-offs** — system-level behavior diverges from component-level behavior; a 2% accuracy gain may double model size and capital cost across hundreds of sites.

Recognizing these patterns transforms reactive debugging into proactive design that surfaces downstream constraints early.

## Connections

- [[DAMTaxonomy]] — the interacting Data·Algorithm·Machine triad.
- [[ConstraintPropagationPrinciple]] / [[MultiScaleFeedback]] / [[EmergentBehavior]] — the three patterns.
- [[MLWorkflow]] — the discipline that operationalizes systems thinking.
- [[mlsysbook-ch03-ml-workflow]] — source.
