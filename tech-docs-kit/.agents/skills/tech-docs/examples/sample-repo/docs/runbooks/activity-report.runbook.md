# Run the Activity Report — Runbook

Produce the `activity-report` artifact from `data/records.csv`, and fix the common failures. How it works: [design](../design/activity-report.design.md).

## Before you start

- You can run workflows in this repository's Actions.
- `data/records.csv` on the branch you will run from contains the records you want reported.
- For the commands below: GitHub CLI (`gh`), signed in to this repository. The web UI works too.

## Steps

1. Start the workflow, from **Actions → Activity report → Run workflow**, or:

   ```bash
   gh workflow run activity-report.yml --ref main
   ```

2. Follow the run until it finishes:

   ```bash
   gh run watch
   ```

   Both jobs, `build` and `validate`, should end green. If one fails, go to [Troubleshooting](#troubleshooting).

3. Download the report into the current directory:

   ```bash
   gh run download --name activity-report
   ```

## Check the result

`report.txt` holds one ID per line. Its line count should match the number of `active` rows in the CSV:

```bash
wc -l < report.txt
awk -F, 'NR > 1 && $2 == "active"' data/records.csv | wc -l
```

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| `build` fails at **Build report** with `Cannot read input` | `data/records.csv` is missing on that branch | run again with the right `--ref` |
| `build` fails at **Publish report** with "No files were found" | the script did not write `report.txt` | read the **Build report** log above the error |
| `validate` fails at **Require nonempty report** | no row has status exactly `active` (case and spaces count) | fix the data, commit, run again |
| `validate` is skipped | `build` failed | fix `build` first |

The workflow changes nothing outside the run, so it is always safe to run it again.
