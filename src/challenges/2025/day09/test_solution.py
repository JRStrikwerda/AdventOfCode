"""Tests for Day 9: Movie Theater"""

from .solution import solve


def test_example(example_file):
    """Test with example input."""
    part1, part2 = solve(example_file)
    assert part1 == 50  # Largest rectangle with any tiles
    assert part2 == 24  # Largest rectangle with only red/green tiles
