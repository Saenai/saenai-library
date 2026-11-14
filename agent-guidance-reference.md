# Agent guidance reference

> Reusable reference text, not active instructions for this repository. Apply it only when explicitly selected or copied into an instruction file.

## Style Guide

### General Principles

- Keep code in one function unless separation provides genuine reuse or composition.
- Validate unknown values once at their owning boundary. Pass typed values inward; do not repeat checks for guarantees already established by schemas, constructors, or internal types.
- Do not extract single-use helpers prematurely. Keep logic inline unless extraction enables reuse, isolates a complex boundary, or gives the caller a meaningful name.
- For speculative or extremely unlikely race conditions or security edge cases, explain the concrete failure, likelihood, and complexity cost, and obtain the user's agreement before adding complexity. Do not expand scope for theoretical robustness without agreement.
- Avoid `try`/`catch` where possible.
- Reduce unnecessary variables by inlining intermediate values used only once.

### Complex Logic

- When validation branches or supporting details obscure a function, keep its main path clear and move supporting details into small helpers.
- Place helpers near the code they support, below the main export when that improves readability.
- Do not split simple expressions into many single-use helpers. Extract only when doing so represents a meaningful concept.
- Comment on non-obvious constraints and surprising behavior, not routine assignments or control flow.

### No defensive code, no speculative legacy

- Implement what the currently valid execution path requires. Do not introduce error handlers, fallbacks, retries, or input checks for cases excluded by existing contracts. Rely on framework guarantees and internal types. Validate at system boundaries, including user input, external APIs, and untrusted I/O.
- Do not introduce backward-compatibility layers, migration shims, or alternative execution paths for hypothetical breakage. Retain older formats when required by persisted data, released behavior, external consumers, or an explicit user request. Unreleased versions from the same development cycle are drafts rather than established contracts.

## Testing

- Minimize mocks. Avoid `globalThis.*` unless it is the only viable option.
- Test the actual implementation instead of duplicating its logic in tests.

## Scope discipline

- Implement only the requested work. Do not introduce additional features, unsolicited UX improvements, or unrelated refactoring. Mention unrelated issues in the final report rather than changing them.
- If the request is ambiguous, choose the simplest valid interpretation, record the assumption in the final report, and proceed. Ask only when competing interpretations differ substantially in effort (at least twofold).
- If the requested approach appears mistaken, explain the concern briefly, suggest an alternative, and leave the decision to the orchestrator. Do not change direction silently.
- Leave unexpected worktree changes made by others untouched unless they directly conflict with the task. Report such conflicts and complete whatever work remains possible.

## Independent judgment

In discussion and decisions, think independently. Test consequential assumptions, give a clear recommendation with reasons, and raise material concerns or better alternatives even when the user favors another option. Distinguish exploratory questions from clear requests to act; do not treat discussion alone as authorization. Once a direction is decided, execute within scope without reopening settled decisions or adding unnecessary checks or friction. Revise your view when evidence warrants it; do not disagree merely for the sake of disagreeing.
