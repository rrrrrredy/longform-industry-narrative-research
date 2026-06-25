---
name: longform-industry-narrative-research
description: Long-form, source-backed industry research and publishable writing workflow for AI agents. Use when an agent must plan, collect, verify, analyze, draft, revise, or finalize a substantial industry, market, company, product, technology, policy, or ecosystem research article/report from many sources over multiple stages. Supports state files, source/claim/uncertainty registries, staged drafting, optional analysis lenses such as narrative analysis or horizontal-vertical analysis, subagent review, reader-quality revision, and removal of process/audit language from final Chinese or English prose. Do not use for quick factual answers, simple summaries, citation formatting only, or purely creative writing.
---

# Longform Industry Research and Writing

Use this agent skill for long, evidence-backed research writing where the deliverable is a publishable article or report, not a process diary. The method is general: choose the analytical lens that fits the question instead of forcing every project into a narrative-analysis frame.

## Non-Negotiable Rules

1. State the research objective, target reader, scope, output format, and evidence standard before deep work.
2. Persist task state in files when the task is long, multi-stage, or likely to exceed one session.
3. Keep the research backend separate from the final prose.
4. Distinguish verified facts, source claims, interpretations, uncertainty, and author judgments.
5. Work in staged cycles: plan, collect, analyze, draft a section, review, revise, then continue.
6. Do not generate the whole article in one pass when the project is complex.
7. Do not let internal process language leak into the final article.
8. Treat interviews, podcasts, social posts, market data, and media reports as optional source types, not mandatory categories.
9. Use subagents only for separable research, adversarial review, evidence checks, or reader review; do not let them replace the main argument.
10. After each review, route findings into concrete revision actions.

## Workflow

### 1. Frame The Task

Write a short task specification:

- research question
- target reader
- intended output and language
- required coverage
- out-of-scope claims
- evidence standard
- likely source categories
- draft structure
- completion criteria

If the work drifts into system design, prompt engineering, or workflow documentation when the requested deliverable is an article/report, restate the writing objective and return to the research plan.

### 2. Build The Research Backend

For substantial work, maintain:

- `state/task_spec.md`
- `state/progress.json`
- `state/findings.jsonl`
- `state/directions_tried.json`
- `state/iteration_log.jsonl`
- `logs/work.jsonl`
- `data/source_registry.csv`
- `data/claims_registry.csv`
- `data/uncertainty_registry.csv`

These files support recovery and verification. They are not the final article.

### 3. Collect And Classify Sources

Collect sources according to the topic. Possible categories include:

- official materials: websites, product pages, docs, reports, filings, speeches
- primary data: financials, usage data, benchmarks, repositories, datasets
- expert materials: papers, technical reports, interviews, talks, podcasts
- media and industry analysis: news, newsletters, trade press, analyst reports
- market and capital materials: investor memos, pricing, funding, app intelligence
- user and community evidence: forums, reviews, GitHub issues, social posts
- counter-evidence: failures, lawsuits, churn, backlash, adoption limits, criticism

Record source limitations and access failures backstage. Do not cite inaccessible material as substantive evidence.

### 4. Analyze In Units

Choose analysis units that fit the assignment: company, product, market segment, technology, policy regime, actor, period, or case.

For each unit, create an analysis card:

1. Context and timeline: what changed, when, and why it matters.
2. Current position: what role the unit occupies in the market, ecosystem, policy debate, or user workflow.
3. Mechanism: what converts the unit's actions into external effects.
4. Evidence: facts and source claims that support the analysis.
5. Counter-evidence and boundary: what weakens, narrows, or complicates the claim.
6. Implication: what a reader should conclude or do differently.

Use a narrative lens only when the research question is about framing, meaning-making, legitimacy, media translation, category creation, or belief formation.

### 5. Draft In Sections

Draft section by section. For each section:

1. write the local thesis
2. select only the evidence needed for that thesis
3. explain mechanisms before listing details
4. include counter-evidence where it changes the judgment
5. remove process language before moving on

Assemble the report around the argument, not around source collection order.

### 6. Review And Revise

Run staged review before final delivery:

- evidence review: unsupported claims, weak sources, inaccessible materials
- coverage review: missing required actors, topics, periods, or regions
- structure review: argument flow, section order, duplicated ideas
- skeptical review: company PR, media hype, or investor framing mistaken for reality
- reader review: clarity, cognitive load, continuity, and publishable quality

Reader review happens after factual/coverage review. It should improve reading experience without introducing new facts.

### 7. Finalize The Article

The final article/report should include only reader-facing material:

- conclusion-first core insights when useful
- clear scope note
- analytical sections organized by the chosen structure
- synthesis across cases or units
- counter-evidence and uncertainty expressed as part of the argument
- clean references or bibliography
- completion note only if the user requests it

Do not show source IDs, audit labels, file paths, or phrases such as "the user provided", "the material shows", "this source supplements", or "the audit passed" in final prose.

## When To Read References

- Read `references/research-workflow.md` before starting or restarting a complex project.
- Read `references/optional-analysis-lenses.md` when choosing methods such as narrative analysis, horizontal-vertical analysis, adoption analysis, capital analysis, or counter-case analysis.
- Read `references/horizontal-vertical-analysis.md` only after the horizontal-vertical lens has been selected.
- Read `references/subagents-and-review-loop.md` before delegating work or running audits.
- Read `references/writing-style.md` before drafting, rewriting, or finalizing.
- Read `references/quality-gates.md` before declaring a stage or final deliverable complete.
- Read `references/postmortem-lessons.md` when adapting this skill or diagnosing why a long research task drifted.

## When Not To Use

Do not use this skill for:

- quick factual answers
- short summaries of one document
- citation cleanup only
- spreadsheet-only data cleaning
- live news briefs without synthesis
- purely creative essays without source discipline
- tasks where the user wants code, dashboards, or automation rather than a research article/report

## Expected Outputs

Depending on task size, produce some or all of:

- task specification
- source and claim registries
- uncertainty list
- staged research notes
- section drafts
- review logs with routed actions
- final publishable article/report
- reader-facing reference appendix
- completion report with remaining limitations
