"""
Advent of Code 2025 - Day 5: Cafeteria Inventory Management System
Count available fresh ingredient IDs and total fresh ingredients.`
"""

from pathlib import Path

from challenges.constants import INPUT_FILE
from utils import read_lines
from utils.utils import map_range


def get_merged_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Get merged fresh ingredient ranges."""
    merged_ranges: list[tuple[int, int]] = []
    for start, end in sorted(ranges):
        # Does the new range start AFTER the last one ended?
        if not merged_ranges or start > merged_ranges[-1][1]:
            merged_ranges.append((start, end))
        else:
            # max(end of the last range and the current range).
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
    return merged_ranges


def parse_input(lines: list[str]) -> tuple[list[tuple[int, int]], set[int]]:
    """Parses fresh range and available ingredient id input."""
    split_index = lines.index("")
    merged_ranges = get_merged_ranges([map_range(line) for line in lines[:split_index]])
    available_ids = {int(x) for x in lines[split_index + 1 :]}
    return merged_ranges, available_ids


def solve(filepath: Path) -> tuple[int, int]:
    """Solve both parts given an input file."""
    lines = read_lines(filepath, skip_empty=False)
    merged_ranges, available_ids = parse_input(lines)
    part1 = len({id for id in available_ids for start, end in merged_ranges if start <= id <= end})
    part2 = sum(end - start + 1 for start, end in merged_ranges)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve(INPUT_FILE)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
