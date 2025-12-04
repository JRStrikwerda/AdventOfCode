"""Tests for Day 3: Lobby"""

from .solution import (
    find_max_joltage_part1,
    find_max_joltage_part2,
    solve_part1,
    solve_part2,
)


class TestMaxJoltage:
    """Test finding maximum joltage from a bank."""

    def test_first_example(self):
        """987654321111111 produces 98."""
        assert find_max_joltage_part1("987654321111111") == 98

    def test_second_example(self):
        """811111111111119 produces 89."""
        assert find_max_joltage_part1("811111111111119") == 89

    def test_third_example(self):
        """234234234234278 produces 78."""
        assert find_max_joltage_part1("234234234234278") == 78

    def test_fourth_example(self):
        """818181911112111 produces 92."""
        assert find_max_joltage_part1("818181911112111") == 92

    def test_simple_bank(self):
        """12345 produces 45 (positions 3,4)."""
        assert find_max_joltage_part1("12345") == 45

    def test_reverse_order(self):
        """54321 produces 54 (positions 0,1)."""
        assert find_max_joltage_part1("54321") == 54

    def test_two_digits_only(self):
        """99 produces 99."""
        assert find_max_joltage_part1("99") == 99


class TestSolverPart1:
    """Test Part 1 solver logic."""

    def test_example_total(self):
        """Test the full example: 98 + 89 + 78 + 92 = 357."""
        banks = [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ]
        assert solve_part1(banks) == 357

    def test_single_bank(self):
        """Test with a single bank."""
        assert solve_part1(["12345"]) == 45

    def test_multiple_banks(self):
        """Test with multiple simple banks."""
        banks = ["12345", "67890"]
        assert solve_part1(banks) == 45 + 90  # 45 + 90 = 135


class TestSolverPart2:
    """Test Part 2 solver logic."""

    def test_example_part2(self):
        """Test the Part 2 examples."""
        # 987654321111111 -> 987654321111
        assert find_max_joltage_part2("987654321111111") == 987654321111
        # 811111111111119 -> 811111111119
        assert find_max_joltage_part2("811111111111119") == 811111111119
        # 234234234234278 -> 434234234278
        assert find_max_joltage_part2("234234234234278") == 434234234278
        # 818181911112111 -> 888911112111
        assert find_max_joltage_part2("818181911112111") == 888911112111

    def test_example_total_part2(self):
        """Test the full Part 2 example total."""
        banks = [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ]
        expected = 987654321111 + 811111111119 + 434234234278 + 888911112111
        assert solve_part2(banks) == expected
        assert solve_part2(banks) == 3121910778619
