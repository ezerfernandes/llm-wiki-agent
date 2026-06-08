---
title: "99 bottles of beer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, iteration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/99_bottles_of_beer
---

## Summary
The task is to programmatically generate and display the complete lyrics of the song "99 Bottles of Beer on the Wall", counting down each verse from 99 to 0. Each verse follows a fixed template that interpolates the current bottle count, decrementing by one per stanza. The challenge is a classic exercise in loops and string formatting, and Rosetta Code explicitly encourages creative, concise, or comical implementations as well as straightforward ones.

## Task Requirements
- Print the full lyrics, iterating the bottle count from 99 down to 0.
- Each verse uses the form: "N bottles of beer on the wall / N bottles of beer / Take one down, pass it around / N-1 bottles of beer on the wall".
- Grammatical handling of the singular "1 bottle of beer" is optional.
- Solutions may be simple and obvious, or deliberately creative/concise/comical.

## Language Coverage
402 languages implement this task, an extremely broad cross-section spanning mainstream, esoteric, and assembly languages — reflecting its status as a canonical "first program" benchmark. Representative implementations include Python, C, Java, Haskell, Rust, Ruby, Lua, Perl, Brainf***, and Whitespace.

## Connections
- [[StringFormatting]] — verse templates built by interpolating the bottle count
- [[Iteration]] — the countdown is a descending loop or recursion
- [[CodeGolf]] — many entries optimize for brevity per the task's "concise" framing
- [[EsotericProgrammingLanguages]] — esoteric languages like Brainf***, Befunge, and Malbolge are well represented

## Solved in (Rosetta Code languages)
Solved in **368** of the wiki's catalogued languages (Rosetta Code shows 402 language sections for this task). (34 further RC language section(s) are outside the wiki's popularity-list language set.)

[[0815]], [[11l]], [[360 Assembly]], [[6502 Assembly]], [[6800 Assembly]], [[68000 Assembly]], [[8080 Assembly]], [[8th]], [[AArch64 Assembly]], [[ABAP]], [[ABC]], [[ACL2]], [[Acornsoft Lisp]], [[Action!]], [[ActionScript]], [[Ada]], [[Aime]], [[Algae]], [[ALGOL 60]], [[ALGOL 68]], [[ALGOL-M]], [[AmigaE]], [[Apex]], [[APL]], [[App Inventor]], [[AppleScript]], [[Arbre]], [[Argile]], [[Aria]], [[ArkScript]], [[ARM Assembly]], [[ArnoldC]], [[Arturo]], [[AsciiDots]], [[Astro]], [[Asymptote]], [[ATS]], [[AutoHotkey]], [[AutoIt]], [[AWK]], [[Axe]], [[Babel]], [[BabyCobol]], [[Ballerina]], [[BASIC]], [[Batch File]], [[Battlestar]], [[Bc]], [[BCPL]], [[Befunge]], [[BlitzMax]], [[BlooP]], [[BQN]], [[Bracmat]], [[Brainf***]], [[Brat]], [[Bruijn]], [[C]], [[C++]], [[Calcscript]], [[Ceylon]], [[Chapel]], [[Chef]], [[Cind]], [[Clay]], [[Clio]], [[CLIPS]], [[Clojure]], [[CLU]], [[COBOL]], [[CoffeeScript]], [[ColdFusion]], [[Comal]], [[Comefrom0x10]], [[Common Lisp]], [[Component Pascal]], [[Cowgol]], [[Crystal]], [[D]], [[Dart]], [[DBL]], [[Dc]], [[Delphi]], [[DIBOL-11]], [[DM]], [[Draco]], [[DuckDB]], [[Dyalect]], [[Dylan]], [[Déjà Vu]], [[E]], [[EasyLang]], [[ECL]], [[Ecstasy]], [[Egel]], [[EGL]], [[Eiffel]], [[Ela]], [[Elan]], [[Elena]], [[Elixir]], [[Elm]], [[Emacs Lisp]], [[EMal]], [[Erlang]], [[Euphoria]], [[Extended BrainF***]], [[Factor]], [[Falcon]], [[FALSE]], [[Fe]], [[Fexl]], [[FOCAL]], [[Forth]], [[Fortran]], [[Frege]], [[Frink]], [[FunL]], [[FutureBasic]], [[Gambas]], [[GAP]], [[GDScript]], [[Genie]], [[Gleam]], [[Go]], [[Go!]], [[Goboscript]], [[Golfscript]], [[Golo]], [[Gosu]], [[Groovy]], [[GUISS]], [[Halon]], [[Haskell]], [[Haxe]], [[HicEst]], [[HolyC]], [[Hoon]], [[Hope]], [[HQ9+]], [[Huginn]], [[HyperTalk]], [[IDL]], [[Idris]], [[Inform 6]], [[Inform 7]], [[Intercal]], [[Io]], [[Ioke]], [[J]], [[Jakt]], [[Janet]], [[Java]], [[JavaScript]], [[Joy]], [[Jsish]], [[Julia]], [[K]], [[Kabap]], [[Kitten]], [[Klingphix]], [[Klong]], [[Kotlin]], [[LabVIEW]], [[Lambda Prolog]], [[Lambdatalk]], [[Lang]], [[Lasso]], [[LDPL]], [[Lhogho]], [[Limbo]], [[Lingo]], [[Lisp]], [[LLVM]], [[Logo]], [[Logtalk]], [[LOLCODE]], [[Lua]], [[Lucid]], [[M4]], [[MACRO-11]], [[MAD]], [[Malbolge]], [[Maple]], [[MATLAB]], [[Maxima]], [[MAXScript]], [[MEL]], [[Mercury]], [[MiniScript]], [[MIPS Assembly]], [[Mirah]], [[Miranda]], [[ML-I]], [[Modula-2]], [[Modula-3]], [[Monkey]], [[MontiLang]], [[MOO]], [[MoonScript]], [[MUMPS]], [[N-t-roff]], [[Nanoquery]], [[NASL]], [[NATURAL]], [[Neko]], [[Nemerle]], [[NetRexx]], [[Nial]], [[Night]], [[Nim]], [[Nix]], [[NS-HUBASIC]], [[Nu]], [[Nutt]], [[OASYS]], [[OASYS Assembler]], [[Oberon-2]], [[Objeck]], [[Objective-C]], [[OCaml]], [[Octave]], [[Odin]], [[Oforth]], [[Ol]], [[Onyx]], [[OOC]], [[OpenEdge-Progress]], [[Openscad]], [[Order]], [[Oxygene]], [[Oz]], [[PARI-GP]], [[Pascal]], [[PascalABC.NET]], [[Perl]], [[Phix]], [[Phixmonti]], [[PHL]], [[PHP]], [[Picat]], [[PicoLisp]], [[Piet]], [[Pike]], [[PILOT]], [[PIR]], [[PL-I]], [[PL-M]], [[Plain English]], [[Pluto]], [[Pointless]], [[Pony]], [[Pop11]], [[PostScript]], [[Potion]], [[PowerShell]], [[Processing]], [[ProDOS]], [[Prolog]], [[Python]], [[Q]], [[QB64]], [[Qore]], [[Quackery]], [[Quill]], [[Quite BASIC]], [[R]], [[Ra]], [[Racket]], [[Raku]], [[RapidQ]], [[Rascal]], [[Raven]], [[Rebol]], [[Red]], [[Refal]], [[Relation]], [[Retro]], [[REXX]], [[Rhombus]], [[Ring]], [[Rockstar]], [[RPG]], [[RPL]], [[RPL-2]], [[Ruby]], [[Rust]], [[S-BASIC]], [[Sather]], [[Scala]], [[Scheme]], [[Scratch]], [[Seed7]], [[SenseTalk]], [[SequenceL]], [[Set lang]], [[SheerPower 4GL]], [[Shen]], [[Shiny]], [[Sidef]], [[Simula]], [[SkookumScript]], [[Slate]], [[Slope]], [[Smalltalk]], [[SmileBASIC]], [[SNOBOL4]], [[SNUSP]], [[SparForte]], [[Sparkling]], [[SQL]], [[Squirrel]], [[Standard ML]], [[Stata]], [[Stax]], [[Suneido]], [[SuperCollider]], [[SuperTalk]], [[Swift]], [[Symsyn]], [[Tailspin]], [[Tcl]], [[Thyrd]], [[TIScript]], [[TMG]], [[TorqueScript]], [[Transd]], [[TUSCRIPT]], [[TXR]], [[TypeScript]], [[Uiua]], [[UNIX Shell]], [[UnixPipes]], [[Unlambda]], [[Ursa]], [[Ursala]], [[UTFool]], [[Uxntal]], [[V]], [[V (Vlang)]], [[Vala]], [[VBA]], [[VBScript]], [[Vedit macro language]], [[Verbexx]], [[Verilog]], [[Visual Prolog]], [[Viua VM assembly]], [[Vox]], [[VTL-2]], [[Wart]], [[Whenever]], [[Whitespace]], [[Wortel]], [[Wrapl]], [[Wren]], [[X10]], [[X86 Assembly]], [[XBS]], [[Xojo]], [[XPL0]], [[XSLT]], [[Yabasic]], [[Yacas]], [[YAMLScript]], [[Yorick]], [[Z80 Assembly]], [[Zig]]

## Contradictions
- None — reference task page.
