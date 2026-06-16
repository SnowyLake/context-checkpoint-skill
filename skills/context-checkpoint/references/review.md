# review 命令

## 目录

- [会话文件夹解析](#会话文件夹解析)
- [访问模式](#访问模式)
- [工作流](#工作流)
- [输出风格](#输出风格)

本说明文件只覆盖 `review` 命令. 使用时需要同时应用 `SKILL.md` 中的 `全局不变量`. 写入或校验 `REVIEW.md`, 或解读 `CONTEXT.md`, `HISTORY.md` 和 `Work Artifacts` 前, 必须先读取 `file-contracts.md`.

## 会话文件夹解析

解析被审阅会话文件夹:

1. 如果用户没有指定会话文件夹, 将当前会话文件夹解析为被审阅会话文件夹.
2. 如果用户指定了会话文件夹, 将其作为被审阅会话文件夹.
3. 如果当前会话文件夹不明确且用户未指定路径, 要求用户指定一个已有会话文件夹.
4. 不创建被审阅会话文件夹.
5. 不要把无路径 review 视为依赖当前对话记忆. 审阅目标仍然是被审阅会话文件夹中 checkpoint 导航到的实际工作内容.

## 访问模式

- 可以读取被审阅会话文件夹中的 checkpoint 文件和相关项目文件.
- 只能写被审阅会话文件夹中的 `REVIEW.md`. 这是 `review` 唯一允许的写入例外.
- 不得修改被审阅的 `CONTEXT.md`, 被审阅的 `HISTORY.md`, 其他被审阅会话文件夹产物或项目文件, 除非用户明确要求后续工作.
- 用最新审阅结果覆盖被审阅会话文件夹中已有的 `REVIEW.md`.
- 始终输出审阅结果, 并写入 `REVIEW.md`.
- 将 checkpoint 文件视为审阅简报和导航索引. 除非用户明确要求审阅 checkpoint 文件本身, 不要把 checkpoint 文件质量作为主要审阅目标.

## 工作流

1. 解析被审阅会话文件夹.
2. 确认被审阅会话文件夹存在.
3. 确认被审阅会话文件夹包含 `CONTEXT.md`.
4. 如果被审阅会话校验失败, 停止并报告问题. 不要创建 checkpoint 文件, 创建目标文件夹, 写入 `REVIEW.md`, 修改项目文件, 或搜索其他文件夹.
5. 读取被审阅的 `CONTEXT.md`.
6. 当被审阅的 `HISTORY.md` 存在时读取它.
7. 如果缺少 `HISTORY.md`, 继续 review, 并说明历史上下文有限.
8. 使用 `CONTEXT.md` 理解目标, 当前状态, 决策, 约束, 风险, 开放问题, `TODO`, 下一步行动, 相关文件和工作产物.
9. 从 `Current Goal`, `Work Artifacts`, `Relevant Files`, `TODO`, `Next Actions` 以及任何被审阅会话文件夹产物构建审阅范围.
10. 在产出 findings 前, 阅读代表该会话实际工作的被引用项目文件, 生成产物, diff, tests 或配置.
11. 审阅实际工作是否完成 `Current Goal`.
12. 审阅实际工作内容是否存在缺陷, 边界问题, 遗漏验证, 冲突或不一致.
13. 不要把普通 checkpoint 文件质量问题列为 `Findings`. 将 checkpoint 清晰度, 新鲜度, 缺失章节或内部一致性问题放入 `Checkpoint Quality`, 除非它们直接阻止目标完成度评估或隐藏工作范围.
14. 只有当用户要求审阅的目标, 或被审阅会话的 `Current Goal`, 明确是创建或更新 checkpoint 文件时, 才把 `CONTEXT.md` 和 `HISTORY.md` 作为主要工作产物审阅.
15. 不要将会话上下文 restore 成当前活跃工作上下文.
16. 如果被审阅会话文件夹中已有 `REVIEW.md`, 读取其中现有 findings. 对 `Open` findings 按当前工程事实重新验证, 尽量保留仍成立问题的原 finding ID.
17. 旧 `Open` finding 如果仍成立, 保留为 `Open`. 如果不再成立, 标记为 `Resolved`, 添加 `Resolution`, 并在本次 `REVIEW.md` 中保留一轮. 如果用户或项目决策明确不修复, 标记为 `Won't Fix`, 添加 `Resolution`.
18. 已是 `Resolved` 或 `Won't Fix` 的旧 findings 默认不继续保留在最新 `REVIEW.md`, 除非本次 review 需要说明清理结果.
19. 新发现的问题使用下一个稳定 finding ID, 并按 `file-contracts.md` 中的 finding 格式写入.
20. 将审阅结果写入被审阅会话文件夹的 `REVIEW.md`, 覆盖任何已有 `REVIEW.md`, 并同时在回复中输出.

## 输出风格

将结果写入被审阅会话文件夹的 `REVIEW.md`, 并在回复中输出相同结果. 两处都使用这些章节:

```md
## Goal Completion

## Findings

## Checkpoint Quality

## Open Questions

## Summary
```

审阅章节含义:

- `Goal Completion`: 说明 `Current Goal` 是 `Completed`, `Partially Completed`, `Not Completed` 还是 `Unclear`, 并简要解释证据.
- `Findings`: 按严重度排序列出实际被审阅工作中的具体问题. 包括实现缺陷, 逻辑缺口, 边界问题, 行为风险, 遗漏验证, 项目文件冲突, 或被审阅会话创建, 修改, 删除, 移动, 或以其他方式引用的文件中的不一致. 每条 finding 必须使用 `F-001` 形式的稳定 ID, 并包含 `Status`, `Severity`, `Impact`, `Evidence` 和 `Recommended Fix`. 如果检查相关文件后没有发现具体工作问题, 明确说明.
- `Checkpoint Quality`: 评估 `CONTEXT.md` 和可选 `HISTORY.md` 是否足够可靠, 能否支撑未来 restore, handoff 或 review. 包括 `Work Artifacts` 是否指向相关工作范围. 除非仅涉及 checkpoint 的问题直接阻塞实际工作评估, 否则放在这里.
- `Open Questions`: 列出无法从 checkpoint 文件和当前项目文件回答的问题.
- `Summary`: 给出简洁, 可行动的结论.

`REVIEW.md` 还会在这些章节之前记录 `Reviewed Session` 和 `Review Date` 标题, 具体见 `file-contracts.md`.
