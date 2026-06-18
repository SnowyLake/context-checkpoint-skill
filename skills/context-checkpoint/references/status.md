# status 命令

## 目录

- [执行前检查](#执行前检查)
- [会话文件夹解析](#会话文件夹解析)
- [访问模式](#访问模式)
- [工作流](#工作流)
- [输出风格](#输出风格)

本说明文件只覆盖 `status` 命令. 使用时需要同时应用 `SKILL.md` 中的 `全局不变量`. 解读或输出 `CONTEXT.md`, `REVIEW.md` 或 findings 前, 必须先读取 `file-contracts.md`.

## 执行前检查

- 已读取 `SKILL.md` 的 `全局不变量`.
- 已读取 `references/file-contracts.md`.
- 已确认 status 源会话文件夹.
- 已确认本命令只读, 不写 checkpoint, `REVIEW.md` 或项目文件.
- 已确认本命令只做简单列出, 不恢复完整上下文, 不审阅实际工作, 不验证 `Open` findings.

## 会话文件夹解析

解析 status 源会话文件夹:

1. 如果用户没有指定会话文件夹, 解析当前会话文件夹.
2. 如果用户指定了会话文件夹, 将其作为 status 源.
3. 如果当前会话文件夹不明确且用户未指定路径, 要求用户指定一个已有会话文件夹.
4. `status` 不创建新会话文件夹.

## 访问模式

- 只读.
- 可以读取 status 源会话文件夹中的 `CONTEXT.md`.
- 当 status 源会话文件夹中存在 `REVIEW.md` 时, 可以读取它并提取 `Open` findings.
- 默认不读取 `HISTORY.md`, 除非用户明确要求补充历史背景.
- 不得复制 checkpoint 文件, 写入会话文件夹, 修改 `REVIEW.md`, 修改项目文件或执行 TODO.

## 工作流

1. 解析 status 源会话文件夹.
2. 确认源会话文件夹存在.
3. 确认源会话文件夹包含 `CONTEXT.md`.
4. 读取 `CONTEXT.md`.
5. 原文提取 `Current Goal`, `Current State`, `Known Risks`, `Open Questions`, `TODO` 和 `Next Actions`.
6. 如果源会话文件夹中存在 `REVIEW.md`, 读取它.
7. 只提取 `Status` 为 `Open` 的 findings, 不展开 `Impact`, `Evidence` 或 `Recommended Fix`, 不验证 finding 是否仍符合当前工程事实.
8. 如果某个必需 section 缺失, 在对应输出 section 中说明缺失, 不从其他 section 推断.

执行 `status` 时不要修改 checkpoint 文件, `REVIEW.md` 或项目文件.

## 输出风格

输出固定包含以下章节, 并保持这个顺序:

```md
## Current Goal

## Current State

## Known Risks

## Open Questions

## TODO

## Next Actions

## Open Review Findings
```

输出规则:

- 除 `Open Review Findings` 外, 其他章节保持 `CONTEXT.md` 中的原文内容.
- `Open Review Findings` 每条使用一行简短格式:

```md
- [Open][High] F-003: 简短问题标题
```

- `Open Review Findings` 默认输出全部 `Open` findings, 每条只输出 finding 的 `Status`, `Severity`, ID 和标题.
- 不输出 `Impact`, `Evidence` 或 `Recommended Fix`.
- 如果没有 `Open` findings, 明确说明没有 `Open` review findings.
