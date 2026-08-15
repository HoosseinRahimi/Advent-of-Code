# Advent of Code Solutions

[![Tests](https://github.com/HoosseinRahimi/Advent-of-Code/actions/workflows/tests.yml/badge.svg)](https://github.com/HoosseinRahimi/Advent-of-Code/actions/workflows/tests.yml)

My Python solutions and experiments for **Advent of Code**.

This repository keeps solution code organised by year and day while leaving personal puzzle input files out of version control.

> Advent of Code is created by Eric Wastl. This repository contains my solution code, not copies of the puzzle statements or personal input data.

## Current Progress

### 2025

| Day | Part 1 | Part 2 | Language |
|---|:---:|:---:|---|
| Day 1 | ✅ | ✅ | Python |
| Day 2 | ✅ | ✅ | Python |

## Structure

```text
Advent-of-Code/
├── 2025/
│   ├── Day 1/
│   │   ├── Part1.py
│   │   └── Part2.py
│   └── Day 2/
│       ├── D2_p1.py
│       └── D2_p2.py
├── tests/
│   └── test_2025_solutions.py
├── .gitignore
├── LICENSE
└── README.md
```

## Running a Solution

Every current solution accepts the puzzle input file as a command-line argument instead of requiring a hard-coded path.

Examples:

```bash
python "2025/Day 1/Part1.py" input.txt
python "2025/Day 1/Part2.py" input.txt
python "2025/Day 2/D2_p1.py" input.txt
python "2025/Day 2/D2_p2.py" input.txt
```

No third-party Python packages are required for the current solutions.

## Tests

Small regression tests verify the reusable parsing and solution functions without using or publishing personal Advent of Code input data.

Run them with:

```bash
python -m unittest discover -s tests -v
```

The current suite covers:

- Day 1 instruction parsing
- Day 1 Part 1 dial landing behaviour
- Day 1 Part 2 zero-crossing behaviour
- Day 2 range parsing
- Day 2 Part 1 repeated-half detection
- Day 2 Part 2 repeated-pattern detection
- small deterministic range totals

## Implementation Notes

### Day 1

The solutions parse instructions into `(direction, distance)` pairs.

- Part 1 updates the circular dial once per instruction and counts instructions that finish at zero.
- Part 2 simulates each individual movement step and counts every arrival at zero.

### Day 2

The input is parsed as inclusive integer ranges.

- Part 1 identifies decimal strings made of two identical halves.
- Part 2 identifies decimal strings formed by repeating a shorter unit two or more times.

## Input Files

Puzzle input files are intentionally not committed. Store them locally, for example:

```text
inputs/
└── 2025/
    ├── day01.txt
    └── day02.txt
```

The repository `.gitignore` excludes `inputs/`.

## License

See [`LICENSE`](LICENSE).