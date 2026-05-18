---
title: "AI co-mathematician"
type: concept
tags: [system, agentic-ai, mathematics, harness, deepmind]
sources: [2605.06651v2-ai-co-mathematician]
last_updated: 2026-05-15
---

# AI co-mathematician

[[googledeepmind|Google DeepMind]]'s stateful interactive workbench for mathematics research ([[2605.06651v2-ai-co-mathematician]]). A **harness over [[gemini|Gemini 3.1 Pro]] and [[GeminiDeepThink|Gemini 3.1 Deep Think]]** — no custom model training. The user converses with a top-level [[ProjectCoordinatorAgent|Project Coordinator]], which delegates per-goal [[WorkstreamCoordinator|Workstream Coordinators]], each of which runs a linear action sequence and may spawn specialized sub-agents (literature review, coding, prover, reviewer) — all communicating via an internal messaging system over a shared file system.

## Seven design principles (paper §2)
1. **Embrace mathematics beyond proofs** — ideation, literature, computation, theory-building.
2. **Support iterative refinement of intent** — dialogue first, execution second (Pólya, Cantor).
3. **Produce native mathematical artifacts** — a living [[WorkingPaper]] (LaTeX, margin notes).
4. **Enable asynchronous flexible steering** — central coordinator the user can interrupt at any time.
5. **Manage cognitive load via [[ProgressiveDisclosure]]** — high-level intent surface, drill-down on demand.
6. **Track, manage, communicate uncertainty** — version history, validation compute, inline highlighting.
7. **Preserve the history of failed explorations** — dead ends as first-class permanent outcomes (Lakatos).

## Architecture in one diagram
```
USER ↔ Project Coordinator (P)
            ├── Workstream Coordinator 1 → sub-agents
            ├── Workstream Coordinator 2 → sub-agents
            └── Workstream Coordinator 3 → sub-agents
```
All agents read/write a shared filesystem. The user-facing chat is filtered to the Project Coordinator; lower-level sub-agent chatter is available on demand.

## Results
- **48% on [[FrontierMath]] Tier 4** (23/48; new high score; [[gemini|Gemini 3.1 Pro]] base = 19%).
- **87% on a 100-question internal research-math benchmark** vs Gemini 3.1 Pro 57%, [[GeminiDeepThink|Gemini 3.1 Deep Think]] 70%.
- Three independent open-problem case studies resolved by external mathematicians using the system: [[KourovkaNotebook]] Problem 21.10 (M. Lackenby), [[StirlingCoefficients]] log-concavity (G. Bérczi), [[HamiltonianDiffeomorphism]] perturbation lemma (S. Rezchikov).

## Position in the wiki
- An [[LLMModuloFramework|LLM-Modulo instance]] under [[2402.01817-llm-modulo]]'s taxonomy: LLM agents generate; reviewer agents + test passes + golden-value checks are the *external sound critics*.
- A concrete instance of the DAG framework $\Psi = (\mathcal{G}, \mathcal{F}, \Lambda)$ from [[2605.12966-agentic-ai-to-agi]]: bounded [[CompositionalCapacity]], contractive reviewer edges in the [[TopologicalEdgeWeight]] sense.
- Empirical evidence for [[2605.10698-bystander-effect-mas]]'s [[BystanderEffect]]: the [[ReviewerPleasingBias]] failure mode is [[AlignmentHallucination]] inside a reviewer bank.
- Implements *textual memory* (TMM) under [[2604.27707-agentic-memory-is-a-memo]]'s taxonomy; the Ω(k²) compositional ceiling applies, mitigated empirically by the human-in-the-loop.

## Stated limitations (paper §7)
- [[ReviewerPleasingBias]] (False Consensus).
- [[DeathSpiral]] (Non-Termination).
- System autonomy still requires ceding control — current model judgment is far behind human.
- Semantic mismatch between LaTeX typeset-quality and rigor-quality.

## Connections
- [[2605.06651v2-ai-co-mathematician]]
- [[ProjectCoordinatorAgent]] / [[WorkstreamCoordinator]] / [[WorkingPaper]] / [[ProgressiveDisclosure]]
- [[AlphaProof]] / [[Aletheia]] / [[AlphaEvolve]] — designed plug-in points.
- [[FrontierMath]] — primary external benchmark.
