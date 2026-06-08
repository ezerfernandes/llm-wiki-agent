---
title: "Bitmap/PPM conversion through a pipe (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, inter-process-communication, image-format]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitmap/PPM_conversion_through_a_pipe
---

## Summary
This task builds on the raster-image storage type and the PPM-writing routine from earlier Rosetta Code tasks, asking the programmer to produce a JPEG file without writing a JPEG encoder. The trick is to spawn an external conversion utility as a child process and stream raw PPM bytes into its standard input through a pipe; the utility writes out the JPEG. The key insight is delegating format conversion to existing command-line tools rather than implementing the JPEG codec directly.

## Task Requirements
- Reuse the in-memory bitmap storage type defined in the Basic bitmap storage task.
- Reuse the `output_ppm` function (from the Write ppm file task) to emit PPM image data.
- Launch an external conversion utility as a subprocess and connect to it via a pipe.
- Feed the PPM output into the utility's stdin so it produces a JPEG file as output.
- Suggested utilities include `cjpeg` (jpeg-progs), `ppmtojpeg` (netpbm), or `convert` (ImageMagick).

## Language Coverage
20 languages implement this task, spanning systems and scripting languages with strong subprocess/pipe support. Representative implementations include C, Go, Python, Perl, Ruby, OCaml, Racket, Kotlin, Nim, and Tcl.

## Connections
- [[InterProcessCommunication]] — the core mechanism: streaming bytes between processes
- [[UnixPipes]] — the conduit connecting the program's output to the converter's stdin
- [[SubprocessManagement]] — spawning and feeding an external child process
- [[PortablePixmapFormat]] — the intermediate PPM representation being piped
- [[RasterGraphics]] — the bitmap storage model underlying the task

## Contradictions
- None — reference task page.
