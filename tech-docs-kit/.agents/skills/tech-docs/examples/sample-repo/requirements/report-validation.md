# Requirement: reject empty activity reports

- R1: If no record is selected, report generation must fail in the `build` job, before the artifact is uploaded.
- R2: In that case `build-report.sh` must exit with status 3 and print `No active records` to stderr.
- R3: The selection rule, output file name, artifact name, trigger and job structure stay as they are.
