---
title: "chmod"
type: concept
tags: [unix, security, permissions, command-line]
sources: [dis-app2-7-permissions]
last_updated: 2026-05-18
---

# chmod

**`chmod`** (*change mode*) mutates the [[FilePermissions|rwx × ugo permission bits]] on a file or directory. Per [[dis-app2-7-permissions|DIS Appendix 2.7]], it accepts two equivalent notations.

## Octal notation

A three-digit number; each digit is one principal category (u, g, o); each digit is the sum `4r + 2w + 1x`.

| Decimal | Bits | Meaning |
|---|---|---|
| 7 | `rwx` | read + write + execute |
| 6 | `rw-` | read + write |
| 5 | `r-x` | read + execute |
| 4 | `r--` | read only |
| 0 | `---` | none |

```bash
chmod 755 script.sh      # u=rwx g=r-x o=r-x
chmod 644 notes.md       # u=rw- g=r-- o=r--
chmod 700 ~/.ssh         # only owner can enter
```

## Symbolic notation

`<who><op><perm>` — *who* is one or more of `u g o a`; *op* is `+` add / `-` remove / `=` set; *perm* is one or more of `r w x`.

```bash
chmod u+w file           # grant write to owner
chmod o-r secret.txt     # remove read from others
chmod a+x deploy.sh      # grant execute to all
chmod g=rx project/      # set group exactly to r-x
```

Symbolic form is more readable (no octal arithmetic) and supports incremental edits.

## Related
- [[FilePermissions]] — the model `chmod` mutates.
- `chgrp` / `chown` — change the file's group / owner.
- [[UnixCommandLine]] — invocation context.
- [[DiveIntoSystems]] — Appendix 2.7.

## Sources
- [[dis-app2-7-permissions]] — DIS Appendix 2.7 *File Permissions and chmod*.
