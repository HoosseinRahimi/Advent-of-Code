import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name, relative_path):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


D1P1 = load_module("d1p1", "2025/Day 1/Part1.py")
D1P2 = load_module("d1p2", "2025/Day 1/Part2.py")
D2P1 = load_module("d2p1", "2025/Day 2/D2_p1.py")
D2P2 = load_module("d2p2", "2025/Day 2/D2_p2.py")


class Day1Tests(unittest.TestCase):
    def test_parser(self):
        self.assertEqual(D1P1.parse_instruction("R25"), ("R", 25))
        self.assertEqual(D1P1.parse_instruction(" L7 "), ("L", 7))
        with self.assertRaises(ValueError):
            D1P1.parse_instruction("X10")

    def test_part1_counts_only_final_zero_positions(self):
        instructions = [("R", 50), ("R", 100), ("L", 25)]
        self.assertEqual(D1P1.count_zero_landings(instructions), 2)

    def test_part2_counts_each_arrival_at_zero(self):
        self.assertEqual(D1P2.count_zero_crossings([("R", 250)]), 3)
        self.assertEqual(D1P2.count_zero_crossings([("L", 50)]), 1)


class Day2Tests(unittest.TestCase):
    def test_part1_exact_double_pattern(self):
        for value in (11, 1212, 123123):
            self.assertTrue(D2P1.is_double_pattern(value))
        for value in (111, 1234, 123):
            self.assertFalse(D2P1.is_double_pattern(value))

    def test_part2_any_repeated_pattern(self):
        for value in (11, 111, 1212, 123123, 999999):
            self.assertTrue(D2P2.has_repeated_pattern(value))
        for value in (10, 123, 1234):
            self.assertFalse(D2P2.has_repeated_pattern(value))

    def test_range_reader(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "input.txt"
            path.write_text("10-12,20-21\n30-30", encoding="utf-8")
            expected = [(10, 12), (20, 21), (30, 30)]
            self.assertEqual(D2P1.read_ranges(path), expected)
            self.assertEqual(D2P2.read_ranges(path), expected)

    def test_small_range_sums(self):
        self.assertEqual(D2P1.sum_double_patterns([(10, 12)]), 11)
        self.assertEqual(D2P2.sum_repeated_patterns([(110, 112)]), 111)


if __name__ == "__main__":
    unittest.main()
