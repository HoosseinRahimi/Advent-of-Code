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


def has_repeated_pattern(value: int) -> bool:
    text = str(value)
    length = len(text)

    for unit_length in range(1, length // 2 + 1):
        if length % unit_length != 0:
            continue
        repeat_count = length // unit_length
        if repeat_count >= 2 and text[:unit_length] * repeat_count == text:
            return True

    return False


def sum_repeated_patterns(ranges: list[Range]) -> int:
    return sum(
        value
        for start, end in ranges
        for value in range(start, end + 1)
        if has_repeated_pattern(value)
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2025 — Day 2, Part 2")
    parser.add_argument("input", type=Path, help="Path to the puzzle input file")
    args = parser.parse_args()

    print(sum_repeated_patterns(read_ranges(args.input)))


if __name__ == "__main__":
    main()
