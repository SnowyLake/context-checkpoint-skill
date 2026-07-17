#!/usr/bin/env python3
"""Check Codex rate limit reset credit expirations for the current account."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ENDPOINT = "https://chatgpt.com/backend-api/wham/rate-limit-reset-credits"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Query Codex rate limit reset credits using ~/.codex/auth.json.",
    )
    parser.add_argument(
        "--auth",
        default="~/.codex/auth.json",
        help="Path to Codex auth.json. Defaults to ~/.codex/auth.json.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="Request timeout in seconds. Defaults to 30.",
    )
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Print the raw backend response instead of a redacted output.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the redacted summary as JSON instead of Markdown.",
    )
    return parser.parse_args()


def load_auth(path: str) -> tuple[str, str]:
    auth_path = Path(path).expanduser()
    try:
        auth = json.loads(auth_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RuntimeError(f"Codex auth file not found: {auth_path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Codex auth file is not valid JSON: {auth_path}") from exc

    tokens = auth.get("tokens")
    if not isinstance(tokens, dict):
        raise RuntimeError("Codex auth file does not contain a tokens object.")

    access_token = tokens.get("access_token")
    account_id = tokens.get("account_id")
    if not access_token or not account_id:
        raise RuntimeError("Codex auth file is missing tokens.access_token or tokens.account_id.")

    return str(access_token), str(account_id)


def fetch_reset_credits(access_token: str, account_id: str, timeout: float) -> dict[str, Any]:
    request = urllib.request.Request(
        ENDPOINT,
        headers={
            "Authorization": f"Bearer {access_token}",
            "ChatGPT-Account-ID": account_id,
            "OpenAI-Beta": "codex-1",
            "originator": "Codex Desktop",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def parse_utc(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def short_id(value: Any) -> str | None:
    if not isinstance(value, str) or not value:
        return None
    return value[-12:]


def utc_offset_label(value: datetime | None = None) -> str:
    local_time = value.astimezone() if value is not None else datetime.now().astimezone()
    offset = local_time.utcoffset()
    if offset is None:
        return "UTC"

    total_minutes = int(offset.total_seconds() // 60)
    sign = "+" if total_minutes >= 0 else "-"
    total_minutes = abs(total_minutes)
    hours, minutes = divmod(total_minutes, 60)
    if minutes == 0:
        return f"UTC{sign}{hours}"
    return f"UTC{sign}{hours}:{minutes:02d}"


def format_local_time(value: Any) -> str:
    parsed = parse_utc(value)
    if parsed is None:
        return str(value or "")
    return parsed.astimezone().strftime("%Y-%m-%d %H:%M:%S")


def sort_key(credit: dict[str, Any]) -> tuple[int, datetime]:
    expires_at = parse_utc(credit.get("expires_at"))
    if expires_at is None:
        return (1, datetime.max.replace(tzinfo=timezone.utc))
    return (0, expires_at)


def escape_markdown_cell(value: Any) -> str:
    return str(value or "").replace("|", "\\|")


def summarize(payload: dict[str, Any]) -> dict[str, Any]:
    now = datetime.now(timezone.utc)
    credits = payload.get("credits", [])
    if not isinstance(credits, list):
        credits = []

    summarized = []
    for credit in sorted((credit for credit in credits if isinstance(credit, dict)), key=sort_key):
        if not isinstance(credit, dict):
            continue

        expires_at = parse_utc(credit.get("expires_at"))
        granted_at = parse_utc(credit.get("granted_at"))
        expires_in_days = None
        if expires_at is not None:
            expires_in_days = round((expires_at - now).total_seconds() / 86400, 3)

        summarized.append(
            {
                "id_suffix": short_id(credit.get("id")),
                "reset_type": credit.get("reset_type"),
                "status": credit.get("status"),
                "granted_at": granted_at.isoformat().replace("+00:00", "Z") if granted_at else credit.get("granted_at"),
                "expires_at": expires_at.isoformat().replace("+00:00", "Z") if expires_at else credit.get("expires_at"),
                "expires_in_days": expires_in_days,
                "redeem_started_at": credit.get("redeem_started_at"),
                "redeemed_at": credit.get("redeemed_at"),
                "profile_user_id": credit.get("profile_user_id"),
                "title": credit.get("title"),
            }
        )

    return {
        "available_count": payload.get("available_count"),
        "total_earned_count": payload.get("total_earned_count"),
        "credits": summarized,
    }


def format_markdown(payload: dict[str, Any]) -> str:
    credits = payload.get("credits", [])
    if not isinstance(credits, list):
        credits = []
    sorted_credits = sorted((credit for credit in credits if isinstance(credit, dict)), key=sort_key)

    lines = [
        f"Available reset credit count: {payload.get('available_count')}",
        f"Total earned count: {payload.get('total_earned_count')}",
        "",
        f"| 序号 | 状态 | 过期时间 ({utc_offset_label()}) | 来源 |",
        "| --- | --- | --- | --- |",
    ]
    for index, credit in enumerate(sorted_credits, start=1):
        lines.append(
            "| "
            f"{index} | "
            f"{escape_markdown_cell(credit.get('status'))} | "
            f"{escape_markdown_cell(format_local_time(credit.get('expires_at')))} | "
            f"{escape_markdown_cell(credit.get('profile_user_id'))} |"
        )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        access_token, account_id = load_auth(args.auth)
        payload = fetch_reset_credits(access_token, account_id, args.timeout)
    except urllib.error.HTTPError as exc:
        print(f"HTTP {exc.code}: {exc.reason}", file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print(f"Network error: {exc.reason}", file=sys.stderr)
        return 1
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if args.raw:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    elif args.json:
        print(json.dumps(summarize(payload), ensure_ascii=False, indent=2))
    else:
        print(format_markdown(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
