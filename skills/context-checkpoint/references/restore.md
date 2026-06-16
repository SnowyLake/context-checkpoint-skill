# restore 命令

## 目录

- [会话文件夹解析](#会话文件夹解析)
- [访问模式](#访问模式)
- [工作流](#工作流)
- [输出风格](#输出风格)

本说明文件只覆盖 `restore` 命令. 使用时需要同时应用 `SKILL.md` 中的 `全局不变量`. 解读或总结 `CONTEXT.md`, `HISTORY.md`, `REVIEW.md` 或 `Work Artifacts` 前, 必须先读取 `file-contracts.md`.

## 会话文件夹解析

解析 restore 源会话文件夹:

1. 如果用户没有指定会话文件夹, 解析当前会话文件夹.
2. 如果用户指定了会话文件夹, 将其作为 restore 源.
3. 如果用户指定了另一个会话文件夹, 且当前对话自己的会话文件夹中已经存在 checkpoint 文件, 停止并报告冲突. 不要读取, 合并, 复制或修改任一 checkpoint.
4. 如果指定的会话文件夹就是当前会话文件夹, 允许 restore.
5. 如果当前文件夹不明确且用户未指定路径, 要求用户指定一个已有会话文件夹.
6. `restore` 不创建新会话文件夹.

## 访问模式

- 只读.
- 可以读取 restore 源会话文件夹中的 checkpoint 文件和相关项目文件.
- 当 restore 源会话文件夹中存在 `REVIEW.md` 时, 可以读取它, 并把其中 findings 浮出为待重新核验的待处理问题.
- 不得复制 checkpoint 文件, 写入当前会话文件夹, 或修改项目文件, 除非用户明确要求后续工作.

## 工作流

1. 解析 restore 源会话文件夹.
2. 如果用户指定了不同的源会话文件夹, 且当前对话自己的会话文件夹中已经存在 checkpoint 文件, 停止并报告冲突.
3. 当 `CONTEXT.md` 存在时, 先读取它.
4. 只有在需要理解决策背景, 排障依据, 已拒绝方案或历史不确定性时, 才读取 `HISTORY.md`.
5. 读取 `Work Artifacts`, 用于快速理解之前的工作范围.
6. 当 restore 源会话文件夹中存在 `REVIEW.md` 时读取它. 将其中 findings 浮出为待重新核验的待处理问题, 并说明它们反映的是 review 当时的工作状态, 必须对照当前项目文件重新检查.
7. 如果只有 `CONTEXT.md` 存在, 从它恢复.
8. 如果只有 `HISTORY.md` 存在, 尽可能重建背景, 并说明缺失当前状态快照.
9. 如果两个文件都不存在, 说明该会话文件夹中没有可用的 checkpoint 文件.
10. 不要把旧 history 当作当前状态.
11. 不要把未验证假设当作事实.
12. 如果 `HISTORY.md` 与 `CONTEXT.md` 冲突, 以 `CONTEXT.md` 作为当前状态依据.
13. 当恢复出的状态不完整, 来自推断, 或受冲突影响时, 说明信息来源和重建置信度.

执行 `restore` 时不要修改 checkpoint 文件, 除非用户明确要求同时更新它们.

## 输出风格

总结重建后的会话状态, 不要重复整份 `HISTORY.md`. 包含:

- 当前目标, 对应 `Current Goal`
- 当前状态, 对应 `Current State`
- 已确认决策, 对应 `Confirmed Decisions`
- 活跃约束, 对应 `Active Constraints`
- 已知风险, 对应 `Known Risks`
- 开放问题, 对应 `Open Questions`
- TODO
- 下一步行动, 对应 `Next Actions`
- 相关文件, 对应 `Relevant Files`
- 工作产物, 对应 `Work Artifacts`
- 重建状态的信息来源和置信度说明.
- 当源会话文件夹包含 `REVIEW.md` 时, 将其 findings 列为需要对照当前项目文件重新核验的待处理问题, 并说明它们反映的是 review 当时的工作状态.
