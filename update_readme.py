"""
Scans main/*.py, extracts problem metadata from docstrings,
and regenerates the tracker section in README.md.
"""

import glob
import os
import re
from datetime import date

MAIN_DIR = os.path.join(os.path.dirname(__file__), "main")


def get_github_base():
    import subprocess
    try:
        remote = subprocess.check_output(
            ["git", "remote", "get-url", "origin"],
            cwd=os.path.dirname(__file__),
            stderr=subprocess.DEVNULL,
        ).decode().strip()
        # Handle both HTTPS and SSH formats:
        # https://github.com/user/repo.git
        # git@github.com:user/repo.git
        remote = remote.removesuffix(".git")
        if remote.startswith("git@"):
            remote = re.sub(r"git@(.+?):", r"https://\1/", remote)
        return f"{remote}/blob/main/main"
    except Exception:
        return "https://github.com"


GITHUB_BASE = get_github_base()
README_PATH = os.path.join(os.path.dirname(__file__), "README.md")
START_MARKER = "<!-- TRACKER_START -->"
END_MARKER = "<!-- TRACKER_END -->"

DIFF_ORDER = ["Easy", "Medium", "Hard"]
DIFF_COLOR = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
DIFF_BADGE = {"Easy": "4c8b5e", "Medium": "8b7c4c", "Hard": "8b4c4c"}


def parse_problem(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    m = re.search(r'Problem:\s*(\d+)\s*-\s*(.+)', content)
    d = re.search(r'Difficulty:\s*(\w+)', content)
    l = re.search(r'Link:\s*\n(https?://\S+)', content)
    if not m:
        return None
    filename = os.path.basename(path)
    return {
        "number": int(m.group(1)),
        "title":  m.group(2).strip(),
        "difficulty": d.group(1).strip() if d else "Unknown",
        "link":   l.group(1).strip() if l else "",
        "impl":   f"{GITHUB_BASE}/{filename}",
    }


def badge(diff, count):
    color = DIFF_BADGE[diff]
    label = f"{diff}%20%E2%80%93%20{count}"
    return f"![{diff}](https://img.shields.io/badge/{label}-{color}?style=flat-square)"


def build_tracker(problems):
    problems.sort(key=lambda p: p["number"])
    total = len(problems)
    counts = {d: sum(1 for p in problems if p["difficulty"] == d) for d in DIFF_ORDER}
    today = date.today().strftime("%B %d, %Y")

    badges = " &nbsp; ".join(badge(d, counts[d]) for d in DIFF_ORDER)
    total_badge = f"![Total](https://img.shields.io/badge/Total%20solved-{total}-555555?style=flat-square)"

    lines = [
        "## 📊 Progress tracker",
        "",
        f"{total_badge} &nbsp; {badges}",
        "",
        f"_last updated {today}_",
        "",
    ]

    # One collapsible section per difficulty
    for diff in DIFF_ORDER:
        group = [p for p in problems if p["difficulty"] == diff]
        if not group:
            continue
        emoji = DIFF_COLOR[diff]
        lines.append(f"<details>")
        lines.append(f"<summary><b>{emoji} {diff} ({len(group)})</b></summary>")
        lines.append("")
        lines.append("| # | Title | Solution |")
        lines.append("|--:|-------|:--------:|")
        for p in group:
            title_cell = f"[{p['title']}]({p['link']})" if p["link"] else p["title"]
            impl_cell  = f"[`code`]({p['impl']})"
            lines.append(f"| {p['number']} | {title_cell} | {impl_cell} |")
        lines.append("")
        lines.append("</details>")
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
