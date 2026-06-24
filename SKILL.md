---
name: longform-industry-narrative-research
description: Long-form, source-backed industry narrative research and publishing workflow for AI agents. Use when an agent must research, structure, draft, revise, or finalize a substantial industry analysis essay or report, especially company-by-company narrative studies, AI/technology industry essays, cross-market narrative analysis, podcast/interview synthesis, source registry management, final-reader cleanup, and removing process/audit language from a publishable Chinese or bilingual longform article. Packaged in a Codex-compatible skill format, but the method is agent-agnostic.
---

# Longform Industry Narrative Research

Use this agent skill to produce publishable longform industry narrative research, not a process report. The workflow keeps evidence management in the background and makes the final article read as an author's analysis. It is packaged as a Codex-compatible skill, but the method can be used by any agent system that supports reusable instructions, references, state files, and staged review.

## Core Rule

Separate the backstage research system from the frontstage article.

- Backstage: source registry, claim registry, uncertainty list, logs, checkpoints, subagent audits, access failures.
- Frontstage: thesis, structure, company analysis, narrative mechanisms, counter-narratives, conclusions, reader-facing reference appendix.

Never let backstage language leak into the final article unless the user explicitly asks for an audit appendix.

## Workflow

1. Lock the article thesis and target reader before collecting more material.
2. Build source and claim registries, but do not write registry language into the article.
3. Process materials by usefulness: official self-narrative, podcast/interview, media translation, market/capital report, developer/community evidence, counter-narrative.
4. Draft company or topic blocks one at a time. Do not generate the whole article in one pass for complex work.
5. For each company or actor, use the five-part analysis card:
   - narrative history
   - current narrative position
   - construction and diffusion mechanism
   - external behavior change
   - counter-narrative and evidence boundary
6. Assemble the article around the main thesis, not around the order materials were collected.
7. Run a process-language cleanup pass before final delivery.
8. Build a reader-facing reference appendix: categories and titles only, no full audit table unless requested.

## Final Article Style

Write as the author, not as an assistant reporting work.

Avoid:
- "the user provided..."
- "the material shows..."
- "supplementary material..."
- "this report uses..."
- "evidence gap..."
- "source processing..."
- visible source IDs like `[S123]` in the body

Prefer:
- direct judgments
- explicit mechanisms
- clear causal chains
- restrained uncertainty language
- reader-facing structure

Good pattern:

`Company narrative -> product/interface/distribution mechanism -> behavior change -> system impact -> counter-narrative`

Bad pattern:

`I reviewed source X; source X supplements source Y; this material can support section Z.`

## Evidence Handling

Keep facts, company narratives, media interpretations, and author judgments separate.

- Official blogs define self-narrative; they do not prove adoption.
- Podcasts and interviews reveal framing and translation; they do not automatically prove facts.
- Media reports can show public framing; they need corroboration for hard data.
- Community threads show reception and counter-narratives; they are not representative market data.
- Rankings, downloads, traffic, pricing, ARR, valuation, and model benchmark claims need explicit confidence boundaries.

When a source is inaccessible, record it backstage and do not use it as substantive evidence.

## When To Read References

- Read `references/research-workflow.md` when planning or restarting a complex research project.
- Read `references/writing-style.md` before drafting, rewriting, or finalizing the article.
- Read `references/quality-gates.md` before declaring a stage or final article complete.
- Read `references/postmortem-lessons.md` when adapting the method, creating a new related skill, or doing a project retrospective.

## Deliverables

For large projects, maintain:

- `state/task_spec.md`
- `state/progress.json`
- `state/findings.jsonl`
- `data/source_registry.csv`
- `data/claims_registry.csv`
- `data/uncertainty_registry.csv`
- `logs/work.jsonl`
- a final article file
- a reader-facing reference appendix
- a completion report that separates completed work from residual boundaries

For a publishable final article, include:

- conclusion-first core insights
- short research scope note
- company/topic analysis blocks
- commonality and divergence synthesis
- media/podcast/translation mechanism
- global or cross-market synthesis when relevant
- counter-narrative section or integrated counter-narratives
- clean reader-facing reference appendix
