## Subagent delegation

For every non-trivial task, automatically assess whether any bounded, lower-complexity work can be delegated effectively.
When subagent tools are available, delegate suitable independent and parallelizable sidecar work to `gpt-5.6-luna` without requiring a separate user request.
Use low reasoning effort for mechanical tasks and medium reasoning effort for scoped analysis unless the task clearly requires otherwise.
Good candidates include file inventories, pattern searches, documentation consistency checks, mechanical edits with a disjoint write scope, result tabulation, and independent verification.
Keep critical-path, tightly coupled, ambiguous, high-risk, architectural, and final decision-making work with the main agent.
Do not delegate when coordination overhead is likely to exceed the benefit, and do not duplicate delegated work locally.
Review subagent results before integrating or presenting them; the main agent remains responsible for correctness and the final answer.
