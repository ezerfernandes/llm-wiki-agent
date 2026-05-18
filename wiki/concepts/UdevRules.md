---
title: "Udev Rules"
type: concept
tags: [linux, udev, usb, device-management, embedded, permissions]
sources: [rust-embedded-book-intro-install-linux]
last_updated: 2026-05-16
---

# Udev Rules

User-space device-management rules consumed by the Linux **`udev`** subsystem (the device-node manager that runs under `systemd-udevd` on most modern distros). A rule is a single-line match-and-action statement in a `.rules` file under `/etc/udev/rules.d/` (system-local) or `/lib/udev/rules.d/` (distro-shipped); on every kernel `uevent` (device add / remove / change), udev iterates the rules and applies the matching ones to set the device node's name, symlinks, permissions, ownership, or environment.

For embedded development, udev rules are the canonical Linux mechanism for granting the logged-in user access to a USB debug probe **without `sudo`** — by matching `ATTRS{idVendor}` / `ATTRS{idProduct}` on the probe and tagging the node with `uaccess` (or, on older systems, assigning `GROUP="plugdev"` + `MODE="0660"`). The `uaccess` tag triggers `systemd-logind` to attach an ACL granting the seat-owning user read/write permission for as long as they're logged in, leaving the device root-owned but accessible.

The [[rust-embedded-book-intro-install-linux|Embedded Rust Book Linux install]] uses this exact pattern: a `70-st-link.rules` file matching the [[STLink|ST-LINK]] USB IDs (`0483:3748` and `0483:374b`) with `TAG+="uaccess"` so [[OpenOCD]] / [[ProbeRs]] can drive the probe as a normal user. After writing or editing a rules file, `sudo udevadm control --reload-rules` reloads the in-memory rule set; the device must then be unplugged and replugged so udev re-runs the match on the new uevent. Verification: `ls -l /dev/bus/usb/<bus>/<device>` shows a `+` in the permission string (ACL present), and `getfacl <path>` enumerates the per-user ACL entries.

## Connections

- [[rust-embedded-book-intro-install-linux]] — the source chapter that introduces udev rules in the wiki, via the `70-st-link.rules` file for the [[STM32F3DISCOVERY]].
- [[STLink|ST-LINK]] — the USB device the `70-st-link.rules` rule targets; udev rules are how every ST-LINK / [[JLink|J-Link]] / [[MCULink|MCU-Link]] / [[RustyProbe|Rusty-probe]] becomes user-accessible on Linux.
- [[OpenOCD]] / [[ProbeRs]] — the debug-server software that talks to the probe; the udev rule exists so these can run as a normal user.
- [[STMicroelectronics]] — vendor whose USB vendor ID (`0x0483`) appears in the rule's `ATTRS{idVendor}` match.

## See also

- `man udev` / `man 7 udev` — full rule syntax and semantics.
- `man udevadm` — the admin tool for inspecting devices (`udevadm info`), reloading rules (`udevadm control --reload-rules`), and replaying events (`udevadm trigger`).
