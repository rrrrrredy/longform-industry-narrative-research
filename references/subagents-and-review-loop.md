# Subagents And Review Loop

Use this file before delegating work or running audits.

## When To Use Subagents

Use subagents when work can be separated without losing the main argument:

- coverage audit across a large requirement list
- source discovery for distinct regions, companies, periods, or source types
- evidence-chain verification
- counterargument search
- reader-quality review after the draft is factually stable
- style cleanup on a bounded section

Do not use subagents to avoid doing the main synthesis. The main agent owns the thesis, structure, and final judgment.

## Useful Subagent Roles

### Requirement Mapper

Turns user requirements into a checklist with completion status and missing items.

### Source And Evidence Auditor

Checks whether important claims are supported, whether sources were actually accessed, and whether inaccessible sources were treated honestly.

### Coverage Auditor

Checks whether required companies, actors, regions, time periods, source categories, or themes are covered.

### Skeptical Reviewer

Finds hype, PR laundering, weak causal claims, overgeneralization, and missing counter-cases.

### Structure Reviewer

Checks whether the report has a clear thesis, section logic, non-duplicative flow, and an actual synthesis.

### Reader Critic

Runs only after factual and coverage audits. It evaluates readability, cognitive load, continuity, friction points, and research-report feel. It must not introduce new facts.

## Subagent Prompt Requirements

Each prompt should include:

- objective
- exact files or sections to inspect
- output format
- what counts as PASS or FAIL
- what the subagent must not do
- requirement to distinguish facts, source claims, interpretations, and suggestions

Avoid leaking the intended answer unless the task is pure compliance checking.

## Common Failure Modes

- Subagent pretends to verify sources it did not access.
- Subagent rewrites the main thesis instead of auditing the assigned scope.
- Subagent adds new requirements not requested by the user.
- Subagent summarizes instead of checking.
- Subagent marks PASS without listing evidence.
- Multiple agents edit the same file concurrently.

Mitigation:

- Give bounded inputs and bounded outputs.
- Ask for missing evidence and concrete revision actions.
- Require PASS/FAIL plus reasons.
- Route findings through the main agent before editing.
- Keep concurrent agents read-only unless the workflow explicitly supports separate output files.

## Review Loop

Use this loop after each major section and before final delivery:

1. Run the appropriate review role.
2. Convert review findings into a revision checklist.
3. Fix the draft or evidence registry.
4. Record what changed in `logs/review.jsonl`.
5. Re-run only the review dimension that failed.

Do not treat an audit report as the final deliverable. The audit exists to improve the article.

## Reader-Driven Revision

Trigger reader review after:

- data collection is complete enough for the current draft
- evidence and coverage audits have passed or remaining limitations are explicit
- an initial full draft exists

The Reader Critic scores:

- Reading Flow
- Cognitive Load
- Argument Continuity
- Research Report Quality

Allowed revisions:

- section order
- transitions
- paragraph density
- titles
- redundant explanations
- process-language cleanup
- clarity and rhythm

Disallowed revisions:

- inventing new facts
- changing evidence boundaries
- reopening source collection unless a separate evidence audit requires it
- replacing the author's thesis without explanation

Cap reader-driven revision at three cycles unless the user asks for more.
