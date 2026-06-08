---
title: "Validate International Securities Identification Number (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, checksum, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Validate_International_Securities_Identification_Number
---

## Summary
The task asks the programmer to write a function that validates an ISIN (International Securities Identification Number), the unique identifier for financial securities such as stocks and bonds. A string is valid only if it matches the required 12-character format AND its embedded checksum is correct. The key insight is that letters are first transcribed to digits via base-36-to-base-10 conversion, after which a standard Luhn check verifies the resulting numeric string.

## Task Requirements
- Accept a string and return a Boolean indicating whether it is a valid ISIN.
- Enforce the format: 2-character ISO country code (A-Z), 9-character security code (A-Z, 0-9), and 1 checksum digit (0-9) — 12 characters total.
- Any 2-character alphabetic sequence may be assumed to be a valid country code.
- Validate the checksum by replacing each letter with its base-36 numeric value (A=10 ... Z=35), then running the Luhn test on the resulting base-10 digit string.
- Reuse of an existing Luhn-test implementation is permitted (noted via comment).
- Pass all listed test cases (e.g. US0378331005 valid, US0373831005 invalid, AU0000XVGZA3 valid, FR0000988040 valid).

## Language Coverage
66 languages implement this task, spanning systems, scripting, functional, and database/SQL dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Perl, Raku, COBOL, and SQL PL.

## Connections
- [[LuhnAlgorithm]] — the checksum step is a Luhn modulus-10 test on the transcribed digits.
- [[Base36]] — letters are converted from base 36 to base 10 before checksum validation.
- [[Checksum]] — ISIN embeds a check digit to detect transcription errors.
- [[StringValidation]] — format constraints are verified before the numeric check.
- [[RegularExpressions]] — many solutions use a regex to enforce the country/security/check-digit pattern.

## Contradictions
- None — reference task page.
