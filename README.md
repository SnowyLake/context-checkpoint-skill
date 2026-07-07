# SnowyAgentSkills

Language: English | [中文](README.zh-CN.md)

## Table of Contents

- [Overview](#overview)
- [Available Skills](#available-skills)
  - [checkpoint](#checkpoint)
  - [codex-reset-credits](#codex-reset-credits)
  - [grill-me](#grill-me)
- [Add Skills](#add-skills)
- [Repository Layout](#repository-layout)

## Overview

SnowyAgentSkills is a collection repository for reusable agent skills.

Each skill lives under `skills/<skill-name>/` as a self-contained folder. The repository is intended to stay agent-neutral so different agent runtimes can adopt the skill content that fits their own loading model.

## Available Skills

### checkpoint

- Description: Checkpoint skill family for saving, restoring, handing off, listing status, and reviewing session context in long-running, multi-session, handoff-based, or review-driven agent work.

- Skills: `checkpoint-save`, `checkpoint-restore`, `checkpoint-handoff`, `checkpoint-status`, `checkpoint-review`.

- Documentation: [English](skills/checkpoint/README.md), [中文](skills/checkpoint/README.zh-CN.md)

- Agent scope: All agents.

### codex-reset-credits

- Description: Query the current Codex account's available rate limit reset credits and expiration times.

- Documentation: [English](skills/codex-reset-credits/README.md), [中文](skills/codex-reset-credits/README.zh-CN.md)

- Agent scope: Codex only.

### grill-me

- Description: Forked from mattpocock/skills. A relentless interview to sharpen a plan or design.

- Documentation: [SKILL.md](skills/grill-me/SKILL.md)

- Agent scope: All agents.

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
|   |   |   |-- references/
|   |   |   |   |-- common-rules.md
|   |   |   |   |-- file-contracts.md
|   |   |   |   `-- status-summary.md
|   |   |   `-- agents/
|   |   |       `-- openai.yaml
|   |   |-- checkpoint-restore/
|   |   |   |-- SKILL.md
|   |   |   `-- agents/
|   |   |       `-- openai.yaml
|   |   |-- checkpoint-handoff/
|   |   |   |-- SKILL.md
|   |   |   `-- agents/
|   |   |       `-- openai.yaml
|   |   |-- checkpoint-status/
|   |   |   |-- SKILL.md
|   |   |   `-- agents/
|   |   |       `-- openai.yaml
|   |   `-- checkpoint-review/
|   |       |-- SKILL.md
|   |       `-- agents/
|   |           `-- openai.yaml
|   `-- grill-me/
|       |-- SKILL.md
|       `-- agents/
|           `-- openai.yaml
|-- README.md
|-- README.zh-CN.md
|-- LICENSE
`-- .gitignore
```
