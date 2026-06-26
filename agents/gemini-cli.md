# Gemini CLI Adapter

Use this when Gemini CLI has access to a local working directory.

## Setup

Clone or copy the framework into the workspace:

```bash
git clone https://github.com/rrrrrredy/industry-research-framework.git .agent/industry-research-framework
```

Prompt Gemini CLI:

```text
Read .agent/industry-research-framework/SKILL.md and use it as the research protocol.
Use files under references/ only when the current stage needs them.
Create state/, logs/, data/, drafts/, and final/ in the task folder.
Do not treat source count as completion.
```

## Operating Notes

- Keep generated research state in the task folder, not inside the framework repository.
- Use the CLI's file operations to update registries after source intake and claim extraction.
- Ask for an explicit `next_action` in `state/progress.json` after each stage.
- Run the conformance checklist before final delivery.

## 中文提示

在 Gemini CLI 中，可以把框架放到 `.agent/industry-research-framework`。研究任务自己的 `state/`、`logs/`、`data/` 应放在任务目录，不要写回框架仓库。
