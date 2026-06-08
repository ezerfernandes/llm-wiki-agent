---
title: "Andreas Zeller"
type: entity
tags: [person, author, researcher, software-engineering, testing, fuzzing, debugging, security]
sources: [fuzzingbook-01-tours, fuzzingbook-02-intro-testing, fuzzingbook-03-fuzzer, fuzzingbook-04-coverage, fuzzingbook-05-mutation-fuzzer, fuzzingbook-06-greybox-fuzzer, fuzzingbook-07-search-based-fuzzer, fuzzingbook-08-mutation-analysis, fuzzingbook-09-grammars, fuzzingbook-10-grammar-fuzzer, fuzzingbook-11-grammar-coverage-fuzzer, fuzzingbook-14-generator-grammar-fuzzer, fuzzingbook-15-greybox-grammar-fuzzer, fuzzingbook-16-reducer, fuzzingbook-17-fuzzing-with-constraints, fuzzingbook-18-grammar-miner, fuzzingbook-19-information-flow, fuzzingbook-20-concolic-fuzzer, fuzzingbook-21-symbolic-fuzzer, fuzzingbook-22-dynamic-invariants, fuzzingbook-23-configuration-fuzzer, fuzzingbook-24-api-fuzzer, fuzzingbook-25-carver, fuzzingbook-26-python-fuzzer-testing-compilers, fuzzingbook-27-web-fuzzer, fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

# Andreas Zeller

**Andreas Zeller** is a software-engineering researcher known for foundational work on automated debugging and software testing. He is a faculty member / fellow at the **CISPA Helmholtz Center for Information Security** and is the lead author of *[[fuzzingbook-01-tours|The Fuzzing Book]]* (with Rahul Gopinath, Marcel Böhme, Gordon Fraser, and Christian Holler) and its companion *The Debugging Book*. His research themes include delta debugging, automated fault localization, dynamic specification mining, and input grammar mining — many of which appear as chapters in *The Fuzzing Book*.

## Role in The Fuzzing Book
Lead author of the continuously updated online edition (CISPA, 2024). The book is a code-first, notebook-based treatment of [[Fuzzing|fuzzing]] and [[Testing|software testing]], organized as a prerequisite graph with role-based reading tours (see [[fuzzingbook-01-tours]]).

## From The Fuzzing Book — Fuzzing with Constraints
[[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] is built around [[ISLa]], the [[InputSpecificationLanguage|Input Specification Language]] Zeller co-created with [[DominicSteinhofel|Dominic Steinhöfel]] (their ESEC/FSE 2022 paper "Input Invariants"). It opens the book's semantic-fuzzing part with the *declarative* [[ConstraintBasedFuzzing|constraint-based]] approach — a grammar plus [[SemanticConstraint|constraints]] solved by an [[SMTSolver|SMT solver]] — contrasted with the imperative generators of his own [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]].

## From The Fuzzing Book — Mining Input Grammars
[[fuzzingbook-18-grammar-miner|Ch 18]] realizes Zeller's **input grammar mining** research line: it is based directly on the **AUTOGRAM** approach (Höschele & Zeller, 2017), recovering an input [[Grammar|grammar]] by tracing how a program decomposes input substrings into named variables ([[GrammarInference|grammar inference]] via the [[GrammarMiner|`GrammarMiner`]] pipeline). It sits alongside co-author [[RahulGopinath]]'s related Mimid work, and continues the dynamic specification-mining theme that runs through Zeller's career.

## From The Fuzzing Book — Tracking Information Flow
[[fuzzingbook-19-information-flow|Ch 19]] develops the [[InformationFlow|information-flow]] / [[DynamicTaintAnalysis|dynamic taint analysis]] toolkit (the [[TaintedString|`tstr`]] and [[CharacterOrigin|`ostr`]] string subclasses) that underpins the semantic-fuzzing part — including the precise [[DynamicTaintTracking|taint tracking]] his and [[RahulGopinath]]'s grammar miners ([[fuzzingbook-18-grammar-miner|Ch 18]]) can build on, and the [[TaintDirectedFuzzing|taint-directed fuzzing]] that anticipates the symbolic/concolic methods of [[fuzzingbook-20-concolic-fuzzer|Ch 20]].

## From The Fuzzing Book — Concolic Fuzzing
[[fuzzingbook-20-concolic-fuzzer|Ch 20]] advances his semantic-fuzzing part from taint tracking to [[ConcolicExecution|concolic execution]]: a `ConcolicTracer` of symbolic proxy objects collects [[PathConstraint|path conditions]] solved by [[Z3Prover|Z3]] ([[SMTSolver|SMT solving]]), and `SimpleConcolicFuzzer`/`ConcolicGrammarFuzzer` turn this into [[ConcolicFuzzing|concolic fuzzing]] that lifts discovered constraints into the input [[Grammar|grammar]]. It reuses the [[fuzzingbook-19-information-flow|Ch 19]] vulnerable database and sets up the costlier [[fuzzingbook-21-symbolic-fuzzer|symbolic fuzzing of Ch 21]].

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] completes his semantic-fuzzing arc with *pure* [[SymbolicExecution|symbolic execution]]: the [[SymbolicFuzzer|`SymbolicFuzzer`]] statically walks a function's [[ControlFlow|control-flow graph]], enumerates all paths to a bounded depth (handling reassignment by SSA renaming and loops by [[PathExplosion|unrolling]]), and solves each [[PathConstraint|path condition]] with [[Z3Prover|Z3]] to mint inputs — no seed required, the static counterpart to his [[fuzzingbook-20-concolic-fuzzer|Ch 20]] concolic fuzzer. The chapter situates the work against the symbolic-execution literature ([[KLEE]], [[angr]], Driller, [[SAGE]], CHEF; King 1976).

## From The Fuzzing Book — Mining Function Specifications
[[fuzzingbook-22-dynamic-invariants|Ch 22]] closes Zeller's semantic-fuzzing part (Part IV) by turning the lens around: instead of *consuming* specifications to generate inputs ([[fuzzingbook-20-concolic-fuzzer|Ch 20]]/[[fuzzingbook-21-symbolic-fuzzer|Ch 21]]), it *mines* them. The chapter realizes his long-running **dynamic specification-mining** research line — reconstructing a miniature [[Daikon]] — with a `TypeAnnotator` ([[TypeInference|type mining]]) and an `InvariantAnnotator` ([[InvariantInference|invariant mining]]) that emit `@precondition`/`@postcondition` decorators ([[DynamicInvariant|dynamic invariants]] / [[SpecificationMining]]). It explicitly connects mining to test generation — diverse generated runs make mined specs precise — echoing the mining↔generation loop that recurs through his work (cf. his AUTOGRAM grammar mining in [[fuzzingbook-18-grammar-miner|Ch 18]], itself a specification-mining approach).

## From The Fuzzing Book — Testing Configurations
[[fuzzingbook-23-configuration-fuzzer|Ch 23]] opens Zeller's domain-specific part (Part V) by extending his grammar-mining theme from input data to a program's *configuration*: the [[OptionGrammarMiner|`OptionGrammarMiner`]] introspects `argparse` (via `sys.settrace`, stopping at `parse_args()`) to mine an [[OptionGrammar|option grammar]] with no hand-written spec, and the `OptionRunner`/`OptionFuzzer` toolkit fuzzes real tools (`autopep8`, [[MyPy|`mypy`]], `notedown`) with a [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]]. It adds [[CombinatorialTesting|pairwise combinatorial testing]] of options. The chapter continues his recurring mining↔generation loop — recover a model from a program, then use it to generate tests — here for [[ConfigurationFuzzing|configuration fuzzing]].

## From The Fuzzing Book — Fuzzing APIs
[[fuzzingbook-24-api-fuzzer|Ch 24]] continues Zeller's domain-specific part (Part V) by moving the fuzzing target from system input to the **API / function level**: it synthesizes function-call code from [[Grammar|grammars]] ([[APIFuzzing|API fuzzing]]), reuses his own [[GeneratorGrammar|generator grammars]] ([[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]]) to bound argument values and synthesize [[TestOracle|oracles]], and sets up the automatic call-recording of [[fuzzingbook-25-carver|Ch 25]] (Carver) — another instance of his recurring mining↔generation loop.

## From The Fuzzing Book — Carving Unit Tests
[[fuzzingbook-25-carver|Ch 25]] continues Zeller's domain-specific part (Part V) and is a clean instance of his recurring *mining↔generation* loop applied to tests: a [[Carver|`CallCarver`]] **records** real function calls during a system run and [[TestCarving|carving]] replays each as a fast standalone [[UnitTesting|unit test]] ([[RecordReplay|record-and-replay]], with [[Serialization|pickled]] objects), while the [[APIGrammarMining|`CallGrammarMiner`]] **mines** an API grammar from those calls to fuzz the API ([[APIFuzzing]]) — automating the hand-written call grammars of his [[fuzzingbook-24-api-fuzzer|Ch 24]]. The chapter credits Elbaum et al. (2006) for carving and Kampmann & Zeller (2018) for combining carving with API fuzzing.

## From The Fuzzing Book — Testing Compilers (Python Fuzzer)
[[fuzzingbook-26-python-fuzzer-testing-compilers|Ch 26]] continues Zeller's domain-specific part (Part V) by aiming fuzzing at the hardest target — *program code itself* — to test a compiler/interpreter ([[CompilerTesting|compiler testing]]). It reuses his [[ISLa]] framework ([[fuzzingbook-17-fuzzing-with-constraints|Ch 17]]) as the engine: the [[PythonFuzzer]] subclasses `ISLaSolver` to generate Python from a grammar of [[AbstractSyntaxTree|AST]] constructor calls (`PYTHON_AST_GRAMMAR`), and his search-based/evolutionary methods ([[fuzzingbook-07-search-based-fuzzer|Ch 7]]) return as a [[Coverage|coverage]]-guided [[EvolutionaryFuzzing|evolutionary fuzzer]] that mutates parsed code toward a planted bug. The chapter credits [[CSmith]] (Yang et al., 2011) as the seminal compiler-testing work and suggests his own [[fuzzingbook-16-reducer|Delta Debugging]] to shrink bug-triggering programs.

## From The Fuzzing Book — Testing Web Applications
[[fuzzingbook-27-web-fuzzer|Ch 27]] continues Zeller's domain-specific part (Part V) by turning fuzzing toward *user interfaces*: it builds a deliberately vulnerable HTTP shop server and mines a grammar straight from its served HTML form ([[WebFormFuzzer|`WebFormFuzzer`]] / `HTMLGrammarMiner`), so any Web form can be fuzzed from just a URL ([[WebApplicationFuzzing|Web-application fuzzing]]). It is another instance of his recurring *mining↔generation* loop — recover a model (the form's input grammar) from the system, then generate tests against it — and it reuses his [[GrammarFuzzer|`GrammarFuzzer`]] ([[fuzzingbook-10-grammar-fuzzer|Ch 10]]) and crawler as the engine. The chapter then weaponizes it into automatic [[SQLInjection|SQL]]/[[CrossSiteScripting|XSS]]/[[HTMLInjection|HTML]] [[CodeInjection|injection]] attacks, and points to his own [[fuzzingbook-19-information-flow|Ch 19]] information-flow work as the principled defense. It leads into the generic [[fuzzingbook-28-gui-fuzzer|GUI fuzzing of Ch 28]].

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] closes Zeller's domain-specific part (Part V) by generalizing UI testing from HTML forms to *arbitrary graphical user interfaces* ([[GUIFuzzing|GUI fuzzing]]), driven through a real browser with [[Selenium]] ([[WebDriver|WebDriver]]). It is another instance of his recurring *mining↔generation* loop: a [[GUIFuzzer|`GUIGrammarMiner`]] mines a [[UINavigationModel|UI navigation model]] — a [[FiniteStateMachine|finite state machine]] of pages — by exploration, the model is *embedded in a [[Grammar|grammar]]* so one structure encodes states and form values ([[ModelBasedTesting|model-based testing]]), and his own [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] ([[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]]) is reused so transition coverage comes for free. It directly generalizes his [[fuzzingbook-27-web-fuzzer|Ch 27]] Web fuzzer past JavaScript and leads into [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]].

## Connections
- [[GUIFuzzing]] / [[GUIFuzzer]] / [[UINavigationModel]] / [[ModelBasedTesting]] / [[Selenium]] — the Ch 28 GUI-fuzzing material (FSM-in-a-grammar UI model driven via Selenium).
- [[WebApplicationFuzzing]] / [[WebFormFuzzer]] / [[SQLInjection]] / [[CrossSiteScripting]] — the Ch 27 Web-application fuzzing and injection-attack material.
- [[CompilerTesting]] / [[PythonFuzzer]] / [[EvolutionaryFuzzing]] — the Ch 26 compiler-testing material (grammar over ASTs, `PythonFuzzer`, coverage-guided evolution); cites [[CSmith]].
- [[TestCarving]] / [[Carver]] / [[RecordReplay]] / [[Serialization]] / [[APIGrammarMining]] — the Ch 25 carving material (record calls, replay as unit tests, mine API grammars).
- [[APIFuzzing]] / [[CallSequenceFuzzing]] — the Ch 24 API/function-level fuzzing material (synthesizing and running function calls).
- [[ConfigurationFuzzing]] / [[OptionGrammar]] / [[OptionGrammarMiner]] / [[CombinatorialTesting]] — the Ch 23 configuration-testing material opening Part V.
- [[SpecificationMining]] / [[DynamicInvariant]] / [[InvariantInference]] / [[TypeInference]] — the Ch 22 dynamic specification-mining material (the `TypeAnnotator`/`InvariantAnnotator`).
- [[Daikon]] — the seminal invariant detector Ch 22 reconstructs in miniature.
- [[SymbolicExecution]] / [[SymbolicFuzzer]] / [[PathExplosion]] — the Ch 21 pure-symbolic material (CFG path enumeration, loop unrolling, Z3-solved path conditions).
- [[ConcolicExecution]] / [[ConcolicFuzzing]] — the Ch 20 semantic-fuzzing material (path conditions, Z3, the two concolic fuzzers).
- [[GrammarInference]] / [[GrammarMiner]] / [[GrammarMining]] — Ch 18's input-grammar mining, based on his AUTOGRAM work.
- [[InformationFlow]] / [[DynamicTaintAnalysis]] / [[TaintDirectedFuzzing]] — the Ch 19 information-flow material in his semantic-fuzzing part.
- [[RahulGopinath]] — co-author and fellow grammar-mining researcher (Mimid lineage).
- [[ISLa]] / [[InputSpecificationLanguage]] — the constraint framework he co-created with [[DominicSteinhofel]], the basis of Ch 17.
- [[DominicSteinhofel]] — his ISLa co-author.
- [[fuzzingbook-01-tours]] — orientation chapter of *The Fuzzing Book*, which he co-authors and leads.
- [[fuzzingbook-02-intro-testing]] — the book's first technical chapter, "Introduction to Software Testing."
- [[fuzzingbook-03-fuzzer]] — the foundational fuzzing chapter that mints the book's `Fuzzer`/`Runner` architecture and recounts [[BartonMiller]]'s origin experiment.
- [[fuzzingbook-04-coverage]] — the code-coverage chapter that builds the `Coverage` class and seeds [[CoverageGuidedFuzzing|coverage-guided fuzzing]].
- [[fuzzingbook-05-mutation-fuzzer]] — the mutation-based fuzzing chapter (`MutationFuzzer`/`MutationCoverageFuzzer`) introducing [[AFL]]'s core ideas.
- [[fuzzingbook-06-greybox-fuzzer]] — the greybox-fuzzing chapter reconstructing [[AFL]]/[[AFLFast]]/AFLGo and [[PowerSchedule|power schedules]] (co-authored with [[MarcelBohme]]).
- [[fuzzingbook-07-search-based-fuzzer]] — the search-based fuzzing chapter ([[SearchBasedTesting|SBST]]: [[FitnessFunction|fitness]]/[[BranchDistance|branch distance]], [[HillClimbing|hill climbing]], [[GeneticAlgorithm|genetic algorithms]]), rooted in co-author [[GordonFraser|Fraser]]'s [[EvoSuite]] work.
- [[fuzzingbook-08-mutation-analysis]] — the [[MutationAnalysis|mutation analysis]] chapter, evaluating [[TestAdequacy|test-suite adequacy]] via the [[MutationScore|mutation score]]; Zeller is also the originator of [[DeltaDebugging|delta debugging]] referenced in its residual-defect exercise.
- [[fuzzingbook-09-grammars]] — the foundational grammar chapter opening Part III, minting the [[Grammar|`Grammar`]] data structure and [[GrammarBasedFuzzing|grammar-based fuzzing]] (co-author Christian Holler's LangFuzz is cited in its Background).
- [[fuzzingbook-10-grammar-fuzzer]] — the "hub" chapter that makes grammar fuzzing efficient via [[DerivationTree|derivation trees]] and the [[GrammarFuzzer|`GrammarFuzzer`]] base class.
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — the grammar-coverage chapter ([[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]], [[ContextCoverage|context coverage]], and the grammar↔code coverage correlation due to CISPA's Nikolas Havrikov).
- [[fuzzingbook-14-generator-grammar-fuzzer]] — the generator chapter attaching Python functions to grammar expansions ([[GeneratorGrammar|generator grammars]], [[GeneratorGrammarFuzzer|`GeneratorGrammarFuzzer`]], [[PGGCFuzzer|`PGGCFuzzer`]]) for [[SemanticConstraint|semantic validity]].
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — the [[GrammarAwareGreyboxFuzzing|grammar-aware greybox]] chapter closing Part III, fusing coverage feedback with structure-aware mutation (reconstructing co-author [[ChristianHoller]]'s [[LangFuzz]] and the [[AFLSmart]] fuzzer).
- [[fuzzingbook-16-reducer]] — the reducer chapter implementing his own [[DeltaDebugging|delta debugging]] (Zeller & Hildebrandt 2002) as the [[DDMin|`ddmin`]] `DeltaDebuggingReducer`, then [[GrammarReducer|grammar-based reduction]] ([[HierarchicalDeltaDebugging|HDD]]) for structured inputs.
- [[CISPA]] — Zeller's home institution and the book's publisher.
- [[Fuzzing]] — the book's central subject.
- [[Testing]] — the broader discipline the book sits within.

## Sources
- [[fuzzingbook-01-tours]] — *The Fuzzing Book* Ch 1, "Tours through the Book."
- [[fuzzingbook-02-intro-testing]] — *The Fuzzing Book* Ch 2, "Introduction to Software Testing."
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3, "Fuzzing: Breaking Things with Random Inputs."
- [[fuzzingbook-04-coverage]] — *The Fuzzing Book* Ch 4, "Code Coverage."
- [[fuzzingbook-05-mutation-fuzzer]] — *The Fuzzing Book* Ch 5, "Mutation-Based Fuzzing."
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing."
- [[fuzzingbook-07-search-based-fuzzer]] — *The Fuzzing Book* Ch 7, "Search-Based Fuzzing."
- [[fuzzingbook-08-mutation-analysis]] — *The Fuzzing Book* Ch 8, "Mutation Analysis."
- [[fuzzingbook-09-grammars]] — *The Fuzzing Book* Ch 9, "Fuzzing with Grammars."
- [[fuzzingbook-10-grammar-fuzzer]] — *The Fuzzing Book* Ch 10, "Efficient Grammar Fuzzing."
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — *The Fuzzing Book* Ch 11, "Grammar Coverage."
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators."
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars."
- [[fuzzingbook-16-reducer]] — *The Fuzzing Book* Ch 16, "Reducing Failure-Inducing Inputs" (his delta debugging algorithm).
- [[fuzzingbook-17-fuzzing-with-constraints]] — *The Fuzzing Book* Ch 17, "Fuzzing with Constraints" (built on his ISLa work with [[DominicSteinhofel]]).
- [[fuzzingbook-18-grammar-miner]] — *The Fuzzing Book* Ch 18, "Mining Input Grammars" (based on his AUTOGRAM grammar-mining work).
- [[fuzzingbook-19-information-flow]] — *The Fuzzing Book* Ch 19, "Tracking Information Flow."
- [[fuzzingbook-20-concolic-fuzzer]] — *The Fuzzing Book* Ch 20, "Concolic Fuzzing."
- [[fuzzingbook-21-symbolic-fuzzer]] — *The Fuzzing Book* Ch 21, "Symbolic Fuzzing."
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22, "Mining Function Specifications" (his dynamic specification-mining line; a miniature Daikon).
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations" (opens Part V; mining option grammars from `argparse` and combinatorial option testing).
- [[fuzzingbook-24-api-fuzzer]] — *The Fuzzing Book* Ch 24, "Fuzzing APIs" (synthesizing function-call code from grammars; API/function-level fuzzing).
- [[fuzzingbook-25-carver]] — *The Fuzzing Book* Ch 25, "Carving Unit Tests" (recording/replaying calls as unit tests; mining API grammars from carved calls).
- [[fuzzingbook-26-python-fuzzer-testing-compilers]] — *The Fuzzing Book* Ch 26, "Testing Compilers" (the `PythonFuzzer`: grammar over Python ASTs, ISLa-based generation/mutation, coverage-guided evolutionary fuzzing).
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications" (`WebFormFuzzer` mining grammars from HTML forms; automatic SQL/HTML/XSS injection attacks).
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces" (generic GUI fuzzing via Selenium; a mined FSM-in-a-grammar UI navigation model, `GUICoverageFuzzer`).
