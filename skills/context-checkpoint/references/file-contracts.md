# File Contracts

## 目录

- [TOC 规则](#toc-规则)
- [CONTEXT.md](#contextmd)
  - [Work Artifacts](#work-artifacts)
- [HISTORY.md](#historymd)
  - [Handoff Entry](#handoff-entry)
- [REVIEW.md](#reviewmd)
  - [Finding 格式](#finding-格式)
  - [Finding 状态](#finding-状态)
  - [Severity 范围](#severity-范围)

本说明文件定义所有 `context-checkpoint` 命令共享的 checkpoint 和 review 文件结构. 命令说明文件指向这里, 不重复这些结构.

## TOC 规则

`CONTEXT.md`, `HISTORY.md` 和 `REVIEW.md` 必须包含 `## Table of Contents`. TOC 是 checkpoint 和 review 文件结构的一部分, 放在一级标题之后, 正文二级章节之前.

TOC 必须列出文件中的所有二级章节. 模板中的 `- ...` 表示按实际章节生成 TOC, 不是要保留的字面内容. 每次追加, 删除或重命名章节时, 必须同步更新 TOC.

## CONTEXT.md

`CONTEXT.md` 只保存当前仍然有效, 并且会影响未来工作的当前信息. 使用以下结构:

```md
# CONTEXT.md

## Table of Contents

- ...

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

每次创建或更新 `CONTEXT.md` 时, 必须同步更新 `Table of Contents`, 确保 TOC 列出所有实际存在的二级章节.

执行 `handoff` 时, 目标 `CONTEXT.md` 必须在 `Current State` 下包含一条简洁来源说明, 标明源会话文件夹. 不要把已复制 / 已丢弃文件列表, 用户要求的修正或详细引用改写记录放入 `CONTEXT.md`.

### Work Artifacts

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

## Table of Contents

- ...

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
- 同步更新 `Table of Contents`, 确保 TOC 列出所有实际存在的二级历史条目.
- 显式标记已拒绝和已暂缓项, 例如 `[Rejected]` 或 `[Deferred]`.
- 显式标记假设, 例如 `[Verified]` 或 `[Unverified]`.

### Handoff Entry

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

## Table of Contents

- ...

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

每次创建或更新 `REVIEW.md` 时, 必须同步更新 `Table of Contents`, 确保 TOC 列出所有实际存在的二级章节.

`REVIEW.md` 是 review 产物, 不是 checkpoint 文件. `restore` 将其视为导航提示, 不视为当前状态. `handoff` 默认不复制源会话文件夹的 `REVIEW.md`, 因为它审阅的是源会话文件夹, 不是目标会话文件夹. 如果用户明确要求保留源 `REVIEW.md`, 必须把它复制为非活跃历史文件, 例如 `REVIEW.from-{source-session-folder}.md`, 不得复制为目标 `REVIEW.md`, 也不得改写其中的 `Reviewed Session`.

### Finding 格式

`REVIEW.md` 中的每条 finding 必须使用稳定 ID, 标题格式如下:

```md
### F-001: 简短问题标题

- **Status:** Open
- **Severity:** Medium
- **Impact:** ...
- **Evidence:** ...
- **Recommended Fix:** ...
```

字段名必须使用粗体加冒号格式, 例如 `**Status:** Open`. 当 `Status` 不是 `Open` 时, 必须在 `Status` 下添加一级缩进的 `Resolution` 子项:

```md
- **Status:** Resolved
  - **Resolution:** ...
```

字段顺序固定为:

1. `**Status:**`
2. `**Severity:**`
3. `**Impact:**`
4. `**Evidence:**`
5. `**Recommended Fix:**`

`Recommended Fix` 在 `Open` 时必填. 当 `Status` 是 `Resolved` 或 `Won't Fix` 时, 可以保留原建议, 但不要求更新它.

### Finding 状态

`Status` 必须是以下值之一:

- `Open`: 问题仍未解决, 需要继续关注或处理.
- `Resolved`: 问题已解决, 并已按当前工程事实验证不再成立.
- `Won't Fix`: 用户或项目决策明确不修复. 必须通过 `Resolution` 说明原因或决策依据.

`restore` 只读 `REVIEW.md`, 不修改 finding 状态. 当已知问题修复完成, 或用户明确拒绝修复时, agent 可以在非 `restore` 流程中帮助更新对应 finding 状态. `update` 不更新 `REVIEW.md`.

`Open` finding 如果被验证仍成立, 才可能作为待处理风险在后续 `update` 中纳入 `Known Risks`. `Won't Fix` finding 不进入 `Known Risks`; 它表示已接受的取舍, 应在后续 `update` 中纳入 `Confirmed Decisions`, 必要时在 `HISTORY.md` 记录理由.

### Severity 范围

`Severity` 必须是以下值之一:

- `Blocker`: 阻断目标完成, 或会导致严重错误, 数据丢失, 上下文破坏等不可接受后果.
- `High`: 高风险问题, 可能导致错误行为, 明显误导 agent, 或破坏关键工作流.
- `Medium`: 真实问题, 影响明确, 但范围有限, 有规避方式, 或不立即阻断目标.
- `Low`: 低风险问题, 多为表达清晰度, 文档一致性, 可维护性或轻微边界问题.
