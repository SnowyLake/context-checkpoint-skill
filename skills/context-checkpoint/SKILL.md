---
name: context-checkpoint
description: Manage session context for long-running, multi-session, handoff-based, or review-driven agent work.
---

# Context Checkpoint

## 目录

- [概览](#概览)
- [命令选择](#命令选择)
- [执行](#执行)
- [全局不变量](#全局不变量)
- [语言和格式](#语言和格式)

## 概览

提供四个能力:

- `update`: 在 `CONTEXT.md` 和 `HISTORY.md` 中创建或刷新当前会话 checkpoint.
- `restore`: 以只读方式从当前会话 checkpoint 文件, 或显式指定会话文件夹中的 checkpoint 文件恢复当前会话上下文.
- `handoff`: 从另一个会话文件夹接管, 迁移或派生上下文, 然后把结果保存到当前对话的会话文件夹.
- `review`: 客观审阅当前会话文件夹或显式指定会话文件夹中 checkpoint 指向的实际工作内容, 然后把结果写入该文件夹的 `REVIEW.md`, 不恢复上下文, 也不继续实现.

## 命令选择

优先响应命令式请求, 或明确点名 `$context-checkpoint` 的自然语言请求. 当用户清楚要求 checkpoint 更新, 恢复, 接管或审阅时, 也允许完全隐式的自然语言请求.

如果请求明确调用本 skill, 但无法可靠判断应执行 `update`, `restore`, `handoff`, `review` 中哪一个命令, 停止并询问用户明确指定命令. 不要擅自猜测, 也不要默认选择某个命令.

使用 `update` 的场景:

- 用户明确要求生成, 更新或刷新 checkpoint 文件.
- 用户要求把当前会话保存为可供后续会话继续使用的 checkpoint.
- 用户要求把当前会话整理到 `CONTEXT.md` 和 `HISTORY.md`.

使用 `restore` 的场景:

- 用户要求读取当前会话 checkpoint.
- 用户要求以只读方式从当前会话的 `CONTEXT.md` 和 `HISTORY.md` 恢复或重建会话上下文.
- 用户要求以只读方式从指定会话文件夹中的 checkpoint 文件恢复或重建会话上下文.
- 用户只说从某个 checkpoint 或会话文件夹"恢复"或"重建"上下文, 但没有要求接管, 迁移, 分支, 保存或写入当前 / 目标会话文件夹.

使用 `handoff` 的场景:

- 用户明确要求从另一个会话文件夹接管, 迁移或分支上下文.
- 用户要求从另一个会话文件夹恢复或重建上下文, 并把结果写入当前会话文件夹或指定目标会话文件夹.
- 用户要求从更旧或不同的会话 checkpoint 接管当前对话, 并保存接管后的状态.
- 用户要求把 checkpoint 上下文从 session A 迁移到 session B.
- 新会话需要从另一个会话文件夹中的既有 checkpoint 接管, 并把重建后的 checkpoint 持久化到自己的会话文件夹.
- 不要仅因为用户使用"重建"或 `rebuild` 一词就选择 `handoff`; 只有当用户同时表达写入, 保存, 迁移, 接管或分支到目标会话文件夹时才使用 `handoff`.

使用 `review` 的场景:

- 用户要求 review, 审阅, 评估, 检查或批评当前会话文件夹的实际工作内容.
- 用户要求 review, 审阅, 评估, 检查或批评指定会话文件夹的实际工作内容.
- 用户询问某个会话是否完成目标.
- 用户询问某个会话的工作是否存在缺陷, 边界问题, 遗漏验证, 冲突或不一致.
- 用户要求进行一次基于 checkpoint 导航的客观工作审阅, 且不恢复上下文, 不继续实现.

## 执行

执行任何命令前, 先读取 `references/` 下对应的说明文件. 每个命令说明文件定义该命令的会话文件夹解析, 访问模式, 工作流和输出风格. 同时应用本文件中的 `全局不变量` 和命令说明文件. 不要在命令说明文件中重复路由逻辑或全局规则.

任何命令只要会读取, 写入, 校验, 总结或输出 `CONTEXT.md`, `HISTORY.md`, `REVIEW.md`, `Work Artifacts` 或 handoff 条目, 都必须先读取 `references/file-contracts.md`. 当文件契约可用时, 不要凭记忆重建文件结构.

命令说明文件:

- `references/update.md`: 刷新当前会话 checkpoint.
- `references/restore.md`: 从 checkpoint 重建会话上下文.
- `references/handoff.md`: 把 checkpoint 转移到当前会话文件夹.
- `references/review.md`: 审阅 checkpoint 背后的实际工作内容, 并写入 `REVIEW.md`.

共享文件契约:

- `references/file-contracts.md`: `CONTEXT.md`, `HISTORY.md`, `REVIEW.md` 的结构, 包括 `Work Artifacts` 和 handoff 条目格式.

## 全局不变量

这些规则适用于所有命令. 命令说明文件不应重复这些规则.

- checkpoint 文件存放在项目根目录的 `.agent-sessions/{YYYYMMDD}-{short-kebab-case-session-summary}/` 下. summary 片段使用小写 kebab-case, 并优先保持简洁.
- 当会话文件夹不明确时, 不要检查 `.agent-sessions/` 来猜测语义匹配的文件夹, 除非用户明确要求发现或列出候选.
- 当 checkpoint 文件与当前项目文件冲突时, 优先相信当前项目文件.
- 只把 `Work Artifacts` 当作导航索引. 它不是完整 diff, 不是事实来源, 也不是 handoff 复制白名单.
- 不要执行 `TODO` 项, 修改项目文件, 或继续实现, 除非用户明确要求后续工作.

## 语言和格式

写入 checkpoint Markdown 文件或审阅输出时:

- 保留 `references/file-contracts.md` 中要求的文件名和章节标题, 除非项目级指令明确覆盖它们.
- 把本 skill 中的英文标题视为结构契约, 不视为正文默认语言.
- 正文语言优先遵循项目级或用户级指令.
- 如果没有项目级或用户级语言指令, 正文使用当前对话语言.
- 这条规则适用于本 skill 写入的所有 checkpoint Markdown, 包括 `CONTEXT.md`, `HISTORY.md`, handoff 条目和 `REVIEW.md`.
