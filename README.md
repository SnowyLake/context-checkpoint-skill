# SnowyAgentSkills

Language: English | [中文](README.zh-CN.md)

## Table of Contents

- [Overview](#overview)
- [Available Skills](#available-skills)
  - [checkpoint](#checkpoint)
  - [grill-me](#grill-me)
  - [multi-agent-dispatch](#multi-agent-dispatch)
- [Deprecated Skills](#deprecated-skills)
  - [codex-reset-credits](#codex-reset-credits)
- [Add Skills](#add-skills)
- [Repository Layout](#repository-layout)

## Overview

SnowyAgentSkills is a collection repository for reusable agent skills.

Each skill lives under `skills/<skill-name>/` as a self-contained folder. The repository is intended to stay agent-neutral so different agent runtimes can adopt the skill content that fits their own loading model.

## Available Skills

### [checkpoint](skills/checkpoint/README.md)

- Description: Checkpoint skill family for saving, restoring, handing off, listing status, and reviewing session context in long-running, multi-session, handoff-based, or review-driven agent work.

- Skills: `checkpoint-save`, `checkpoint-restore`, `checkpoint-handoff`, `checkpoint-status`, `checkpoint-review`.

- Agent scope: All agents.

### [grill-me](skills/grill-me/SKILL.md)

- Description: Forked from mattpocock/skills. A relentless interview to sharpen a plan or design.

- Agent scope: All agents.

### [multi-agent-dispatch](skills/multi-agent-dispatch/SKILL.md)

- Description: Require the current agent to complete the user's task through multi-agent dispatch.

- Agent scope: Agents with Subagent support.

## Deprecated Skills

### [codex-reset-credits](deprecated/codex-reset-credits/SKILL.md)

- Description: Query the current Codex account's available rate limit reset credits and expiration times.

- Agent scope: Codex only.

## Add Skills

Add new skills under:

```text
skills/<skill-name>/
```

Each skill folder must include:

- `SKILL.md`: Required skill metadata and instructions.

Optional resources can be added only when the skill needs them:

- `README.md`
- `README.zh-CN.md`
- `agents/`
- `scripts/`
- `references/`
- `assets/`

Use `agents/` for optional runtime-specific metadata, such as `agents/openai.yaml`.

Keep each skill self-contained and avoid placing skill-specific documentation in the repository root.

## Repository Layout

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
|   `-- multi-agent-dispatch/
|-- deprecated/
|   `-- codex-reset-credits/
|-- README.md
|-- README.zh-CN.md
|-- LICENSE
`-- .gitignore
```
