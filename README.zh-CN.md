# SnowyAgentSkills

语言: [English](README.md) | 中文

## Table of Contents

- [概览](#概览)
- [可用 Skills](#可用-skills)
  - [checkpoint](#checkpoint)
  - [grill-me](#grill-me)
  - [subagent-workflow](#subagent-workflow)
- [弃用 Skills](#弃用-skills)
  - [codex-reset-credits](#codex-reset-credits)
- [新增 Skills](#新增-skills)
- [仓库结构](#仓库结构)

## 概览

SnowyAgentSkills 是一个可复用 agent skills 集合仓库.

每个 skill 都位于 `skills/<skill-name>/` 下, 并作为自包含目录独立维护. 仓库目标是保持 agent-neutral, 让不同 agent runtime 都能按自己的加载模型采用合适的 skill 内容.

## 可用 Skills

### [checkpoint](skills/checkpoint/README.zh-CN.md)

- 简介: checkpoint skill family, 用于在 long-running, multi-session, handoff-based 或 review-driven agent work 中保存, 恢复, 接管, 查看状态和审阅会话上下文.

- Skills: `checkpoint-save`, `checkpoint-restore`, `checkpoint-handoff`, `checkpoint-status`, `checkpoint-review`.

- 适用范围: All agents.

### [grill-me](skills/grill-me/SKILL.md)

- 简介: Forked from mattpocock/skills. A relentless interview to sharpen a plan or design.

- 适用范围: All agents.

### [subagent-workflow](skills/subagent-workflow/SKILL.md)

- 简介: 命令当前 Agent 通过 Subagent 工作流完成用户任务.

- 适用范围: Agents with Subagent support.

## 弃用 Skills

### [codex-reset-credits](deprecated/codex-reset-credits/SKILL.md)

- 简介: 查询当前 Codex 账户可用的 rate limit reset credits 和过期时间.

- 适用范围: Codex only.

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
|   |-- checkpoint/
|   |   |-- checkpoint-save/
|   |   |-- checkpoint-restore/
|   |   |-- checkpoint-handoff/
|   |   |-- checkpoint-status/
|   |   `-- checkpoint-review/
|   |-- grill-me/
|   `-- subagent-workflow/
|-- deprecated/
|   `-- codex-reset-credits/
|-- README.md
|-- README.zh-CN.md
|-- LICENSE
`-- .gitignore
```
