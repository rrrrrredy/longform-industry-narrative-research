# Codex Adapter

Use this when Codex can read or clone repositories in a local workspace.

## Setup

Clone this repository into the location where you keep reusable skills or project instructions:

```bash
git clone https://github.com/rrrrrredy/industry-research-framework.git agent-skills/industry-research-framework
```

Then tell Codex:

```text
Use the Industry Research Framework in agent-skills/industry-research-framework.
Read SKILL.md first. Load references only when needed.
For this research task, create task state files before broad source collection.
```

## Operating Notes

- Use Codex file access for `state/`, `logs/`, `data/`, drafts, and review notes.
- Keep the final answer separate from backstage registries.
- If the session resumes after compaction or interruption, recover from `state/task_spec.md`, `state/progress.json`, recent findings, and `directions_tried.json`.
- Do not let coding workflow habits replace research workflow gates; the deliverable is the research report.

## 中文提示

在 Codex 中使用时，最稳妥的方式是把本仓库克隆到项目或技能目录，让 Codex 先读 `SKILL.md`。长任务必须先建状态文件，再收集大量资料；断点恢复时从 `state/` 读取，而不是依赖聊天记忆。
