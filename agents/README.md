# Agent Adapters

These notes explain how to use Industry Research Framework with common agents without turning this repository into a heavy product. The invariant is the same across tools:

1. Load `SKILL.md` first.
2. Load files under `references/` only when the task needs that method.
3. For substantial work, create `state/`, `logs/`, and `data/`.
4. Keep evidence and audit records backstage.
5. Final prose should read like a finished research article or report.

## Adapters

- [Codex](./codex.md)
- [Claude](./claude.md)
- [Gemini CLI](./gemini-cli.md)
- [Cursor](./cursor.md)
- [ChatGPT / general agents](./chatgpt.md)

## 中文说明

这些文件不是新的 agent 产品，而是不同 agent 环境下的轻量使用说明。无论使用哪种工具，都遵守同一个核心流程：先读 `SKILL.md`，按需读取 `references/`，较大任务创建 `state/`、`logs/`、`data/`，后台保存证据和审阅，最终输出干净的研究成稿。
