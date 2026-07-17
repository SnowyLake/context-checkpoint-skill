---
name: subagent-workflow
description: Delegate the current task through subagents.
disable-model-invocation: true
---

1. 读取当前环境适用的 Subagent 编排规则.
2. 使用可用的 Subagent 工具委派当前用户任务.
3. 按适用规则完成角色选择, 调用预告, 上下文交接, 顺序控制, 结果等待, 验证和整合.
4. 不直接执行被委派的任务. 如果无法调用 Subagent, 向用户报告阻塞原因.
