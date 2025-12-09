"""
Advent of Code 2025 - Day 7: Teleporter Lab
Count tachyon splits and paths.
"""

from functools import cache
from pathlib import Path

from challenges.constants import INPUT_FILE
from utils import Coordinate, get_grid_size, iterate_over_grid, read_lines


def solve(filepath: Path) -> tuple[int, int]:
    """Solve both parts given an input file."""
    grid = read_lines(filepath)
    height, width = get_grid_size(grid)

    start_coord: Coordinate = next(iterate_over_grid(grid, condition=lambda x: x == "S"))
    splitters = set(iterate_over_grid(grid, condition=lambda x: x == "^"))
    splits: set[Coordinate] = set()

    @cache
    def count_paths(row: int, col: int) -> int:
        """Recursively count possible tachyon paths."""
        # Stop recursion if out of bounds (reached bottom or side)
        if row >= height or col >= width or col < 0:
            return 1

        # Split found, check both left and right paths/columns
        if (row, col) in splitters:
            # Increment split count
            splits.add(Coordinate((row, col)))
            return count_paths(row, col - 1) + count_paths(row, col + 1)

        # Move down a row
        return count_paths(row + 1, col)

    part2 = count_paths(*start_coord)
    part1 = len(splits)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve(INPUT_FILE)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
