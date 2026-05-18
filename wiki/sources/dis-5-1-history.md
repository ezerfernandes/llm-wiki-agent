---
title: "Dive into Systems — Ch 5.1 The Origins of Modern Computing"
type: source
tags: [dive-into-systems, computer-architecture, history, foundational]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C5-Arch/hist.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 5.1** of *[[DiveIntoSystems]]* — the **opening section of Ch 5 *Computer Architecture***, and the corpus's first descent into the historical lineage rather than a technical mechanism. Traces how the [[VonNeumannArchitecture|stored-program]] model that underlies essentially every modern computer emerged in the **1930s–1940s** as a **convergence** of independent threads — [[ClaudeShannon|Shannon]]'s [[BooleanAlgebra|Boolean]] circuits, [[AlanTuring|Turing]]'s [[TuringMachine|abstract machine]], [[KonradZuse|Zuse]]'s [[Z3]], [[TommyFlowers|Flowers]]'s [[Colossus]], [[HowardAiken|Aiken]]'s [[HarvardMarkI|Mark I]], [[JohnMauchly|Mauchly]] / [[PresperEckert|Eckert]]'s [[ENIAC]], and [[JohnVonNeumann|von Neumann]]'s [[EDVAC]] paper — **not** a single linear progression. Explicitly foregrounds the women whose contributions were historically underrecognized (the six [[ENIAC|ENIAC]] programmers; [[GraceHopper|Grace Hopper]]; the [[WomensRoyalNavalService|WRNS]] operators of [[Colossus]]). Closes by naming the [[VonNeumannArchitecture|von Neumann architecture]] as the unifying synthesis that fuses **instructions + data in the same internal memory** — the structural thesis Ch 5.2+ will operationalize.

## Key Claims

- **Modern [[ComputerArchitecture|computer architecture]] is a convergence, not a linear inheritance** — the 1930s–1940s produced several independent computing machines (Z3, Colossus, Mark I, ENIAC) that each contributed pieces of what we now call the [[VonNeumannArchitecture|von Neumann architecture]].
- **Binary computing's logic foundation is [[ClaudeShannon|Shannon]]'s 1937 MIT master's thesis** — applying [[BooleanAlgebra|Boolean algebra]] to switching circuits, establishing that **electrical relays can implement logical operations**. The bridge between mathematical logic and physical circuits.
- **The [[TuringMachine|Turing machine]] is the abstract model of computation** — proposed 1937 by [[AlanTuring]] as the *"Logical Computing Machine,"* defining what is computable independent of any physical implementation. Underlies the [[ChurchTuringThesis|Church-Turing thesis]] and the formal notion of an *algorithm*.
- **[[KonradZuse|Konrad Zuse]]'s [[Z3]] (1941, Germany) was the first programmable electromechanical binary computer** — built independently of the Anglo-American line, in wartime isolation.
- **[[Colossus]] (1943, [[TommyFlowers|Tommy Flowers]]) cracked German Lorenz cipher traffic** at [[BletchleyPark]] — operated by the [[WomensRoyalNavalService|Women's Royal Naval Service (WRNS)]]; existence stayed classified for decades.
- **[[HarvardMarkI|Mark I]] (1944, [[HowardAiken|Howard Aiken]], Harvard) ran calculations for the [[ManhattanProject|atomic bomb]]** — electromechanical, programmed via paper tape.
- **[[ENIAC]] (1945, [[JohnMauchly|John Mauchly]] + [[PresperEckert|Presper Eckert]], [[UniversityOfPennsylvania|Penn]]) was the first general-purpose electronic digital computer** — programmed by **six women** ([[JeanJenningsBartik|Jean Jennings Bartik]], [[BettySnyderHolberton|Betty Snyder Holberton]], [[KayMcNultyMauchly|Kay McNulty Mauchly]], [[FrancesBilasSpence|Frances Bilas Spence]], [[MarlynWescoffMeltzer|Marlyn Wescoff Meltzer]], [[RuthLichtermanTeitelbaum|Ruth Lichterman Teitelbaum]]) who independently invented programming techniques including **algorithmic flow charts and [[Subroutine|subroutines]]**.
- **[[JohnVonNeumann|John von Neumann]]'s 1945 [[EDVAC]] paper synthesized prior innovations into the [[StoredProgram|stored-program]] model** — instructions and data both reside in the same internal memory — the architectural template under essentially every modern [[CPU]].
- **[[AlanTuring|Turing]]'s 1946 [[AutomaticComputingEngine|Automatic Computing Engine (ACE)]] was a stored-program design** developed contemporaneously at the [[NationalPhysicalLaboratory|UK NPL]].
- **[[GraceHopper]] developed [[COBOL]]** — the first high-level **machine-independent** programming language, decoupling source code from underlying [[ISA]].
- **Women's contributions were systematically underrecognized** — Ch 5.1 explicitly names this as a corrective historical thrust.

## Key Quotes

> "The Analytical Engine has no pretensions whatever to originate anything. It can do whatever we know how to order it to perform." — [[AdaLovelace|Ada Lovelace]] (quoted in the section's framing of the Analytical Engine as the conceptual antecedent of programmable computers)

> Modern computers descend from a *convergence* of 1930s–1940s innovations, not a single inventor. — Ch 5.1 framing

## Chronological Timeline

| Year | Event | People |
|---|---|---|
| 1837 | [[CharlesBabbage|Babbage]]'s [[AnalyticalEngine]] design (mechanical, never completed); [[AdaLovelace|Lovelace]] writes first algorithm | [[CharlesBabbage]], [[AdaLovelace]] |
| 1937 | MIT master's thesis applying [[BooleanAlgebra|Boolean algebra]] to switching circuits | [[ClaudeShannon]] |
| 1937 | *Logical Computing Machine* paper — the [[TuringMachine]] | [[AlanTuring]] |
| 1941 | [[Z3]] — first programmable electromechanical binary computer (Germany) | [[KonradZuse]] |
| 1943 | [[Colossus]] — code-breaking computer at [[BletchleyPark]] | [[TommyFlowers]] + [[WomensRoyalNavalService|WRNS]] operators |
| 1944 | [[HarvardMarkI|Mark I]] — electromechanical computer for atomic-bomb calculations | [[HowardAiken]] |
| 1945 | [[ENIAC]] — first general-purpose electronic digital computer ([[UniversityOfPennsylvania|Penn]]) | [[JohnMauchly]] + [[PresperEckert]] + the six [[ENIAC|ENIAC programmers]] |
| 1945 | [[EDVAC]] paper — *"First Draft of a Report on the EDVAC"* — codifies [[StoredProgram|stored-program]] architecture | [[JohnVonNeumann]] |
| 1946 | [[AutomaticComputingEngine|ACE]] — stored-program design at [[NationalPhysicalLaboratory|UK NPL]] | [[AlanTuring]] |
| 1959 | [[COBOL]] — first machine-independent high-level language | [[GraceHopper]] |

## Connections

- [[DiveIntoSystems]] — **opens Ch 5 *Computer Architecture***; the corpus's first historical-context section (preceding chapters were technical: C language, debugging, binary representation).
- [[VonNeumannArchitecture]] — the synthesized [[StoredProgram|stored-program]] model that the section converges on; Ch 5.2+ will operationalize the [[CPU]] / [[RAM]] / [[Bus]] structure.
- [[TuringMachine]] — abstract model that [[ChurchTuringThesis|defines]] what is *computable*; conceptual dual of the [[VonNeumannArchitecture|physical machine]].
- [[BooleanAlgebra]] (existing concept: `booleanalgebra.md`) — [[ClaudeShannon|Shannon]]'s 1937 circuit insight is the algebraic-to-electrical bridge.
- [[ClaudeShannon]] — already in wiki via [[d2l-appendix-mathematics]] for [[InformationTheory]]; Ch 5.1 adds the **1937 switching-circuit thesis** dimension.
- [[ENIAC]] / [[EDVAC]] / [[Z3]] / [[Colossus]] / [[HarvardMarkI]] — the convergence of independent machines.
- [[CharlesBabbage]] / [[AdaLovelace]] — 19th-century conceptual antecedents.
- [[ComputerHardware]] / [[ComputerSystem]] (existing) — Ch 5.1 supplies the historical lineage; [[dis-0-introduction|Ch 0]] supplied the abstract definition.

## Contradictions

- None with existing wiki content. Ch 5.1 supplies historical context that complements, rather than conflicts with, the technical [[CPU]] / [[RAM]] / [[ComputerHardware|hardware]] treatment elsewhere.

## Position in corpus

- **48th ingested chapter** — opens **Ch 5 *Computer Architecture*** of [[DiveIntoSystems]] (Ch 4 *Binary and Data Representation* fully closed with [[dis-4-10-exercises|Ch 4.10]]).
- **First historical / context-setting section** in the corpus — prior chapters (Ch 0 through Ch 4) were technical-mechanism sections.
- Forward-references the rest of Ch 5: [[CPU]] internals, [[ALU]], [[ControlUnit|control unit]], [[Register|registers]], [[Bus|system bus]], [[ISA|instruction set architecture]] — all of which descend from the [[VonNeumannArchitecture|von Neumann]] synthesis named in Ch 5.1.
