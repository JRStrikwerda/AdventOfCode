"""
Advent of Code 2025 - Day 9: [Puzzle Title]
[Brief description]
"""

from pathlib import Path

from challenges.constants import INPUT_FILE
from utils import read_lines


def solve(filepath: Path) -> tuple[int, int]:
    """Solve both parts given an input file."""
    _lines = read_lines(filepath)

    # Part 1 solution
    part1 = 0

    # Part 2 solution
    part2 = 0

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve(INPUT_FILE)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
