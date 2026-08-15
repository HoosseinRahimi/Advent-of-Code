from __future__ import annotations

import argparse
import re
from pathlib import Path

Instruction = tuple[str, int]
INSTRUCTION_RE = re.compile(r"([LR])(\d+)")


def parse_instruction(line: str) -> Instruction:
    match = INSTRUCTION_RE.fullmatch(line.strip())
    if not match:
        raise ValueError(f"invalid instruction: {line!r}")
    direction, distance = match.groups()
    return direction, int(distance)


def read_instructions(file_name: str | Path) -> list[Instruction]:
    instructions: list[Instruction] = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                instructions.append(parse_instruction(line))
            except ValueError as exc:
                raise ValueError(f"line {line_number}: {exc}") from exc
    return instructions


def count_zero_crossings(
    instructions: list[Instruction],
    *,
    start: int = 50,
    dial_size: int = 100,
) -> int:
    """Count every individual dial step that arrives at zero."""
    if dial_size <= 0:
        raise ValueError("dial_size must be positive")

    position = start % dial_size
    counter = 0

    for direction, distance in instructions:
        if direction not in {"L", "R"}:
            raise ValueError(f"unknown direction: {direction!r}")

        delta = 1 if direction == "R" else -1
        for _ in range(distance):
            position = (position + delta) % dial_size
            if position == 0:
                counter += 1

    return counter


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2025 — Day 1, Part 2")
    parser.add_argument("input", type=Path, help="Path to the puzzle input file")
    args = parser.parse_args()

    print(count_zero_crossings(read_instructions(args.input)))


if __name__ == "__main__":
    main()
