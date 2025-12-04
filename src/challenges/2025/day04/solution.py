"""
Advent of Code 2025 - Day 4: Printing Department
Count accessible paper rolls based on neighbour count.
"""

from pathlib import Path

from utils import read_lines


def parse_rolls(grid: list[str]) -> set[tuple[int, int]]:
    """Parse grid into set of roll coordinates."""
    return {
        (row_idx, col_idx)
        for row_idx, row in enumerate(grid)
        for col_idx, cell in enumerate(row)
        if cell == "@"
    }


def count_neighbours(rolls: set[tuple[int, int]], row: int, col: int) -> int:
    """Count the number of neighbouring rolls."""
    # fmt: off
    neighbours = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1), # top-left, top, top-right
        (row, col - 1),                     (row, col + 1),     # left, right
        (row + 1, col - 1), (row + 1, col), (row + 1, col +1 ), # bottom-left, bottom, bottom-right
    ]
    # fmt: on

    return sum(neighbour in rolls for neighbour in neighbours)


def get_accessible_rolls(rolls: set[tuple[int, int]]) -> set[tuple[int, int]]:
    """
    Get all rolls that can be accessed by a forklift.
    A roll is accessible if it has fewer than 4 neighbouring rolls.
    """
    return {(row, col) for row, col in rolls if count_neighbours(rolls, row, col) < 4}


def iteratively_get_accessible_rolls(rolls: set[tuple[int, int]]) -> int:
    """
    Iteratively remove accessible rolls until no more can be removed.
    Returns the total count of removed rolls.
    """
    total_removed = 0

    while accessible_rolls := get_accessible_rolls(rolls):
        rolls -= accessible_rolls
        total_removed += len(accessible_rolls)

    return total_removed


def main() -> None:
    """Entry point."""
    input_file = Path(__file__).parent / "input.txt"
    grid = read_lines(input_file)
    rolls = parse_rolls(grid)

    part1 = len(get_accessible_rolls(rolls))
    print(f"Part 1: {part1}")

    part2 = iteratively_get_accessible_rolls(rolls)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
