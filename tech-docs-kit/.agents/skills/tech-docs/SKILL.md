---
name: tech-docs
description: Write or review technical Markdown documents in English (designs As-Is or To-Be, runbooks, ADRs, references, READMEs) grounded in the repository's source. Use when asked to document, design, specify or explain code, Shell scripts, CI workflows or a planned change, or to review such a document.
---

# Technical documents

The deliverable is a `.md` file in the repository, not a chat reply.

## 1. Pick the type

Choose by what the reader needs to do after reading. An explicit type or path from the user wins.

| Reader needs to… | Type | Default path |
| --- | --- | --- |
| understand how a component works, or what a change will do | [design](references/types/design.md) | `docs/design/<name>.design.md` |
| carry out a task or recover from a failure | [runbook](references/types/runbook.md) | `docs/runbooks/<name>.runbook.md` |
| know why a choice was made and what it costs | [adr](references/types/adr.md) | `docs/adr/NNNN-<decision>.md` |
| look up parameters, config keys, env vars, formats | [reference](references/types/reference.md) | `docs/reference/<name>.reference.md` |
| get oriented in a repository or directory | [readme](references/types/readme.md) | `README.md` in that directory |

If a request mixes needs, write the main document and link to the others (or offer them) rather than merging them into one.

## 2. Read

- Always: [writing.md](references/writing.md) and the type file.
- Shell scripts or CI workflow YAML: [shell-workflow.md](references/shell-workflow.md).
- Before drawing: [diagrams.md](references/diagrams.md).
- The finished example of the type in [examples/sample-repo/](examples/sample-repo/), if there is one. Match its density and tone.

## 3. Inspect

Read the target, and the things that call it or that it calls, as far as they affect what the reader needs. Read the requirements if any are given.

Do not run business scripts, trigger CI, deploy, or change source unless the user asks. Harmless local checks (syntax checks, running a script against a temporary test file) are fine when the user allows commands; name them in the document's Basis line.

## 4. Write

Follow the type's skeleton. Write for a reader who has the repository but not this conversation.

When a fact the reader needs cannot be established (a business rule, an external system's behavior, a missing requirement), do not guess: record it as an open question and finish the rest.

## 5. Check

- If Python is available, run `python <skill-dir>/scripts/check_doc.py <file>` and fix what it reports.
- Reread as the reader. Could they do what they came for without asking you? Is there anything they would skip? Cut it.

## 6. Hand off

Reply with the file path, what you read and ran, and any open questions.

## Reviewing a document

Check it against writing.md, its type file, and the source it describes. Report findings as `location — problem — fix`, most important first. Do not rewrite it unless asked.

## Updating a document

Keep structure and wording that are still correct. Fix what the source change made wrong; delete what no longer applies.
