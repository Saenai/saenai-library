# 0001. Fail the build job when the activity report is empty

## Context

An empty report passes the `build` job and is rejected only by `validate`, after an empty `activity-report` artifact has been published ([As-Is design](../design/activity-report.design.md)). Requirement [R1](../../requirements/report-validation.md) asks for the failure to happen in `build`, before upload.

## Decision

`build-report.sh` exits with code 3 and prints `No active records` when the report it wrote is empty. Details are in the [To-Be design](../design/reject-empty-report.design.md).

## Consequences

- No empty artifact is published. The run fails one job earlier, with a message that names the cause.
- Exit code 3 becomes part of the script's interface. Any other caller of the script has to handle it.
- `validate` repeats the check on the normal path. It stays because R3 fixes the job structure.

## Alternatives Considered

- **Keep `validate` as the only check.** An empty artifact is still published before the run fails; R1 rules this out.
- **Add a check step to the workflow after `Build report`.** Meets R1, but the error rule would live outside the script, so running the script by hand would still accept an empty report.
