# Reject Empty Activity Reports — Design (To-Be)

Source: [build-report.sh](../../scripts/build-report.sh), [activity-report.yml](../../.github/workflows/activity-report.yml)
Requirements: [report-validation.md](../../requirements/report-validation.md)
Basis: source as of this commit and the requirements. The change is not implemented yet.

## Summary

`build-report.sh` will exit with code 3 when no row is selected, so an empty report stops the `build` job before upload instead of being caught later by `validate`. Everything else stays as described in the [As-Is design](activity-report.design.md).

| Case | Before | After |
| --- | --- | --- |
| No `active` row | `build` succeeds and uploads an empty report; `validate` fails | `build` fails with exit 3; no upload; `validate` skipped |
| At least one `active` row | report uploaded and validated | unchanged |

## Context

- R1 and R2 require the failure inside `build`, before upload, with exit 3 and `No active records` on stderr.
- R3 keeps the selection rule, file name, artifact name, trigger and job structure.
- Only `build-report.sh` changes. The workflow file does not.

## Interfaces

| Name | Before | After |
| --- | --- | --- |
| exit `3` | — | no row selected |
| stderr | `Cannot read input: <path>` with exit 2 | also `No active records` with exit 3 |

Other interfaces are unchanged.

## Behavior

| ID | Condition | Behavior |
| --- | --- | --- |
| B1 | `report.txt` is empty after `awk` | print `No active records` to stderr, exit 3 |
| B2 | `report.txt` is not empty | exit 0, as today |

Append to the end of `build-report.sh`, after the `awk` line ([L13](../../scripts/build-report.sh#L13)):

```bash
if [[ ! -s "$output_dir/report.txt" ]]; then
  printf 'No active records\n' >&2
  exit 3
fi
```

On exit 3, the `Build report` step fails, `Publish report` is skipped, and `validate` is skipped through `needs: build`. The empty `report.txt` stays under `runner.temp` and is discarded with the runner.

## Decisions

- **Fail in the script, not in a separate workflow step.** See [ADR 0001](../adr/0001-fail-empty-report-in-build.md).
- **Test the written file with `-s` rather than counting matches inside `awk`.** It keeps the selection rule and the error rule apart, and uses the same condition as `validate`.
- **Keep `validate`.** R3 fixes the job structure. After the change it is a second check on the downloaded artifact.

## Verification

| Check | Covers | Expected | Status |
| --- | --- | --- | --- |
| Run the script on a CSV with no `active` row | B1 | exit 3; stderr `No active records` | Planned |
| Run it on `data/records.csv` | B2 | exit 0; `report.txt` is `A100`, `A102` | Planned |
| Run it with a path that does not exist | — | exit 2, as today | Planned |
| Dispatch the workflow with no `active` row | B1 | `build` fails at `Build report`; upload and `validate` skipped | Planned |

## Open Questions

None.
