---
title: "Bitmap/Read an image through a pipe (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, interprocess-communication]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitmap/Read_an_image_through_a_pipe
---

## Summary
This task asks the programmer to load an arbitrary foreign image format into a simple in-memory bitmap data structure by piping the file through an external delegate conversion tool. Rather than parsing every image format directly, the program shells out to a utility such as ImageMagick's `convert`, `cjpeg`, or a netpbm tool, captures the converted output via a pipe, and reads it into the bitmap. The key insight is using PPM as a universal bridge format between the foreign encoding and the program's own minimal raster storage.

## Task Requirements
- Read an image file of some foreign format (e.g. JPEG, PNG) into the bitmap storage type.
- Use a delegate command-line tool (cjpeg, a netpbm utility, or ImageMagick `convert`) to perform the decoding.
- Communicate with that tool through a pipe rather than an intermediate file on disk.
- Reuse the PPM reading code (from the "Read ppm file" task) and the bitmap storage definition (from "Basic bitmap storage"), treating PPM as the bridge format.
- This is the inverse of the "PPM conversion through a pipe" task.

## Language Coverage
21 languages implement this task, a modest spread reflecting its reliance on external processes and OS pipe facilities. Representative implementations include C, Go, Python, Perl, Ruby, OCaml, Racket, Tcl, Lua, and Nim.

## Connections
- [[InterProcessCommunication]] — reading converted data through a pipe from a child process
- [[PipesAndStreams]] — the pipe mechanism that carries the converted bytes
- [[RasterGraphics]] — the bitmap storage being populated
- [[PPMFormat]] — the intermediate bridge format used between tools
- [[ImageMagick]] — a common delegate conversion utility

## Contradictions
- None — reference task page.
