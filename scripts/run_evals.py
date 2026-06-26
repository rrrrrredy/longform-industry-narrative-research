#!/usr/bin/env python3
"""Run lightweight conformance checks for Industry Research Framework eval cases."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_REQUIRED_ARTIFACTS = [
    "state/task_spec.md",
    "state/progress.json",
    "data/source_registry.csv",
    "data/claims_registry.csv",
    "logs/review.jsonl",
    "final.md",
]

UNCERTAINTY_TERMS = [
    "不确定",
    "反证",
    "边界",
    "限制",
    "风险",
    "alternative explanation",
    "counter-evidence",
    "uncertainty",
    "limitation",
]

CLAIM_DISCIPLINE_TERMS = [
    "事实",
    "来源说法",
    "判断",
    "证据",
    "confidence",
    "source claim",
    "author judgment",
]


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def load_cases(cases_dir: Path) -> list[dict[str, Any]]:
    cases = [read_json(path) for path in sorted(cases_dir.glob("*.json"))]
    if not cases:
        raise FileNotFoundError(f"No eval cases found in {cases_dir}")
    return cases


def load_sources(evals_dir: Path) -> dict[str, dict[str, Any]]:
    sources_by_id: dict[str, dict[str, Any]] = {}
    for sources_file in (evals_dir / "source_packs").glob("*/sources.jsonl"):
        for row in load_jsonl(sources_file):
            sources_by_id[row["source_id"]] = row
    return sources_by_id


def contains_any(text: str, terms: list[str]) -> bool:
    text_lower = text.lower()
    return any(term.lower() in text_lower for term in terms)


def count_reader_references(final_text: str, source_ids: list[str], sources_by_id: dict[str, dict[str, Any]]) -> int:
    count = 0
    for source_id in source_ids:
        title = str(sources_by_id.get(source_id, {}).get("title", ""))
        if title and title in final_text:
            count += 1
    return count


def count_registry_sources(source_registry_text: str, source_ids: list[str], sources_by_id: dict[str, dict[str, Any]]) -> int:
    count = 0
    for source_id in source_ids:
        title = str(sources_by_id.get(source_id, {}).get("title", ""))
        if source_id in source_registry_text and (not title or title in source_registry_text):
            count += 1
    return count


def evaluate_case(
    case: dict[str, Any],
    run_dir: Path,
    sources_by_id: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    findings: list[str] = []
    score = 0
    max_score = 100

    required_artifacts = case.get("artifact_requirements") or DEFAULT_REQUIRED_ARTIFACTS
    artifact_results = {artifact: (run_dir / artifact).exists() for artifact in required_artifacts}
    artifact_score = round(25 * sum(artifact_results.values()) / len(artifact_results))
    score += artifact_score
    missing_artifacts = [name for name, ok in artifact_results.items() if not ok]
    if missing_artifacts:
        findings.append("Missing artifacts: " + ", ".join(missing_artifacts))

    final_text = read_text(run_dir / "final.md")
    if not final_text:
        findings.append("Missing final.md, so content checks could not run.")
        return {
            "case_id": case["case_id"],
            "score": score,
            "max_score": max_score,
            "status": "missing_output",
            "findings": findings,
            "artifacts": artifact_results,
        }

    section_hits = [section for section in case.get("required_sections", []) if section in final_text]
    if case.get("required_sections"):
        section_score = round(15 * len(section_hits) / len(case["required_sections"]))
    else:
        section_score = 15
    score += section_score
    if section_score < 15:
        missing = sorted(set(case.get("required_sections", [])) - set(section_hits))
        findings.append("Missing expected sections or headings: " + ", ".join(missing))

    entity_hits = [entity for entity in case.get("must_cover_entities", []) if entity.lower() in final_text.lower()]
    if case.get("must_cover_entities"):
        entity_score = round(15 * len(entity_hits) / len(case["must_cover_entities"]))
    else:
        entity_score = 15
    score += entity_score
    if entity_score < 15:
        missing = sorted(set(case.get("must_cover_entities", [])) - set(entity_hits))
        findings.append("Missing must-cover entities: " + ", ".join(missing))

    source_registry_text = read_text(run_dir / "data" / "source_registry.csv")
    final_reference_hits = count_reader_references(final_text, case.get("source_ids", []), sources_by_id)
    registry_hits = count_registry_sources(source_registry_text, case.get("source_ids", []), sources_by_id)
    traceability_score = min(10, registry_hits * 3)
    reference_score = min(5, final_reference_hits * 2)
    score += traceability_score + reference_score
    if traceability_score < 6:
        findings.append("Weak backstage traceability: expected source ids and titles in data/source_registry.csv.")
    if reference_score < 2:
        findings.append("Weak reader-facing references: final.md should cite source titles or include a clean reference appendix.")

    leaked_source_ids = sorted(set(re.findall(r"\bS\d{3}\b", final_text)))
    if leaked_source_ids:
        findings.append("Internal source ids leaked into final.md: " + ", ".join(leaked_source_ids))

    if contains_any(final_text, UNCERTAINTY_TERMS):
        score += 10
    else:
        findings.append("No clear uncertainty, risk, limitation, or counter-evidence language found.")

    if contains_any(final_text, CLAIM_DISCIPLINE_TERMS):
        score += 10
    else:
        findings.append("No clear claim/evidence/judgment discipline language found.")

    banned = case.get("banned_process_phrases", [])
    leaked = [phrase for phrase in banned if phrase.lower() in final_text.lower()]
    if leaked:
        findings.append("Process language leaked into final.md: " + ", ".join(leaked))
    elif not leaked_source_ids:
        score += 10

    char_count = len(re.sub(r"\s+", "", final_text))
    if char_count >= 1800:
        score += 10
    elif char_count >= 900:
        score += 5
        findings.append(f"Output may be thin for this case: {char_count} non-space chars.")
    else:
        findings.append(f"Output is too short for this case: {char_count} non-space chars.")

    status = "pass" if score >= 80 and not leaked else "review"
    if score < 60:
        status = "fail"

    return {
        "case_id": case["case_id"],
        "score": score,
        "max_score": max_score,
        "status": status,
        "findings": findings,
        "artifacts": artifact_results,
        "section_hits": section_hits,
        "entity_hits": entity_hits,
        "registry_hits": registry_hits,
        "final_reference_hits": final_reference_hits,
        "char_count": char_count,
    }


def make_prompt(case: dict[str, Any], sources_by_id: dict[str, dict[str, Any]]) -> str:
    source_lines = []
    for source_id in case.get("source_ids", []):
        source = sources_by_id.get(source_id, {})
        source_lines.append(f"- {source_id}: {source.get('title', '')}")

    return "\n".join(
        [
            f"# Eval Case: {case['title']}",
            "",
            "Use the Industry Research Framework for this task.",
            "",
            "## Task",
            case["prompt"],
            "",
            f"Target reader: {case.get('target_reader', '')}",
            f"Expected depth: {case.get('expected_depth', '')}",
            "",
            "## Required Sources",
            *source_lines,
            "",
            "Read evals/source_packs/ai_knowledge_sanitized/sources.jsonl and use only the listed source ids in backstage registries unless you explicitly record a limitation. Do not expose internal source ids in final.md; use reader-facing source titles instead.",
            "",
            "## Required Artifacts",
            *[f"- {artifact}" for artifact in case.get("artifact_requirements", DEFAULT_REQUIRED_ARTIFACTS)],
            "",
            "## Must Cover",
            *[f"- {entity}" for entity in case.get("must_cover_entities", [])],
            "",
            "## Expected Sections",
            *[f"- {section}" for section in case.get("required_sections", [])],
            "",
        ]
    )


def create_skeletons(cases: list[dict[str, Any]], runs_dir: Path, sources_by_id: dict[str, dict[str, Any]]) -> None:
    for case in cases:
        case_dir = runs_dir / case["case_id"]
        (case_dir / "state").mkdir(parents=True, exist_ok=True)
        (case_dir / "data").mkdir(parents=True, exist_ok=True)
        (case_dir / "logs").mkdir(parents=True, exist_ok=True)
        write_text(case_dir / "prompt.md", make_prompt(case, sources_by_id))
        for placeholder in [
            "state/task_spec.md",
            "state/progress.json",
            "data/source_registry.csv",
            "data/claims_registry.csv",
            "logs/review.jsonl",
        ]:
            path = case_dir / placeholder
            if not path.exists():
                write_text(path, "")


def render_markdown(results: list[dict[str, Any]]) -> str:
    lines = [
        "# Industry Research Framework Eval Report",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        "| Case | Status | Score | Findings |",
        "|---|---:|---:|---|",
    ]
    for result in results:
        findings = "<br>".join(result.get("findings", [])) or "No blocking findings."
        lines.append(
            f"| {result['case_id']} | {result['status']} | "
            f"{result['score']}/{result['max_score']} | {findings} |"
        )
    lines.append("")
    lines.append("Scores are heuristic conformance checks. Human taste review remains required for serious framework changes.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evals-dir", default="evals")
    parser.add_argument("--runs-dir", default="evals/runs")
    parser.add_argument("--report", default="evals/runs/report.md")
    parser.add_argument("--json-report", default="evals/runs/report.json")
    parser.add_argument("--create-skeletons", action="store_true")
    parser.add_argument("--allow-missing-output", action="store_true")
    args = parser.parse_args()

    evals_dir = Path(args.evals_dir).resolve()
    runs_dir = Path(args.runs_dir).resolve()
    cases = load_cases(evals_dir / "cases")
    sources_by_id = load_sources(evals_dir)

    if args.create_skeletons:
        create_skeletons(cases, runs_dir, sources_by_id)

    results = [evaluate_case(case, runs_dir / case["case_id"], sources_by_id) for case in cases]
    report_md = render_markdown(results)

    report_path = Path(args.report).resolve()
    json_report_path = Path(args.json_report).resolve()
    write_text(report_path, report_md)
    json_report_path.parent.mkdir(parents=True, exist_ok=True)
    json_report_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_report_path}")
    allowed_statuses = {"pass", "review"}
    if args.allow_missing_output:
        allowed_statuses.add("missing_output")
    return 0 if all(result["status"] in allowed_statuses for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
