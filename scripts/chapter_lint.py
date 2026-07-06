#!/usr/bin/env python3
"""Lightweight chapter linter for 自动化规划写小说skill projects.

The linter is read-only. It reports measurable pre-landing and review risks:
length, quote hygiene, repeated lines, punctuation density, contrast-shell
patterns, and basic project-file alignment.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Iterable


CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
HEADING_RE = re.compile(r"^\s{0,3}#")
CHAPTER_NUM_RE = re.compile(r"第\s*\d+\s*章")
CONTRAST_PATTERNS = [
    re.compile(r"不是[^。！？\n]{1,40}[，。—-](?:而)?是[^。！？\n]{1,40}"),
    re.compile(r"不是[^。！？\n]{1,40}而是[^。！？\n]{1,40}"),
    re.compile(r"不只是[^。！？\n]{1,40}更是[^。！？\n]{1,40}"),
    re.compile(r"不仅是[^。！？\n]{1,40}也是[^。！？\n]{1,40}"),
    re.compile(r"不像[^。！？\n]{1,40}更像[^。！？\n]{1,40}"),
]
ABSTRACT_LABEL_RE = re.compile(
    r"(声音|语气|眼神|神色|呼吸|情绪|表情|整个人).{0,4}(很稳|很平|很冷|很静|很淡|很疯|很危险|不冷|不急|不快|不慢)"
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def body_lines(text: str) -> list[str]:
    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if HEADING_RE.match(line):
            continue
        if line in {"---", "***"}:
            continue
        lines.append(line)
    return lines


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def count_cjk(text: str) -> int:
    return len(CJK_RE.findall(text))


def line_hits(lines: Iterable[str], pattern: re.Pattern[str]) -> list[dict[str, object]]:
    hits = []
    for idx, line in enumerate(lines, start=1):
        if pattern.search(line):
            hits.append({"line": idx, "text": line[:160]})
    return hits


def repeated_adjacent_lines(lines: list[str]) -> list[dict[str, object]]:
    hits = []
    previous = None
    for idx, line in enumerate(lines, start=1):
        normalized = re.sub(r"\s+", "", line)
        if normalized and normalized == previous:
            hits.append({"line": idx, "text": line[:160]})
        previous = normalized
    return hits


def repeated_sentences(text: str) -> list[dict[str, object]]:
    sentences = re.split(r"(?<=[。！？!?])", text)
    seen: dict[str, int] = {}
    hits = []
    for idx, sentence in enumerate(sentences, start=1):
        normalized = re.sub(r"\s+", "", sentence)
        if len(normalized) < 12:
            continue
        if normalized in seen:
            hits.append({"sentence_index": idx, "first_seen": seen[normalized], "text": sentence[:160]})
        else:
            seen[normalized] = idx
    return hits


def contrast_hits(lines: list[str]) -> list[dict[str, object]]:
    hits = []
    for idx, line in enumerate(lines, start=1):
        for pattern in CONTRAST_PATTERNS:
            for match in pattern.finditer(line):
                hits.append({"line": idx, "text": match.group(0)[:160]})
    return hits


def question_period_hits(lines: list[str]) -> list[dict[str, object]]:
    # Conservative Chinese heuristic: interrogative markers before a sentence-ending period.
    pattern = re.compile(
        r"(吗|呢|为什么|怎么了|怎么会|谁|哪里|哪儿|哪边|哪种|多少|多久|几点了|几号|几天|几次|能不能|可不可以|做什么|什么事)[^。！？!?]{0,12}。"
    )
    hits = []
    for idx, line in enumerate(lines, start=1):
        for match in pattern.finditer(line):
            hits.append({"line": idx, "text": match.group(0)[:160]})
    return hits


def find_control_cards(project_root: Path, chapter_num: str | None, title: str | None) -> list[str]:
    cards_dir = project_root / "control-cards"
    if not cards_dir.exists():
        return []
    candidates = []
    for path in cards_dir.glob("*.md"):
        if ".tmp." in path.name:
            continue
        name = path.name
        if chapter_num and re.search(rf"(^|[^0-9])0*{re.escape(chapter_num)}([^0-9]|$)", name):
            candidates.append(str(path))
            continue
        if title and title in name:
            candidates.append(str(path))
    return sorted(set(candidates))


def infer_chapter_id(path: Path, text: str) -> tuple[str | None, str | None]:
    name_match = re.search(r"(\d+)[-_ ]?([^\\/]+?)?\.md$", path.name)
    chapter_num = name_match.group(1) if name_match else None
    title = None
    for line in text.splitlines()[:5]:
        heading = line.strip().lstrip("#").strip()
        m = re.search(r"第\s*(\d+)\s*章\s*(.+)?", heading)
        if m:
            chapter_num = chapter_num or m.group(1)
            title = (m.group(2) or "").strip() or title
            break
    if not title and name_match and name_match.group(2):
        title = name_match.group(2).replace("-control-card", "").strip("-_ ")
    return chapter_num, title


def lint_chapter(path: Path, project_root: Path | None, floor: int) -> dict[str, object]:
    text = read_text(path)
    lines = body_lines(text)
    body = "\n".join(lines)
    chapter_num, title = infer_chapter_id(path, text)

    metrics = {
        "sha256": sha256_text(text),
        "cjk_chars": count_cjk(body),
        "non_whitespace_chars": len(re.sub(r"\s+", "", body)),
        "total_lines": len(text.splitlines()),
        "non_empty_body_lines": len(lines),
    }

    punctuation = {
        "english_double_quotes": text.count('"'),
        "english_single_quotes": text.count("'"),
        "left_double_quotes": text.count("“"),
        "right_double_quotes": text.count("”"),
        "left_single_quotes": text.count("‘"),
        "right_single_quotes": text.count("’"),
        "em_dash_pairs": text.count("——"),
        "ellipsis": text.count("……"),
        "period": text.count("。"),
        "comma": text.count("，"),
        "question": text.count("？"),
        "exclamation": text.count("！"),
        "colon": text.count("："),
        "semicolon": text.count("；"),
        "enumeration_comma": text.count("、"),
    }

    issues: list[dict[str, object]] = []

    if metrics["cjk_chars"] < floor:
        issues.append({"severity": "C", "code": "word_floor", "message": f"CJK count below floor {floor}"})
    if punctuation["english_double_quotes"]:
        issues.append({"severity": "C", "code": "english_double_quotes", "message": "English double quotes found"})
    if punctuation["english_single_quotes"]:
        issues.append({"severity": "B", "code": "english_single_quotes", "message": "English single quotes found"})
    if punctuation["left_double_quotes"] != punctuation["right_double_quotes"]:
        issues.append({"severity": "C", "code": "unpaired_double_quotes", "message": "Chinese double quotes are not paired"})
    if punctuation["left_single_quotes"] != punctuation["right_single_quotes"]:
        issues.append({"severity": "B", "code": "unpaired_single_quotes", "message": "Chinese single quotes are not paired"})
    if punctuation["em_dash_pairs"] > 6:
        issues.append({"severity": "C", "code": "em_dash_density", "message": "Em dash count above strict review threshold"})
    elif punctuation["em_dash_pairs"] > 4:
        issues.append({"severity": "B", "code": "em_dash_density", "message": "Em dash count in warning range"})

    duplicates = repeated_adjacent_lines(lines)
    if duplicates:
        issues.append({"severity": "C", "code": "adjacent_duplicate_lines", "message": "Adjacent duplicate lines found", "hits": duplicates[:10]})

    repeated = repeated_sentences(body)
    if repeated:
        issues.append({"severity": "B", "code": "repeated_sentences", "message": "Repeated sentences found", "hits": repeated[:10]})

    contrasts = contrast_hits(lines)
    if len(contrasts) > 8:
        issues.append({"severity": "C", "code": "contrast_shell_density", "message": "Contrast-shell pattern count above strict threshold", "hits": contrasts[:20]})
    elif len(contrasts) > 5:
        issues.append({"severity": "B", "code": "contrast_shell_density", "message": "Contrast-shell pattern count in warning range", "hits": contrasts[:20]})

    question_periods = question_period_hits(lines)
    if question_periods:
        issues.append({"severity": "B", "code": "question_period", "message": "Possible question sentence ending with period", "hits": question_periods[:20]})

    abstract_labels = line_hits(lines, ABSTRACT_LABEL_RE)
    if abstract_labels:
        issues.append({"severity": "B", "code": "abstract_state_labels", "message": "Possible abstract state labels", "hits": abstract_labels[:20]})

    chapter_leaks = []
    for idx, line in enumerate(lines, start=1):
        if CHAPTER_NUM_RE.search(line) and not line.startswith("#"):
            chapter_leaks.append({"line": idx, "text": line[:160]})
    if chapter_leaks:
        issues.append({"severity": "C", "code": "chapter_number_leak", "message": "Chapter number reference appears in body", "hits": chapter_leaks[:20]})

    cards = find_control_cards(project_root, chapter_num, title) if project_root else []
    if project_root is not None:
        if not cards:
            issues.append({"severity": "C", "code": "missing_control_card", "message": "No matching control card found"})
        elif len(cards) > 1:
            issues.append({"severity": "B", "code": "multiple_control_cards", "message": "Multiple possible control cards found", "hits": cards})

    return {
        "chapter_path": str(path),
        "project_root": str(project_root) if project_root else None,
        "chapter_num": chapter_num,
        "title": title,
        "metrics": metrics,
        "punctuation": punctuation,
        "pattern_counts": {
            "adjacent_duplicate_lines": len(duplicates),
            "repeated_sentences": len(repeated),
            "contrast_shells": len(contrasts),
            "question_periods": len(question_periods),
            "abstract_state_labels": len(abstract_labels),
            "chapter_number_leaks": len(chapter_leaks),
            "matching_control_cards": len(cards),
        },
        "matching_control_cards": cards,
        "issues": issues,
    }


def print_text_report(result: dict[str, object]) -> None:
    print(f"chapter: {result['chapter_path']}")
    print(f"chapter_num: {result.get('chapter_num')} title: {result.get('title')}")
    print("\nmetrics:")
    for key, value in result["metrics"].items():
        print(f"  {key}: {value}")
    print("\npunctuation:")
    for key, value in result["punctuation"].items():
        print(f"  {key}: {value}")
    print("\npattern_counts:")
    for key, value in result["pattern_counts"].items():
        print(f"  {key}: {value}")
    print("\nissues:")
    for issue in result["issues"]:
        print(f"  [{issue['severity']}] {issue['code']}: {issue['message']}")
        for hit in issue.get("hits", [])[:5]:
            print(f"    - {hit}")
    if not result["issues"]:
        print("  none")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint an 自动化规划写小说skill chapter manuscript.")
    parser.add_argument("chapter", type=Path, help="Path to chapter markdown file")
    parser.add_argument("--project-root", type=Path, default=None, help="Project root containing control-cards/")
    parser.add_argument("--floor", type=int, default=3000, help="CJK character floor")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args(argv)

    chapter = args.chapter.resolve()
    project_root = args.project_root.resolve() if args.project_root else chapter.parent.parent
    result = lint_chapter(chapter, project_root, args.floor)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_text_report(result)

    return 1 if result["issues"] else 0


if __name__ == "__main__":
    sys.exit(main())
