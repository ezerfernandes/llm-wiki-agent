---
title: "CISPA Helmholtz Center for Information Security"
type: entity
tags: [organization, research-institute, security, germany, publisher]
sources: [fuzzingbook-11-grammar-coverage-fuzzer, fuzzingbook-14-generator-grammar-fuzzer, fuzzingbook-15-greybox-grammar-fuzzer, fuzzingbook-17-fuzzing-with-constraints, fuzzingbook-19-information-flow, fuzzingbook-20-concolic-fuzzer, fuzzingbook-22-dynamic-invariants, fuzzingbook-23-configuration-fuzzer, fuzzingbook-24-api-fuzzer, fuzzingbook-25-carver, fuzzingbook-26-python-fuzzer-testing-compilers, fuzzingbook-27-web-fuzzer, fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

# CISPA

**CISPA Helmholtz Center for Information Security** is a German national research center for information security (a member of the Helmholtz Association, based in Saarbrücken). It is the home institution of [[AndreasZeller|Andreas Zeller]] and the publisher of *The Fuzzing Book* (Zeller, Gopinath, Böhme, Fraser & Holler) and its companion *The Debugging Book* — the continuously updated, code-first online textbooks on [[Fuzzing|fuzzing]] and software [[Testing|testing]] cited throughout this wiki's Fuzzing Book source pages.

## Role in The Fuzzing Book
Listed as the publisher in every Fuzzing Book chapter's citation (CISPA, 2024 online edition). Several book chapters reflect CISPA-affiliated research, including the grammar-coverage / code-coverage correlation explored by CISPA PhD researcher Nikolas Havrikov in [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]].

## Connections
- [[AndreasZeller]] — CISPA faculty member / fellow and lead author of *The Fuzzing Book*.
- [[Fuzzing]] / [[Testing]] — the research areas of the book CISPA publishes.
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — Ch 11, whose grammar↔code coverage result is due to CISPA researcher Nikolas Havrikov.
- [[fuzzingbook-14-generator-grammar-fuzzer]] — Ch 14, "Fuzzing with Generators," published by CISPA.
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — Ch 15, "Greybox Fuzzing with Grammars," published by CISPA (reconstructs co-author [[ChristianHoller]]'s [[LangFuzz]]).
- [[fuzzingbook-17-fuzzing-with-constraints]] — Ch 17, "Fuzzing with Constraints," built on the [[ISLa]] work of CISPA-affiliated [[DominicSteinhofel]] & [[AndreasZeller]].
- [[fuzzingbook-19-information-flow]] — Ch 19, "Tracking Information Flow," developing [[CISPA]]-led [[DynamicTaintAnalysis|dynamic taint analysis]] / [[InformationFlow|information-flow]] tracking.
- [[fuzzingbook-20-concolic-fuzzer]] — Ch 20, "Concolic Fuzzing," published by CISPA (advancing semantic fuzzing to [[ConcolicExecution|concolic execution]] with [[Z3Prover|Z3]]).
- [[fuzzingbook-22-dynamic-invariants]] — Ch 22, "Mining Function Specifications," published by CISPA (closing Part IV with [[SpecificationMining|dynamic specification mining]] / [[Daikon]]-style invariant detection).
- [[fuzzingbook-23-configuration-fuzzer]] — Ch 23, "Testing Configurations," published by CISPA (opens Part V with [[ConfigurationFuzzing|configuration fuzzing]] and [[CombinatorialTesting|combinatorial testing]]).
- [[fuzzingbook-24-api-fuzzer]] — Ch 24, "Fuzzing APIs," published by CISPA ([[APIFuzzing|API/function-level fuzzing]] by synthesizing function-call code from grammars).
- [[fuzzingbook-25-carver]] — Ch 25, "Carving Unit Tests," published by CISPA ([[TestCarving|carving]] real calls into [[UnitTesting|unit tests]] and mining API grammars from them).
- [[fuzzingbook-26-python-fuzzer-testing-compilers]] — Ch 26, "Testing Compilers," published by CISPA ([[CompilerTesting|compiler testing]] via the [[PythonFuzzer]]: an [[ISLa]]-driven grammar over Python [[AbstractSyntaxTree|ASTs]]).
- [[fuzzingbook-27-web-fuzzer]] — Ch 27, "Testing Web Applications," published by CISPA ([[WebApplicationFuzzing|Web-application fuzzing]] via [[WebFormFuzzer|`WebFormFuzzer`]] and automatic [[SQLInjection]]/[[CrossSiteScripting|XSS]] attacks).
- [[fuzzingbook-28-gui-fuzzer]] — Ch 28, "Testing Graphical User Interfaces," published by CISPA (generic [[GUIFuzzing|GUI fuzzing]] via [[Selenium]] and a mined FSM-in-a-grammar [[UINavigationModel|UI navigation model]]).

## Sources
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — *The Fuzzing Book* Ch 11, "Grammar Coverage."
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators."
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars."
- [[fuzzingbook-17-fuzzing-with-constraints]] — *The Fuzzing Book* Ch 17, "Fuzzing with Constraints."
- [[fuzzingbook-19-information-flow]] — *The Fuzzing Book* Ch 19, "Tracking Information Flow."
- [[fuzzingbook-20-concolic-fuzzer]] — *The Fuzzing Book* Ch 20, "Concolic Fuzzing."
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22, "Mining Function Specifications."
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations."
- [[fuzzingbook-24-api-fuzzer]] — *The Fuzzing Book* Ch 24, "Fuzzing APIs."
- [[fuzzingbook-25-carver]] — *The Fuzzing Book* Ch 25, "Carving Unit Tests."
- [[fuzzingbook-26-python-fuzzer-testing-compilers]] — *The Fuzzing Book* Ch 26, "Testing Compilers (Python Fuzzer)."
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications."
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces."
