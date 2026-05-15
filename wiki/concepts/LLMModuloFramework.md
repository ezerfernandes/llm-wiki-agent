---
title: "LLM-Modulo Framework"
type: concept
tags: [planning, neuro-symbolic, agents, verification]
sources: [2402.01817-llm-modulo]
last_updated: 2026-05-10
---

# LLM-Modulo Framework

An architecture for **robust planning** that combines an LLM (as a candidate-plan generator and approximate knowledge source) with a **bank of external sound critics** in a tight Generate-Test-Critique loop. Proposed by [[SubbaraoKambhampati]] et al. ([[ArizonaStateUniversity]]) in [[2402.01817-llm-modulo]] (ICML 2024).

## Name
"Modulo" is borrowed from **SAT-Modulo Theories** (SMT; Nieuwenhuis & Oliveras 2006): a SAT solver extended with theory-specific decision procedures. By analogy, **LLM-Modulo** = an LLM extended with task-specific critics/verifiers.

## Architecture (Fig 3 of the paper)
1. **Problem Specification** (complete, partial, or abstract) — refined collaboratively with end-user using LLM help.
2. **LLM** proposes a candidate plan onto the **Plan Blackboard**.
3. **Bank of Critics** evaluates the candidate:
   - **Hard critics** — model-based, sound (e.g. [[PDDL|VAL]] plan validator, unit tests, simulators). Provide soundness guarantees.
   - **Soft critics** — style / explicability / preference / common-sense. May be LLM-based; soundness not required.
   - **Constructive critics** can suggest specific extensions/modifications.
4. **Reformatters** (LLM-driven) translate the candidate plan into each critic's representation.
5. **Meta (Backprompt) Controller** pools critiques into the next iterative prompt — round-robin, summarized, or *prompt-diversified* to explore search space.
6. Loop until **all hard critics sign off** → valid solution.
7. Optional: valid plans + interactions form **synthetic data** for fine-tuning the LLM.

## Soundness theorem (informal)
> *The soundness of the LLM-Modulo framework is inherited from the soundness of the correctness (hard) critics.*

LLMs are **never ascribed planning or verification competence**. Completeness depends on the LLM's ability to enumerate plausible candidates within the budget.

## Roles the LLM plays
1. Candidate plan generator
2. Reformatter (format change across syntactic reps)
3. Domain-model acquisition partner (extract PDDL with human sign-off)
4. Problem-spec refiner with end-users
5. Critic enumerator (suggest what critics are needed)
6. Soft-style critic itself

## Humans
- **Out of the inner loop** (replaced by automated critics — avoids Clever Hans, time burden).
- **In the outer loop** once-per-domain (sign off on extracted domain model) and once-per-problem (refine spec).

## Contrasted with neighboring approaches
- **Vs LLM-as-translator** (LLM+P, Logic-LM, Xie et al.): LLM-Modulo deliberately keeps the LLM as Generate-Test front-end, not a pipeline to a back-end symbolic solver — avoids inheriting solver expressivity/search-complexity limits.
- **Vs autonomous-mode LLM planning** ([[ChainOfThought]], [[Reflexion]], [[react]], [[TreeOfThoughts]]): ToT in particular is recast as "prompt diversification with task-specific verifier"; any apparent soundness comes from the verifier.
- **Vs agentic frameworks** (AutoGPT, LangChain): these confuse *acting* with *planning*; no soundness on trajectories.

## Empirical results
| Domain | Setup | Result |
|---|---|---|
| Blocksworld (PlanBench) | GPT-4 + VAL backprompts, 15 rounds | 82% pass |
| Logistics | GPT-4 + VAL backprompts | ~70% pass |
| Mystery BW (obfuscated) | GPT-4 + VAL backprompts | ~10% (LLM can't propose plausible candidates) |
| TravelPlanner (Xie 2024) | GPT-3.5-Turbo + hard+soft critics, ≤10 rounds | 6× over CoT/ReAct baseline (0.7% → ~4%+) |

## Connections
- [[SubbaraoKambhampati]], [[ArizonaStateUniversity]] — proposers
- [[Planning]] — the target class of tasks
- [[PDDL]], [[Blocksworld]], [[PlanBench]] — empirical evidence base
- [[SelfVerification]] — what the framework avoids depending on LLMs for
- [[System1And2]] — taxonomic framing
- [[NeuroSymbolicAI]] — the broader research lineage
- [[HumanInTheLoop]] — humans engage outer loop only
- [[SyntheticData]] — sound plans → fine-tuning data
- [[Voyager]], [[ReinforcementLearning]] — simulator-as-verifier instances
- [[2402.01817-llm-modulo]] — canonical source
