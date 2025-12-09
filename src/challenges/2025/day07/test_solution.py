"""Tests for Day 7: Teleporter Lab"""

from .solution import solve


def test_example(example_file):
    """Test with example input."""
    part1, part2 = solve(example_file)
    assert part1 == 21
    assert part2 == 40
