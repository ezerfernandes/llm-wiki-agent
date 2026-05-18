---
title: "The Embedded Rust Book — Verify Installation"
type: source
tags: [rust, embedded, book-chapter, installation]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/intro/install/verify.md
---

# The Embedded Rust Book — Verify Installation

## Summary

File 9 of 44 of *[[TheEmbeddedRustBook|The Embedded Rust Book]]* — the **closing page of the intro chapter**, a one-shot end-to-end smoke test that confirms the per-OS install branches ([[rust-embedded-book-intro-install-linux|Linux]] / [[rust-embedded-book-intro-install-macos|macOS]] / [[rust-embedded-book-intro-install-windows|Windows]]) actually wired the [[STM32F3DISCOVERY]] board to the host. Procedure: Mini-USB into the "USB ST-LINK" connector (centered on the board edge), confirm the [[STLink|ST-LINK]] header is populated, then run `openocd -f interface/stlink.cfg -f target/stm32f3x.cfg`. The **pass signal** is the final `Info` line — `stm32f3x.cpu: hardware has 6 breakpoints, 4 watchpoints` — which proves the [[OpenOCD]] HLA/SWD transport enumerated the [[STLink|ST-LINK]] probe, reached the [[STM32F303VCT6]] core, and read its debug registers. Fallbacks for old hardware revisions (`interface/stlink-v2.cfg`, `interface/stlink-v2-1.cfg`); fallback for ACL problems (`sudo openocd …`, then fix [[UdevRules|udev rules]] on Linux).

## Key Claims

- **The pass criterion is one line of output.** Hardware contents may not match exactly across runs, but the final `hardware has 6 breakpoints, 4 watchpoints` line is necessary and sufficient: if present, move on; if absent, debug. Everything earlier in the banner ("Open On-Chip Debugger 0.10.0", "auto-selecting first available session transport hla_swd", "Target voltage: 2.919881", etc.) is informational.
- **`interface/stlink.cfg` is the modern OpenOCD config.** Old OpenOCD releases (including the 0.10.0 release from 2017) lacked the unified `interface/stlink.cfg` and required users to pick `interface/stlink-v2.cfg` (older F3 revision) or `interface/stlink-v2-1.cfg` (newer F3 revision) explicitly. Whichever cfg works also tells the user which hardware revision they have — relevant for later chapters.
- **Target config is fixed: `target/stm32f3x.cfg`.** Only the interface side varies across boards/probes; the target side stays anchored on the STM32F3 family for this book.
- **Permission failure is diagnostic.** If the command only works under `sudo` on Linux, the [[UdevRules|udev rule]] from [[rust-embedded-book-intro-install-linux]] is missing or wrong — running as root is a workaround, not the fix.
- **Termination is manual.** OpenOCD does not return — it blocks the console serving the GDB target. The user terminates the process after seeing the breakpoints line and proceeds to the next section (start/index).

## Key Quotes

> "You should get the following output and the program should block the console" — i.e. a successful `openocd` invocation is a long-running server, not a one-shot command.

> "The contents may not match exactly but you should get the last line about breakpoints and watchpoints."

> "If none of the commands work as a normal user then try to run them with root permission (e.g. `sudo openocd ..`). If the commands do work with root permission then check that the udev rules have been correctly set."

## Connections

- [[TheEmbeddedRustBook]] — file 9/44; closes the intro chapter as the smoke test that the install sub-chapters set up. Successor jumps to the `start/` chapter.
- [[rust-embedded-book-intro-install]] — the OS-agnostic install manifest this page validates.
- [[rust-embedded-book-intro-install-linux]] — sibling that defines the [[UdevRules|udev rule]] referenced as the Linux ACL fix.
- [[rust-embedded-book-intro-install-macos]] — sibling; no driver/udev step there, so the verify command should "just work" once [[OpenOCD]] is on `$PATH`.
- [[rust-embedded-book-intro-install-windows]] — sibling; on Windows the ACL-equivalent is the `stsw-link009` driver from [[STMicroelectronics]].
- [[OpenOCD]] — the binary invoked here; `hla_swd` transport, auto-selected.
- [[STLink|ST-LINK]] — the USB hardware probe enumerated by [[OpenOCD]] via the `interface/stlink*.cfg` files.
- [[STM32F3DISCOVERY]] — the dev board hosting both [[STLink|ST-LINK]] and target MCU.
- [[STM32F303VCT6]] — the target MCU whose debug registers expose the "6 breakpoints, 4 watchpoints" pass-signal.
- [[UdevRules]] — the Linux ACL mechanism referenced in the `sudo`-only failure path.
- [[SWD]] — the wire protocol auto-selected by [[OpenOCD]] (`hla_swd`) over the [[STLink|ST-LINK]] probe.

## Contradictions

- None. Strictly additive — operational end-of-intro checkpoint over the install trio. The page does not introduce new tools, only validates the prior ones.
