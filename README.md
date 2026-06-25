# Longform Industry Research and Writing

An agent skill for source-backed longform industry research and publishable Chinese/English writing.

This repository contains a reusable research-writing protocol for AI agents. It is designed for complex tasks where an agent must plan research, collect and classify sources, manage evidence, analyze a market or topic in stages, draft section by section, run review loops, and turn the result into a clean reader-facing article or report.

The method is intentionally general. Narrative analysis is one optional lens, not the default frame. The skill can also support market analysis, company research, product/category studies, policy and regulation research, technology ecosystem analysis, organization/talent studies, and counter-case analysis.

## What This Skill Helps With

Use this skill when you need to produce substantial research writing such as:

- company, product, or market category studies
- technology ecosystem analysis
- industry structure and competition reports
- policy, regulation, and institutional analysis
- organization, talent, and operating-model research
- product adoption and user-behavior analysis
- capital-market, pricing, and business-model analysis
- cross-region or cross-market comparison
- synthesis of official materials, data, papers, media, interviews, community discussion, and counter-evidence
- final cleanup of a research draft into a publishable article or report

The central idea:

> Keep the research backend rigorous, but keep the final article clean.

The skill separates two layers:

- **Research backend**: task spec, source registry, claim registry, uncertainty list, logs, checkpoints, review records, access failures.
- **Publishing frontend**: thesis, argument, section structure, analysis, synthesis, implications, reader-facing references.

## Core Method

The workflow is:

1. **Frame the task**: define the question, reader, scope, evidence standard, output form, and completion criteria.
2. **Build the backend**: maintain state files and registries when the task is long or multi-stage.
3. **Collect and classify sources**: official materials, primary data, expert materials, media, market evidence, community reception, and counter-evidence as relevant.
4. **Analyze in units**: company, product, market, technology, policy, actor, period, or case.
5. **Choose optional lenses**: narrative analysis, horizontal-vertical analysis, adoption analysis, capital analysis, organization/talent analysis, policy analysis, or counter-case analysis.
6. **Draft in sections**: do not generate the whole report in one pass when the project is complex.
7. **Review and revise**: run evidence, coverage, skeptical, structure, and reader-quality review loops.
8. **Finalize cleanly**: remove process language and produce reader-facing references.

## Repository Structure

```text
longform-industry-narrative-research/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── research-workflow.md
    ├── optional-analysis-lenses.md
    ├── horizontal-vertical-analysis.md
    ├── subagents-and-review-loop.md
    ├── writing-style.md
    ├── quality-gates.md
    └── postmortem-lessons.md
```

## Installation / Reuse

Clone or copy this repository into the directory where your agent system loads reusable skills or instruction bundles.

```bash
git clone https://github.com/rrrrrredy/longform-industry-narrative-research.git \
  ./agent-skills/longform-industry-research
```

For systems without a formal skill loader, use `SKILL.md` as the main instruction file and load files under `references/` only when the task requires them.

## Example Prompts

```text
Use $longform-industry-narrative-research to plan a source-backed report on the enterprise adoption of AI coding tools.
```

```text
Use $longform-industry-narrative-research to turn these source notes into a publishable market structure analysis.
```

```text
Use $longform-industry-narrative-research to review this draft, remove process language, and make the argument read like a finished research article.
```

## Design Principles

- State before scale: define the question and reader before collecting more material.
- Evidence is not prose: registries belong backstage; the final article should not read like a log.
- Use methods conditionally: narrative analysis, horizontal-vertical analysis, and capital analysis are optional lenses.
- Work in stages: plan, collect, analyze, draft, review, revise.
- Review must close the loop: every audit finding should become a concrete revision action.
- Reader quality matters: after factual and coverage checks, run a reader-focused revision pass.

## What This Is Not

This is not:

- a scraping tool
- a citation manager
- a generic report template
- a replacement for source verification
- a one-click article generator
- a narrative-analysis-only framework

It is a reusable workflow for long, judgment-heavy research writing where evidence discipline and final prose quality both matter.

---

# 长篇产业研究与写作 Skill

这是一个适用于 AI agent 的通用研究写作 skill，用于资料量大、周期长、需要形成可发布中文或英文文章/报告的产业研究任务。

它不是某个特定主题的研究框架，也不是只服务于“叙事分析”的方法。叙事分析只是可选分析镜头之一。这个 skill 更核心的目标是：让 agent 在长周期研究中保持任务状态、证据纪律、分段写作、审计闭环和终稿可读性。

一句话概括：

> 后台研究要严谨，前台文章要干净。

## 适用场景

这个 skill 适合用于：

- 公司、产品或市场类别研究
- 技术生态与产业链分析
- 行业结构与竞争格局研究
- 政策、监管与制度分析
- 组织、人才流动与运营模式研究
- 产品采用与用户行为分析
- 商业模式、定价、融资与资本市场分析
- 跨区域、跨市场、跨公司比较研究
- 官方材料、数据、论文、媒体、访谈、社区讨论和反面案例的综合分析
- 把研究草稿改成可发布文章或报告

## 核心流程

1. **定义任务**：明确研究问题、目标读者、覆盖范围、证据标准、输出形式和完成标准。
2. **建立后台**：对长任务维护状态文件、来源台账、判断台账和不确定性清单。
3. **收集并分类资料**：根据题目选择官方材料、原始数据、专家材料、媒体报道、市场证据、社区反馈和反面证据。
4. **按分析单元处理**：可以按公司、产品、市场、技术、政策、人物、阶段或案例拆解。
5. **选择分析镜头**：按需使用叙事分析、横纵分析、采用分析、资本分析、组织/人才分析、政策分析或反面案例分析。
6. **分段写作**：复杂任务不要一次性生成全文，而是按章节、公司、主题或观点逐步写。
7. **审计与修订**：执行事实、覆盖、反方、结构和读者体验 review，并把反馈转成具体修改动作。
8. **终稿清理**：删除过程语言、内部 source id、审计痕迹和 assistant 第一视角，形成读者可读的文章。

## 推荐文件结构

```text
longform-industry-narrative-research/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── research-workflow.md
    ├── optional-analysis-lenses.md
    ├── horizontal-vertical-analysis.md
    ├── subagents-and-review-loop.md
    ├── writing-style.md
    ├── quality-gates.md
    └── postmortem-lessons.md
```

## 安装 / 复用

将本仓库 clone 或复制到你的 agent 系统用于加载 skill / instruction bundle 的目录中：

```bash
git clone https://github.com/rrrrrredy/longform-industry-narrative-research.git \
  ./agent-skills/longform-industry-research
```

如果你的 agent 系统没有正式的 skill loader，可以把 `SKILL.md` 作为主说明文件，把 `references/` 下的文件作为按需加载的参考材料。

## 示例提示词

```text
Use $longform-industry-narrative-research to plan a source-backed report on the enterprise adoption of AI coding tools.
```

```text
Use $longform-industry-narrative-research to turn these notes into a publishable market structure analysis.
```

```text
Use $longform-industry-narrative-research to clean this draft, remove process language, and make it read like a finished research article.
```

## 设计原则

- 先定问题和读者，再扩大资料规模。
- 证据台账不是正文；终稿不能像工作日志。
- 方法按需选择；叙事分析、横纵分析、资本分析都只是可选镜头。
- 长任务必须分阶段推进：规划、收集、分析、写作、审计、修订。
- 审计必须闭环；每个问题都要落到具体修改动作。
- 读者体验是终稿质量的一部分；事实与覆盖审计之后，还要做读者视角修订。

## 它不是什么

这个 skill 不是：

- 抓取工具
- 引文管理器
- 通用报告模板
- 来源核查的替代品
- 一键生成文章的工具
- 只适用于叙事研究的方法

它是一套服务于长篇、复杂、重判断研究写作的通用 agent 工作流。
