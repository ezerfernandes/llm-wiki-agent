---
title: "DSPy Tutorial — Building a Creative Text-Based AI Game"
type: source
tags: [dspy, tutorial, signatures, chain-of-thought, modules, game, narrative-generation, structured-outputs]
date: 2026-05-24
source_file: raw/dspy-ai-text-game-tutorial.md
---

## Summary

Official [[DSPy]] tutorial that builds an interactive text-based adventure game by composing **three [[DSPySignatures|Signatures]] under [[chainofthought|`dspy.ChainOfThought`]] modules** inside a single [[DSPyModules|`dspy.Module`]] subclass (`GameAI`). The tutorial frames DSPy as the **AI substrate for creative-systems applications**: deterministic Python game logic (`Player`/`GameContext`/`GameEngine` dataclasses, save/load, inventory, leveling) handles state, while LM calls — wrapped by typed Signatures — handle narrative generation, NPC dialogue, and action resolution. **No [[DSPyOptimizers|Optimizer]] step, no metric, no eval set** — the tutorial stops at the *Programming* rung of [[DSPyProgrammingModel|the DSPy three-stage workflow]], demonstrating the [[DSPyModules|Module-composition]] pattern in isolation.

## Key Claims

- **Three Signatures, three CoT Modules, one Program.** The `GameAI(dspy.Module)` constructor wires three [[chainofthought|`dspy.ChainOfThought`]] sub-modules — `story_gen` (over `StoryGenerator`), `dialogue_gen` (over `DialogueGenerator`), `action_resolver` (over `ActionResolver`) — exposing `generate_scene()`, `handle_dialogue()`, and `resolve_action()` as the public surface. **Canonical instance of [[DSPyModules|the "compose into bigger modules"]] property**: a program *is* a Module, with sub-modules registered as `self.*` attributes (the PyTorch-shaped pattern, not a LangChain-shaped chain DSL).

- **Structured outputs replace prompt parsing.** Every Signature returns typed Python objects, not free text:
  - `StoryGenerator → scene_description: str, available_actions: list[str], npcs_present: list[str], items_available: list[str]`
  - `DialogueGenerator → npc_response: str, mood_change: str, quest_offered: bool, information_revealed: str`
  - `ActionResolver → success: bool, outcome_description: str, stat_changes: dict[str, int], items_gained: list[str], experience_gained: int`
  The `dict[str, int]` and `list[str]` annotations are load-bearing — [[DSPyAdapters|the Adapter]] serializes them to/from the LM's text channel, so game logic can do `player.stats[k] += v` without regex-parsing a narrative paragraph.

- **CoT is the default reasoning wrapper.** Every signature is wrapped by [[chainofthought|`dspy.ChainOfThought`]] rather than [[DSPyPredict|`dspy.Predict`]]. The tutorial does not justify the choice — it follows [[dspy-programming-overview|the Programming Overview's]] *"start simple"* recommendation that CoT is the canonical default for any new task. The `.reasoning` field added by CoT is not exposed to the player but improves output quality.

- **One LM, no per-call overrides.** Configuration is the [[DSPyLM|standard one-liner]]: `dspy.LM(model='openai/gpt-4o-mini')` then `dspy.configure(lm=lm)`. No teacher/student split, no temperature override per Signature, no `dspy.context(...)` block — all three Signatures run on the same configured LM.

- **Deterministic game state, LM-driven narrative.** The dataclass split is deliberate: `Player` (health, level, experience, inventory, skills) and `GameContext` (location, story progress, NPCs met, completed quests) are **Python data the LM reads as inputs**, never derives. The LM owns the *creative* dimensions (scene prose, NPC mood, success/failure narrative) and proposes *bounded* state mutations (`stat_changes`, `items_gained`, `experience_gained`) that Python applies. This is the **"LM handles creative generation while game logic remains deterministic and controllable"** thesis the tutorial closes on.

- **No optimization step.** Unlike [[dspy-entity-extraction-tutorial|entity-extraction]], [[dspy-rag-tutorial|RAG]], [[dspy-tutorial-rag-as-agent|RAG-as-agent]], or [[dspy-customer-service-agent|customer-service-agent]] tutorials, this tutorial **never invokes [[MIPROv2]] or any [[DSPyOptimizers|Optimizer]]** — no `dspy.Evaluate`, no metric function, no train/dev split. The wiki's first DSPy tutorial that exits at *"declare Signatures + compose Modules"* without proceeding to the optimization rung.

- **Setup is three packages.** `pip install dspy rich typer` — DSPy for the LM-program layer, [[Rich|Rich]] for the terminal UI (panels, status displays, menus), [[Typer|Typer]] for CLI argument handling. Smaller dependency footprint than every other DSPy tutorial in the wiki.

## Key Quotes

> "Generate dynamic story content based on current game state." — `StoryGenerator` docstring (the Signature's docstring becomes the system instruction the LM sees)

> "Main AI module for game logic and narrative." — `GameAI` class docstring; positions the Module as **the** AI surface of the program

> "AI handles narrative generation, character interactions, and adaptive gameplay" — the tutorial's framing of which subsystems delegate to the LM vs. stay deterministic

## Connections

- [[DSPy]] — canonical framework; this is the **creative-systems / interactive-fiction application** rung of the official tutorial collection (sibling to [[dspy-entity-extraction-tutorial|NER]], [[dspy-rag-tutorial|RAG]], [[dspy-tutorial-rag-as-agent|RAG-as-agent]], [[dspy-customer-service-agent|customer-service-agent]], [[dspy-conversation-history|multi-turn chatbot]], [[dspy-custom-module|custom module]], [[dspy-tutorial-math|MATH algebra]]) — **seventh wiki-corpus DSPy tutorial**
- [[DSPySignatures]] — **three concrete typed Signatures**, all class-form (not inline-string form), with rich output types (`list[str]`, `dict[str, int]`, `bool`); receipt that *class-form is mandatory once outputs include containers*
- [[chainofthought]] — three CoT wrappers in one Module; canonical example of "CoT is the default, not a special case"
- [[DSPyModules]] — `GameAI(dspy.Module)` is the **canonical compose-three-sub-modules pattern** the page describes
- [[DSPyLM]] — minimal one-line configuration with no per-call overrides
- [[DSPyAdapters]] — implicit Adapter handling of `list[str]` / `dict[str, int]` / `bool` output types; the Adapter's serialization is what makes the Python-driven game loop possible
- [[DSPyProgrammingModel]] — tutorial exercises **only** the *Programming* stage; never reaches *Evaluation* or *Optimization*
- [[ChainRule]] — not relevant; just a name-collision check
- [[StructuredOutputs]] — the typed-output discipline that makes the game-state mutations safely applicable in Python

## Contradictions

- None with prior wiki content. The tutorial's *omissions* (no Optimizer, no metric, no eval) are not contradictions — they reflect a deliberate scope choice to keep the tutorial focused on Module composition. The [[DSPyOptimization|Optimization page]] is the next-step pointer for anyone who wants to tune `GameAI` against a quality metric (e.g., player engagement, narrative coherence).

## Scope-Limit Gaps

- **No metric is defined.** The tutorial does not propose how one would *score* a generated scene, dialogue, or action resolution — a non-trivial open problem for creative tasks (the [[2604.14585-prompt-optimization-coin-flip|"can but doesn't" pattern]] would need a learned reward model or human-preference signal, neither of which is mentioned).
- **No prompt optimization.** Three CoT modules with raw zero-shot defaults; no [[MIPROv2]] / [[BootstrapFewShot]] sweep. Whether [[MIPROv2|`auto="light"`]] would improve narrative quality is left open.
- **No multi-turn state in the LM call itself.** `recent_actions` and `context` strings are constructed by Python and passed in as inputs; the LM has no persistent conversation history. Contrast with [[dspy-conversation-history|the multi-turn chatbot tutorial]] which uses `dspy.History`.
- **No tool use / ReAct.** The LM never *calls* game functions — it only *proposes* state changes as structured output. Compare with [[dspy-tutorial-rag-as-agent|the RAG-as-agent tutorial]] which uses [[react|`dspy.ReAct`]] with real tool calls.
- **No multi-model strategy.** Single `openai/gpt-4o-mini` for all three Signatures. A natural extension would route `DialogueGenerator` (cheaper, simpler) to a smaller model and reserve `StoryGenerator` (longer, richer prose) for a larger model via `dspy.context(lm=...)`.
