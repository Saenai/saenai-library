# tech-docs kit

An Agent Skill for technical Markdown documents that a person can read quickly and an agent can use reliably: designs (As-Is and To-Be), runbooks, ADRs, references and READMEs.

## Install

Copy `.agents/skills/tech-docs/` into the work repository:

| Agent | Location |
| --- | --- |
| Codex, or another agent that reads `.agents/skills/` | `<repo>/.agents/skills/tech-docs/` |
| Claude Code | `<repo>/.claude/skills/tech-docs/` |

If the agent does not discover skills, start the task with: `Read .agents/skills/tech-docs/SKILL.md and follow it.`

## Use

Say what you need and where the source is. The skill picks the document type and the output path; name them yourself to override.

```text
Use $tech-docs. Write an As-Is design for .github/workflows/build.yml and scripts/build.sh.
```

```text
Use $tech-docs. Write a To-Be design for the change in docs/requirements/publish-change.md.
```

```text
Use $tech-docs. Write a runbook for re-running the nightly export after a failure.
```

```text
Use $tech-docs. Review docs/design/build.design.md and list what to fix.
```

In Claude Code, use `/tech-docs` instead of `$tech-docs`.

## Check documents

```bash
python .agents/skills/tech-docs/scripts/check_doc.py docs/
```

It reports broken links, line ranges past the end of a file, missing anchors, leftover placeholders, unknown Mermaid diagram types, and missing or misordered sections for the document type. Whether the content is right is for review to decide.

## What is inside

| Path | Contents |
| --- | --- |
| `SKILL.md` | Workflow and choice of document type |
| `references/writing.md` | Rules for every document |
| `references/types/` | One file per type: purpose, skeleton, what to leave out |
| `references/shell-workflow.md` | What to look for in Shell scripts and CI workflow YAML |
| `references/diagrams.md` | When to draw, and which Mermaid diagram |
| `examples/sample-repo/` | A small repository with a finished document of each main type |
| `scripts/check_doc.py` | Structural checker (Python 3.8+, standard library only) |

To adapt it to your team, edit the examples first. Agents copy the examples more faithfully than they follow rules.

If your organization requires a fixed template (Word, Excel), write the Markdown first and transfer the content.
