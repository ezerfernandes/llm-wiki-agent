---
title: "XML/Input (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, xml, parsing, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/XML/Input
---

## Summary
This task asks the programmer to parse a given XML fragment of student records and extract the list of student names from the `Name` attribute of each `<Student>` element. The key insight is that names should be read from attributes (not element text), and the solution must correctly decode XML character entities (e.g. `&#x00C9;` → É) so accented names like "Émily" round-trip properly.

## Task Requirements
- Parse the supplied `<Students>` XML fragment using any available method.
- Extract each student's name from the `Name` attribute on every `<Student>` element.
- Produce the output list: April, Bob, Chad, Dave, Émily.
- Handle nested child elements (e.g. a `<Pet>` inside a `<Student>`) without confusing them for students.
- If XPath is the only viable approach, the reader is referred to the companion task XML and XPath.

## Language Coverage
87 languages implement this task, a broad cross-section spanning systems, scripting, and functional languages, including C, C++, C#, Java, Python, Perl, Ruby, Go, Haskell, Racket, Rust, and Tcl. Approaches range from dedicated DOM/SAX parsers and XPath queries to lightweight regex extraction.

## Connections
- [[XmlParsing]] — the core technique of reading structured XML
- [[XPath]] — a common query method for selecting attribute values
- [[CharacterEncoding]] — decoding XML entities such as `&#x00C9;`
- [[DocumentObjectModel]] — tree-based representation many solutions traverse
- [[StringProcessing]] — regex-based alternatives to full parsing

## Contradictions
- None — reference task page.
