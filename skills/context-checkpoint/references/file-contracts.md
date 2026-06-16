# File Contracts

## 目录

- [CONTEXT.md](#contextmd)
- [Work Artifacts](#work-artifacts)
- [HISTORY.md](#historymd)
- [Handoff Entry](#handoff-entry)
- [REVIEW.md](#reviewmd)

本说明文件定义所有 `context-checkpoint` 命令共享的 checkpoint 和 review 文件结构. 命令说明文件指向这里, 不重复这些结构.

## CONTEXT.md

`CONTEXT.md` 只保存当前仍然有效, 并且会影响未来工作的当前信息. 使用以下结构:

```md
# CONTEXT.md

## Current Goal

## Current State

## Confirmed Decisions

## Active Constraints

## Known Risks

## Open Questions

## TODO

## Next Actions

## Relevant Files

## Work Artifacts
```

Section 含义:

- `Current Goal`: 当前目标.
- `Current State`: 当前实现状态或会话状态.
- `Confirmed Decisions`: 仍然有效的决策.
- `Active Constraints`: 后续工作仍必须遵守的约束.
- `Known Risks`: 已知风险, 陷阱或注意事项.
- `Open Questions`: 需要讨论, 调研或验证的问题.
- `TODO`: 仍然有效的剩余工作池.
- `Next Actions`: 从 `TODO` 中提炼出的前 1 到 3 个具体下一步动作.
- `Relevant Files`: 与理解当前会话直接相关的文件, 文件夹或资源.
- `Work Artifacts`: 本会话创建, 修改, 删除或移动的主要文件. 它是导航索引, 不是完整 diff, 不是完整事实来源, 也不是 handoff 复制白名单.

执行 `handoff` 时, 目标 `CONTEXT.md` 必须在 `Current State` 下包含一条简洁来源说明, 标明源会话文件夹. 不要把已复制 / 已丢弃文件列表, 用户要求的修正或详细引用改写记录放入 `CONTEXT.md`.

## Work Artifacts

使用以下 `Work Artifacts` 条目结构:

```md
- [Modified] `path/to/file.md`
  - Briefly explain what changed in this file.
```

允许的 `Work Artifacts` 动作:

- `[Created]`: 本会话创建了该文件.
- `[Modified]`: 本会话修改了已有文件.
- `[Deleted]`: 本会话删除了该文件.
- `[Moved]`: 本会话移动或重命名了该文件.

每次 `update` 都必须维护 `Work Artifacts`, 但没有工作产物时可以为空.

## HISTORY.md

`HISTORY.md` 保存历史摘要, 排障记录, 已拒绝或暂缓方案和推理归档. 使用多条目结构:

```md
# HISTORY.md

## {YYYY-MM-DD} - {entry-title}

### Summary

### Important Findings

### Decisions

### Rejected / Deferred Approaches

### Assumptions

### Notes
```

每个新的历史条目:

- 使用 `YYYY-MM-DD` 格式的实际条目日期.
- 使用简短描述性的条目标题.
- 新增一个二级条目. 不要使用重复的 `Entry Date` 或 `Entry Title` 标题.
- 显式标记已拒绝和已暂缓项, 例如 `[Rejected]` 或 `[Deferred]`.
- 显式标记假设, 例如 `[Verified]` 或 `[Unverified]`.

## Handoff Entry

每次 `handoff` 都向目标 `HISTORY.md` 追加一个 handoff 条目. 使用以下结构:

```md
## {YYYY-MM-DD} - Handoff from {source-session-folder}

### Summary

### Source

### Target

### Copied Files

### Discarded Files

### Reference Rewrites

### User Overrides

### Assumptions

### Notes
```

Handoff entry 必须记录已复制 checkpoint 文件, 已复制产物, 已丢弃产物, 引用路径改写, 用户要求的修正, 缺失的可选源文件, 例如 `HISTORY.md`, 以及未解决的不确定性.

## REVIEW.md

`REVIEW.md` 保存某个会话文件夹的最新 `review` 结果. `review` 将其写入被审阅会话文件夹, 并覆盖任何旧的 `REVIEW.md`. 使用以下结构:

```md
# REVIEW.md

## Reviewed Session

## Review Date

## Goal Completion

## Findings

## Checkpoint Quality

## Open Questions

## Summary
```

`REVIEW.md` 章节含义:

- `Reviewed Session`: 本次 review 指向的被审阅会话文件夹.
- `Review Date`: `YYYY-MM-DD` 格式的审阅日期.
- `Goal Completion`, `Findings`, `Checkpoint Quality`, `Open Questions`, `Summary`: 与 `review.md` 中定义的审阅输出章节含义相同.

`REVIEW.md` 是 review 产物, 不是 checkpoint 文件. `restore` 和 `handoff` 将其视为导航提示, 不视为当前状态. `handoff` 像处理其他非 checkpoint 源文件夹产物一样分类它.
