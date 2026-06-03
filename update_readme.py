"""
Scans main/*.py, extracts problem metadata from docstrings,
and regenerates the tracker section in README.md.
"""

import glob
import os
import re
from datetime import date

MAIN_DIR = os.path.join(os.path.dirname(__file__), "main")
README_PATH = os.path.join(os.path.dirname(__file__), "README.md")
START_MARKER = "<!-- TRACKER_START -->"
END_MARKER = "<!-- TRACKER_END -->"

DIFF_ORDER = ["Easy", "Medium", "Hard"]
DIFF_COLOR = {"Easy":   "🟢", "Medium": "🟡", "Hard":   "🔴"}
BAR_WIDTH = 24


def parse_problem(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    m = re.search(r'Problem:\s*(\d+)\s*-\s*(.+)', content)
    d = re.search(r'Difficulty:\s*(\w+)', content)
    l = re.search(r'Link:\s*\n(https?://\S+)', content)
    if not m:
        return None
    return {
        "number": int(m.group(1)),
        "title":  m.group(2).strip(),
        "difficulty": d.group(1).strip() if d else "Unknown",
        "link":   l.group(1).strip() if l else "",
    }


def make_bar(count, total):
    filled = round(count / total * BAR_WIDTH) if total else 0
    return "█" * filled + "░" * (BAR_WIDTH - filled)


def pct(count, total):
    return f"{round(count / total * 100)}%" if total else "0%"


def build_tracker(problems):
    problems.sort(key=lambda p: p["number"])
    total = len(problems)
    counts = {d: sum(1 for p in problems if p["difficulty"] == d) for d in DIFF_ORDER}
    today = date.today().strftime("%B %d, %Y")

    lines = [
        "## 📊 Progress tracker",
        "",
        f"**{total} problem{'s' if total != 1 else ''} solved** &nbsp;·&nbsp; _last updated {today}_",
        "",
        "```",
    ]

    # Aligned difficulty bars
    label_w = max(len(d) for d in DIFF_ORDER)
    count_w = len(str(total))
    for diff in DIFF_ORDER:
        c = counts[diff]
        bar = make_bar(c, total)
        p = pct(c, total)
        label = diff.ljust(label_w)
        count_str = str(c).rjust(count_w)
        lines.append(f"  {label}  {bar}  {count_str} ({p})")

    lines += [
        "```",
        "",
    ]

    # Problems table
    lines += [
        "| # | Title | Difficulty |",
        "|--:|-------|------------|",
    ]
    for p in problems:
        emoji = DIFF_COLOR.get(p["difficulty"], "⚪")
        title_cell = f"[{p['title']}]({p['link']})" if p["link"] else p["title"]
        lines.append(f"| {p['number']} | {title_cell} | {emoji} {p['difficulty']} |")

    lines.append("")
    return "\n".join(lines)


def update_readme(tracker_block):
    with open(README_PATH, encoding="utf-8") as f:
        content = f.read()

    new_section = f"{START_MARKER}\n{tracker_block}{END_MARKER}"

    if START_MARKER in content and END_MARKER in content:
        content = re.sub(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            new_section,
            content,
            flags=re.DOTALL,
        )
    else:
        content = content.rstrip("\n") + "\n\n" + new_section + "\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    paths = glob.glob(os.path.join(MAIN_DIR, "*.py"))
    problems = [p for p in (parse_problem(path) for path in paths) if p]
    tracker = build_tracker(problems)
    update_readme(tracker)
    print(f"README updated — {len(problems)} problem(s) tracked.")


if __name__ == "__main__":
    main()
