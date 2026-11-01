# Runbook

Step-by-step instructions for a task: running a job, recovering from a failure, rotating a credential. Written for someone doing it now, possibly under pressure.

File: `docs/runbooks/<name>.runbook.md`

Example: [activity-report.runbook.md](../../examples/sample-repo/docs/runbooks/activity-report.runbook.md)

## Skeleton

The first four sections are required, in this order. `Undo` is required when a step changes data or deploys something.

```markdown
# {{Task}} — Runbook

{{One or two sentences: what this achieves and when to use it.}}

## Before you start
## Steps
## Check the result
## Troubleshooting
## Undo
```

## Sections

**Before you start.** Access, tools and inputs needed, and conditions under which the reader should not proceed. A short list.

**Steps.** Numbered, one action per step. The exact command (in a code block) or UI path, then what the reader should see. A decision point is its own step: "If X, go to step 6." Start an irreversible step with **Irreversible:**.

**Check the result.** How to tell it worked: commands and the expected output.

**Troubleshooting.** Table: symptom, likely cause, action. Only causes the source or real experience supports.

**Undo.** How to reverse each step that changes something, or what to do instead when it cannot be reversed. If nothing changes outside the run, say so in one line under Troubleshooting and leave this section out.

## Leave out

Background and design explanation (link the design), steps the stated access does not allow, and "contact the administrator" without saying who and with what information.
