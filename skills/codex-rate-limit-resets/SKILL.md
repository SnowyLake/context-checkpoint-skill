---
name: codex-rate-limit-resets
description: Query the current Codex account's available rate limit reset credits and expiration times.
---

# Codex Rate Limit Resets

## 目录

- [概览](#概览)
- [执行流程](#执行流程)
- [输出要求](#输出要求)
- [故障处理](#故障处理)

## 概览

查询当前机器上 Codex Desktop 登录账户的 rate limit reset credits, 包括可用数量, 获取时间, 过期时间, 兑换状态和来源标识.

优先使用 `scripts/check_reset_credits.py`, 它会从 `~/.codex/auth.json` 读取当前 Codex 登录态, 调用 `https://chatgpt.com/backend-api/wham/rate-limit-reset-credits`, 并默认输出脱敏后的 JSON 摘要.

## 执行流程

1. 说明本操作会读取本机 `~/.codex/auth.json` 并访问 `chatgpt.com`; 不要输出 access token.
2. 运行脚本:

```bash
python scripts/check_reset_credits.py
```

3. 如果当前 shell 不是 skill 目录, 使用脚本的完整路径运行.
4. 如果运行环境限制网络, 文件系统或远程认证访问, 按当前宿主的权限流程请求必要授权后重试.
5. 将脚本输出转述给用户. 默认输出已经脱敏, 通常可以直接汇总其中的 `available_count`, `total_earned_count` 和每个 credit 的 `expires_at`.

可选参数:

- `--raw`: 输出后端原始 JSON. 只有在用户明确需要排查接口字段时使用, 因为原始响应可能包含邮箱, 头像 URL 或用户标识.
- `--auth PATH`: 指定其他 `auth.json` 路径.
- `--timeout SECONDS`: 调整请求超时时间.

## 输出要求

- 不要输出或记录 `access_token`.
- 默认不要展示完整 credit `id`; 如果用户需要排查, 只展示末尾 8 到 12 位即可.
- 优先展示 UTC 原始过期时间 `expires_at`; 如需要本地时间, 明确标注时区.
- 如果 `status` 不是 `available`, 保留该状态, 不要把它计入可用机会.
- 不要把此接口当成稳定公开 API. 如果字段缺失或响应格式变化, 如实说明并展示可确认字段.

## 故障处理

- `~/.codex/auth.json` 不存在: 告诉用户当前机器没有可用 Codex 登录态, 需要先登录 Codex Desktop.
- `access_token` 或 `account_id` 缺失: 说明 auth 文件结构与预期不一致, 不要猜测 token 位置; 可在不输出敏感值的前提下检查顶层键名.
- `401` 或 `403`: 说明登录态可能过期, 账户不匹配, 或后端权限拒绝; 建议用户重新登录 Codex Desktop 后重试.
- 网络, DNS 或超时错误: 说明是访问 `chatgpt.com` 失败, 可稍后重试或在允许网络访问的环境中运行.
