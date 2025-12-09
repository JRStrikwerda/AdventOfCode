"""
Advent of Code 2025 - Day 4: Printing Department
Count accessible paper rolls based on neighbour count.
"""

from pathlib import Path

from challenges.constants import INPUT_FILE
from utils import Coordinate, iterate_over_grid, read_lines


def parse_rolls(grid: list[str]) -> set[Coordinate]:
    """Parse grid into set of roll coordinates."""
    return set(iterate_over_grid(grid, condition=lambda x: x == "@"))


def count_neighbours(rolls: set[Coordinate], coordinate: Coordinate) -> int:
    """Count the number of neighbouring rolls."""
    # fmt: off
    row = coordinate[0]
    col = coordinate[1]
    neighbours = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1), # top-left, top, top-right
        (row, col - 1),                     (row, col + 1),     # left, right
        (row + 1, col - 1), (row + 1, col), (row + 1, col +1 ), # bottom-left, bottom, bottom-right
    ]
    # fmt: on

    return sum(neighbour in rolls for neighbour in neighbours)


def get_accessible_rolls(rolls: set[Coordinate]) -> set[Coordinate]:
    """
    Get all rolls that can be accessed by a forklift.
    A roll is accessible if it has fewer than 4 neighbouring rolls.
    """
    return {coordinate for coordinate in rolls if count_neighbours(rolls, coordinate) < 4}


def iteratively_get_accessible_rolls(rolls: set[Coordinate]) -> int:
    """
    Iteratively remove accessible rolls until no more can be removed.
    Returns the total count of removed rolls.
    """
    total_removed = 0

    while accessible_rolls := get_accessible_rolls(rolls):
        rolls -= accessible_rolls
        total_removed += len(accessible_rolls)

    return total_removed


def solve(filepath: Path) -> tuple[int, int]:
    """Solve both parts given an input file."""
    grid = read_lines(filepath)
    rolls = parse_rolls(grid)

    part1 = len(get_accessible_rolls(rolls))
    # Make a copy for part2 since it modifies the set
    part2 = iteratively_get_accessible_rolls(rolls.copy())

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve(INPUT_FILE)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
