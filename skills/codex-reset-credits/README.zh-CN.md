# codex-reset-credits

## Table of Contents

- [概览](#概览)
- [快速开始](#快速开始)
- [输出格式](#输出格式)
- [高级请求](#高级请求)
- [注意事项](#注意事项)

语言: [English](README.md) | 中文

## 概览

`codex-reset-credits` 用于查看当前 Codex Desktop 登录账户可用的 reset credits, 包括可用数量和每个 credit 的过期时间.

当你想快速确认"我还有多少次 Codex rate limit reset, 分别什么时候过期"时, 使用这个 skill.

## 快速开始

让 Codex 使用这个 skill:

```text
$codex-reset-credits
```

也可以用自然语言提出请求:

```text
使用 $codex-reset-credits 查询我当前可用的 reset credits.
使用 $codex-reset-credits, 并用脱敏 JSON 展示结果.
```

## 输出格式

默认响应为 Markdown 表格, 按过期时间从近到远排序:

```markdown
Available reset credit count: 2
Total earned count: 1

| 序号 | 状态 | 过期时间 | 来源 |
| --- | --- | --- | --- |
| 1 | available | 2026-07-14 18:25:39 | @example |
| 2 | available | 2026-07-18 00:20:44 | Codex Team |
```

过期时间使用 UTC, 格式为 `YYYY-MM-DD HH:MM:SS`.

## 高级请求

需要时可以让 Codex 调整输出方式:

- "用脱敏 JSON 展示结果."
- "展示原始响应用于调试."
- "改用这个 auth 文件: `path/to/auth.json`."

## 注意事项

- 这个 skill 是 Codex only, 因为它依赖本机 Codex Desktop 登录态.
- 默认输出不会打印 access token 和完整 credit ID.
- 原始响应可能包含账户相关标识, 只在需要查看原始字段时请求.
