from __future__ import annotations

import argparse
from pathlib import Path

Range = tuple[int, int]


def read_ranges(file_name: str | Path) -> list[Range]:
    text = Path(file_name).read_text(encoding="utf-8")
    tokens = [token.strip() for token in text.replace("\n", ",").split(",")]

    ranges: list[Range] = []
    for token in tokens:
        if not token:
            continue
        try:
            start_text, end_text = token.split("-", maxsplit=1)
            start, end = int(start_text), int(end_text)
        except (ValueError, TypeError) as exc:
            raise ValueError(f"invalid range: {token!r}") from exc
        if start > end:
            raise ValueError(f"range start must not exceed end: {token!r}")
        ranges.append((start, end))
    return ranges


def is_double_pattern(value: int) -> bool:
    text = str(value)
    midpoint = len(text) // 2
    return len(text) % 2 == 0 and text[:midpoint] == text[midpoint:]


def sum_double_patterns(ranges: list[Range]) -> int:
    return sum(
        value
        for start, end in ranges
        for value in range(start, end + 1)
        if is_double_pattern(value)
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2025 — Day 2, Part 1")
    parser.add_argument("input", type=Path, help="Path to the puzzle input file")
    args = parser.parse_args()

    print(sum_double_patterns(read_ranges(args.input)))


if __name__ == "__main__":
    main()
