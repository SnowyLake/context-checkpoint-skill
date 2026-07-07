# SnowyAgentSkills

语言: [English](README.md) | 中文

## Table of Contents

- [概览](#概览)
- [可用 Skills](#可用-skills)
  - [checkpoint](#checkpoint)
  - [codex-reset-credits](#codex-reset-credits)
  - [grill-me](#grill-me)
- [新增 Skills](#新增-skills)
- [仓库结构](#仓库结构)

## 概览

SnowyAgentSkills 是一个可复用 agent skills 集合仓库.

每个 skill 都位于 `skills/<skill-name>/` 下, 并作为自包含目录独立维护. 仓库目标是保持 agent-neutral, 让不同 agent runtime 都能按自己的加载模型采用合适的 skill 内容.

## 可用 Skills

### checkpoint

- 简介: checkpoint skill family, 用于在 long-running, multi-session, handoff-based 或 review-driven agent work 中保存, 恢复, 接管, 查看状态和审阅会话上下文.

- Skills: `checkpoint-save`, `checkpoint-restore`, `checkpoint-handoff`, `checkpoint-status`, `checkpoint-review`.

- 文档: [English](skills/checkpoint/README.md), [中文](skills/checkpoint/README.zh-CN.md)

- 适用范围: All agents.

### codex-reset-credits

- 简介: 查询当前 Codex 账户可用的 rate limit reset credits 和过期时间.

- 文档: [English](skills/codex-reset-credits/README.md), [中文](skills/codex-reset-credits/README.zh-CN.md)

- 适用范围: Codex only.

### grill-me

- 简介: Forked from mattpocock/skills. A relentless interview to sharpen a plan or design.

- 文档: [SKILL.md](skills/grill-me/SKILL.md)

- 适用范围: All agents.

## 新增 Skills

新增 skill 时放入:

```text
skills/<skill-name>/
```

每个 skill 文件夹必须包含:

- `SKILL.md`: 必需的 skill 元数据和说明.

只有在 skill 需要时才添加可选资源:

- `README.md`
- `README.zh-CN.md`
- `agents/`
- `scripts/`
- `references/`
- `assets/`

`agents/` 用于可选 runtime-specific metadata, 例如 `agents/openai.yaml`.

保持每个 skill 自包含, 不要把 skill 专属文档放在仓库根目录.

## 仓库结构

```text
SnowyAgentSkills/
|-- skills/
|   |-- codex-reset-credits/
|   |   |-- SKILL.md
|   |   |-- README.md
|   |   |-- README.zh-CN.md
|   |   |-- scripts/
|   |   |   `-- check_reset_credits.py
|   |   `-- agents/
|   |       `-- openai.yaml
|   |-- checkpoint/
|   |   |-- README.md
|   |   |-- README.zh-CN.md
|   |   |-- checkpoint-save/
|   |   |   |-- SKILL.md
|   |   |   `-- references/
|   |   |       |-- common-rules.md
|   |   |       |-- file-contracts.md
|   |   |       `-- status-summary.md
|   |   |-- checkpoint-restore/
|   |   |   `-- SKILL.md
|   |   |-- checkpoint-handoff/
|   |   |   `-- SKILL.md
|   |   |-- checkpoint-status/
|   |   |   `-- SKILL.md
|   |   `-- checkpoint-review/
|   |       `-- SKILL.md
|   `-- grill-me/
|       |-- SKILL.md
|       `-- agents/
|           `-- openai.yaml
|-- README.md
|-- README.zh-CN.md
|-- LICENSE
`-- .gitignore
```
