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


def count_zero_landings(
    instructions: list[Instruction],
    *,
    start: int = 50,
    dial_size: int = 100,
) -> int:
    """Count instructions that leave the dial exactly at zero."""
    if dial_size <= 0:
        raise ValueError("dial_size must be positive")

    position = start % dial_size
    counter = 0

    for direction, distance in instructions:
        if direction == "R":
            position = (position + distance) % dial_size
        elif direction == "L":
            position = (position - distance) % dial_size
        else:
            raise ValueError(f"unknown direction: {direction!r}")

        if position == 0:
            counter += 1

    return counter


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2025 — Day 1, Part 1")
    parser.add_argument("input", type=Path, help="Path to the puzzle input file")
    args = parser.parse_args()

    print(count_zero_landings(read_instructions(args.input)))


if __name__ == "__main__":
    main()
