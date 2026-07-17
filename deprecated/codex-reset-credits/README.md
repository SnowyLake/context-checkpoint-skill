# codex-reset-credits

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Output](#output)
- [Advanced Requests](#advanced-requests)
- [Notes](#notes)

Language: English | [中文](README.zh-CN.md)

## Overview

`codex-reset-credits` shows the reset credits available to the currently signed-in Codex Desktop account, including how many credits are available and when each credit expires.

Use it when you want a quick answer to: "How many Codex rate limit resets do I have, and when do they expire?"

## Quick Start

Ask Codex to use the skill:

```text
$codex-reset-credits
```

You can also ask in natural language:

```text
Use $codex-reset-credits to check my available reset credits.
Use $codex-reset-credits and show the result as redacted JSON.
```

## Output

The default response is a Markdown table sorted by expiration time, from soonest to latest:

```markdown
Available reset credit count: 2
Total earned count: 1

| 序号 | 状态 | 过期时间 (UTC+8) | 来源 |
| --- | --- | --- | --- |
| 1 | available | 2026-07-15 02:25:39 | @example |
| 2 | available | 2026-07-18 08:20:44 | Codex Team |
```

Expiration times are shown in the current device timezone as `YYYY-MM-DD HH:MM:SS`, and the table header includes the detected UTC offset.

## Advanced Requests

You can ask Codex for alternate output when needed:

- "Show the result as redacted JSON."
- "Show the raw response for debugging."
- "Use this auth file instead: `path/to/auth.json`."

## Notes

- This skill is Codex only because it depends on the local Codex Desktop sign-in state.
- The default output avoids printing access tokens and full credit IDs.
- Raw output may include account-related identifiers, so request it only when you need the original response fields.
