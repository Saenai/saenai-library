# Writing rules

These apply to every document type.

## What to write

**Write what the source cannot say.** People and agents can read the code. A document earns its place with what the code does not show directly:

- intent: what this is for, and what it deliberately does not do
- contracts at boundaries: what passes between caller and callee, job and job, system and system
- behavior that is easy to miss: truncating writes, skipped steps, exit codes that later steps rely on
- how to operate it, and what to do when it fails
- decisions and their reasons, when known

Do not restate code line by line. Link to it.

**Size follows risk and non-obviousness, not source length.** A 10-line script that deletes production data needs more than a 500-line formatter.

**Never invent.** Behavior, defaults, reasons, business rules, test results and approvals come from the source, the requirements, or something actually run. If a needed fact is missing, record it as an open question (in the document's Open Questions section if the type has one, otherwise in your hand-off reply); do not fill the gap with a plausible guess.

## Basis and uncertainty

State the basis once, near the top: what was read, and what, if anything, was run. For example: `Basis: source as of this commit; scripts not executed.`

Everything not otherwise marked then rests on that basis. Do not repeat it per statement, and do not write disclaimers about what the document does not claim. Mark only the specific statements that rest on something weaker (documentation of an action you could not read, an inference), and collect real unknowns in one place.

## Shape

**Lead with the answer.** The first screen tells the reader what this is, what it does or changes, and the one thing they most need to know.

**Headings** name what the section contains. A section should make sense to someone who arrives at it from a link.

**Tables** are for lookup: many items with the same attributes. Keep cells short: a value, a name, a phrase. If a cell needs a full sentence with a clause, use a list or a paragraph instead. About five columns at most.

**Numbered lists** for steps in order, **bullets** for unordered items, **paragraphs** for reasons and trade-offs, **code blocks** for commands, config and output the reader will copy or compare.

**Diagrams** only where a relationship (order, branching, dependency, state) is easier to see than to read. See [diagrams.md](diagrams.md).

**Bold** only what a skimming reader must not miss.

## Words

- Exact identifiers in backticks: `REPORT_DIR`, `needs: build`, `exit 3`.
- Name things. Avoid "it", "this step", "the above" when the referent is not in the same sentence.
- One term per concept throughout. Define a domain term at first use.
- Short, direct sentences. Present tense for behavior. "Must" only for real requirements.
- English. Identifiers, paths, commands and messages exactly as in the source.

## Links

- Link to source with paths relative to the document. Add a line range when pointing at specific behavior: `[build-report.sh](../../scripts/build-report.sh#L7-L10)`.
- Link instead of copying. Each fact (a schema, a parameter list, a requirement) has one home; other documents link to it.

## Leave out

- Self-assessment and compliance statements ("all behaviors are covered", quality-gate tables).
- Narration of your own process ("I inspected…", "this document does not assume…").
- Generic risks and advice not tied to this system.
- Recommendations in an As-Is document, unless the user asked for them.
- Document status, approvals, revision history: Git and pull requests hold those.
- Secret values. Refer to a secret by its name and role.
- Placeholders and TODOs. Write `None.` for a required section that is genuinely empty.
