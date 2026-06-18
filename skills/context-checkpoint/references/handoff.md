# handoff 命令

## 目录

- [会话文件夹解析](#会话文件夹解析)
- [访问模式](#访问模式)
- [工作流](#工作流)
- [源会话文件夹保护规则](#源会话文件夹保护规则)
- [非 Checkpoint 产物处理](#非-checkpoint-产物处理)
- [目标 Checkpoint 处理](#目标-checkpoint-处理)
- [输出风格](#输出风格)

本说明文件只覆盖 `handoff` 命令. 使用时需要同时应用 `SKILL.md` 中的 `全局不变量`. 写入或校验目标 `CONTEXT.md`, 目标 `HISTORY.md`, handoff 条目或 `Work Artifacts` 前, 必须先读取 `file-contracts.md`.

## 会话文件夹解析

`handoff` 解析两个会话文件夹:

- 源会话文件夹: `handoff` 读取的旧会话文件夹.
- 目标会话文件夹: `handoff` 写入的当前对话会话文件夹.

解析源会话文件夹时:

1. 如果用户指定了源会话文件夹, 使用它.
2. 如果用户没有指定源会话文件夹, 要求用户指定一个已有会话文件夹.
3. 不创建源会话文件夹.

解析目标会话文件夹时:

1. 将目标会话文件夹解析为三种状态: 明确有, 明确没有, 不确定.
2. 明确有: 当前对话或用户输入中已经明确指向一个目标会话文件夹时, 使用它.
3. 明确没有: 当前对话没有任何可用目标会话文件夹线索, 且用户请求本身是在把源 checkpoint 接管, 迁移或分支到新会话时, 自动创建新的目标会话文件夹.
4. 不确定: 当前对话存在会话文件夹线索, 但无法可靠判断哪一个是目标会话文件夹, 或用户同时提到多个路径但没有标明角色时, 询问用户指定已有目标会话文件夹或确认创建新目标会话文件夹.
5. 不要检查 `.agent-sessions/` 来猜测语义匹配的目标文件夹, 除非用户明确要求发现或列出候选.
6. 创建新目标会话文件夹后, 在输出中说明新建的文件夹路径.
7. 如果目标会话文件夹已经存在 checkpoint 文件, 停止并报告冲突. 不要读取, 合并, 复制或修改任一 checkpoint.
8. 不要把源会话文件夹用作目标会话文件夹.

## 访问模式

- 源会话文件夹只读.
- 目标会话文件夹可读写.
- 只可以复制源会话文件夹内部的非 checkpoint 产物.
- 不得复制项目文件或源会话文件夹之外的任何文件, 即使 `Work Artifacts` 引用了它们.
- 不得修改项目文件, 除非用户明确要求后续工作.

## 工作流

1. 解析源会话文件夹.
2. 确认源会话文件夹存在.
3. 确认源会话文件夹包含 `CONTEXT.md`.
4. 如果源校验失败, 停止并报告问题. 不要创建 checkpoint 文件, 创建目标文件夹, 分类产物, 复制文件, 或搜索其他文件夹.
5. 解析目标会话文件夹.
6. 如果目标会话文件夹已经存在 `CONTEXT.md` 或 `HISTORY.md`, 停止并报告冲突. 不要读取, 合并, 复制或修改任一 checkpoint.
7. 读取源 `CONTEXT.md`.
8. 当源 `HISTORY.md` 存在时读取它.
9. 读取 `Work Artifacts`, 用于快速理解之前的工作范围.
10. 扫描源会话文件夹中的其他文件.
11. 将源会话文件夹内部的非 checkpoint 文件分类为仍然相关的产物或历史 / 过期产物. 对源 `REVIEW.md` 使用下方专门规则, 不按普通产物复制.
12. 根据分类决定复制或丢弃哪些非 checkpoint 源文件夹产物, 不等待用户确认.
13. 在 handoff 条目和最终输出中记录已复制和已丢弃产物, 方便用户按需要求后续修正.
14. 创建或更新目标会话文件夹.
15. 将目标 `CONTEXT.md` 写为重建后的当前状态快照.
16. 写入目标 `HISTORY.md`, 保留有用的源历史, 并追加一个 handoff 条目.
17. 将仍然相关的产物从源会话文件夹复制到目标会话文件夹.
18. 必要时将目标 `CONTEXT.md`, 目标 `HISTORY.md` 和已复制产物中的引用从源路径改写为目标路径. 不得改写从源 `REVIEW.md` 保留下来的历史审阅文件中的 `Reviewed Session`.
19. 校验已复制文件和已改写引用.
20. 报告源文件夹, 目标文件夹, 已复制文件, 已丢弃文件和已更新文件.

## 源会话文件夹保护规则

- 源文件只读.
- `handoff` 要求源会话文件夹中必须存在 `CONTEXT.md`.
- 如果源会话文件夹不存在, 停止并报告问题.
- 如果源会话文件夹存在但不包含 `CONTEXT.md`, 停止并报告缺少 `CONTEXT.md`.
- 如果源会话文件夹只包含 `HISTORY.md` 或其他生成文档, 停止并报告缺少 `CONTEXT.md`.
- 当源校验失败时, 不要创建 checkpoint 文件, 推断缺失 checkpoint 内容, 创建目标文件夹, 分类产物, 复制文件, 或搜索其他文件夹.

## 非 Checkpoint 产物处理

- 只分类源会话文件夹内部的非 checkpoint 文件.
- 不要复制项目文件或源会话文件夹之外的任何文件.
- 使用源 `CONTEXT.md` 中的 `Relevant Files`, `Work Artifacts`, `TODO`, `Next Actions` 和 `Known Risks` 等章节来分类源文件夹产物.
- 仍会影响未来决策或实现的源文件夹文件视为仍然相关的产物.
- 已拒绝, 已暂缓, 已被取代, 过期或纯历史过程文档视为历史 / 过期产物.
- 复制或丢弃非 checkpoint 源文件夹产物前, 不停下来请求确认.
- 在 handoff 条目和最终输出中记录已复制和已丢弃产物, 方便用户审阅并要求后续修正.
- `Discarded` 表示没有复制到目标会话文件夹. 绝不删除源文件.
- 源 `REVIEW.md` 默认视为历史 / 过期产物并丢弃, 因为它审阅的是源会话文件夹, 不是目标会话文件夹.
- 不得将源 `REVIEW.md` 复制为目标 `REVIEW.md`.
- 如果用户明确要求保留源 `REVIEW.md`, 只能把它复制为非活跃历史文件, 例如 `REVIEW.from-{source-session-folder-name}.md`, 并记录在 handoff entry 的 copied files 中. `{source-session-folder-name}` 只取源会话文件夹的末段名称, 例如 `20260605-example-session`, 不得使用完整路径.
- 保留源 `REVIEW.md` 时, 不得改写其中的 `Reviewed Session`. 该字段必须继续指向原被审阅会话文件夹.
- 目标会话文件夹中名为 `REVIEW.md` 的文件只能由 `review` 生成, 不由 `handoff` 从源会话文件夹复制得到.

## 目标 Checkpoint 处理

- 如果目标会话文件夹已经存在 `CONTEXT.md` 或 `HISTORY.md`, `handoff` 必须停止并报告冲突. 不要读取, 合并, 复制或修改任一 checkpoint.
- 目标 `CONTEXT.md` 必须是干净的当前状态快照, 不是源 `CONTEXT.md` 的机械复制.
- 目标 `CONTEXT.md` 必须在 `Current State` 下包含一条简洁来源说明, 标明源会话文件夹.
- 详细 handoff records 属于目标 `HISTORY.md`, 不属于目标 `CONTEXT.md`.
- 目标 `HISTORY.md` 必须保留有用的源历史, 并追加一个 handoff 条目.
- Handoff entry 必须记录源文件夹, 目标文件夹, 已复制 checkpoint 文件, 已复制产物, 已丢弃产物, 引用改写, 用户要求的修正, 缺失的可选源文件和未解决的不确定性. Handoff entry 结构见 `file-contracts.md`.

## 输出风格

先包含一段简短 handoff 结果摘要:

- 源会话文件夹
- 目标会话文件夹
- 已更新 checkpoint 文件
- 已复制产物
- 已丢弃产物
- 引用改写
- 未解决风险或开放问题

然后总结重建后的会话状态, 不要重复整份 `HISTORY.md`. 包含:

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
- 重建状态的信息来源和置信度说明
