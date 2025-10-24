#!/usr/bin/env python3
"""
Chọn ngẫu nhiên N bài đủ điều kiện để tối ưu, cập nhật index.json,
và sinh OPTIMIZE_TODAY.md (checklist).
"""
import argparse
import datetime
import json
import pathlib
import random

ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.json"
OUT = ROOT / "OPTIMIZE_TODAY.md"


def load_index():
    if not INDEX.exists():
        raise SystemExit("index.json not found. Run scripts/new.py first.")
    return json.loads(INDEX.read_text())


def parse_date(s: str) -> datetime.date:
    return datetime.date.fromisoformat(s)


def eligible(entries, min_days: int, status: str):
    today = datetime.date.today()
    for e in entries:
        if status and e.get("status") != status:
            continue
        d = parse_date(e.get("date", str(today)))
        if (today - d).days < min_days:
            continue
        yield e


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=2)
    ap.add_argument("--min-days", type=int, default=7, help="min days since solved")
    ap.add_argument("--status", type=str, default="done", help="filter by status")
    ap.add_argument("--seed", type=int, default=None)
    args = ap.parse_args()

    data = load_index()
    entries = list(eligible(data.get("problems", []), args.min_days, args.status))
    if args.seed is not None:
        random.seed(args.seed)
    random.shuffle(entries)
    pick = entries[: args.count]

    if not pick:
        print("No eligible problems. Try lowering --min-days or check status.")
        return

    for e in data["problems"]:
        if e in pick:
            e["opt_rounds"] = int(e.get("opt_rounds", 0)) + 1
            e["status"] = "optimize"

    INDEX.write_text(json.dumps(data, indent=2))

    lines = ["# Optimize Today", f"- Date: {datetime.date.today().isoformat()}", ""]
    for i, e in enumerate(pick, 1):
        lines += [
            f"## {i}. {e['title']} ({e.get('difficulty','')})",
            f"- File: `{e['file']}`",
            f"- Link: {e.get('link','N/A')}",
            f"- Tags: {', '.join(e.get('tags', [])) or 'N/A'}",
            f"- Previous rounds: {int(e.get('opt_rounds', 1)) - 1}",
            "- Tasks:",
            "  - [ ] Viết test bổ sung (biên, stress).",
            "  - [ ] Refactor đặt tên, tách hàm, docstring.",
            "  - [ ] Kiểm tra độ phức tạp (Time/Space).",
            "  - [ ] Benchmark (nếu phù hợp) và lưu số liệu.",
            "",
        ]
    OUT.write_text("\n".join(lines))
    print(f"Selected {len(pick)} problems. See {OUT}")


if __name__ == "__main__":
    main()
