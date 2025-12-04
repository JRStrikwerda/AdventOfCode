"""Tests for Day 2: Gift Shop"""

from .solution import (
    is_invalid_part1,
    is_invalid_part2,
    sum_invalid_ids,
)


class TestInvalidDetectionPart1:
    """Test Part 1 invalid ID detection (pattern repeated exactly twice)."""

    def test_single_digit_repeated(self):
        assert is_invalid_part1(11)
        assert is_invalid_part1(22)
        assert is_invalid_part1(55)
        assert is_invalid_part1(99)

    def test_two_digits_repeated(self):
        assert is_invalid_part1(6464)
        assert is_invalid_part1(1010)

    def test_three_digits_repeated(self):
        assert is_invalid_part1(123123)
        assert is_invalid_part1(999999)

    def test_longer_patterns(self):
        assert is_invalid_part1(1188511885)
        assert is_invalid_part1(222222)
        assert is_invalid_part1(446446)
        assert is_invalid_part1(38593859)

    def test_valid_ids(self):
        assert not is_invalid_part1(12)
        assert not is_invalid_part1(100)
        assert not is_invalid_part1(101)
        assert not is_invalid_part1(1234)
        assert not is_invalid_part1(95)
        assert not is_invalid_part1(115)

    def test_odd_length_ids_are_valid(self):
        assert not is_invalid_part1(123)
        assert not is_invalid_part1(12345)

    def test_not_matching_halves(self):
        assert not is_invalid_part1(1122)
        assert not is_invalid_part1(123456)


class TestInvalidDetectionPart2:
    """Test Part 2 invalid ID detection (pattern repeated at least twice)."""

    def test_repeated_twice(self):
        assert is_invalid_part2(11)
        assert is_invalid_part2(6464)
        assert is_invalid_part2(123123)

    def test_repeated_more_than_twice(self):
        assert is_invalid_part2(111)  # 1 three times
        assert is_invalid_part2(1111)  # 1 four times
        assert is_invalid_part2(999)  # 9 three times
        assert is_invalid_part2(123123123)  # 123 three times
        assert is_invalid_part2(1212121212)  # 12 five times

    def test_specific_examples_from_problem(self):
        assert is_invalid_part2(12341234)  # 1234 two times
        assert is_invalid_part2(123123123)  # 123 three times
        assert is_invalid_part2(1212121212)  # 12 five times
        assert is_invalid_part2(1111111)  # 1 seven times

    def test_valid_ids(self):
        assert not is_invalid_part2(12)
        assert not is_invalid_part2(100)
        assert not is_invalid_part2(101)
        assert not is_invalid_part2(1234)
        assert not is_invalid_part2(95)
        assert not is_invalid_part2(115)
        assert not is_invalid_part2(1122)
        assert not is_invalid_part2(123456)


class TestSolverPart1:
    """Test Part 1 solver logic."""

    def test_range_11_22(self):
        """Test range with 11 and 22 (both invalid)."""
        assert sum_invalid_ids([(11, 22)], is_invalid_part1) == 33  # 11 + 22

    def test_range_95_115(self):
        """Test range with only 99 invalid."""
        assert sum_invalid_ids([(95, 115)], is_invalid_part1) == 99

    def test_range_998_1012(self):
        """Test range crossing 1000 with only 1010 invalid."""
        assert sum_invalid_ids([(998, 1012)], is_invalid_part1) == 1010

    def test_range_1188511880_1188511890(self):
        """Test range with a long number pattern."""
        assert sum_invalid_ids([(1188511880, 1188511890)], is_invalid_part1) == 1188511885

    def test_range_222220_222224(self):
        """Test range with 222222."""
        assert sum_invalid_ids([(222220, 222224)], is_invalid_part1) == 222222

    def test_range_1698522_1698528(self):
        """Test range with no invalid IDs."""
        assert sum_invalid_ids([(1698522, 1698528)], is_invalid_part1) == 0

    def test_range_446443_446449(self):
        """Test range with 446446."""
        assert sum_invalid_ids([(446443, 446449)], is_invalid_part1) == 446446

    def test_range_38593856_38593862(self):
        """Test range with 38593859."""
        assert sum_invalid_ids([(38593856, 38593862)], is_invalid_part1) == 38593859

    def test_example_sum(self):
        """Test the full example from the problem."""
        ranges = [
            (11, 22),
            (95, 115),
            (998, 1012),
            (1188511880, 1188511890),
            (222220, 222224),
            (1698522, 1698528),
            (446443, 446449),
            (38593856, 38593862),
            (565653, 565659),
            (824824821, 824824827),
            (2121212118, 2121212124),
        ]

        assert sum_invalid_ids(ranges, is_invalid_part1) == 1227775554

    def test_small_example(self):
        """Test multiple ranges combined."""
        assert sum_invalid_ids([(11, 22), (95, 115)], is_invalid_part1) == 132  # 11 + 22 + 99


class TestSolverPart2:
    """Test Part 2 solver logic."""

    def test_range_11_22(self):
        """Test range with 11 and 22 (both invalid for part 2 as well)."""
        assert sum_invalid_ids([(11, 22)], is_invalid_part2) == 33

    def test_range_95_115(self):
        """Test range with 99 and 111 invalid."""
        assert sum_invalid_ids([(95, 115)], is_invalid_part2) == 210  # 99 + 111

    def test_range_998_1012(self):
        """Test range crossing 1000 with 999 and 1010 invalid."""
        assert sum_invalid_ids([(998, 1012)], is_invalid_part2) == 2009  # 999 + 1010

    def test_example_sum(self):
        """Test the full Part 2 example."""
        ranges = [
            (11, 22),
            (95, 115),
            (998, 1012),
            (1188511880, 1188511890),
            (222220, 222224),
            (1698522, 1698528),
            (446443, 446449),
            (38593856, 38593862),
            (565653, 565659),
            (824824821, 824824827),
            (2121212118, 2121212124),
        ]

        assert sum_invalid_ids(ranges, is_invalid_part2) == 4174379265
