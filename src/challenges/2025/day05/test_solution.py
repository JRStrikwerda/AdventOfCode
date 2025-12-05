"""Tests for Day 5: Cafeteria Inventory Management System"""

import pytest

from utils import read_lines

from .solution import get_merged_ranges, parse_input, solve


@pytest.fixture
def example_lines(example_file):
    """Lines from example.txt."""
    return read_lines(example_file, skip_empty=False)


@pytest.fixture
def example_parsed(example_lines):
    """Parsed merged ranges and available IDs."""
    return parse_input(example_lines)


@pytest.fixture
def example_merged_ranges(example_parsed):
    """Merged ranges from example data."""
    return example_parsed[0]


@pytest.fixture
def example_available_ids(example_parsed):
    """Available IDs from example data."""
    return example_parsed[1]


class TestGetMergedRanges:
    """Test range merging logic."""

    def test_no_overlap(self):
        """Test ranges that don't overlap."""
        ranges = [(1, 3), (5, 7), (10, 12)]
        result = get_merged_ranges(ranges)
        assert result == [(1, 3), (5, 7), (10, 12)]

    def test_complete_overlap(self):
        """Test ranges that completely overlap."""
        ranges = [(1, 10), (2, 5), (3, 8)]
        result = get_merged_ranges(ranges)
        assert result == [(1, 10)]

    def test_adjacent_ranges(self):
        """Test ranges that are adjacent but not overlapping."""
        ranges = [(1, 3), (5, 7)]
        result = get_merged_ranges(ranges)
        assert result == [(1, 3), (5, 7)]

    def test_touching_ranges(self):
        """Test ranges that touch at a boundary."""
        ranges = [(1, 3), (4, 7)]
        result = get_merged_ranges(ranges)
        assert result == [(1, 3), (4, 7)]

    def test_partial_overlap(self):
        """Test ranges with partial overlap."""
        ranges = [(1, 5), (3, 8)]
        result = get_merged_ranges(ranges)
        assert result == [(1, 8)]

    def test_example_ranges(self):
        """Test merging example ranges."""
        ranges = [(3, 5), (10, 14), (16, 20), (12, 18)]
        result = get_merged_ranges(ranges)
        assert result == [(3, 5), (10, 20)]

    def test_single_range(self):
        """Test with a single range."""
        ranges = [(5, 10)]
        result = get_merged_ranges(ranges)
        assert result == [(5, 10)]

    def test_empty_ranges(self):
        """Test with empty list."""
        ranges = []
        result = get_merged_ranges(ranges)
        assert result == []

    def test_unsorted_input(self):
        """Test that unsorted input is handled correctly."""
        ranges = [(10, 15), (1, 3), (5, 8)]
        result = get_merged_ranges(ranges)
        assert result == [(1, 3), (5, 8), (10, 15)]


class TestParseInput:
    """Test input parsing."""

    def test_example_input(self, example_lines):
        """Test parsing example input."""
        merged_ranges, available_ids = parse_input(example_lines)
        assert merged_ranges == [(3, 5), (10, 20)]
        assert available_ids == {1, 5, 8, 11, 17, 32}

    def test_split_by_empty_line(self, example_lines):
        """Test that input is correctly split by empty line."""
        merged_ranges, available_ids = parse_input(example_lines)
        # Verify we have ranges and IDs
        assert len(merged_ranges) > 0
        assert len(available_ids) > 0


class TestPart1Logic:
    """Test Part 1: Count available fresh ingredients."""

    def test_example_part1(self, example_merged_ranges, example_available_ids):
        """Test Part 1 with example data."""
        fresh_ids = {
            ingredient_id
            for ingredient_id in example_available_ids
            for start, end in example_merged_ranges
            if start <= ingredient_id <= end
        }
        assert fresh_ids == {5, 11, 17}
        assert len(fresh_ids) == 3

    def test_id_in_range(self):
        """Test ID within a range."""
        ranges = [(10, 20)]
        ids = {15}
        fresh = {id for id in ids for start, end in ranges if start <= id <= end}
        assert fresh == {15}

    def test_id_outside_range(self):
        """Test ID outside all ranges."""
        ranges = [(10, 20)]
        ids = {5, 25}
        fresh = {id for id in ids for start, end in ranges if start <= id <= end}
        assert fresh == set()

    def test_id_at_boundaries(self):
        """Test IDs at range boundaries."""
        ranges = [(10, 20)]
        ids = {10, 20}
        fresh = {id for id in ids for start, end in ranges if start <= id <= end}
        assert fresh == {10, 20}


class TestPart2Logic:
    """Test Part 2: Count total fresh ingredients."""

    def test_example_part2(self, example_merged_ranges):
        """Test Part 2 with example data."""
        total = sum(end - start + 1 for start, end in example_merged_ranges)
        assert total == 14

    def test_single_range_count(self):
        """Test counting ingredients in a single range."""
        ranges = [(3, 5)]
        total = sum(end - start + 1 for start, end in ranges)
        assert total == 3

    def test_multiple_ranges_count(self):
        """Test counting ingredients in multiple ranges."""
        ranges = [(1, 3), (5, 7), (10, 12)]
        total = sum(end - start + 1 for start, end in ranges)
        assert total == 9


class TestMain:
    """Test main entry point and solve function."""

    def test_solve_with_example(self, example_file):
        """Test solve function with example.txt."""
        part1, part2 = solve(example_file)
        assert part1 == 3
        assert part2 == 14
