"""Tests for Day 6: Trash Compactor (Cephalopod Math)"""

from .solution import parse_operators, parse_problems, solve


def test_example(example_file):
    """Test with example input."""
    part1, part2 = solve(example_file)
    assert part1 == 4277556
    assert part2 == 3263827


def test_parse_operators():
    """Test operator parsing."""
    operators = parse_operators("*   +   *   + ")
    assert len(operators) == 4
    assert operators[0]([2, 3]) == 6  # multiply
    assert operators[1]([2, 3]) == 5  # sum
    assert operators[2]([2, 3]) == 6  # multiply
    assert operators[3]([2, 3]) == 5  # sum


def test_parse_problems():
    """Test problem parsing preserves spacing and separates correctly."""
    lines = ["123 328  51 64 ", " 45 64  387 23 ", "  6 98  215 314"]
    problems = parse_problems(lines)

    assert len(problems) == 4

    # Each problem preserves the exact spacing from the original input
    assert problems[0] == ["123", " 45", "  6"]
    assert problems[1] == ["328", "64 ", "98 "]
    assert problems[2] == [" 51", "387", "215"]
    assert problems[3] == ["64 ", "23 ", "314"]
