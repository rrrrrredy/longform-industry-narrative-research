# Postmortem Lessons

These lessons came from a long AI company narrative research project.

## What Worked

- State files and registries prevented context loss.
- Company-by-company stages improved quality.
- Subagent audits caught coverage and evidence problems.
- Podcast and interview materials were most useful when treated as narrative translation, not factual summaries.
- WeChat and Chinese longform pieces were valuable because they showed how global narratives were reinterpreted locally.
- A final reader-facing rewrite dramatically improved publishability.

## What Failed Or Was Risky

- Too much process scaffolding leaked into the article.
- The task drifted toward system design and agent architecture before being corrected.
- Overusing "source/material/user provided" made the article sound like an assistant report.
- Evidence caveats became repetitive and weakened the author's judgment.
- Large source registries were useful backstage but unreadable as final appendices.
- Trying to complete the whole report in one pass reduced quality.

## User Preference Pattern

For this kind of work, the preferred output is:

- long, detailed, analytical
- company-by-company or section-by-section
- conclusion-first
- strong thesis and main line
- no visible citation IDs in body
- no process explanations
- no prompt-engineering or system-design drift
- references grouped by reader-facing categories

## Method Pattern

Use a two-layer system:

1. Research backend: sources, claims, uncertainty, logs, review.
2. Publishing frontend: thesis, argument, company analysis, readable references.

The backend makes the article reliable. The frontend makes it worth reading.
